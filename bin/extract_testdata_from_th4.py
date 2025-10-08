#!/usr/bin/env python3

import json
import logging
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

FAILED_TYPES = []
INPUT_DIRECTORY = "/home/senzing/github.com/jaeadams/MichaelTemp"
OUTPUT_DIRECTORY = "/home/senzing/senzing-json"

TYPE_TO_FILENAME_MAP = {
    "SZ_FIND_INTERESTING_ENTITIES_BY_ENTITY_ID": "SzEngineFindInterestingEntitiesByEntityIdResponse.jsonl",
    "SZ_FIND_INTERESTING_ENTITIES_BY_RECORD_ID": "SzEngineFindInterestingEntitiesByRecordIdResponse.jsonl",
    "SZ_FIND_NETWORK_BY_ENTITY_ID_V2": "SzEngineFindNetworkByEntityIdResponse.jsonl",
    "SZ_FIND_NETWORK_BY_ENTITY_ID": "SzEngineFindNetworkByEntityIdResponse.jsonl",
    "SZ_FIND_NETWORK_BY_RECORD_ID_V2": "SzEngineFindNetworkByRecordIdResponse.jsonl",
    "SZ_FIND_NETWORK_BY_RECORD_ID": "SzEngineFindNetworkByRecordIdResponse.jsonl",
    "SZ_FIND_PATH_BY_ENTITY_ID_INCLUDING_SOURCE_V2": "SzEngineFindPathByEntityIdResponse.jsonl",
    "SZ_FIND_PATH_BY_ENTITY_ID_INCLUDING_SOURCE": "SzEngineFindPathByEntityIdResponse.jsonl",
    "SZ_FIND_PATH_BY_ENTITY_ID_V2": "SzEngineFindPathByEntityIdResponse.jsonl",
    "SZ_FIND_PATH_BY_ENTITY_ID_WITH_AVOIDS_V2": "SzEngineFindPathByEntityIdResponse.jsonl",
    "SZ_FIND_PATH_BY_ENTITY_ID_WITH_AVOIDS": "SzEngineFindPathByEntityIdResponse.jsonl",
    "SZ_FIND_PATH_BY_ENTITY_ID": "SzEngineFindPathByEntityIdResponse.jsonl",
    "SZ_FIND_PATH_BY_RECORD_ID_INCLUDING_SOURCE_V2": "SzEngineFindPathByRecordIdResponse.jsonl",
    "SZ_FIND_PATH_BY_RECORD_ID_INCLUDING_SOURCE": "SzEngineFindPathByRecordIdResponse.jsonl",
    "SZ_FIND_PATH_BY_RECORD_ID_V2": "SzEngineFindPathByRecordIdResponse.jsonl",
    "SZ_FIND_PATH_BY_RECORD_ID_WITH_AVOIDS_V2": "SzEngineFindPathByRecordIdResponse.jsonl",
    "SZ_FIND_PATH_BY_RECORD_ID_WITH_AVOIDS": "SzEngineFindPathByRecordIdResponse.jsonl",
    "SZ_FIND_PATH_BY_RECORD_ID": "SzEngineFindPathByRecordIdResponse.jsonl",
    "SZ_GET_ENTITY_BY_ENTITY_ID_V2": "SzEngineGetEntityByEntityIdResponse.jsonl",
    "SZ_GET_ENTITY_BY_ENTITY_ID": "SzEngineGetEntityByEntityIdResponse.jsonl",
    "SZ_GET_ENTITY_BY_RECORD_ID": "SzEngineGetEntityByRecordIdResponse.jsonl",
    "SZ_GET_ENTITY_BY_RECORD_ID_V2": "SzEngineGetEntityByRecordIdResponse.jsonl",
    "SZ_GET_RECORD_PREVIEW": "SzEngineGetRecordPreviewResponse.jsonl",
    "SZ_GET_RECORD_V2": "SzEngineGetRecordResponse.jsonl",
    "SZ_GET_RECORD": "SzEngineGetRecordResponse.jsonl",
    "SZ_GET_VIRTUAL_ENTITY_BY_RECORD_ID_V2": "SzEngineGetVirtualEntityByRecordIdResponse.jsonl",
    "SZ_HOW_ENTITY_BY_ENTITY_ID_V2": "SzEngineHowEntityByEntityIdResponse.jsonl",
    "SZ_HOW_ENTITY_BY_ENTITY_ID": "SzEngineHowEntityByEntityIdResponse.jsonl",
    "SZ_SEARCH_BY_ATTRIBUTES_V2": "SzEngineSearchByAttributesResponse.jsonl",
    "SZ_SEARCH_BY_ATTRIBUTES_V3": "SzEngineSearchByAttributesResponse.jsonl",
    "SZ_SEARCH_BY_ATTRIBUTES": "SzEngineSearchByAttributesResponse.jsonl",
    "SZ_WHY_ENTITIES_V2": "SzEngineWhyEntitiesResponse.jsonl",
    "SZ_WHY_RECORD_IN_ENTITY_V2": "SzEngineWhyRecordInEntityResponse.jsonl",
    "SZ_WHY_RECORD_IN_ENTITY": "SzEngineWhyRecordInEntityResponse.jsonl",
    "SZ_WHY_RECORDS_V2": "SzEngineWhyRecordsResponse.jsonl",
    "SZ_WHY_RECORDS": "SzEngineWhyRecordsResponse.jsonl",
    "SZ_WHY_SEARCH_V2": "SzEngineWhySearchResponse.jsonl",
    "SZ_WHY_SEARCH": "SzEngineWhySearchResponse.jsonl",
    "SZCONFIG_GET_DATA_SOURCE_REGISTRY": "SzConfigGetDataSourceRegistryResponse.jsonl",
    "SZCONFIG_REGISTER_DATA_SOURCE": "SzConfigRegisterDataSourceResponse.jsonl",
    "SZDIAGNOSTIC_GET_FEATURE": "SzDiagnosticGetFeatureResponse.jsonl",
}


