import datadotworld as dw

ZIPCODE_DATASET_PATH = "lukewhyte/us-population-by-zip-code-2010-2016"
API_TOKEN = "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJwcm9kLXVzZXItY2xpZW50OmFidWNrZmlyZSIsImlzcyI6ImFnZW50OmFidWNrZmlyZTo6MjRkODc4N2MtZGVjYy00OGUyLTgzODMtYzEzMzE5NzM0OTJiIiwiaWF0IjoxNTM4NjgwNjgyLCJyb2xlIjpbInVzZXJfYXBpX3JlYWQiLCJ1c2VyX2FwaV93cml0ZSJdLCJnZW5lcmFsLXB1cnBvc2UiOnRydWV9.9Pe4wpnQSj3nbR0IJvMGcqc1eYWHzhx57IKn5peqcb7dbIM_Gni2OqO2faJy0wjIJ3wYNjnXSKi-fAu3lC6_hQ"


def dataworld_table_to_csv(data_path, dataworld_path=ZIPCODE_DATASET_PATH):
    dataset = dw.load_dataset(dataworld_path)
    properties = dataset.describe()
    dataset_name = properties["resources"][0]["name"]
    zipcode_df = dataset.dataframes[dataset_name]
    zipcode_df["zip_code"] = zipcode_df["zip_code"].apply(lambda x: '{0:0>5}'.format(x))
    zipcode_df.to_csv(data_path)
