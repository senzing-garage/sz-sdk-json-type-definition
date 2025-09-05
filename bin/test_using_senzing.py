#! /usr/bin/env python3

# pylint: disable=duplicate-code

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json
import os
import pathlib
import subprocess
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
# from python.typedef import (  # pylint: disable=wrong-import-position disable=wildcard-import
#     SzEngineAddRecordResponse,
#     SzEngineDeleteRecordResponse,
#     SzEngineFindNetworkByEntityIDResponse,
#     SzEngineFindNetworkByRecordIDResponse,
#     SzEngineFindPathByEntityIDResponse,
#     SzEngineFindPathByRecordIDResponse,
#     SzEngineGetEntityByEntityIDResponse,
#     SzEngineGetEntityByRecordIDResponse,
#     SzEngineGetRecordResponse,
#     SzEngineGetVirtualEntityByRecordIDResponse,
# )

# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Parse
# -----------------------------------------------------------------------------


GLOBAL_OUTPUT_DIRECTORY = "./docs/json-responses"
GLOBAL_JSON_KEYS = [
    "SzConfigExportResponse",
    "SzConfigGetDataSourceRegistryResponse",
    "SzConfigManagerGetConfigRegistryResponse",
    "SzConfigRegisterDataSourceResponse",
    "SzConfigUnregisterDataSourceResponse",
    "SzDiagnosticCheckRepositoryPerformanceResponse",
    "SzDiagnosticGetFeatureResponse",
    "SzDiagnosticGetRepositoryInfoResponse",
    "SzEngineAddRecordResponse",
    "SzEngineDeleteRecordResponse",
    "SzEngineExportCsvEntityReportCsvColumnList",
    "SzEngineFetchNextResponse",
    "SzEngineFindInterestingEntitiesByEntityIdResponse",
    "SzEngineFindInterestingEntitiesByRecordIdResponse",
    "SzEngineFindNetworkByEntityIdEntityIds",
    "SzEngineFindNetworkByEntityIdResponse",
    "SzEngineFindNetworkByRecordIdRecordKeys",
    "SzEngineFindNetworkByRecordIdResponse",
    "SzEngineFindPathByEntityIdAvoidEntityIds",
    "SzEngineFindPathByEntityIdRequiredDataSources",
    "SzEngineFindPathByEntityIdResponse",
    "SzEngineFindPathByRecordIdAvoidRecordKeys",
    "SzEngineFindPathByRecordIdRequiredDataSources",
    "SzEngineFindPathByRecordIdResponse",
    "SzEngineGetEntityByEntityIdResponse",
    "SzEngineGetEntityByRecordIdResponse",
    "SzEngineGetRecordPreviewResponse",
    "SzEngineGetRecordResponse",
    "SzEngineGetRedoRecordResponse",
    "SzEngineGetStatsResponse",
    "SzEngineGetVirtualEntityByRecordIdRecordKeys",
    "SzEngineGetVirtualEntityByRecordIdResponse",
    "SzEngineHowEntityByEntityIdResponse",
    "SzEngineProcessRedoRecordResponse",
    "SzEngineReevaluateEntityResponse",
    "SzEngineReevaluateRecordResponse",
    "SzEngineSearchByAttributesAttributes",
    "SzEngineSearchByAttributesResponse",
    "SzEngineSearchByAttributesSearchProfile",
    "SzEngineStreamExportJsonEntityReportResponse",
    "SzEngineWhyEntitiesResponse",
    "SzEngineWhyRecordInEntityResponse",
    "SzEngineWhyRecordsResponse",
    "SzEngineWhySearchAttributes",
    "SzEngineWhySearchResponse",
    "SzEngineWhySearchSearchProfile",
    "SzProductGetLicenseResponse",
    "SzProductGetVersionResponse",
]

DEFINITIONS = {}
SCHEMA = {}


def handle_elements(json_value):
    elements = json_value.get("elements", {})
    result = recurse(elements)
    return [result]


def handle_metadata(json_value):
    metadata = json_value.get("metadata")
    python_type = metadata.get("pythonType")
    if python_type:
        return handle_python_type(python_type)
    return None


def handle_properties(json_value):
    result = {}
    properties = json_value.get("properties", {})
    for key, value in properties.items():
        result[key] = recurse(value)
    return result