def normalize_files(directory):
    """Deduplicate and sort JSON lines."""
    for root, _, files in os.walk(directory):
        for file in files:
            remove_duplicate_lines(f"{root}/{file}")


def process_file(filename):
    """Extract the RESPONSE_MESSAGE from appropriate files."""

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


def publish(type, json_string):
    """Write the json_string to a file determined by `type`."""

    if not json_string:
        return

    filename = TYPE_TO_FILENAME_MAP.get(type)

    if not filename:
        if type not in FAILED_TYPES:
            FAILED_TYPES.append(type)
        return

    logger.info(f"Writing {type} >>> {json_string}")

    with open(f"{OUTPUT_DIRECTORY}/{filename}", "a", encoding="utf-8") as target_file:
        target_file.write(f"{json_string}\n")


def remove_duplicate_lines(input_filepath, output_filepath=None):
    """
    Removes duplicate lines from a text file.

    Args:
        input_filepath (str): The path to the input file.
        output_filepath (str, optional): The path to the output file.
        If None, the input file will be overwritten.
    """
    unique_lines = set()
    try:
        with open(input_filepath, "r") as infile:
            for line in infile:
                unique_lines.add(line)  # Add each line to the set (duplicates are ignored)
    except FileNotFoundError:
        print(f"Error: Input file '{input_filepath}' not found.")
        return

    if output_filepath is None:
        output_filepath = input_filepath

    try:
        with open(output_filepath, "w") as outfile:
            for line in sorted(list(unique_lines)):  # Sort for consistent output, then write
                outfile.write(line)
        logger.info(f"Duplicates removed. Unique lines written to '{output_filepath}'.")
    except IOError:
        logger.error(f"Error: Could not write to output file '{output_filepath}'.")


def recurse_directory(directory):
    """Recurse through directories to process all of the appropriate files."""
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            recurse_directory(dir)

        for file in files:
            process_file(f"{root}/{file}")


def stringify_json(candidate_json):
    """Normalize a JSON string."""
    if not candidate_json:
        return None
    if isinstance(candidate_json, dict):
        return json.dumps(candidate_json, sort_keys=True)
    if isinstance(candidate_json, str):
        try:
            as_dict = json.loads(candidate_json)
            return json.dumps(as_dict, sort_keys=True)
        except Exception:
            logger.warning(f'Unable to create a dictionary from "{candidate_json}"')
    return None


if __name__ == "__main__":
    recurse_directory(INPUT_DIRECTORY)
    normalize_files(OUTPUT_DIRECTORY)
