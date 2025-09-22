#! /usr/bin/env python3

# pylint: disable=duplicate-code

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json
import os
import pathlib
import random
import sys

from senzing import SzAbstractFactory, SzEngineFlags, SzError
from senzing_core import SzAbstractFactoryCore

# Global variables.

DEBUG = 0
DEFINITIONS = {}
ERROR_COUNT = 0
GLOBAL_OUTPUT_DIRECTORY = "./docs/json-responses"
HR_START = ">" * 80
HR_STOP = "<" * 80
LOADED_ENTITY_IDS = []
LOADED_RECORD_KEYS = []
SCHEMA = {}
VARIABLE_JSON_KEY = "<user_defined_json_key>"

FLAGS = [
    SzEngineFlags.SZ_WITH_INFO,  # 1
    SzEngineFlags.SZ_ADD_RECORD_DEFAULT_FLAGS,  # 2
    SzEngineFlags.SZ_DELETE_RECORD_DEFAULT_FLAGS,  # 3
    SzEngineFlags.SZ_ENTITY_BRIEF_DEFAULT_FLAGS,  # 4
    SzEngineFlags.SZ_ENTITY_CORE_FLAGS,  # 5
    SzEngineFlags.SZ_ENTITY_DEFAULT_FLAGS,  # 6
    SzEngineFlags.SZ_ENTITY_INCLUDE_ALL_FEATURES,  # 7
    SzEngineFlags.SZ_ENTITY_INCLUDE_ALL_RELATIONS,  # 8
    SzEngineFlags.SZ_ENTITY_INCLUDE_DISCLOSED_RELATIONS,  # 9
    SzEngineFlags.SZ_ENTITY_INCLUDE_ENTITY_NAME,  # 10
    SzEngineFlags.SZ_ENTITY_INCLUDE_FEATURE_STATS,  # 11
    SzEngineFlags.SZ_ENTITY_INCLUDE_INTERNAL_FEATURES,  # 12
    SzEngineFlags.SZ_ENTITY_INCLUDE_NAME_ONLY_RELATIONS,  # 13
    SzEngineFlags.SZ_ENTITY_INCLUDE_POSSIBLY_RELATED_RELATIONS,  # 14
    SzEngineFlags.SZ_ENTITY_INCLUDE_POSSIBLY_SAME_RELATIONS,  # 15
    SzEngineFlags.SZ_ENTITY_INCLUDE_RECORD_DATA,  # 16
    SzEngineFlags.SZ_ENTITY_INCLUDE_RECORD_DATES,  # 17
    SzEngineFlags.SZ_ENTITY_INCLUDE_RECORD_FEATURE_DETAILS,  # 18
    SzEngineFlags.SZ_ENTITY_INCLUDE_RECORD_FEATURE_STATS,  # 19
    SzEngineFlags.SZ_ENTITY_INCLUDE_RECORD_FEATURES,  # 20
    SzEngineFlags.SZ_ENTITY_INCLUDE_RECORD_JSON_DATA,  # 21
    SzEngineFlags.SZ_ENTITY_INCLUDE_RECORD_MATCHING_INFO,  # 22
    SzEngineFlags.SZ_ENTITY_INCLUDE_RECORD_SUMMARY,  # 23
    SzEngineFlags.SZ_ENTITY_INCLUDE_RECORD_TYPES,  # 24
    SzEngineFlags.SZ_ENTITY_INCLUDE_RECORD_UNMAPPED_DATA,  # 25
    SzEngineFlags.SZ_ENTITY_INCLUDE_RELATED_ENTITY_NAME,  # 26
    SzEngineFlags.SZ_ENTITY_INCLUDE_RELATED_MATCHING_INFO,  # 27
    SzEngineFlags.SZ_ENTITY_INCLUDE_RELATED_RECORD_DATA,  # 28
    SzEngineFlags.SZ_ENTITY_INCLUDE_RELATED_RECORD_SUMMARY,  # 29
    SzEngineFlags.SZ_ENTITY_INCLUDE_RELATED_RECORD_TYPES,  # 30
    SzEngineFlags.SZ_ENTITY_INCLUDE_REPRESENTATIVE_FEATURES,  # 31
    SzEngineFlags.SZ_EXPORT_DEFAULT_FLAGS,  # 32
    SzEngineFlags.SZ_EXPORT_INCLUDE_ALL_ENTITIES,  # 33
    SzEngineFlags.SZ_EXPORT_INCLUDE_ALL_HAVING_RELATIONSHIPS,  # 34
    SzEngineFlags.SZ_EXPORT_INCLUDE_DISCLOSED,  # 35
    SzEngineFlags.SZ_EXPORT_INCLUDE_MULTI_RECORD_ENTITIES,  # 36
    SzEngineFlags.SZ_EXPORT_INCLUDE_NAME_ONLY,  # 37
    SzEngineFlags.SZ_EXPORT_INCLUDE_POSSIBLY_RELATED,  # 38
    SzEngineFlags.SZ_EXPORT_INCLUDE_POSSIBLY_SAME,  # 39
    SzEngineFlags.SZ_EXPORT_INCLUDE_SINGLE_RECORD_ENTITIES,  # 40
    SzEngineFlags.SZ_FIND_INTERESTING_ENTITIES_DEFAULT_FLAGS,  # 41
    SzEngineFlags.SZ_FIND_NETWORK_DEFAULT_FLAGS,  # 42
    SzEngineFlags.SZ_FIND_NETWORK_INCLUDE_MATCHING_INFO,  # 43
    SzEngineFlags.SZ_FIND_PATH_DEFAULT_FLAGS,  # 44
    SzEngineFlags.SZ_FIND_PATH_INCLUDE_MATCHING_INFO,  # 45
    SzEngineFlags.SZ_FIND_PATH_STRICT_AVOID,  # 46
    SzEngineFlags.SZ_HOW_ENTITY_DEFAULT_FLAGS,  # 47
    SzEngineFlags.SZ_INCLUDE_FEATURE_SCORES,  # 48
    SzEngineFlags.SZ_INCLUDE_MATCH_KEY_DETAILS,  # 49
    SzEngineFlags.SZ_NO_FLAGS,  # 50
    SzEngineFlags.SZ_RECORD_DEFAULT_FLAGS,  # 51
    SzEngineFlags.SZ_RECORD_PREVIEW_DEFAULT_FLAGS,  # 52
    SzEngineFlags.SZ_REEVALUATE_ENTITY_DEFAULT_FLAGS,  # 53
    SzEngineFlags.SZ_REEVALUATE_RECORD_DEFAULT_FLAGS,  # 54
    SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_ALL,  # 55
    SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_DEFAULT_FLAGS,  # 56
    SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_MINIMAL_ALL,  # 57
    SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_MINIMAL_STRONG,  # 58
    SzEngineFlags.SZ_SEARCH_BY_ATTRIBUTES_STRONG,  # 59
    SzEngineFlags.SZ_SEARCH_INCLUDE_ALL_CANDIDATES,  # 60
    SzEngineFlags.SZ_SEARCH_INCLUDE_ALL_ENTITIES,  # 61
    SzEngineFlags.SZ_SEARCH_INCLUDE_NAME_ONLY,  # 62
    SzEngineFlags.SZ_SEARCH_INCLUDE_POSSIBLY_RELATED,  # 63
    SzEngineFlags.SZ_SEARCH_INCLUDE_POSSIBLY_SAME,  # 64
    SzEngineFlags.SZ_SEARCH_INCLUDE_REQUEST_DETAILS,  # 65
    SzEngineFlags.SZ_SEARCH_INCLUDE_REQUEST,  # 66
    SzEngineFlags.SZ_SEARCH_INCLUDE_RESOLVED,  # 67
    SzEngineFlags.SZ_SEARCH_INCLUDE_STATS,  # 68
    SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS,  # 69
    SzEngineFlags.SZ_WHY_ENTITIES_DEFAULT_FLAGS,  # 70
    SzEngineFlags.SZ_WHY_RECORD_IN_ENTITY_DEFAULT_FLAGS,  # 71
    SzEngineFlags.SZ_WHY_RECORDS_DEFAULT_FLAGS,  # 72
    SzEngineFlags.SZ_WHY_SEARCH_DEFAULT_FLAGS,  # 73
]

