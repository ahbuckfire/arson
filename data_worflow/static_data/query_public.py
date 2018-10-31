import io
import os
import pandas as pd
import requests


BASE_API_URL = "https://public.enigma.com/api/"

def create_file_name(dataset, data_path):
    year = dataset["display_name"][-4:]
    return os.path.join(data_path, "nfirs_{}.csv".format(year))


def get_datasets_in_collection(c_id, headers):
    url = BASE_API_URL + "datasets/?parent_collection_id=" + c_id
    r = requests.get(url, headers=headers)
    return r.json()    


def get_snapshot_schema(dataset):
    fields_json = dataset["current_snapshot"]["fields"]
    schema = {field['name']:field['data_type'] for field in fields_json}
    replacements = {'string':'str', 'integer':'float', 'datetime':'str', 'decimal':'float', 'boolean':'bool'}
    for name, d_type in schema.items():
        if d_type in replacements:
            schema[name] = replacements[d_type]
    return schema


def snapshot_to_df(snapshot_id, schema, headers):
    snapshot_url = BASE_API_URL + 'export/{}'.format(snapshot_id)
    response = requests.get(snapshot_url, headers=headers).content
    return pd.read_csv(io.StringIO(response.decode('utf-8')), dtype=schema)


def download_datasets_in_collection(collection_id, api_token, data_path):
    headers = {"authorization": "Bearer {}".format(api_token)}
    datasets = get_datasets_in_collection(collection_id, headers)

    for dataset in datasets:
        schema = get_snapshot_schema(dataset)
        df = snapshot_to_df(dataset["current_snapshot"]["id"], schema, headers)
        df.to_csv(create_file_name(dataset, data_path))
