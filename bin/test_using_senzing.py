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

from senzing import SzAbstractFactory, SzEngineFlags, SzError
from senzing_core import SzAbstractFactoryCore

ERROR_COUNT = 0

# -----------------------------------------------------------------------------
# Functions to process RFC8927.json file and create SCHEMA variable.
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
# Functions to compare JSON vs the RFC8927 schema.
# -----------------------------------------------------------------------------


def add_records(sz_abstract_factory: SzAbstractFactory):

    filenames = [
        "customers.jsonl",
        "reference.jsonl",
        "watchlist.jsonl",
    ]

    sz_engine = sz_abstract_factory.create_engine()
    sz_config_manager = sz_abstract_factory.create_configmanager()

    # Register datasources.  TODO: fix underlying database.

    current_config_id = sz_config_manager.get_default_config_id()
    sz_config = sz_config_manager.create_config_from_config_id(current_config_id)

    for data_source in ("CUSTOMERS", "REFERENCE", "WATCHLIST"):
        sz_config.register_data_source(data_source)

    new_config = sz_config.export()
    new_config_id = sz_config_manager.register_config(
        new_config, "sz-sdk-json-type-definition"
    )
    sz_config_manager.replace_default_config_id(current_config_id, new_config_id)
    sz_abstract_factory.reinitialize(new_config_id)

    # Add records.

    flags = SzEngineFlags.SZ_ADD_RECORD_DEFAULT_FLAGS

    current_path = pathlib.Path(__file__).parent.resolve()
    for filename in filenames:
        file_path = os.path.abspath(
            "{0}/../testdata/truthsets/{1}".format(current_path, filename)
        )
        with open(file_path, "r", encoding="utf-8") as input_file:
            for line in input_file:
                line_as_dict = json.loads(line)
                data_source = line_as_dict.get("DATA_SOURCE")
                record_id = line_as_dict.get("RECORD_ID")
                response = sz_engine.add_record(data_source, record_id, line, flags)
                test_this(
                    f"Add record: {filename}/{data_source}/{record_id}",
                    "SzEngineAddRecordResponse",
                    response,
                )


def compare_static(sz_abstract_factory: SzAbstractFactory):

    sz_config_manager = sz_abstract_factory.create_configmanager()
    sz_config = sz_config_manager.create_config_from_template()
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    sz_engine = sz_abstract_factory.create_engine()
    sz_product = sz_abstract_factory.create_product()

    # Define testcases

    testcases = [
        {
            "testcase": "sz_config.export()",
            "response": "SzConfigExportResponse",
        },
        {
            "testcase": "sz_config.get_data_source_registry()",
            "response": "SzConfigGetDataSourceRegistryResponse",
        },
        {
            "testcase": "sz_config_manager.get_config_registry()",
            "response": "SzConfigManagerGetConfigRegistryResponse",
        },
        {
            "testcase": 'sz_config.register_data_source("A_DATASOURCE_NAME")',
            "response": "SzConfigRegisterDataSourceResponse",
        },
        {
            "testcase": 'sz_config.unregister_data_source("A_DATASOURCE_NAME")',
            "response": "SzConfigUnregisterDataSourceResponse",
        },
        {
            "testcase": "sz_diagnostic.check_repository_performance(2)",
            "response": "SzDiagnosticCheckRepositoryPerformanceResponse",
        },
        # {
        #     "testcase": "sz_diagnostic.get_feature(1)",
        #     "response": "SzDiagnosticGetFeatureResponse",
        # },
        {
            "testcase": "sz_diagnostic.get_repository_info()",
            "response": "SzDiagnosticGetRepositoryInfoResponse",
        },
        {
            "testcase": "sz_engine.get_stats()",
            "response": "SzEngineGetStatsResponse",
        },
        {
            "testcase": "sz_product.get_license()",
            "response": "SzProductGetLicenseResponse",
        },
        {
            "testcase": "sz_product.get_version()",
            "response": "SzProductGetVersionResponse",
        },
    ]

    for testcase in testcases:
        test_this(
            testcase.get("testcase"),
            testcase.get("response"),
            eval(testcase.get("testcase")),
        )


# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


def test_this(test_name, title, response):
    if response:
        json_schema = SCHEMA.get(title)
        compare_to_schema(test_name, title, json_schema, json.loads(response))


def compare_to_schema(test_name, json_path, schema, fragment):
    global ERROR_COUNT

    if isinstance(fragment, list):
        if not isinstance(schema, list):
            ERROR_COUNT += 1
            error_message(test_name, json_path, "Missing list", schema, fragment)
            return
        schema_list = schema[0]
        index = 0
        for x in fragment:
            index += 1
            compare_to_schema(test_name, f"{json_path}.{index}", schema_list, x)
        return

    if isinstance(fragment, dict):
        if not isinstance(schema, dict):
            ERROR_COUNT += 1
            error_message(test_name, json_path, "Missing dict", schema, fragment)
            return
        for key, value in fragment.items():
            schema_value = schema.get(key, {})
            compare_to_schema(test_name, f"{json_path}.{key}", schema_value, value)
        return

    if isinstance(fragment, int):
        if not schema == "int32":
            ERROR_COUNT += 1
            error_message(
                test_name,
                json_path,
                "Incorrect specification for int",
                schema,
                fragment,
            )
        return

    if isinstance(fragment, str):
        if not schema == "string":
            error_message(
                test_name,
                json_path,
                "Incorrect specification for string",
                schema,
                fragment,
            )
        return

    if fragment is None:
        return

    # If ending up here, there's an error.

    ERROR_COUNT += 1
    error_message(test_name, json_path, "Unknown value", schema, fragment)


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


def output(indentation, message):
    print(f"{"    " * indentation}{message}")


def error_message(test_name, json_path, message, schema, fragment):
    output(0, test_name)
    output(1, f"Path: {json_path}")
    output(2, "Error:")
    output(3, message)
    output(3, f"schema: {schema}")
    output(3, f"  json: {fragment}")


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

    # Create SzAbstractFactory

    instance_name = "Example"
    settings = {
        "PIPELINE": {
            "CONFIGPATH": "/etc/opt/senzing",
            "RESOURCEPATH": "/opt/senzing/er/resources",
            "SUPPORTPATH": "/opt/senzing/data",
        },
        "SQL": {"CONNECTION": "sqlite3://na:na@/tmp/sqlite/G2C.db"},
    }

    try:
        sz_abstract_factory = SzAbstractFactoryCore(instance_name, settings)
    except SzError as err:
        print(f"\nERROR: {err}\n")

    # Xxxxxx

    add_records(sz_abstract_factory)
    compare_static(sz_abstract_factory)

    # example_json = '{"DATA_SOURCES":[{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1},{"DSRC_CODE":"blank","DSRC_ID":1}]}'
    # example_json = '{"AFFECTED_ENTITIES":[{"ENTITY_ID":"100002"}],"DATA_SOURCE":"TEST","INTERESTING_ENTITIES":{"ENTITIES":[]},"RECORD_ID":"DELETE_TEST"}'
    # example_json = '{"AFFECTED_ENTITIES": [{"ENTITY_ID": "int32"}], "DATA_SOURCE": "string", "INTERESTING_ENTITIES": {"ENTITIES": [{"DEGREES": "int32", "ENTITY_ID": "int32", "FLAGS": ["string"], "SAMPLE_RECORDS": [{"DATA_SOURCE": "string", "FLAGS": ["string"], "RECORD_ID": "string"}]}], "NOTICES": [{"CODE": "string", "DESCRIPTION": "string"}]}, "RECORD_ID": "string"}'

    # title = "SzEngineDeleteRecordResponse"
    # json_schema = SCHEMA.get(title)

    # xschema = infer_json_type_definition(example_json)
    # print(xschema)
    # print(json.dumps(json_schema))

    # print(is_json_subset(example_json, json_schema))
    # test_name = "bob"
    # compare_to_schema(test_name, title, json_schema, json.loads(example_json))

if ERROR_COUNT > 0:
    sys.exit(1)