def handle_python_type(python_type):
    result = {}

    match python_type:
        case "Dict[str, FeatureScoresForAttribute]":
            return {
                "<user_defined_json_key>": recurse(
                    DEFINITIONS.get("FeatureScoresForAttribute")
                )
            }
        case "Dict[str, List[FeatureForAttribute]]":
            return {
                "<user_defined_json_key>": [
                    recurse(DEFINITIONS.get("FeatureForAttribute"))
                ]
            }
        case "Dict[str, List[FeatureForAttributeWithAttributes]]":
            return {
                "<user_defined_json_key>": [
                    recurse(DEFINITIONS.get("FeatureForAttributeWithAttributes"))
                ]
            }
        case "Dict[str, List[FeatureForGetEntity]]":
            return {
                "<user_defined_json_key>": [
                    recurse(DEFINITIONS.get("FeatureForGetEntity"))
                ]
            }
        case "Dict[str, List[MatchInfoForAttribute]]":
            return {
                "<user_defined_json_key>": [
                    recurse(DEFINITIONS.get("MatchInfoForAttribute"))
                ]
            }
        case "Dict[str, object]":
            return {
                "<user_record_json_key_1>": "user_record_json_value_1",
                "<user_record_json_key_2>": "user_record_json_value_2",
            }
        case _:
            print(f"Error: Bad 'pythonType:' {python_type}")
            raise NotImplementedError
    return result


def handle_ref(json_value):
    return recurse(DEFINITIONS.get(json_value.get("ref")))


def handle_type(json_value):
    return json_value.get("type")


def recurse(json_value):
    if "metadata" in json_value:
        result = handle_metadata(json_value)
        if result:
            return result

    if "type" in json_value:
        return handle_type(json_value)

    if "ref" in json_value:
        return handle_ref(json_value)

    if "properties" in json_value:
        return handle_properties(json_value)

    if "elements" in json_value:
        return handle_elements(json_value)

    return {}


# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


def is_json_subset(subset_json, full_json):
    """
    Checks if one JSON object (subset_json) is a subset of another (full_json).

    Args:
        subset_json (dict or list): The potential subset JSON.
        full_json (dict or list): The JSON to check against.

    Returns:
        bool: True if subset_json is a subset of full_json, False otherwise.
    """
    if isinstance(subset_json, dict):
        if not isinstance(full_json, dict):
            return False
        for key, value in subset_json.items():
            if key not in full_json:
                return False
            if not is_json_subset(value, full_json[key]):
                return False
        return True
    elif isinstance(subset_json, list):
        if not isinstance(full_json, list):
            return False
        for item in subset_json:
            if item not in full_json:
                return False
        return True
    else:  # Primitive types (int, str, bool, float, None)
        return subset_json == full_json


def path_to_testdata(filename: str) -> str:
    current_path = pathlib.Path(__file__).parent.resolve()
    result = os.path.abspath("{0}/testdata/{1}".format(current_path, filename))
    return result


def infer_json_type_definition(example_json: str) -> str:
    try:
        cmd_echo_result = subprocess.run(
            ["echo", example_json],
            capture_output=True,
            text=True,
            check=True,
        )

        cmd_jtd_infer_result = subprocess.run(
            ["jtd-infer"],
            input=cmd_echo_result.stdout,
            capture_output=True,
            text=True,
            check=True,
        )

        return cmd_jtd_infer_result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Stderr: {e.stderr}")
    except FileNotFoundError:
        print("Error: The specified command was not found.")

    return ""


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":

    # Read JSON from file.

    INPUT_FILENAME = "./senzingapi-RFC8927.json"
    with open(INPUT_FILENAME, "r", encoding="utf-8") as input_file:
        DATA = json.load(input_file)

    DEFINITIONS = DATA.get("definitions", {})

    # Recurse through dictionary.

    for requested_json_key in GLOBAL_JSON_KEYS:
        json_value = DEFINITIONS.get(requested_json_key)

        # Short-circuit when JSON key not found.

        if json_value is None:
            print(f"Could not find JSON key: {requested_json_key}")
            continue

        SCHEMA[requested_json_key] = recurse(json_value)

    example_json = '{"DATA_SOURCES":[{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1}]}'
    example_json = '{"AFFECTED_ENTITIES": [{"ENTITY_ID": "int32"}], "DATA_SOURCE": "string", "INTERESTING_ENTITIES": {"ENTITIES": [{"DEGREES": "int32", "ENTITY_ID": "int32", "FLAGS": ["string"], "SAMPLE_RECORDS": [{"DATA_SOURCE": "string", "FLAGS": ["string"], "RECORD_ID": "string"}]}], "NOTICES": [{"CODE": "string", "DESCRIPTION": "string"}]}, "RECORD_ID": "string"}'
    xschema = infer_json_type_definition(example_json)
    print(xschema)

    full_json = SCHEMA.get("SzEngineDeleteRecordResponse")
    print(json.dumps(full_json))

    print(is_json_subset(example_json, full_json))
