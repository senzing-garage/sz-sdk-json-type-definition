#! /usr/bin/env python3

# pylint: disable=duplicate-code

import json

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""


VARIABLE_JSON_KEY = "user_defined_json_key"
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


def recurse_json(level, key, value) -> str:

    result = ""

    if value.get("metadata", {}).get("pythonType"):
        result += handle_json_python_type(
            level, key, value.get("metadata", {}).get("description"), value
        )
    elif "type" in value:
        result += handle_json_type(level, key, value)
    elif "ref" in value:
        result += handle_json_ref(level, key, value)
    elif "properties" in value:
        result += handle_json_properties(level, key, value)
    elif "elements" in value:
        result += handle_json_elements(level, key, value)
    elif "metadata" in value:
        result += handle_json_metadata(level, key, value)

    return result


def html_println(level, message) -> str:
    return f"\n<br>{INDENT * level}{message}"


def make_json_key(key, description, suffix) -> str:
    result = suffix
    if description and key:
        result = f'"<a href="#" data-toggle="tooltip" data-placement="bottom" title="{description}">{key}</a>": {suffix}'
    elif key:
        result = f'"{key}": {suffix}'
    return result


def handle_json_elements(level, key, value) -> str:
    elements = value.get("elements", [])
    description = value.get("metadata", {}).get("description")
    result = html_println(level, make_json_key(key, description, "["))
    result += recurse_json(level + 1, None, elements)[:-1]
    result += html_println(level, "],")
    return result


def handle_json_metadata(level, key, json_value) -> str:
    result = ""
    metadata = json_value.get("metadata", {})
    python_type = metadata.get("pythonType")
    if python_type:
        description = metadata.get("description")
        result += handle_json_python_type(level, key, description, python_type)
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


def handle_json_dict(level, key, description, json_key):
    result = make_json_key(key, description, "{")
    result += recurse_json(level + 1, VARIABLE_JSON_KEY, DEFINITIONS.get(json_key, {}))[
        :-1
    ]
    result += html_println(level, "},")
    return html_println(level, result)


def handle_json_dict_list(level, key, description, json_key):
    result = make_json_key(key, description, "{")
    result += html_println(level + 1, f'"{VARIABLE_JSON_KEY}": [')
    result += recurse_json(level + 2, None, DEFINITIONS.get(json_key, {}))[:-1]
    result += html_println(level + 1, "]")
    result += html_println(level, "},")
    return html_println(level, result)


def handle_json_dict_data_type(level, key, description, data_type):
    result = make_json_key(key, description, "{")
    result += html_println(level + 1, f'"{VARIABLE_JSON_KEY}": "{data_type}"')
    result += html_println(level, "},")
    return html_println(level, result)


def handle_json_python_type(level, key, description, value) -> str:
    result = ""

    python_type = value.get("metadata", {}).get("pythonType")

    match python_type:
        case "Dict[str, FeatureScoresForAttribute]":
            return handle_json_dict(
                level, key, description, "FeatureScoresForAttribute"
            )
        case "Dict[str, List[FeatureDescriptionValue]]":
            return handle_json_dict_list(
                level, key, description, "FeatureDescriptionValue"
            )
        case "Dict[str, List[FeatureForAttribute]]":
            return handle_json_dict_list(level, key, description, "FeatureForAttribute")

        case "Dict[str, List[FeatureForAttributeWithAttributes]]":
            return handle_json_dict_list(
                level, key, description, "FeatureForAttributeWithAttributes"
            )
        case "Dict[str, List[FeatureForGetEntity]]":
            return handle_json_dict_list(level, key, description, "FeatureForGetEntity")
        case "Dict[str, List[MatchInfoForAttribute]]":
            return handle_json_dict_list(
                level, key, description, "MatchInfoForAttribute"
            )
        case "Dict[str, int]":
            return handle_json_dict_data_type(level, key, description, "int32")
        case "Dict[str, object]":
            return handle_json_dict_data_type(level, key, description, "object")
        case "Dict[str, str]":
            return handle_json_dict_data_type(level, key, description, "string")
        case "object":
            return html_println(level, f'"{key}": "object",')
        case "string":
            return html_println(level, f'"{key}": "string",')
        case _:
            print(f"Error: Bad 'pythonType:' {value}")
            raise NotImplementedError

    return result


def handle_json_ref(level, key, value) -> str:
    return recurse_json(level, key, DEFINITIONS.get(value.get("ref")))


def handle_json_type(level, key, value) -> str:
    data_type = value.get("type")
    description = value.get("metadata", {}).get("description")

    # html_value = ""
    # if description and key:
    #     html_value += f'"{data_type} - {description}",'
    # else:
    #     html_value += f'"{data_type}",'
    html_value = f'"{data_type}",'

    json_key = make_json_key(key, description, html_value)

    return html_println(level, json_key)


# -----------------------------------------------------------------------------
# --- Make HTML
# -----------------------------------------------------------------------------


def make_html(title: str, input_dict: dict) -> str:

    # HTML prefix.

    result = """<!DOCTYPE html>
<html>
<head>
    <style>
        body {background-color: White;}
        .code-block {font-family: "Courier New", Courier, monospace; background-color: LightGrey;}
    </style>
"""

    result += f"    <title>{title}</title>"

    result += """
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>
"""

    result += f"<h1>{title}</h1>"
    result += """
<div class="code-block">"""

    # HTML body.

    result += recurse_json(0, None, input_dict)[:-1]

    # HTML suffix.

    result += """
<br>&nbsp;
</div>
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

for requested_json_key in GLOBAL_JSON_KEYS:
    json_value = DEFINITIONS.get(requested_json_key)

    # Short-circuit when JSON key not found.

    if json_value is None:
        print(f"Could not find JSON key: {requested_json_key}")
        continue

    html = make_html(requested_json_key, json_value)

    output_file = f"{GLOBAL_OUTPUT_DIRECTORY}/{requested_json_key}.html"
    with open(output_file, "w", encoding="utf-8") as json_file:
        json_file.write(html)
