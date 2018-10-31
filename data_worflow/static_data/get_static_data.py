import argparse
import logging
import os

import get_codebook
import query_dataworld
import query_public

CODEBOOK_FILEPATH = os.path.join("fire_codes", "nfirs_codebook.pdf")
POP_PER_ZIPCODE_FILEPATH = os.path.join("zipcodes", "pop_per_zip.csv")

NFIRS_ARSON_COLLECTION_ID = "66325433-f1dc-43c0-aadd-70a8837bd9e9"
NFIRS_FIRE_DEPARTMENTS_COLLECTION_ID = "fe3550ae-d6fc-487a-9e71-fde56439c4d8"
ARSON_FILE_PATH = "nfirs_arson"
FIRE_DEPT_FILE_PATH = "nfirs_fire_depts"

def configure_logging():
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="[%(asctime)s] %(message)s"
    )


def parse_args():
    parser = argparse.ArgumentParser("Grab data from public API")
    parser.add_argument("--public_api_token", required=True, help="public api key")
    return parser.parse_args()


def main():
    configure_logging()
    args = parse_args()

    logging.info("Downloading the fire department codebook")
    get_codebook.download_codebook(CODEBOOK_FILEPATH)
    logging.info("Data successfully saved to: {}".format(CODEBOOK_FILEPATH))

    logging.info("Downloading the population per zipcode data")
    query_dataworld.dataworld_table_to_csv(POP_PER_ZIPCODE_FILEPATH)
    logging.info("Data successfully saved to: {}".format(POP_PER_ZIPCODE_FILEPATH))

    logging.info("Downloading Enigma Public: Arson Cases")
    query_public.download_datasets_in_collection(NFIRS_ARSON_COLLECTION_ID, args.public_api_token, ARSON_FILE_PATH)
    logging.info("Data successfully saved to: {}".format(ARSON_FILE_PATH))

    logging.info("Downloading Enigma Public: Fire Dept. Locations")
    query_public.download_datasets_in_collection(NFIRS_FIRE_DEPARTMENTS_COLLECTION_ID, args.public_api_token, FIRE_DEPT_FILE_PATH)
    logging.info("Data successfully saved to: {}".format(FIRE_DEPT_FILE_PATH))


if __name__ == "__main__":
    main()