FLAGS_LEN = len(FLAGS)

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
    # "SzEngineExportCsvEntityReportCsvColumnList",
    # "SzEngineFetchNextResponse",
    "SzEngineFindInterestingEntitiesByEntityIdResponse",
    "SzEngineFindInterestingEntitiesByRecordIdResponse",
    # "SzEngineFindNetworkByEntityIdEntityIds",
    "SzEngineFindNetworkByEntityIdResponse",
    # "SzEngineFindNetworkByRecordIdRecordKeys",
    "SzEngineFindNetworkByRecordIdResponse",
    # "SzEngineFindPathByEntityIdAvoidEntityIds",
    # "SzEngineFindPathByEntityIdRequiredDataSources",
    "SzEngineFindPathByEntityIdResponse",
    # "SzEngineFindPathByRecordIdAvoidRecordKeys",
    # "SzEngineFindPathByRecordIdRequiredDataSources",
    "SzEngineFindPathByRecordIdResponse",
    "SzEngineGetEntityByEntityIdResponse",
    "SzEngineGetEntityByRecordIdResponse",
    "SzEngineGetRecordPreviewResponse",
    "SzEngineGetRecordResponse",
    "SzEngineGetRedoRecordResponse",
    "SzEngineGetStatsResponse",
    # "SzEngineGetVirtualEntityByRecordIdRecordKeys",
    "SzEngineGetVirtualEntityByRecordIdResponse",
    "SzEngineHowEntityByEntityIdResponse",
    "SzEngineProcessRedoRecordResponse",
    "SzEngineReevaluateEntityResponse",
    "SzEngineReevaluateRecordResponse",
    # "SzEngineSearchByAttributesAttributes",
    "SzEngineSearchByAttributesResponse",
    # "SzEngineSearchByAttributesSearchProfile",
    # "SzEngineStreamExportJsonEntityReportResponse",
    "SzEngineWhyEntitiesResponse",
    "SzEngineWhyRecordInEntityResponse",
    "SzEngineWhyRecordsResponse",
    # "SzEngineWhySearchAttributes",
    "SzEngineWhySearchResponse",
    # "SzEngineWhySearchSearchProfile",
    "SzProductGetLicenseResponse",
    "SzProductGetVersionResponse",
]

SEARCH_RECORDS = [
    {
        "NAME_FULL": "Susan Moony",
        "DATE_OF_BIRTH": "15/6/1998",
        "SSN_NUMBER": "521212123",
    },
    {
        "NAME_FIRST": "Robert",
        "NAME_LAST": "Smith",
        "ADDR_FULL": "123 Main Street Las Vegas NV 89132",
    },
    {
        "NAME_FIRST": "Makio",
        "NAME_LAST": "Yamanaka",
        "ADDR_FULL": "787 Rotary Drive Rotorville FL 78720",
    },
]

# -----------------------------------------------------------------------------
# Functions to process RFC8927.json file and create SCHEMA variable.
# -----------------------------------------------------------------------------


