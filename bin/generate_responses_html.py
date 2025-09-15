#! /usr/bin/env python3

# pylint: disable=duplicate-code


import json

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""


VARIABLE_JSON_KEY = "<user_defined_json_key>"
DEFINITIONS = {}
INDENT = "&nbsp;&nbsp;"

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


def handle_json_elements(level, metadata, key, json_value) -> str:
    result = ""
    metadata = json_value.get("metadata")
    elements = json_value.get("elements", [])
    if key:
        result += html_println(level, f'"{key}": [')
    else:
        result += html_println(level, "[")
    result += recurse_json(level + 1, metadata, None, elements)
    result = result[:-1]
    result += html_println(level, "],")
    return result


def handle_json_metadata(level, metadata, key, json_value) -> str:
    result = ""
    metadata = json_value.get("metadata")
    python_type = metadata.get("pythonType")
    if python_type:
        result += handle_json_python_type(level, metadata, key, python_type)
    return result


def handle_json_properties(level, metadata, key, json_value) -> str:
    metadata = json_value.get("metadata")
    properties = json_value.get("properties", {})
    result = html_println(level, "{")
    for key, value in properties.items():
        result += recurse_json(level + 1, metadata, key, value)
    result = result[:-1]
    result += html_println(level, "},")
    return result


def handle_json_python_type(level, metadata, key, value) -> str:
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


def handle_json_ref(level, metadata, key, value) -> str:
    print(
        f">>>>>>>> handle_json_ref: level {level}, metadata: {metadata}, key: {key}, json_value: {value}"
    )
    message = ""
    description = value.get("metadata", {}).get("description")

    if description and key:
        message += f'<a href="_" title="{description}">"{key}"</a>: '

    elif key:
        message += f'"{key}": '

    message += recurse_json(level + 1, metadata, key, DEFINITIONS.get(value.get("ref")))
    return html_println(level, message)


def handle_json_type(level, metadata, key, value) -> str:
    data_type = value.get("type")
    description = value.get("metadata", {}).get("description")

    html_value = ""
    if description and key:
        html_value += f'"{data_type} - {description}"'
    else:
        html_value += f'"{data_type}"'

    message = ""
    if description and key:
        message += f'<a href="_" title="{description}">"{key}"</a>: {html_value},'
    elif key:
        message += f'"{key}": {html_value},'
    else:
        message += f"{html_value},"

    return html_println(level, message)


def recurse_json(level, metadata, key, value) -> str:

    print(f"\n>>>>>> level: {level};  json_value: {json.dumps(value)}")
    result = ""

    if "type" in value:
        print(f">>>>>>>>> level: {level};  type")
        result += handle_json_type(level, metadata, key, value)

    elif "ref" in value:
        print(f">>>>>>>>> level: {level};  ref")
        result += handle_json_ref(level, metadata, key, value)

    elif "properties" in value:
        print(f">>>>>>>>> level: {level};  properties")
        result += handle_json_properties(level, metadata, key, value)

    elif "elements" in value:
        print(f">>>>>>>>> level: {level};  elements")
        result += handle_json_elements(level, metadata, key, value)

    elif "metadata" in value:
        print(f">>>>>>>>> level: {level};  metadata")
        result += handle_json_metadata(level, metadata, key, value)

    print(f"\n<<<<<< level: {level}; json_value: {json.dumps(value)}; result: {result}")

    return result


# -----------------------------------------------------------------------------
# --- Make HTML
# -----------------------------------------------------------------------------


# def handle_html_dict(level, json_value) -> str:
#     indent1 = INDENT * (level - 1)
#     indent2 = INDENT * (level + 1)

#     popup = "_"

#     result = "{<br>\n"
#     for key, value in json_value.items():
#         xxx = recurse_html(level + 2, value)
#         result += f'\n{indent2}<a href="{popup}" title="bob">{key}</a>: {xxx}'
#     result += f"{indent1}}}<br>\n"

#     return result


# def handle_html_list(level, json_value) -> str:
#     indent1 = INDENT * (level - 1)
#     indent2 = INDENT * (level + 1)

#     result = "[<br>\n"
#     for value in json_value:
#         xxx = recurse_html(level + 2, value)
#         result += f"{indent2}{xxx}"
#     result += f"{indent1}]<br>\n"
#     return result


# def handle_html_misc(level, json_value) -> str:
#     return f"{json_value},<br>\n"


# def recurse_html(level: int, json_value) -> str:
#     result = ""
#     if isinstance(json_value, dict):
#         result += handle_html_dict(level, json_value)
#     elif isinstance(json_value, list):
#         result += handle_html_list(level, json_value)
#     else:
#         result += handle_html_misc(level, json_value)
#     return result


def make_html(input_dict: dict) -> str:

    print(f">>>> Initial JSON: \n{json.dumps(input_dict)}")

    result = """<!DOCTYPE html>
<html>
<body>
"""

    result += recurse_json(0, None, None, input_dict)[:-1]

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

for requested_json_key in GLOBAL_JSON_KEYS[0:1]:
    json_value = DEFINITIONS.get(requested_json_key)

    # Short-circuit when JSON key not found.

    if json_value is None:
        print(f"Could not find JSON key: {requested_json_key}")
        continue

    html = make_html(json_value)

    output_file = f"{GLOBAL_OUTPUT_DIRECTORY}/{requested_json_key}.html"
    with open(output_file, "w", encoding="utf-8") as json_file:
        json_file.write(html)
