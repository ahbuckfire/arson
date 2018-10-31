import collections
import json

import pandas as pd

import elastic
from lookup_tables import STATE_CODES, STATES

es = elastic.ElasticSearch()

COLOR_SCALE = [[0.0, 'rgb(242,240,247)'],[0.2, 'rgb(218,218,235)'],[0.4, 'rgb(188,189,220)'], [0.6, 'rgb(158,154,200)'],[0.8, 'rgb(117,107,177)'],[1.0, 'rgb(84,39,143)']]
YEARS_AVAILABLE = map(str, range(2009, 2015))


def build_density_df(hits):
    d = collections.defaultdict(str)
    for row in hits:
        source = row["_source"]
        d[STATE_CODES[source["state"]]] = source["pop_density"]
    return pd.DataFrame(d.items(), columns=["state", "pop_density"])


def build_text_df(indices, year):
    desc = collections.defaultdict(str)
    for index in indices:
        response = es.query_index(index, year, field="year")
        for row in response:
            source = row["_source"]
            desc[source["state"]] += index + ": " + str(source[index]) + "<br>"
    return pd.DataFrame(desc.items(), columns=["state", "text"])


def build_data_per_year(indices):
    densities_per_year = []
    for year in YEARS_AVAILABLE:
        hits = es.query_index("arson_density", year)
        densities_per_year.append(
            build_density_df(hits).merge(
                build_text_df(indices, year), on="state", how="outer"))
    return densities_per_year

######### PLOTTING STUFF #########
def set_data(dfs, scale=COLOR_SCALE):
    densities_per_year = []
    for df in dfs:
        d = {
            "type": "choropleth",
            "colorscale": scale,
            "autocolorscale": False,
            "locations": df["state"],
            "z": df["pop_density"],
            "locationmode": "USA-states",
            "text": df["text"],
            "marker": {
                "line": {
                    "color": "rgb(255,255,255)",
                    "width": 2
                }
            },
            "colorbar": {
                "title": "arson per 100k people"
            },
            "name": ""
        }
        densities_per_year.extend([d])
    return densities_per_year


def set_steps(dfs, years=YEARS_AVAILABLE):
    steps = []
    for idx, year in enumerate(years):
        step = {
            "method": "restyle",
            "args": ["visible", [False] * len(years)],
            "label": year
        }
        step["args"][1][idx] = True
        steps.append(step)
    return steps


def set_sliders(steps):
    return [{
        "active": 10,
        "currentvalue": {"prefix": "Year: "},
        "pad": {"t": 50},
        "steps": steps
    }]


def set_layout(sliders):
    return {
        "title": "USA Arson Density",
        "geo": {
            "scope": "usa",
            "projection": {"type": "albers usa"},
            "showlakes": True,
            "lakecolor": "rgb(255, 255, 255)"
        },
        "sliders": sliders
    }


def create_map():
    density_df = build_data_per_year(["ownership"])
    data = set_data(density_df)
    layout = set_layout(
        set_sliders(
            set_steps(density_df)))
    graph = {"data": data, "layout": layout}
    return graph