def handle_json_elements(json_value):
    """Unwrap an RFC8927 'element'."""
    elements = json_value.get("elements", {})
    result = recurse_json(elements)
    return [result]


def handle_json_metadata(json_value):
    """Unwrap an RFC8927 'metadata'."""
    metadata = json_value.get("metadata")
    python_type = metadata.get("pythonType")
    if python_type:
        return handle_json_python_type(python_type)
    return None


def handle_json_properties(json_value):
    """Unwrap an RFC8927 'properties'."""
    result = {}
    properties = json_value.get("properties", {})
    for key, value in properties.items():
        result[key] = recurse_json(value)
    return result


def handle_json_python_type(python_type):
    """Unwrap based on custom datatype."""

    result = {}
    match python_type:
        case "Dict[str, FeatureScoresForAttribute]":
            return {VARIABLE_JSON_KEY: recurse_json(DEFINITIONS.get("FeatureScoresForAttribute"))}
        case "Dict[str, List[FeatureDescriptionValue]]":
            return {VARIABLE_JSON_KEY: [recurse_json(DEFINITIONS.get("FeatureDescriptionValue"))]}
        case "Dict[str, List[FeatureForAttribute]]":
            return {VARIABLE_JSON_KEY: [recurse_json(DEFINITIONS.get("FeatureForAttribute"))]}
        case "Dict[str, List[FeatureForAttributes]]":
            return {VARIABLE_JSON_KEY: [recurse_json(DEFINITIONS.get("FeatureForAttributes"))]}
        case "Dict[str, List[FeatureForGetEntity]]":
            return {VARIABLE_JSON_KEY: [recurse_json(DEFINITIONS.get("FeatureForGetEntity"))]}
        case "Dict[str, List[MatchInfoForAttribute]]":
            return {VARIABLE_JSON_KEY: [recurse_json(DEFINITIONS.get("MatchInfoForAttribute"))]}
        case "Dict[str, int]":
            return {
                VARIABLE_JSON_KEY: "int32",
            }
        case "Dict[str, object]":
            return {
                VARIABLE_JSON_KEY: "object",
            }
        case "Dict[str, str]":
            return {
                VARIABLE_JSON_KEY: "string",
            }
        case "object":
            return "object"
        case "string":
            return "string"
        case _:
            print(f"Error: Bad 'pythonType:' {python_type}")
            raise NotImplementedError
    return result


def handle_json_ref(json_value):
    """Unwrap an RFC8927 'ref'."""
    return recurse_json(DEFINITIONS.get(json_value.get("ref")))


def handle_json_type(json_value):
    """Unwrap an RFC8927 'type'."""
    return json_value.get("type")


def handle_json_values(json_value):
    """Unwrap an RFC8927 'value'."""
    ref_type = json_value.get("values", {}).get("ref")
    if not ref_type:
        ref_type = json_value.get("values", {}).get("type")

    if ref_type in ["int32", "string"]:
        result = {VARIABLE_JSON_KEY: ref_type}
    elif ref_type:
        result = {VARIABLE_JSON_KEY: recurse_json(DEFINITIONS.get(ref_type))}
    else:
        result = {VARIABLE_JSON_KEY: recurse_json(json_value.get("values", {}))}
    return result


def recurse_json(json_value):
    """Do recursive descent through the JSON/dictionary."""

    result = {}
    if "metadata" in json_value:
        result = handle_json_metadata(json_value)
        if result:
            return result

    if "type" in json_value:
        return handle_json_type(json_value)

    if "values" in json_value:
        return handle_json_values(json_value)

    if "ref" in json_value:
        return handle_json_ref(json_value)

    if "properties" in json_value:
        return handle_json_properties(json_value)

    if "elements" in json_value:
        return handle_json_elements(json_value)

    return result


# -----------------------------------------------------------------------------
# Add records.
# -----------------------------------------------------------------------------


