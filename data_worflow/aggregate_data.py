import collections
import csv
import operator
import os
import sys

from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
from pyspark.sql import functions

import elastic
from static_data.lookup_tables import STATES, SUSPECTED_MOTIVATION_FACTORS, IGNITION_DELAY_DEVICE, PROPERTY_OWNERSHIP, MONTHS


STATE = "state"
POP_STATE = "NAME"
POPULATION_FIELD = "POPESTIMATE"
POPULATION = "population"
COUNT = "count"

UNKNOWNS = ["UU", "NN", None]

YEARS_AVAILABLE = map(str, range(2009, 2015))
FILE_PREFIX = "nfirs_arson_"
ARSON_PATH = os.path.join("static_data", "nfirs_arson")
POPULATION_PATH = os.path.join("static_data", "zipcodes", "nst-est2017-popchg2010_2017.csv")

FIELDS = {"motives": [STATE, "motive", "year"],
          "method": [STATE, "method", "year"],
          "ownership": [STATE, "ownership", "year"],
          "monthly_counts": [STATE, "month", "count", "year"],
          "arson_density" : [STATE, "count", "population", "year", "pop_density"]
        }


def lookup_code(candidate_list, column, codebook):
    candidates = [row for row in candidate_list if row[column] not in UNKNOWNS]
    if candidates:
        return codebook[max(candidates, key=operator.itemgetter(1))[0]]
    return None


def build_max_count_dicts(df, column, codebook, state_codes=STATES):
    results = collections.defaultdict()
    for state in state_codes:
        count_list = df[df.state==state].select(column, COUNT).collect()
        results[state] = lookup_code(count_list, column, codebook)

    overall_res = df.groupBy(column).agg(functions.sum(COUNT)).alias(COUNT).collect()
    results["overall"] = lookup_code(overall_res, column, codebook)
    return results


def get_motives(df, column="motivation"):
    df1 = df.groupBy(["mot_facts1", STATE]).count().withColumnRenamed("mot_facts1", column).withColumnRenamed(COUNT, "count_1")
    df2 = df.groupBy(["mot_facts2", STATE]).count().withColumnRenamed("mot_facts2", column).withColumnRenamed(COUNT, "count_2")
    df3 = df.groupBy(["mot_facts3", STATE]).count().withColumnRenamed("mot_facts3", column).withColumnRenamed(COUNT, "count_3")

    motives = df1.join(df2, [column, STATE], "outer").join(df3, [column, STATE], "outer").na.fill(0)

    motives_per_state = motives.withColumn(COUNT, sum(motives[col] for col in ["count_1", "count_2", "count_3"]))
    return build_max_count_dicts(motives_per_state, column, SUSPECTED_MOTIVATION_FACTORS)


def parse_date_by_month(date_string):
    return MONTHS[date_string[:2] if date_string[:2] in MONTHS else date_string[0]]


def get_arson_per_month(df, column="inc_date"):
    parse_date_by_month_udf = functions.udf(parse_date_by_month, "string")
    date_as_month_df = df.withColumn(column, parse_date_by_month_udf(df[column]))
    by_state = date_as_month_df.groupBy([column, STATE]).count()
    overall = date_as_month_df.groupBy(column).count().withColumn(STATE, functions.lit("overall")).select(column, STATE, COUNT)
    return overall.union(by_state).collect()


def get_fast_fact_one_column(df, column, codebook):
    df1 = df.groupBy([column, STATE]).count()
    return build_max_count_dicts(df1, column, codebook)


def calculate_arson_density(population_df, df, year, state_rename_udf, es):
    arson_df = df.select([STATE, "fdid"]).groupBy(STATE).count()

    y1 = year if year != "2009" else "2010" #adjusting for lack of 2009 population data
    population_for_year = population_df.select(POP_STATE, POPULATION_FIELD + y1)\
                                       .withColumnRenamed(POP_STATE, STATE)\
                                       .withColumnRenamed(POPULATION_FIELD + y1, POPULATION)

    joined_data = arson_df.withColumn(STATE, state_rename_udf(arson_df[STATE]))\
                          .join(population_for_year, STATE)\
                          .withColumn("year", functions.lit(year))
    
    densities = joined_data.withColumn("pop_density", joined_data[COUNT] * 100000 / joined_data[POPULATION]).collect()
    es.add_to_elastic(densities, "arson_density", year, FIELDS)


def calculate_stats_with_spark(df, year, es):
    # Question 1: What is the most common motivation for starting a fire?
    motives = get_motives(df)
    es.add_to_elastic(motives, "motives", year)

    # Question 2: What are the most common materials used for starting a fire?
    method = get_fast_fact_one_column(df, "devi_ignit", IGNITION_DELAY_DEVICE)
    es.add_to_elastic(method, "method", year, FIELDS)

    # Question 3: What is the most common type of property burned?
    ownership = get_fast_fact_one_column(df, "prop_owner", PROPERTY_OWNERSHIP)
    es.add_to_elastic(ownership, "ownership", year, FIELDS)

    # Question 4: Number of Arsons per Month
    monthly_arsons = get_arson_per_month(df)
    es.add_to_elastic(monthly_arsons, "monthly_counts", year, FIELDS)


def ingest_facts_into_es():
    # Initializing Spark Context and reading data in
    spark = SparkSession.builder.enableHiveSupport().getOrCreate()
    es = elastic.ElasticSearch()
    es.create_indices()

    population_df = spark.read.csv(POPULATION_PATH, header=True)
    state_rename_udf = functions.udf(lambda x: STATES[x.strip()] if STATES.get(x) else 0, "string")

    for year in YEARS_AVAILABLE:
        df = spark.read.csv(os.path.join(ARSON_PATH, FILE_PREFIX + year + ".csv"), header=True)
        calculate_stats_with_spark(df, year, es)
        calculate_arson_density(population_df, df, year, state_rename_udf, es)

if __name__ == "__main__":
    ingest_facts_into_es()
