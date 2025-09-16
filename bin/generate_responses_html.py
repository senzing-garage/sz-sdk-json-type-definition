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
    "SzTestResponse",
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


def html_println(level, message) -> str:
    return f"\n<br>{INDENT * level}{message}"


def make_json_key(key, description, suffix) -> str:
    result = suffix
    if description and key:
        result = f'<a href="_" title="{description}">"{key}"</a>: {suffix}'
    elif key:
        result = f'"{key}": {suffix}'
    return result


def handle_json_elements(level, key, value) -> str:
    elements = value.get("elements", [])
    description = value.get("metadata", {}).get("description")
    result = html_println(level, make_json_key(key, description, "["))
    result += recurse_json(level + 1, None, elements)
    result = result[:-1]
    result += html_println(level, "],")
    return result


def handle_json_metadata(level, key, json_value) -> str:
    result = ""
    metadata = json_value.get("metadata")
    python_type = metadata.get("pythonType")
    if python_type:
        result += handle_json_python_type(level, key, python_type)
    return result


def handle_json_properties(level, key, json_value) -> str:
    properties = json_value.get("properties", {})
    description = json_value.get("metadata", {}).get("description")
    result = html_println(level, make_json_key(key, description, "{"))
    for key, value in properties.items():
        result += recurse_json(level + 1, key, value)
    result = result[:-1]
    result += html_println(level, "},")
    return result


def handle_json_python_type(level, key, value) -> str:
    result = ""

    match value:
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
        case "string":
            return "string"
        case _:
            print(f"Error: Bad 'pythonType:' {value}")
            raise NotImplementedError
    return result


def handle_json_ref(level, key, value) -> str:
    # description = value.get("metadata", {}).get("description")
    # result = html_println(level, make_json_key(key, description, ""))
    result = recurse_json(level, key, DEFINITIONS.get(value.get("ref")))
    return result


def handle_json_type(level, key, value) -> str:
    data_type = value.get("type")
    description = value.get("metadata", {}).get("description")

    html_value = ""
    if description and key:
        html_value += f'"{data_type} - {description}",'
    else:
        html_value += f'"{data_type}",'

    json_key = make_json_key(key, description, html_value)

    return html_println(level, json_key)


def recurse_json(level, key, value) -> str:

    print(f"\n>>>>>> level: {level};  json_value: {json.dumps(value)}")
    result = ""

    if "type" in value:
        print(f">>>>>>>>> level: {level};  type")
        result += handle_json_type(level, key, value)

    elif "ref" in value:
        print(f">>>>>>>>> level: {level};  ref")
        result += handle_json_ref(level, key, value)

    elif "properties" in value:
        print(f">>>>>>>>> level: {level};  properties")
        result += handle_json_properties(level, key, value)

    elif "elements" in value:
        print(f">>>>>>>>> level: {level};  elements")
        result += handle_json_elements(level, key, value)

    elif "metadata" in value:
        print(f">>>>>>>>> level: {level};  metadata")
        result += handle_json_metadata(level, key, value)

    return result


# -----------------------------------------------------------------------------
# --- Make HTML
# -----------------------------------------------------------------------------


def make_html(input_dict: dict) -> str:

    print(f">>>> Initial JSON: \n{json.dumps(input_dict)}")

    # HTML prefix.

    result = """<!DOCTYPE html>
<html>
<body>
"""

    # HTML body.

    result += recurse_json(0, None, input_dict)[:-1]

    # HTML suffix.

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

for requested_json_key in GLOBAL_JSON_KEYS[10:11]:
    json_value = DEFINITIONS.get(requested_json_key)

    # Short-circuit when JSON key not found.

    if json_value is None:
        print(f"Could not find JSON key: {requested_json_key}")
        continue

    html = make_html(json_value)

    output_file = f"{GLOBAL_OUTPUT_DIRECTORY}/{requested_json_key}.html"
    with open(output_file, "w", encoding="utf-8") as json_file:
        json_file.write(html)
