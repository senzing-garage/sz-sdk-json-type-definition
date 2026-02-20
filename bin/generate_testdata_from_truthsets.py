#! /usr/bin/env python3

# pylint: disable=duplicate-code

"""
generate_testdata_from_truthsets.py

Generate test data by fetching truth-set records from GitHub and calling
every abstract method that returns str across all 5 Senzing SDK abstract
classes, using flags=-1 (all flag bits on).

Output: testdata/responses_truthsets/
"""

import json
import logging
import os
import pathlib
import urllib.request

from senzing import SzAbstractFactory, SzError
from senzing_core import SzAbstractFactoryCore

# Logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Global constants

ALL_FLAGS = -1  # All flag bits on
MAX_DEGREES = 5
BUILD_OUT_DEGREES = 5
BUILD_OUT_MAX_ENTITIES = 5
PATH_VARIATION_COUNT = 5  # Iterations for start_*/end_* param pairs

CURRENT_PATH = pathlib.Path(__file__).parent.resolve()
OUTPUT_DIRECTORY = os.path.abspath(f"{CURRENT_PATH}/../testdata/responses_truthsets")

TRUTHSET_URLS = [
    "https://raw.githubusercontent.com/Senzing/truth-sets/refs/heads/main/truthsets/demo/customers.jsonl",
    "https://raw.githubusercontent.com/Senzing/truth-sets/refs/heads/main/truthsets/demo/reference.jsonl",
    "https://raw.githubusercontent.com/Senzing/truth-sets/refs/heads/main/truthsets/demo/watchlist.jsonl",
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

LOADED_RECORD_KEYS = []  # [{"data_source": ..., "record_id": ..., "record_definition": ...}]
LOADED_ENTITY_IDS = []

# -----------------------------------------------------------------------------
# Data fetching
# -----------------------------------------------------------------------------


def fetch_truthset_lines(url):
    """Fetch lines from a truth-set URL, return list of (line_str, line_dict) tuples."""
    results = []
    with urllib.request.urlopen(url) as response:  # noqa: S310
        for raw_line in response:
            line_str = raw_line.decode("utf-8").strip()
            if not line_str:
                continue
            line_dict = json.loads(line_str)
            results.append((line_str, line_dict))
    return results


def load_truthsets():
    """Fetch all truth-set URLs, return list of (line_str, line_dict) tuples."""
    all_records = []
    for url in TRUTHSET_URLS:
        logger.info("Fetching %s", url)
        all_records.extend(fetch_truthset_lines(url))
    return all_records


# -----------------------------------------------------------------------------
# Senzing setup
# -----------------------------------------------------------------------------


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
        logger.error("%s", err)

    return sz_abstract_factory


def register_datasources(sz_abstract_factory: SzAbstractFactory):
    """Add Data Sources CUSTOMERS, REFERENCE, WATCHLIST to the Senzing repository."""
    sz_config_manager = sz_abstract_factory.create_configmanager()

    current_config_id = sz_config_manager.get_default_config_id()
    sz_config = sz_config_manager.create_config_from_config_id(current_config_id)

    for data_source in ("CUSTOMERS", "REFERENCE", "WATCHLIST"):
        sz_config.register_data_source(data_source)

    new_config = sz_config.export()
    new_config_id = sz_config_manager.register_config(new_config, "generate_testdata_from_truthsets.py")
    sz_config_manager.replace_default_config_id(current_config_id, new_config_id)
    sz_abstract_factory.reinitialize(new_config_id)


# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


def collect(responses_dict, title, response):
    """Add a non-empty response string to the appropriate list, avoiding duplicates."""
    if not response:
        return
    bucket = responses_dict.setdefault(title, [])
    if response not in bucket:
        bucket.append(response)


def output_file(title, responses):
    """Write list of JSON strings to {OUTPUT_DIRECTORY}/{title}.jsonl.

    Always includes an empty-JSON sentinel line ("{}") so every file has
    at least one entry and test scaffolding can safely parse the file.
    """
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIRECTORY, f"{title}.jsonl")
    lines = list(responses)
    if "{}" not in lines:
        lines.insert(0, "{}")
    with open(filepath, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(f"{line}\n")
    logger.info("Wrote %d lines to %s", len(lines), filepath)


def remove_duplicate_lines(input_filepath, output_filepath=None):
    """Remove duplicate JSON lines from a file, sort remaining lines."""
    unique_lines = set()
    try:
        with open(input_filepath, "r", encoding="utf-8") as infile:
            for line in infile:
                line = line.strip()
                if len(line) > 0:
                    line_as_dict = json.loads(line)
                    unique_lines.add(json.dumps(line_as_dict, sort_keys=True))
    except FileNotFoundError:
        logger.warning("Error: Input file '%s' not found.", input_filepath)
        return

    if output_filepath is None:
        output_filepath = input_filepath

    try:
        with open(output_filepath, "w", encoding="utf-8") as outfile:
            for line in sorted(list(unique_lines)):
                outfile.write(f"{line}\n")
        logger.debug("Duplicates removed in '%s'.", output_filepath)
    except IOError:
        logger.error("Error: Could not write to output file '%s'.", output_filepath)


def normalize_files(directory):
    """Deduplicate and sort JSON lines in all .jsonl files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".jsonl"):
                remove_duplicate_lines(os.path.join(root, file))


def get_entity_ids(sz_abstract_factory: SzAbstractFactory):
    """Get unique entity IDs for all loaded records."""
    result = []
    sz_engine = sz_abstract_factory.create_engine()
    for record in LOADED_RECORD_KEYS:
        try:
            response = sz_engine.get_entity_by_record_id(record.get("data_source", ""), record.get("record_id", ""))
            response_dict = json.loads(response)
            entity_id = response_dict.get("RESOLVED_ENTITY", {}).get("ENTITY_ID", 0)
            if entity_id and entity_id not in result:
                result.append(entity_id)
        except SzError:
            pass
    return result


# -----------------------------------------------------------------------------
# Phase 1: Add records (captures SzEngineAddRecordResponse)
# -----------------------------------------------------------------------------


def add_records(sz_abstract_factory: SzAbstractFactory, truthset_records):
    """Add truth-set records to Senzing, collect AddRecord responses."""
    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineAddRecordResponse"
    responses = []

    for line_str, line_dict in truthset_records:
        data_source = line_dict.get("DATA_SOURCE")
        record_id = line_dict.get("RECORD_ID")

        LOADED_RECORD_KEYS.append(
            {
                "data_source": data_source,
                "record_id": record_id,
                "record_definition": line_str,
            }
        )

        try:
            response = sz_engine.add_record(data_source, record_id, line_str, ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("add_record failed for %s/%s: %s", data_source, record_id, err)

    output_file(title, responses)


# -----------------------------------------------------------------------------
# Phase 2: SzConfig responses
# -----------------------------------------------------------------------------


def collect_szconfig_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect responses from SzConfig methods."""
    sz_config_manager = sz_abstract_factory.create_configmanager()
    current_config_id = sz_config_manager.get_default_config_id()
    sz_config = sz_config_manager.create_config_from_config_id(current_config_id)

    # export
    response = sz_config.export()
    output_file("SzConfigExportResponse", [response] if response else [])

    # get_data_source_registry
    response = sz_config.get_data_source_registry()
    output_file("SzConfigGetDataSourceRegistryResponse", [response] if response else [])

    # register_data_source (use a temp DS that won't be persisted)
    reg_responses = []
    try:
        response = sz_config.register_data_source("GENERATE_TEST_DS")
        if response:
            reg_responses.append(response)
    except SzError as err:
        logger.warning("register_data_source failed: %s", err)
    output_file("SzConfigRegisterDataSourceResponse", reg_responses)

    # unregister_data_source
    unreg_responses = []
    try:
        response = sz_config.unregister_data_source("GENERATE_TEST_DS")
        if response:
            unreg_responses.append(response)
    except SzError as err:
        logger.warning("unregister_data_source failed: %s", err)
    output_file("SzConfigUnregisterDataSourceResponse", unreg_responses)


# -----------------------------------------------------------------------------
# Phase 3: SzConfigManager responses
# -----------------------------------------------------------------------------


def collect_szconfigmanager_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect responses from SzConfigManager methods."""
    sz_config_manager = sz_abstract_factory.create_configmanager()

    # get_config_registry
    response = sz_config_manager.get_config_registry()
    output_file("SzConfigManagerGetConfigRegistryResponse", [response] if response else [])


# -----------------------------------------------------------------------------
# Phase 4: SzDiagnostic responses
# -----------------------------------------------------------------------------


def collect_szdiagnostic_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect responses from SzDiagnostic methods."""
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    sz_engine = sz_abstract_factory.create_engine()

    # check_repository_performance
    response = sz_diagnostic.check_repository_performance(2)
    output_file("SzDiagnosticCheckRepositoryPerformanceResponse", [response] if response else [])

    # get_repository_info
    response = sz_diagnostic.get_repository_info()
    output_file("SzDiagnosticGetRepositoryInfoResponse", [response] if response else [])

    # get_feature — extract feature IDs from entity responses
    feature_ids = []
    for entity_id in LOADED_ENTITY_IDS:
        try:
            response = sz_engine.get_entity_by_entity_id(entity_id, ALL_FLAGS)
            response_dict = json.loads(response)
            features = response_dict.get("RESOLVED_ENTITY", {}).get("FEATURES", {})
            for feature_values in features.values():
                for feature_value in feature_values:
                    fid = feature_value.get("LIB_FEAT_ID")
                    if fid and fid not in feature_ids:
                        feature_ids.append(fid)
        except SzError:
            pass

    feat_responses = []
    for fid in feature_ids:
        try:
            response = sz_diagnostic.get_feature(fid)
            if response and response not in feat_responses:
                feat_responses.append(response)
        except SzError as err:
            logger.warning("get_feature(%s) failed: %s", fid, err)
    output_file("SzDiagnosticGetFeatureResponse", feat_responses)


# -----------------------------------------------------------------------------
# Phase 5: SzEngine responses (read-only queries)
# -----------------------------------------------------------------------------


def collect_szengine_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect responses from read-only SzEngine methods."""
    sz_engine = sz_abstract_factory.create_engine()
    n_entities = len(LOADED_ENTITY_IDS)
    n_records = len(LOADED_RECORD_KEYS)

    # --- find_interesting_entities_by_entity_id ---
    responses = []
    for entity_id in LOADED_ENTITY_IDS:
        try:
            response = sz_engine.find_interesting_entities_by_entity_id(entity_id, ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("find_interesting_entities_by_entity_id(%s): %s", entity_id, err)
    output_file("SzEngineFindInterestingEntitiesByEntityIdResponse", responses)

    # --- find_interesting_entities_by_record_id ---
    responses = []
    for record in LOADED_RECORD_KEYS:
        try:
            response = sz_engine.find_interesting_entities_by_record_id(
                record["data_source"], record["record_id"], ALL_FLAGS
            )
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("find_interesting_entities_by_record_id: %s", err)
    output_file("SzEngineFindInterestingEntitiesByRecordIdResponse", responses)

    # --- find_network_by_entity_id ---
    responses = []
    for i, entity_id in enumerate(LOADED_ENTITY_IDS):
        entity_ids = [LOADED_ENTITY_IDS[(i + j) % n_entities] for j in range(min(5, n_entities))]
        try:
            response = sz_engine.find_network_by_entity_id(
                entity_ids, MAX_DEGREES, BUILD_OUT_DEGREES, BUILD_OUT_MAX_ENTITIES, ALL_FLAGS
            )
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("find_network_by_entity_id: %s", err)
    output_file("SzEngineFindNetworkByEntityIdResponse", responses)

    # --- find_network_by_record_id ---
    responses = []
    for i, record in enumerate(LOADED_RECORD_KEYS):
        record_keys = [
            (
                LOADED_RECORD_KEYS[(i + j) % n_records]["data_source"],
                LOADED_RECORD_KEYS[(i + j) % n_records]["record_id"],
            )
            for j in range(min(5, n_records))
        ]
        try:
            response = sz_engine.find_network_by_record_id(
                record_keys, MAX_DEGREES, BUILD_OUT_DEGREES, BUILD_OUT_MAX_ENTITIES, ALL_FLAGS
            )
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("find_network_by_record_id: %s", err)
    output_file("SzEngineFindNetworkByRecordIdResponse", responses)

    # --- find_path_by_entity_id ---
    responses = []
    for i in range(PATH_VARIATION_COUNT):
        if n_entities < 2:
            break
        start_id = LOADED_ENTITY_IDS[i % n_entities]
        end_id = LOADED_ENTITY_IDS[(i + 1) % n_entities]
        try:
            response = sz_engine.find_path_by_entity_id(start_id, end_id, MAX_DEGREES, None, None, ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("find_path_by_entity_id: %s", err)
    output_file("SzEngineFindPathByEntityIdResponse", responses)

    # --- find_path_by_record_id ---
    responses = []
    for i in range(PATH_VARIATION_COUNT):
        if n_records < 2:
            break
        start = LOADED_RECORD_KEYS[i % n_records]
        end = LOADED_RECORD_KEYS[(i + 1) % n_records]
        try:
            response = sz_engine.find_path_by_record_id(
                start["data_source"],
                start["record_id"],
                end["data_source"],
                end["record_id"],
                MAX_DEGREES,
                None,
                None,
                ALL_FLAGS,
            )
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("find_path_by_record_id: %s", err)
    output_file("SzEngineFindPathByRecordIdResponse", responses)

    # --- get_entity_by_entity_id ---
    responses = []
    for entity_id in LOADED_ENTITY_IDS:
        try:
            response = sz_engine.get_entity_by_entity_id(entity_id, ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("get_entity_by_entity_id(%s): %s", entity_id, err)
    output_file("SzEngineGetEntityByEntityIdResponse", responses)

    # --- get_entity_by_record_id ---
    responses = []
    for record in LOADED_RECORD_KEYS:
        try:
            response = sz_engine.get_entity_by_record_id(record["data_source"], record["record_id"], ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("get_entity_by_record_id: %s", err)
    output_file("SzEngineGetEntityByRecordIdResponse", responses)

    # --- get_record ---
    responses = []
    for record in LOADED_RECORD_KEYS:
        try:
            response = sz_engine.get_record(record["data_source"], record["record_id"], ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("get_record: %s", err)
    output_file("SzEngineGetRecordResponse", responses)

    # --- get_record_preview ---
    responses = []
    for record in LOADED_RECORD_KEYS:
        record_definition = record.get("record_definition", "")
        try:
            response = sz_engine.get_record_preview(record_definition, ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("get_record_preview: %s", err)
    output_file("SzEngineGetRecordPreviewResponse", responses)

    # --- get_stats ---
    try:
        response = sz_engine.get_stats()
        output_file("SzEngineGetStatsResponse", [response] if response else [])
    except SzError as err:
        logger.warning("get_stats: %s", err)
        output_file("SzEngineGetStatsResponse", [])

    # --- get_virtual_entity_by_record_id ---
    responses = []
    for i, record in enumerate(LOADED_RECORD_KEYS):
        record_keys = [
            (
                LOADED_RECORD_KEYS[(i + j) % n_records]["data_source"],
                LOADED_RECORD_KEYS[(i + j) % n_records]["record_id"],
            )
            for j in range(min(5, n_records))
        ]
        try:
            response = sz_engine.get_virtual_entity_by_record_id(record_keys, ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("get_virtual_entity_by_record_id: %s", err)
    output_file("SzEngineGetVirtualEntityByRecordIdResponse", responses)

    # --- how_entity_by_entity_id ---
    responses = []
    for entity_id in LOADED_ENTITY_IDS:
        try:
            response = sz_engine.how_entity_by_entity_id(entity_id, ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("how_entity_by_entity_id(%s): %s", entity_id, err)
    output_file("SzEngineHowEntityByEntityIdResponse", responses)

    # --- search_by_attributes ---
    responses = []
    for search_record in SEARCH_RECORDS:
        attributes = json.dumps(search_record)
        try:
            response = sz_engine.search_by_attributes(attributes, ALL_FLAGS, "")
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("search_by_attributes: %s", err)
    output_file("SzEngineSearchByAttributesResponse", responses)

    # --- why_entities ---
    responses = []
    for i, entity_id in enumerate(LOADED_ENTITY_IDS):
        entity_id_2 = LOADED_ENTITY_IDS[(i + 1) % n_entities]
        try:
            response = sz_engine.why_entities(entity_id, entity_id_2, ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("why_entities: %s", err)
    output_file("SzEngineWhyEntitiesResponse", responses)

    # --- why_record_in_entity ---
    responses = []
    for record in LOADED_RECORD_KEYS:
        try:
            response = sz_engine.why_record_in_entity(record["data_source"], record["record_id"], ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("why_record_in_entity: %s", err)
    output_file("SzEngineWhyRecordInEntityResponse", responses)

    # --- why_records ---
    responses = []
    for i, record in enumerate(LOADED_RECORD_KEYS):
        record_2 = LOADED_RECORD_KEYS[(i + 1) % n_records]
        try:
            response = sz_engine.why_records(
                record["data_source"],
                record["record_id"],
                record_2["data_source"],
                record_2["record_id"],
                ALL_FLAGS,
            )
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("why_records: %s", err)
    output_file("SzEngineWhyRecordsResponse", responses)

    # --- why_search ---
    responses = []
    for entity_id in LOADED_ENTITY_IDS:
        for search_record in SEARCH_RECORDS:
            attributes = json.dumps(search_record)
            try:
                response = sz_engine.why_search(attributes, entity_id, ALL_FLAGS, "")
                if response and response not in responses:
                    responses.append(response)
            except SzError as err:
                logger.warning("why_search: %s", err)
    output_file("SzEngineWhySearchResponse", responses)

    # --- fetch_next (via export_json_entity_report) ---
    fetch_responses = []
    try:
        handle = sz_engine.export_json_entity_report(ALL_FLAGS)
        while True:
            response = sz_engine.fetch_next(handle)
            if not response:
                break
            if response not in fetch_responses:
                fetch_responses.append(response)
        sz_engine.close_export_report(handle)
    except SzError as err:
        logger.warning("fetch_next: %s", err)
    output_file("SzEngineFetchNextResponse", fetch_responses)


# -----------------------------------------------------------------------------
# Phase 6: Redo records
# -----------------------------------------------------------------------------


def collect_redo_responses(sz_abstract_factory: SzAbstractFactory):
    """Drain and process redo records, collect responses."""
    sz_engine = sz_abstract_factory.create_engine()

    # Drain all redo records
    redo_records = []
    get_redo_responses = []
    while True:
        try:
            response = sz_engine.get_redo_record()
        except SzError as err:
            logger.warning("get_redo_record: %s", err)
            break
        if not response:
            break
        redo_records.append(response)
        if response not in get_redo_responses:
            get_redo_responses.append(response)
    output_file("SzEngineGetRedoRecordResponse", get_redo_responses)

    # Process redo records
    process_responses = []
    for redo_record in redo_records:
        try:
            response = sz_engine.process_redo_record(redo_record, ALL_FLAGS)
            if response and response not in process_responses:
                process_responses.append(response)
        except SzError as err:
            logger.warning("process_redo_record: %s", err)
    output_file("SzEngineProcessRedoRecordResponse", process_responses)


# -----------------------------------------------------------------------------
# Phase 7: Reevaluate
# -----------------------------------------------------------------------------


def collect_reevaluate_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect reevaluate_entity and reevaluate_record responses."""
    sz_engine = sz_abstract_factory.create_engine()

    # reevaluate_entity
    responses = []
    for entity_id in LOADED_ENTITY_IDS:
        try:
            response = sz_engine.reevaluate_entity(entity_id, ALL_FLAGS)
            if not response:
                continue
            if response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("reevaluate_entity(%s): %s", entity_id, err)
    output_file("SzEngineReevaluateEntityResponse", responses)

    # reevaluate_record
    responses = []
    for record in LOADED_RECORD_KEYS:
        try:
            response = sz_engine.reevaluate_record(record["data_source"], record["record_id"], ALL_FLAGS)
            if not response:
                continue
            if response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("reevaluate_record: %s", err)
    output_file("SzEngineReevaluateRecordResponse", responses)


# -----------------------------------------------------------------------------
# Phase 8: Delete records (captures SzEngineDeleteRecordResponse)
# -----------------------------------------------------------------------------


def delete_records(sz_abstract_factory: SzAbstractFactory):
    """Delete all loaded records, collect DeleteRecord responses."""
    sz_engine = sz_abstract_factory.create_engine()
    title = "SzEngineDeleteRecordResponse"
    responses = []

    for record in LOADED_RECORD_KEYS:
        try:
            response = sz_engine.delete_record(record["data_source"], record["record_id"], ALL_FLAGS)
            if response and response not in responses:
                responses.append(response)
        except SzError as err:
            logger.warning("delete_record: %s", err)

    output_file(title, responses)


# -----------------------------------------------------------------------------
# Phase 9: SzProduct responses
# -----------------------------------------------------------------------------


def collect_szproduct_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect responses from SzProduct methods."""
    sz_product = sz_abstract_factory.create_product()

    response = sz_product.get_license()
    output_file("SzProductGetLicenseResponse", [response] if response else [])

    response = sz_product.get_version()
    output_file("SzProductGetVersionResponse", [response] if response else [])


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


if __name__ == "__main__":

    logger.info("Begin %s", os.path.basename(__file__))

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    # Fetch truth-set records from GitHub
    logger.info("Fetching truth-set records from GitHub...")
    all_truthset_records = load_truthsets()
    logger.info("Fetched %d records", len(all_truthset_records))

    # Create SzAbstractFactory
    the_factory = create_sz_abstract_factory()

    # Register data sources
    logger.info("Registering data sources...")
    register_datasources(the_factory)

    # Phase 1: Add records
    logger.info("Phase 1: Adding records...")
    add_records(the_factory, all_truthset_records)

    # Collect entity IDs
    logger.info("Collecting entity IDs...")
    LOADED_ENTITY_IDS = get_entity_ids(the_factory)
    logger.info("Found %d unique entity IDs", len(LOADED_ENTITY_IDS))

    # Phase 2: SzConfig responses
    logger.info("Phase 2: Collecting SzConfig responses...")
    collect_szconfig_responses(the_factory)

    # Phase 3: SzConfigManager responses
    logger.info("Phase 3: Collecting SzConfigManager responses...")
    collect_szconfigmanager_responses(the_factory)

    # Phase 4: SzDiagnostic responses
    logger.info("Phase 4: Collecting SzDiagnostic responses...")
    collect_szdiagnostic_responses(the_factory)

    # Phase 5: SzEngine read-only responses
    logger.info("Phase 5: Collecting SzEngine read-only responses...")
    collect_szengine_responses(the_factory)

    # Phase 6: Redo records
    logger.info("Phase 6: Collecting redo record responses...")
    collect_redo_responses(the_factory)

    # Phase 7: Reevaluate
    logger.info("Phase 7: Collecting reevaluate responses...")
    collect_reevaluate_responses(the_factory)

    # Phase 8: Delete records
    logger.info("Phase 8: Deleting records...")
    delete_records(the_factory)

    # Phase 9: SzProduct responses
    logger.info("Phase 9: Collecting SzProduct responses...")
    collect_szproduct_responses(the_factory)

    # Normalize all output files (deduplicate + sort)
    logger.info("Normalizing output files...")
    normalize_files(OUTPUT_DIRECTORY)

    logger.info("End   %s", os.path.basename(__file__))
