#!/usr/bin/env python3

import json
import logging
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


INPUT_DIRECTORY = "/home/senzing/github.com/jaeadams/MichaelTemp"
OUTPUT_DIRECTORY = "/home/senzing/senzing-json"

TYPE_TO_FILENAME_MAP = {
    "SZ_GET_ENTITY_BY_ENTITY_ID_V2": "SzEngineGetEntityByEntityIdResponse.jsonl",
    "SZ_GET_ENTITY_BY_ENTITY_ID": "SzEngineGetEntityByEntityIdResponse.jsonl",
}


def publish(type, json_string):

    if not json_string:
        return

    filename = TYPE_TO_FILENAME_MAP.get(type)

    if not filename:
        return

    with open(f"{OUTPUT_DIRECTORY}/{filename}", "a", encoding="utf-8") as target_file:
        target_file.write(json_string)


def stringify_json(json_thingee):
    if not json_thingee:
        return None
    if isinstance(json_thingee, dict):
        return json.dumps(json_thingee, sort_keys=True)
    if isinstance(json_thingee, str):
        try:
            as_dict = json.loads(json_thingee)
            return json.dumps(as_dict, sort_keys=True)
        except Exception:
            logger.warning(f'Unable to create a dictionary from "{json_thingee}"')

    return None


def process_file(filename):

    # Filter out non-JSON files.

    _, extension = os.path.splitext(filename)
    if extension not in [".json"]:
        return

    # Read contents of file.

    data = {}
    try:
        with open(filename, "r", encoding="utf-8") as input_file:
            data = json.load(input_file)
    except Exception:
        logger.info(f"Could not read {filename}")
        return

    # Determine if it's a testcase file.

    if "TEST_STEPS" not in data:
        logger.info(f"TEST_STEPS not in {filename}")
        return

    # Process file

    logger.info(f"Processing {filename}")

    for test_step in data.get("TEST_STEPS", []):
        for validation in test_step.get("VALIDATION", []):
            validation_type = validation.get("TYPE")
            response = stringify_json(validation.get("VALIDATION_DATA", {}).get("DATA", {}).get("RESPONSE_MESSAGE"))
            publish(validation_type, response)


def recurse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            recurse_directory(dir)

        for file in files:
            process_file(f"{root}/{file}")


if __name__ == "__main__":

    recurse_directory(INPUT_DIRECTORY)
