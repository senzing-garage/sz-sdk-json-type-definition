#! /usr/bin/env python3

# pylint: disable=duplicate-code

import json

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""


VARIABLE_JSON_KEY = "<user_defined_json_key>"
DEFINITIONS = {}
INDENT = "&nbsp;&nbsp;&nbsp;&nbsp;"

GLOBAL_OUTPUT_DIRECTORY = "./docs/responses-html"
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

# -----------------------------------------------------------------------------
# Functions to process RFC8927.json file and create SCHEMA variable.
# -----------------------------------------------------------------------------


def handle_json_elements(json_value):
    elements = json_value.get("elements", {})
    result = recurse_json(elements)
    return [result]


def handle_json_metadata(json_value):
    metadata = json_value.get("metadata")
    python_type = metadata.get("pythonType")
    if python_type:
        return handle_json_python_type(python_type)
    return None


def handle_json_properties(json_value):
    result = {}
    properties = json_value.get("properties", {})
    for key, value in properties.items():
        result[key] = recurse_json(value)
    return result


def handle_json_python_type(python_type):
    result = {}

    match python_type:
        case "Dict[str, FeatureScoresForAttribute]":
            return {
                VARIABLE_JSON_KEY: recurse_json(
                    DEFINITIONS.get("FeatureScoresForAttribute")
                )
            }
        case "Dict[str, List[FeatureDescriptionValue]]":
            return {
                VARIABLE_JSON_KEY: [
                    recurse_json(DEFINITIONS.get("FeatureDescriptionValue"))
                ]
            }
        case "Dict[str, List[FeatureForAttribute]]":
            return {
                VARIABLE_JSON_KEY: [
                    recurse_json(DEFINITIONS.get("FeatureForAttribute"))
                ]
            }
        case "Dict[str, List[FeatureForAttributeWithAttributes]]":
            return {
                VARIABLE_JSON_KEY: [
                    recurse_json(DEFINITIONS.get("FeatureForAttributeWithAttributes"))
                ]
            }
        case "Dict[str, List[FeatureForGetEntity]]":
            return {
                VARIABLE_JSON_KEY: [
                    recurse_json(DEFINITIONS.get("FeatureForGetEntity"))
                ]
            }
        case "Dict[str, List[MatchInfoForAttribute]]":
            return {
                VARIABLE_JSON_KEY: [
                    recurse_json(DEFINITIONS.get("MatchInfoForAttribute"))
                ]
            }
        case "Dict[str, str]":
            return {
                VARIABLE_JSON_KEY: "string",
            }
        case "Dict[str, object]":
            return {
                VARIABLE_JSON_KEY: "string",
            }
        case "Dict[str, int]":
            return {
                VARIABLE_JSON_KEY: "int32",
            }
        case "object":
            return "object"
        case _:
            print(f"Error: Bad 'pythonType:' {python_type}")
            raise NotImplementedError
    return result


def handle_json_ref(json_value):
    return recurse_json(DEFINITIONS.get(json_value.get("ref")))


def handle_json_type(json_value):
    return json_value.get("type")


def recurse_json(json_value) -> dict:
    if "metadata" in json_value:
        result = handle_json_metadata(json_value)
        if result:
            return result

    if "type" in json_value:
        return handle_json_type(json_value)

    if "ref" in json_value:
        return handle_json_ref(json_value)

    if "properties" in json_value:
        return handle_json_properties(json_value)

    if "elements" in json_value:
        return handle_json_elements(json_value)

    return {}


# -----------------------------------------------------------------------------
# --- Make HTML
# -----------------------------------------------------------------------------


def handle_html_dict(level, json_value) -> str:
    indent1 = INDENT * level
    indent2 = INDENT * (level + 1)

    popup = "_"

    result = "{<br>\n"
    for key, value in json_value.items():
        xxx = recurse_html(level + 2, value)
        result += f'\n{indent2}<span href="{popup}" title="bob">{key}</span>: {xxx}'
    result += f"{indent1}}}<br>\n"

    return result


def handle_html_list(level, json_value) -> str:
    indent1 = INDENT * level
    indent2 = INDENT * (level + 1)

    result = f"[<br>\n{indent2}"
    for value in json_value:
        xxx = recurse_html(level + 2, value)
        result += xxx
    result += f"{indent1}]<br>\n"
    return result


def handle_html_misc(level, json_value) -> str:
    return f"{json_value},<br>\n"


def recurse_html(level: int, json_value) -> str:
    result = ""
    if isinstance(json_value, dict):
        result += handle_html_dict(level, json_value)
    elif isinstance(json_value, list):
        result += handle_html_list(level, json_value)
    else:
        result += handle_html_misc(level, json_value)
    return result


def make_html(input_dict: dict) -> str:

    print(json.dumps(input_dict))

    result = """<!DOCTYPE html>
<html>
<body>
"""

    result += recurse_html(0, input_dict)

    result += """
</body>
</html>
"""

    return result


# -----------------------------------------------------------------------------
# --- Main
# -----------------------------------------------------------------------------

# Read JSON from file.

INPUT_FILENAME = "./senzingapi-RFC8927.json"
with open(INPUT_FILENAME, "r", encoding="utf-8") as input_file:
    DATA = json.load(input_file)

DEFINITIONS = DATA.get("definitions", {})

# Recurse through dictionary.

for requested_json_key in GLOBAL_JSON_KEYS[9:10]:
    json_value = DEFINITIONS.get(requested_json_key)

    # Short-circuit when JSON key not found.

    if json_value is None:
        print(f"Could not find JSON key: {requested_json_key}")
        continue

    result = recurse_json(json_value)

    html = make_html(result)

    output_file = f"{GLOBAL_OUTPUT_DIRECTORY}/{requested_json_key}.html"
    with open(output_file, "w", encoding="utf-8") as json_file:
        json_file.write(html)
