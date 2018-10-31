import argparse
import json
import requests

import elastic
import ensure_unique_articles

SUBSCRIPTION_KEY = "0acf73f240d24b6d97c85550105193e2"
SEARCH_URL = "https://api.cognitive.microsoft.com/bing/v7.0/news/search"
KEYS = ["summary", "url", "article_name", "news_source_name", "date_published", "all_text"]

def _parse_args():
    parser = argparse.ArgumentParser("Execute the structure pipeline")
    parser.add_argument("-t", "--search_term", default="arson", help="term to query for")
    return parser.parse_args()


def query_bing_api(url, headers, parameters):
    response = requests.get(url, headers=headers, params=parameters)
    response.raise_for_status()
    return response.json()


def ingest_to_elastic(query_results, index="bing", keys=KEYS):
    es = elastic.ElasticSearch()
    es.create_indices(mappings=elastic.BING_MAPPINGS)
    for record in query_results["value"]:
        body = dict(zip(keys,
                        [record["description"], record["url"], record["name"],
                        record["provider"][0]["name"], record["datePublished"],
                        record["description"] + record["name"]]
                    )
                )
        es.add_to_index(es, index, index, body)


def main():
    args = _parse_args()
    headers = {"Ocp-Apim-Subscription-Key" : SUBSCRIPTION_KEY}
    parameters = {"q": args.search_term,
              "textDecorations": True,
              "textFormat": "HTML",
              "count": 100,
              "responseFilter": "News",
              "freshness": "Week",
              "mkt": "en-US"
            }

    query_results = query_bing_api(SEARCH_URL, headers, parameters)
    ingest_to_elastic(query_results)
    ensure_unique_articles.get_non_duplicate_articles()

if __name__ == "__main__":
    main()