def add_records(sz_abstract_factory: SzAbstractFactory):
    """Add records to the Senzing repository."""

    # global LOADED_RECORD_KEYS

    debug_records = [  # Format: (data_source, record_id)
        ("CUSTOMER", "0"),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    sz_config_manager = sz_abstract_factory.create_configmanager()
    title = "SzEngineAddRecordResponse"
    json_schema = SCHEMA.get(title)

    # Register datasources.  TODO: fix underlying database.

    current_config_id = sz_config_manager.get_default_config_id()
    sz_config = sz_config_manager.create_config_from_config_id(current_config_id)

    for data_source in ("CUSTOMERS", "REFERENCE", "WATCHLIST"):
        sz_config.register_data_source(data_source)

    new_config = sz_config.export()
    new_config_id = sz_config_manager.register_config(new_config, "sz-sdk-json-type-definition")
    sz_config_manager.replace_default_config_id(current_config_id, new_config_id)
    sz_abstract_factory.reinitialize(new_config_id)

    # Add records.

    filenames = [
        "customers.jsonl",
        "reference.jsonl",
        "watchlist.jsonl",
    ]

    current_path = pathlib.Path(__file__).parent.resolve()
    test_count = 0
    for filename in filenames:
        file_path = os.path.abspath(f"{current_path}/../testdata/truthsets/{filename}")
        with open(file_path, "r", encoding="utf-8") as input_file:
            for line in input_file:
                line_as_dict = json.loads(line)
                data_source = line_as_dict.get("DATA_SOURCE")
                record_id = line_as_dict.get("RECORD_ID")

                LOADED_RECORD_KEYS.append(
                    {
                        "data_source": data_source,
                        "record_id": record_id,
                    }
                )
                test_name = f"Add record: {filename}/{data_source}/{record_id}"
                response = sz_engine.add_record(data_source, record_id, line, SzEngineFlags.SZ_WITH_INFO)
                if not response:
                    continue
                set_debug((data_source, record_id), debug_records)
                debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
                compare_to_schema(test_name, title, json_schema, json.loads(response))
                test_count += 1
    if not test_count:
        output(0, f"No tests performed for {title}")


# -----------------------------------------------------------------------------
# Compare
# -----------------------------------------------------------------------------


def compare(sz_abstract_factory: SzAbstractFactory):
    """Aggregate all compare functions."""
    compare_find_interesting_entities_by_entity_id(sz_abstract_factory)
    compare_find_interesting_entities_by_record_id(sz_abstract_factory)
    compare_find_network_by_entity_id(sz_abstract_factory)
    compare_find_network_by_record_id(sz_abstract_factory)
    compare_find_path_by_entity_id(sz_abstract_factory)
    compare_find_path_by_record_id(sz_abstract_factory)
    compare_get_entity_by_entity_id(sz_abstract_factory)
    compare_get_entity_by_record_id(sz_abstract_factory)
    compare_get_feature(sz_abstract_factory)
    compare_get_record_preview(sz_abstract_factory)
    compare_get_record(sz_abstract_factory)
    compare_get_virtual_entity_by_record_id(sz_abstract_factory)
    compare_how_entity_by_entity_id(sz_abstract_factory)
    compare_redo(sz_abstract_factory)
    compare_reevaluate_entity(sz_abstract_factory)
    compare_reevaluate_record(sz_abstract_factory)
    compare_search_by_attributes(sz_abstract_factory)
    compare_static_method_signatures(sz_abstract_factory)
    compare_why_entities(sz_abstract_factory)
    compare_why_record_in_entity(sz_abstract_factory)
    compare_why_records(sz_abstract_factory)
    compare_why_search(sz_abstract_factory)


# -----------------------------------------------------------------------------
# FindInterestingEntities
# -----------------------------------------------------------------------------


def compare_find_interesting_entities_by_entity_id(
    sz_abstract_factory: SzAbstractFactory,
):
    """Compare find_interesting_entities_by_entity_id."""
    debug_entities = [  # Format (entity_id, flag_count)
        (0, 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineFindInterestingEntitiesByEntityIdResponse"
    json_schema = SCHEMA.get(title)

    for entity_id in LOADED_ENTITY_IDS:
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - Entity #{entity_id}; Flag #{flag_count}"
            response = sz_engine.find_interesting_entities_by_entity_id(entity_id, flag)
            set_debug((entity_id, flag_count), debug_entities)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


def compare_find_interesting_entities_by_record_id(
    sz_abstract_factory: SzAbstractFactory,
):
    """Compare find_interesting_entities_by_record_id."""
    debug_records = [  # Format: ((data_source, record_id), flag_count)
        (("CUSTOMER", "0"), 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineFindInterestingEntitiesByRecordIdResponse"
    json_schema = SCHEMA.get(title)

    for record in LOADED_RECORD_KEYS:
        data_source = record.get("data_source", "")
        record_id = record.get("record_id", "")
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}; Flag #{flag_count}"
            response = sz_engine.find_interesting_entities_by_record_id(data_source, record_id, flag)
            set_debug(((data_source, record_id), flag_count), debug_records)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# FindNetwork
# -----------------------------------------------------------------------------


def compare_find_network_by_entity_id(sz_abstract_factory: SzAbstractFactory):
    """Compare find_network_by_entity_id."""
    debug_entities = [  # Format (entity_id, flag_count)
        (0, 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineFindNetworkByEntityIdResponse"
    json_schema = SCHEMA.get(title)
    max_degrees = 5
    build_out_degrees = 5
    build_out_max_entities = 5

    for entity_id in LOADED_ENTITY_IDS:

        # Randomize entity_ids.

        entity_ids = [entity_id]
        for _ in range(random.randint(3, 10)):
            new_entity_id = LOADED_ENTITY_IDS[random.randint(0, FLAGS_LEN - 1)]
            if new_entity_id not in entity_ids:
                entity_ids.append(new_entity_id)

        # Compare.

        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - Entity #{entity_id}; Entity List: {entity_ids}; Flag #{flag_count}"
            response = sz_engine.find_network_by_entity_id(
                entity_ids,
                max_degrees,
                build_out_degrees,
                build_out_max_entities,
                flag,
            )
            set_debug((entity_id, flag_count), debug_entities)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


def compare_find_network_by_record_id(sz_abstract_factory: SzAbstractFactory):
    """Compare find_network_by_record_id."""

    debug_records = [  # Format: ((data_source, record_id), flag_count)
        (("CUSTOMER", "0"), 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineFindNetworkByRecordIdResponse"
    json_schema = SCHEMA.get(title)
    max_degrees = 5
    build_out_degrees = 5
    build_out_max_entities = 5

    for record in LOADED_RECORD_KEYS:

        data_source = record.get("data_source", "")
        record_id = record.get("record_id", "")

        # Randomize record_keys.

        record_keys = [(data_source, record_id)]
        for _ in range(random.randint(3, 10)):
            record_key_dict = LOADED_RECORD_KEYS[random.randint(0, FLAGS_LEN - 1)]
            record_key = (
                record_key_dict.get("data_source", ""),
                record_key_dict.get("record_id", ""),
            )
            if record_key not in record_keys:
                record_keys.append(record_key)

        # Compare.

        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}; Record Keys: {record_keys}; Flag #{flag_count}"
            response = sz_engine.find_network_by_record_id(
                record_keys,
                max_degrees,
                build_out_degrees,
                build_out_max_entities,
                flag,
            )
            set_debug(((data_source, record_id), flag_count), debug_records)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# FindPath
# -----------------------------------------------------------------------------


def compare_find_path_by_entity_id(sz_abstract_factory: SzAbstractFactory):
    """Compare find_path_by_entity_id."""
    debug_entities = [  # Format (entity_id, flag_count)
        (0, 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineFindPathByEntityIdResponse"
    json_schema = SCHEMA.get(title)
    max_degrees = 5
    avoid_entity_ids = None
    required_data_sources = None

    for entity_id in LOADED_ENTITY_IDS:
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            end_entity_id = LOADED_ENTITY_IDS[random.randint(0, FLAGS_LEN - 1)]
            test_name = f"{title} - Entity #{entity_id}; End Entity #{end_entity_id}; Flag #{flag_count}"
            response = sz_engine.find_path_by_entity_id(
                entity_id,
                end_entity_id,
                max_degrees,
                avoid_entity_ids,
                required_data_sources,
                flag,
            )
            set_debug((entity_id, flag_count), debug_entities)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


def compare_find_path_by_record_id(sz_abstract_factory: SzAbstractFactory):
    """Compare find_path_by_record_id."""
    debug_records = [  # Format: ((data_source, record_id), flag_count)
        (("CUSTOMER", "0"), 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineFindPathByRecordIdResponse"
    json_schema = SCHEMA.get(title)
    max_degrees = 5
    avoid_record_keys = None
    required_data_sources = None

    for record in LOADED_RECORD_KEYS:
        data_source = record.get("data_source", "")
        record_id = record.get("record_id", "")
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            end_record = LOADED_RECORD_KEYS[random.randint(0, FLAGS_LEN - 1)]
            test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}; End Record: {end_record}; Flag #{flag_count}"
            response = sz_engine.find_path_by_record_id(
                data_source,
                record_id,
                end_record.get("data_source", ""),
                end_record.get("record_id", ""),
                max_degrees,
                avoid_record_keys,
                required_data_sources,
                flag,
            )
            set_debug(((data_source, record_id), flag_count), debug_records)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# GetEntity
# -----------------------------------------------------------------------------


def compare_get_entity_by_entity_id(sz_abstract_factory: SzAbstractFactory):
    """Compare get_entity_by_entity_id."""
    debug_entities = [  # Format (entity_id, flag_count)
        (0, 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineGetEntityByEntityIdResponse"
    json_schema = SCHEMA.get(title)

    for entity_id in LOADED_ENTITY_IDS:
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - Entity #{entity_id}; Flag #{flag_count}"
            response = sz_engine.get_entity_by_entity_id(entity_id, flag)
            set_debug((entity_id, flag_count), debug_entities)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


def compare_get_entity_by_record_id(sz_abstract_factory: SzAbstractFactory):
    """Compare get_entity_by_record_id."""
    debug_records = [  # Format: ((data_source, record_id), flag_count)
        (("CUSTOMER", "0"), 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineGetEntityByRecordIdResponse"
    json_schema = SCHEMA.get(title)

    for record in LOADED_RECORD_KEYS:
        data_source = record.get("data_source", "")
        record_id = record.get("record_id", "")

        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}; Flag #{flag_count}"
            response = sz_engine.get_entity_by_record_id(data_source, record_id, flag)
            set_debug(((data_source, record_id), flag_count), debug_records)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# GetFeature
# -----------------------------------------------------------------------------


def compare_get_feature(sz_abstract_factory: SzAbstractFactory):
    """Compare get_feature."""
    debug_entities = [  # Format (entity_id, flag_count)
        (0, 0),
    ]
    debug_feature_ids = [  # Format (feature_id)
        (0),
    ]

    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    sz_engine = sz_abstract_factory.create_engine()
    title = "SzDiagnosticGetFeatureResponse"
    json_schema = SCHEMA.get(title)

    # Extract feature IDs.

    feature_ids = []
    for entity_id in LOADED_ENTITY_IDS:
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - Entity #{entity_id}; Flag #{flag_count}"
            response = sz_engine.get_entity_by_entity_id(entity_id, flag)
            response_dict = json.loads(response)
            feature = response_dict.get("RESOLVED_ENTITY", {}).get("FEATURES", {})
            for feature_values in feature.values():
                for feature_value in feature_values:
                    feature_id = feature_value.get("LIB_FEAT_ID", None)
                    if feature_id:
                        if feature_id not in feature_ids:
                            feature_ids.append(feature_id)
            set_debug((entity_id, flag_count), debug_entities)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")

    # Test get_feature.

    for feature_id in feature_ids:
        test_name = f"{title} - Feature #{feature_id}"
        response = sz_diagnostic.get_feature(feature_id)
        set_debug((feature_id), debug_feature_ids)
        debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
        compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# GetRecord
# -----------------------------------------------------------------------------


def compare_get_record(sz_abstract_factory: SzAbstractFactory):
    """Compare get_record."""
    debug_records = [  # Format: ((data_source, record_id), flag_count)
        (("CUSTOMER", "0"), 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineGetRecordResponse"
    json_schema = SCHEMA.get(title)

    for record in LOADED_RECORD_KEYS:
        data_source = record.get("data_source", "")
        record_id = record.get("record_id", "")

        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}; Flag #{flag_count}"
            response = sz_engine.get_record(data_source, record_id, flag)
            set_debug(((data_source, record_id), flag_count), debug_records)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# GetRecordPreview
# -----------------------------------------------------------------------------


def compare_get_record_preview(sz_abstract_factory: SzAbstractFactory):
    """Compare get_record_preview."""
    debug_records = [  # Format: (flag_count)
        (0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineGetRecordPreviewResponse"
    json_schema = SCHEMA.get(title)

    for record_dict in LOADED_RECORD_KEYS:

        # Fetch actual record.

        data_source = record_dict.get("data_source", "")
        record_id = record_dict.get("record_id", "")
        record_str = sz_engine.get_record(data_source, record_id)
        record_dict = json.loads(record_str)
        record_json_dict = record_dict.get("JSON_DATA")
        record_json = json.dumps(record_json_dict)

        # Preview record with various flags.

        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}; Flag #{flag_count}"
            response = sz_engine.get_record_preview(record_json, flag)
            set_debug((flag_count), debug_records)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# GetVirtualEntity
# -----------------------------------------------------------------------------


def compare_get_virtual_entity_by_record_id(sz_abstract_factory: SzAbstractFactory):
    """Compare get_virtual_entity_by_record_id."""
    debug_records = [  # Format: ((data_source, record_id), flag_count)
        (("CUSTOMER", "0"), 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineGetVirtualEntityByRecordIdResponse"
    json_schema = SCHEMA.get(title)

    for record in LOADED_RECORD_KEYS:
        data_source = record.get("data_source", "")
        record_id = record.get("record_id", "")

        # Randomize record_keys.

        record_keys = [(data_source, record_id)]
        for _ in range(random.randint(3, 10)):
            record_key_dict = LOADED_RECORD_KEYS[random.randint(0, FLAGS_LEN - 1)]
            record_key = (
                record_key_dict.get("data_source", ""),
                record_key_dict.get("record_id", ""),
            )
            if record_key not in record_keys:
                record_keys.append(record_key)

        # Compare.

        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}; Record keys: {record_keys}; Flag #{flag_count}"
            response = sz_engine.get_virtual_entity_by_record_id(record_keys, flag)
            set_debug(((data_source, record_id), flag_count), debug_records)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# HowEntity
# -----------------------------------------------------------------------------


def compare_how_entity_by_entity_id(sz_abstract_factory: SzAbstractFactory):
    """Compare how_entity_by_entity_id."""
    debug_entities = [  # Format (entity_id, flag_count)
        (0, 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineHowEntityByEntityIdResponse"
    json_schema = SCHEMA.get(title)

    for entity_id in LOADED_ENTITY_IDS:
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - Entity #{entity_id}; Flag #{flag_count}"
            response = sz_engine.how_entity_by_entity_id(entity_id, flag)
            set_debug((entity_id, flag_count), debug_entities)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# Redo
# -----------------------------------------------------------------------------


def compare_redo(sz_abstract_factory: SzAbstractFactory):
    """Compare get_redo_record."""
    debug_get_redo = [  # Format (redo_record_count)
        (0),
    ]

    sz_engine = sz_abstract_factory.create_engine()

    # Get all redo records.

    title = "SzEngineGetRedoRecordResponse"
    json_schema = SCHEMA.get(title)

    redo_records = []
    redo_record_count = 0
    while True:
        redo_record_count += 1
        response = sz_engine.get_redo_record()
        if not response:
            break
        redo_records.append(response)
        test_name = f"{title} - Redo Record count:{redo_record_count}"
        set_debug((redo_record_count), debug_get_redo)
        debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
        compare_to_schema(test_name, title, json_schema, json.loads(response))

    # Process redo records.

    title = "SzEngineProcessRedoRecordResponse"
    json_schema = SCHEMA.get(title)

    redo_record_count = 0
    for redo_record in redo_records:
        redo_record_count += 1
        response = sz_engine.process_redo_record(redo_record, SzEngineFlags.SZ_WITH_INFO)
        test_name = f"{title} - Redo Record count:{redo_record_count}"
        set_debug((redo_record_count), debug_get_redo)
        debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
        compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# Reevaluate
# -----------------------------------------------------------------------------


def compare_reevaluate_entity(sz_abstract_factory: SzAbstractFactory):
    """Compare reevaluate_entity."""
    debug_entities = [  # Format (entity_id, flag_count)
        (0, 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineReevaluateEntityResponse"
    json_schema = SCHEMA.get(title)

    test_count = 0
    for entity_id in LOADED_ENTITY_IDS:
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            flag = flag | SzEngineFlags.SZ_WITH_INFO
            test_name = f"{title} - Entity #{entity_id}; Flag #{flag_count}"
            response = sz_engine.reevaluate_entity(entity_id, flag)
            if not response:
                continue
            set_debug((entity_id, flag_count), debug_entities)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))
            test_count += 1
    if not test_count:
        output(0, f"No tests performed for {title}")


def compare_reevaluate_record(sz_abstract_factory: SzAbstractFactory):
    """Compare reevaluate_record."""
    debug_records = [  # Format: ((data_source, record_id), flag_count)
        (("CUSTOMER", "0"), 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineReevaluateRecordResponse"
    json_schema = SCHEMA.get(title)

    test_count = 0
    for record in LOADED_RECORD_KEYS:
        data_source = record.get("data_source", "")
        record_id = record.get("record_id", "")
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            flag = flag | SzEngineFlags.SZ_WITH_INFO
            test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}; Flag #{flag_count}"
            response = sz_engine.reevaluate_record(data_source, record_id, flag)
            if not response:
                continue
            set_debug(((data_source, record_id), flag_count), debug_records)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))
            test_count += 1
    if not test_count:
        output(0, f"No tests performed for {title}")


# -----------------------------------------------------------------------------
# SearchByAttributes
# -----------------------------------------------------------------------------


def compare_search_by_attributes(sz_abstract_factory: SzAbstractFactory):
    """Compare search_by_attributes."""
    debug_search = [  # Format: (search_record_count, flag_count)
        (0, 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineSearchByAttributesResponse"
    json_schema = SCHEMA.get(title)
    search_profile = ""

    search_record_count = 0
    for search_record in SEARCH_RECORDS:
        search_record_count += 1
        attributes = json.dumps(search_record)
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - Search record #{search_record_count}; Flag #{flag_count}"
            response = sz_engine.search_by_attributes(attributes, flag, search_profile)
            set_debug((search_record_count, flag_count), debug_search)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# Static method signature calls
# -----------------------------------------------------------------------------


def compare_static_method_signatures(sz_abstract_factory: SzAbstractFactory):
    """Compare methods without variable parameters."""

    sz_config_manager = sz_abstract_factory.create_configmanager()
    sz_config = sz_config_manager.create_config_from_template()
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    sz_engine = sz_abstract_factory.create_engine()
    sz_product = sz_abstract_factory.create_product()

    # For linter

    _ = sz_config
    _ = sz_engine
    _ = sz_diagnostic
    _ = sz_product

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
            "testcase": 'sz_config.register_data_source("A_DATASOURCE_NAME")',
            "response": "SzConfigRegisterDataSourceResponse",
        },
        {
            "testcase": 'sz_config.unregister_data_source("A_DATASOURCE_NAME")',
            "response": "SzConfigUnregisterDataSourceResponse",
        },
        {
            "testcase": "sz_config_manager.get_config_registry()",
            "response": "SzConfigManagerGetConfigRegistryResponse",
        },
        {
            "testcase": "sz_diagnostic.check_repository_performance(2)",
            "response": "SzDiagnosticCheckRepositoryPerformanceResponse",
        },
        {
            "testcase": "sz_diagnostic.get_repository_info()",
            "response": "SzDiagnosticGetRepositoryInfoResponse",
        },
        # {
        #     "testcase": "sz_diagnostic.get_feature(1)",
        #     "response": "SzDiagnosticGetFeatureResponse",
        # },
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
            eval(testcase.get("testcase", "")),
        )


# -----------------------------------------------------------------------------
# WhyEntities
# -----------------------------------------------------------------------------


def compare_why_entities(sz_abstract_factory: SzAbstractFactory):
    """Compare why_entities."""
    debug_entities = [  # Format (entity_id, flag_count)
        (0, 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineWhyEntitiesResponse"
    json_schema = SCHEMA.get(title)

    for entity_id in LOADED_ENTITY_IDS:
        entity_id_2 = LOADED_ENTITY_IDS[random.randint(0, FLAGS_LEN - 1)]
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - Entity #{entity_id}; Entity2 #{entity_id_2}; Flag #{flag_count}"
            response = sz_engine.why_entities(entity_id, entity_id_2, flag)
            set_debug((entity_id, flag_count), debug_entities)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# WhyRecordInEntity
# -----------------------------------------------------------------------------


def compare_why_record_in_entity(sz_abstract_factory: SzAbstractFactory):
    """Compare why_record_in_entity."""
    debug_records = [  # Format: ((data_source, record_id), flag_count)
        (("CUSTOMERS", "0"), 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineWhyRecordInEntityResponse"
    json_schema = SCHEMA.get(title)

    for record in LOADED_RECORD_KEYS:
        data_source = record.get("data_source", "")
        record_id = record.get("record_id", "")
        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}; Flag #{flag_count}"
            response = sz_engine.why_record_in_entity(data_source, record_id, flag)
            set_debug(((data_source, record_id), flag_count), debug_records)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# WhyRecords
# -----------------------------------------------------------------------------


def compare_why_records(sz_abstract_factory: SzAbstractFactory):
    """Compare why_records."""
    debug_records = [  # Format: ((data_source, record_id), flag_count)
        (("CUSTOMER", "0"), 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineWhyRecordsResponse"
    json_schema = SCHEMA.get(title)

    for record in LOADED_RECORD_KEYS:

        data_source = record.get("data_source", "")
        record_id = record.get("record_id", "")

        # Randomize record.

        record_key_dict = LOADED_RECORD_KEYS[random.randint(0, FLAGS_LEN - 1)]
        data_source_2 = record_key_dict.get("data_source", "")
        record_id_2 = record_key_dict.get("record_id", "")

        # Compare.

        flag_count = 0
        for flag in FLAGS:
            flag_count += 1
            test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}; Record 2: {record_key_dict}; Flag #{flag_count}"
            response = sz_engine.why_records(data_source, record_id, data_source_2, record_id_2, flag)
            set_debug(((data_source, record_id), flag_count), debug_records)
            debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
            compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# WhySearch
# -----------------------------------------------------------------------------


def compare_why_search(sz_abstract_factory: SzAbstractFactory):
    """Compare why_search."""
    debug_search = [  # Format: (entity, search_record_count, flag_count)
        (0, 0, 0),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineWhySearchResponse"
    json_schema = SCHEMA.get(title)
    search_profile = ""

    for entity_id in LOADED_ENTITY_IDS:
        search_record_count = 0
        for search_record in SEARCH_RECORDS:
            search_record_count += 1
            attributes = json.dumps(search_record)
            flag_count = 0
            for flag in FLAGS:
                flag_count += 1
                test_name = f"{title} - Entity #{entity_id}; Search record #{search_record_count}; Flag #{flag_count}"
                response = sz_engine.why_search(attributes, entity_id, flag, search_profile)
                set_debug((entity_id, search_record_count, flag_count), debug_search)
                debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
                compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# Delete records
# -----------------------------------------------------------------------------


def delete_records(sz_abstract_factory: SzAbstractFactory):
    """Compare delete_record."""
    debug_records = [  # Format: ((data_source, record_id), flag_number)
        ("CUSTOMER", "0"),
    ]

    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineDeleteRecordResponse"
    json_schema = SCHEMA.get(title)

    test_count = 0
    record_count = 0
    for record in LOADED_RECORD_KEYS:
        record_count += 1
        data_source = record.get("data_source", "")
        record_id = record.get("record_id", "")
        test_name = f"{title} - DataSource: {data_source}; RecordID: {record_id}"
        response = sz_engine.delete_record(data_source, record_id, SzEngineFlags.SZ_WITH_INFO)
        if not response:
            continue
        set_debug((data_source, record_id), debug_records)
        debug(1, f"{HR_START}\n{test_name}; Response:\n{response}\n{HR_STOP}\n")
        compare_to_schema(test_name, title, json_schema, json.loads(response))
        test_count += 1
    if not test_count:
        output(0, f"No tests performed for {title}")


# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


def compare_to_schema(test_name, json_path, schema, fragment):
    """Compare a JSON fragment to the schema."""
    global ERROR_COUNT

    debug(2, f"{HR_START}\nSchema for {json_path}:\n{json.dumps(schema)}\n{HR_STOP}\n")

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
            if key not in schema:
                schema_value = schema.get(VARIABLE_JSON_KEY, {})
            compare_to_schema(test_name, f"{json_path}.{key}", schema_value, value)
        return

    if isinstance(fragment, int):
        if schema not in ["int32", "object"]:
            ERROR_COUNT += 1
            error_message(
                test_name,
                json_path,
                "Incorrect specification for int32",
                schema,
                fragment,
            )
        return

    if isinstance(fragment, str):
        if schema not in ["string", "timestamp", "object"]:
            error_message(
                test_name,
                json_path,
                "Incorrect specification for string",
                schema,
                fragment,
            )
        return

    if isinstance(fragment, float):
        if not schema == "float32":
            error_message(
                test_name,
                json_path,
                "Incorrect specification for float32",
                schema,
                fragment,
            )
        return

    if fragment is None:
        return

    # If ending up here, there's an error.

    ERROR_COUNT += 1
    error_message(test_name, json_path, "Unknown value", schema, fragment)


def create_sz_abstract_factory() -> SzAbstractFactory:
    """Create an SzAbstractFactory."""
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

    return sz_abstract_factory


def debug(level, message):
    """If appropriate, print debug statement."""
    if DEBUG >= level:
        print(message)


def error_message(test_name, json_path, message, schema, fragment):
    """Create an error message."""
    output(0, test_name)
    output(1, f"Path: {json_path}")
    output(2, "Error:")
    output(3, message)
    output(3, f"schema: {json.dumps(schema)}")
    output(3, f"  json: {json.dumps(fragment)}")


def get_entity_ids(sz_abstract_factory: SzAbstractFactory):
    """Get a list of entity IDs."""

    result = []
    sz_engine = sz_abstract_factory.create_engine()

    for record in LOADED_RECORD_KEYS:
        response = sz_engine.get_entity_by_record_id(record.get("data_source", ""), record.get("record_id", ""))
        response_dict = json.loads(response)
        entity_id = response_dict.get("RESOLVED_ENTITY", {}).get("ENTITY_ID", 0)
        if entity_id not in result:
            result.append(entity_id)

    return result


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

    if isinstance(subset_json, list):
        if not isinstance(full_json, list):
            return False
        for item in subset_json:
            if item not in full_json:
                return False
        return True

    # Primitive types (int, str, bool, float, None)
    return subset_json == full_json


def output(indentation, message):
    """Create an indented message."""
    print(f"{'    ' * indentation}{message}")


def path_to_testdata(filename: str) -> str:
    """Determine the path to the test data."""
    current_path = pathlib.Path(__file__).parent.resolve()
    result = os.path.abspath(f"{current_path}/testdata/{filename}")
    return result


def process_rfc8927():
    """Process the RFC8927 JSON."""
    # global DEFINITIONS, SCHEMA
    global DEFINITIONS

    input_filename = "./senzingsdk-RFC8927.json"
    with open(input_filename, "r", encoding="utf-8") as input_file:
        rfc8927 = json.load(input_file)

    DEFINITIONS = rfc8927.get("definitions", {})

    # Recurse through dictionary.

    for requested_json_key in GLOBAL_JSON_KEYS:
        json_value = DEFINITIONS.get(requested_json_key)

        # Short-circuit when JSON key not found.

        if json_value is None:
            print(f"Could not find JSON key: {requested_json_key}")
            continue

        SCHEMA[requested_json_key] = recurse_json(json_value)


def set_debug(needle, haystack):
    """Determine if debug should be set."""
    global DEBUG

    DEBUG = 0
    if needle in haystack:
        DEBUG = 1


def test_this(test_name, title, response):
    """Test the response against a schema."""
    if response:
        json_schema = SCHEMA.get(title)
        compare_to_schema(test_name, title, json_schema, json.loads(response))


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


if __name__ == "__main__":

    # Process RFC8927 file to create SCHEMA.

    process_rfc8927()

    # Create SzAbstractFactory.

    the_sz_abstract_factory = create_sz_abstract_factory()

    # Insert test data.

    add_records(the_sz_abstract_factory)
    LOADED_ENTITY_IDS = get_entity_ids(the_sz_abstract_factory)

    # Make comparisons.

    # compare(sz_abstract_factory)
    compare_find_network_by_entity_id(the_sz_abstract_factory)

    # Delete test data.

    delete_records(the_sz_abstract_factory)

    # Epilog.

    if ERROR_COUNT > 0:
        sys.exit(1)
