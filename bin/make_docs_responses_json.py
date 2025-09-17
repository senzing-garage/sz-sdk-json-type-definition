#! /usr/bin/env python3

# pylint: disable=duplicate-code

import json

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

GLOBAL_OUTPUT_DIRECTORY = "./docs/responses-json"
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
                "user_defined_json_key": recurse(
                    DEFINITIONS.get("FeatureScoresForAttribute")
                )
            }
        case "Dict[str, List[FeatureDescriptionValue]]":
            return {
                "user_defined_json_key": recurse(
                    DEFINITIONS.get("FeatureDescriptionValue")
                )
            }
        case "Dict[str, List[FeatureForAttribute]]":
            return {
                "user_defined_json_key": [
                    recurse(DEFINITIONS.get("FeatureForAttribute"))
                ]
            }
        case "Dict[str, List[FeatureForAttributeWithAttributes]]":
            return {
                "user_defined_json_key": [
                    recurse(DEFINITIONS.get("FeatureForAttributeWithAttributes"))
                ]
            }
        case "Dict[str, List[FeatureForGetEntity]]":
            return {
                "user_defined_json_key": [
                    recurse(DEFINITIONS.get("FeatureForGetEntity"))
                ]
            }
        case "Dict[str, List[MatchInfoForAttribute]]":
            return {
                "user_defined_json_key": [
                    recurse(DEFINITIONS.get("MatchInfoForAttribute"))
                ]
            }
        case "Dict[str, int]":
            return {
                "user_defined_json_key": "int32",
            }
        case "Dict[str, object]":
            return {
                "user_defined_json_key": "object",
            }
        case "Dict[str, str]":
            return {
                "user_defined_json_key": "string",
            }
        case "object":
            return "object"
        case "string":
            return "string"
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
# --- Main
# -----------------------------------------------------------------------------

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

    result = recurse(json_value)

    output_file = f"{GLOBAL_OUTPUT_DIRECTORY}/{requested_json_key}.json"
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(result, json_file, indent=4)
