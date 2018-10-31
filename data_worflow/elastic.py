import requests

from elasticsearch import Elasticsearch

SETTINGS = {
    'analysis': {
        'analyzer': {
            # for the vector scoring plug-in configuration
            'payload_analyzer': {
                'type': 'custom',
                'tokenizer': 'whitespace',
                'filter': 'delimited_payload_filter'
            }
        }
    }
}

BING_MAPPINGS = {
    "bing": {
        "properties": {
            "summary": {"type": "text"},
            "url": {"type": "text"},
            "article_name": {"type": "text"},
            "news_source_name": {"type": "text"},
            "date_published": {"type": "date"},
            "all_text": {"type": "text"},
        }
    }
}

DENSITY_MAPPINGS = {
    "arson_density": {
        "properties": {
            "state": {"type": "text"},
            "count": {"type": "integer"},
            "population": {"type": "integer"},
            "year": {"type": "text"},
            "pop_density": {"type": "float"}
            }
        }
}

MAPPINGS = {
    "motives": {
        "properties": {
            "state": {"type": "text"},
            "motive": {"type": "text"},
            "year": {"type": "text"}
        }
    },
    "method": {
        "properties": {
            "state": {"type": "text"},
            "method": {"type": "text"},
            "year": {"type": "text"}
        }
    },
    "ownership": {
        "properties": {
            "state": {"type": "text"},
            "ownership": {"type": "text"},
            "year": {"type": "text"}
        }
    },
    "monthly_counts": {
        "properties": {
            "state": {"type": "text"},
            "month": {"type": "text"},
            "count": {"type": "integer"},
            "year": {"type": "text"}
        }

    },
    "arson_density": {
        "properties": {
            "state": {"type": "text"},
            "count": {"type": "integer"},
            "population": {"type": "integer"},
            "year": {"type": "text"},
            "pop_density": {"type": "float"}
        }
    }
}

class ElasticSearch(object):

    def __init__(self):
        self.host = "localhost"
        self.port = 9200
        self.es = Elasticsearch([{'host': self.host, 'port': self.port}])


    def delete_index(self, index):
        if self.es.indices.exists(index):
            print("Index '{}' exists. Deleting it now...".format(index))
            es_object.indices.delete(index=index)
            print("Deleted index...")


    def create_indices(self, settings=SETTINGS, mappings=MAPPINGS):
        for key, value in mappings.items():
            if not self.es.indices.exists(key):
                self.es.indices.create(
                    index=key,
                    body={"settings": settings, "mappings": {key: value}}
                )
                print("Index '{}' created.".format(key))
            else:
                print("Index '{}' already exists. Cannot create it.".format(key))


    def add_to_index(self, index, doc_type, body):
        self.es.index(index=index, doc_type=doc_type, body=body)


    def add_to_elastic(self, aggs, key, year, fields):
        if key == "monthly_counts":
            for row in aggs:
                self.es.index(
                    index=key,
                    doc_type=key,
                    body=dict(zip(fields[key], [row["state"], row["inc_date"], row["count"], year]))
                )

        elif key == "arson_density":
            for row in aggs:
                self.es.index(
                    index=key,
                    doc_type=key,
                    body=dict(zip(fields[key], [row[field] for field in fields[key]]))
                )

        else:
            for state, value in aggs.items():
                self.es.index(
                    index=key,
                    doc_type=key,
                    body=dict(zip(fields[key], [state, value, year]))
                )

    def query_index(self, index_name, query, field="", max_size=51):
        if len(field) > 0:
            query = field + ":" + query
        res = self.es.search(index=index_name, q=query, size=max_size)
        return res["hits"]["hits"]
