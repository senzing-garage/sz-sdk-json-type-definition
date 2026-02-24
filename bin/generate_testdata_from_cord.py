#! /usr/bin/env python3

# pylint: disable=duplicate-code

"""
generate_testdata_from_cord.py

Generate test data by fetching CORD (Collections Of Relatable Data) records
from senzing.com and calling every abstract method that returns str across
all 5 Senzing SDK abstract classes, using flags=-1 (all flag bits on).

Output: testdata/responses_cord/
"""

import argparse
import contextlib
import json
import logging
import os
import pathlib
import sys
import urllib.request

from senzing import SzAbstractFactory
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
OUTPUT_DIRECTORY = os.path.abspath(f"{CURRENT_PATH}/../testdata/responses_cord")

CORD_URLS = [
    "https://senzing.com/datasets/brightquery_companies-lasvegas.jsonl",
    "https://senzing.com/datasets/enformion-lasvegas_A.jsonl",
    "https://senzing.com/datasets/equifax-lasvegas_A.jsonl",
    "https://senzing.com/datasets/gleif-lasvegas.jsonl",
    "https://senzing.com/datasets/gleif-london.jsonl",
    "https://senzing.com/datasets/gleif-moscow.jsonl",
    "https://senzing.com/datasets/globaldata-london_central_a.jsonl",
    "https://senzing.com/datasets/icij-lasvegas.jsonl",
    "https://senzing.com/datasets/icij-london.jsonl",
    "https://senzing.com/datasets/icij-moscow.jsonl",
    "https://senzing.com/datasets/nominodata_combined-lasvegas.jsonl",
    "https://senzing.com/datasets/nominodata_risk-moscow.jsonl",
    "https://senzing.com/datasets/npi-lasvegas.jsonl",
    "https://senzing.com/datasets/ofac-london.jsonl",
    "https://senzing.com/datasets/ofac-moscow.jsonl",
    "https://senzing.com/datasets/open_ownership-lasvegas.jsonl",
    "https://senzing.com/datasets/open_ownership-moscow.jsonl",
    "https://senzing.com/datasets/open_sanctions-london.jsonl",
    "https://senzing.com/datasets/open_sanctions-moscow.jsonl",
    "https://senzing.com/datasets/ppp_loans_over_150k-lasvegas.jsonl",
    "https://senzing.com/datasets/profound-lasvegas.jsonl",
    "https://senzing.com/datasets/us_labor_violations-lasvegas.jsonl",
]

CORD_DATA_SOURCES = [
    "BQ-COMPANY",
    "ENFORMION",
    "EQUIFAX",
    "GLEIF",
    "GLOBALDATA",
    "ICIJ",
    "NOMINO-RISK",
    "NOMINODATA",
    "NPI-PROVIDERS",
    "OFAC",
    "OPEN-OWNERSHIP",
    "OPEN-SANCTIONS",
    "PPP_LOANS",
    "PROFOUND",
    "US-LABOR-VIOLATIONS",
]

SEARCH_RECORDS = [
    {
        "NAME_ORG": "Nurish Inc",
        "ADDR_FULL": "1951 NW 7th Avenue Miami FL 33136",
    },
    {
        "NAME_FULL": "Dale Jones",
        "ADDR_FULL": "3151 N Rainbow Blvd Las Vegas NV 89108",
    },
    {
        "NAME_ORG": "Medical Group Sun City",
        "ADDR_FULL": "2440 Professional Ct Las Vegas NV 89128",
    },
]

LOADED_RECORD_KEYS = []  # [{"data_source": ..., "record_id": ..., "record_definition": ...}]
LOADED_ENTITY_IDS = []

# -----------------------------------------------------------------------------
# Data fetching
# -----------------------------------------------------------------------------


def fetch_cord_lines(url):
    """Fetch lines from a CORD URL, return list of (line_str, line_dict) tuples."""
    results = []
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request) as response:  # noqa: S310
        for raw_line in response:
            line_str = raw_line.decode("utf-8").strip()
            if not line_str:
                continue
            line_dict = json.loads(line_str)
            results.append((line_str, line_dict))
    return results


def load_cord_data():
    """Fetch all CORD URLs, return list of (line_str, line_dict) tuples."""
    all_records = []
    for url in CORD_URLS:
        logger.info("Fetching %s", url)
        all_records.extend(fetch_cord_lines(url))
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
    except Exception as err:
        logger.error("%s", err)

    return sz_abstract_factory


def register_datasources(sz_abstract_factory: SzAbstractFactory):
    """Add CORD Data Sources to the Senzing repository."""
    sz_config_manager = sz_abstract_factory.create_configmanager()

    current_config_id = sz_config_manager.get_default_config_id()
    sz_config = sz_config_manager.create_config_from_config_id(current_config_id)

    for data_source in CORD_DATA_SOURCES:
        sz_config.register_data_source(data_source)

    new_config = sz_config.export()
    new_config_id = sz_config_manager.register_config(new_config, "generate_testdata_from_cord.py")
    sz_config_manager.replace_default_config_id(current_config_id, new_config_id)
    sz_abstract_factory.reinitialize(new_config_id)


# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


def progress(iterable, label, total=None):
    """Yield items from iterable with a visual progress bar on stderr."""
    if total is None:
        total = len(iterable)
    for i, item in enumerate(iterable, 1):
        filled = (i * 50) // total if total else 0
        bar = "\u2588" * filled + "\u2591" * (50 - filled)
        pct = (i * 100) // total if total else 0
        print(f"\r  {label}: |{bar}| {i}/{total} ({pct}%)", end="", flush=True, file=sys.stderr)
        yield item
    if total > 0:
        print(file=sys.stderr)


@contextlib.contextmanager
def safe_iteration(label):
    """Context manager that catches and logs any exception, allowing loop continuation.

    Only KeyboardInterrupt and GeneratorExit are re-raised so that
    Ctrl-C and generator cleanup still work.  Everything else —
    including BaseException subclasses the Senzing C library may
    raise — is logged and suppressed so the enclosing loop can
    advance to the next iteration.
    """
    try:
        yield
    except (KeyboardInterrupt, GeneratorExit):
        raise
    except BaseException as err:
        logger.warning("%s: %s", label, err)


@contextlib.contextmanager
def streaming_output(title):
    """Context manager that yields a write function for streaming lines to a file.

    Each call to the returned function writes one JSON line immediately,
    avoiding the need to accumulate responses in memory.  Deduplication
    is handled later by normalize_files().
    """
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIRECTORY, f"{title}.jsonl")
    with open(filepath, "w", encoding="utf-8") as fh:

        def write_line(line):
            if line:
                fh.write(f"{line}\n")

        yield write_line
    logger.info("Wrote %s", filepath)


def remove_duplicate_lines(input_filepath, output_filepath=None):
    """Remove duplicate JSON lines from a file, sort remaining lines.

    Always ensures an empty-JSON sentinel line ("{}") so every file has
    at least one entry and test scaffolding can safely parse the file.
    """
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

    # Ensure the empty-JSON sentinel is present
    if "{}" not in unique_lines:
        unique_lines.add("{}")

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
    for record in progress(LOADED_RECORD_KEYS, "get_entity_ids"):
        with safe_iteration("get_entity_ids"):
            response = sz_engine.get_entity_by_record_id(record.get("data_source", ""), record.get("record_id", ""))
            response_dict = json.loads(response)
            entity_id = response_dict.get("RESOLVED_ENTITY", {}).get("ENTITY_ID", 0)
            if entity_id and entity_id not in result:
                result.append(entity_id)
    return result


# -----------------------------------------------------------------------------
# Phase 1: Add records (captures SzEngineAddRecordResponse)
# -----------------------------------------------------------------------------


def add_records(sz_abstract_factory: SzAbstractFactory, cord_records):
    """Add CORD records to Senzing, collect AddRecord responses."""
    sz_engine = sz_abstract_factory.create_engine()
    total = len(cord_records)

    with streaming_output("SzEngineAddRecordResponse") as write_line:
        for i, (line_str, line_dict) in enumerate(cord_records, 1):
            data_source = line_dict.get("DATA_SOURCE")
            record_id = line_dict.get("RECORD_ID")

            LOADED_RECORD_KEYS.append(
                {
                    "data_source": data_source,
                    "record_id": record_id,
                    "record_definition": line_str,
                }
            )

            with safe_iteration(f"add_record {data_source}/{record_id}"):
                response = sz_engine.add_record(data_source, record_id, line_str, ALL_FLAGS)
                write_line(response)

            filled = (i * 50) // total if total else 0
            bar = "\u2588" * filled + "\u2591" * (50 - filled)
            pct = (i * 100) // total if total else 0
            print(f"\r  add_records: |{bar}| {i}/{total} ({pct}%)", end="", flush=True, file=sys.stderr)

    if total > 0:
        print(file=sys.stderr)


# -----------------------------------------------------------------------------
# Phase 2: SzConfig responses
# -----------------------------------------------------------------------------


def collect_szconfig_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect responses from SzConfig methods."""
    sz_config_manager = sz_abstract_factory.create_configmanager()
    current_config_id = sz_config_manager.get_default_config_id()
    sz_config = sz_config_manager.create_config_from_config_id(current_config_id)

    # export
    with streaming_output("SzConfigExportResponse") as write_line:
        response = sz_config.export()
        write_line(response)

    # get_data_source_registry
    with streaming_output("SzConfigGetDataSourceRegistryResponse") as write_line:
        response = sz_config.get_data_source_registry()
        write_line(response)

    # register_data_source (use a temp DS that won't be persisted)
    with streaming_output("SzConfigRegisterDataSourceResponse") as write_line:
        with safe_iteration("register_data_source"):
            response = sz_config.register_data_source("GENERATE_TEST_DS")
            write_line(response)

    # unregister_data_source
    with streaming_output("SzConfigUnregisterDataSourceResponse") as write_line:
        with safe_iteration("unregister_data_source"):
            response = sz_config.unregister_data_source("GENERATE_TEST_DS")
            write_line(response)


# -----------------------------------------------------------------------------
# Phase 3: SzConfigManager responses
# -----------------------------------------------------------------------------


def collect_szconfigmanager_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect responses from SzConfigManager methods."""
    sz_config_manager = sz_abstract_factory.create_configmanager()

    # get_config_registry
    with streaming_output("SzConfigManagerGetConfigRegistryResponse") as write_line:
        response = sz_config_manager.get_config_registry()
        write_line(response)


# -----------------------------------------------------------------------------
# Phase 4: SzDiagnostic responses
# -----------------------------------------------------------------------------


def collect_szdiagnostic_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect responses from SzDiagnostic methods."""
    sz_diagnostic = sz_abstract_factory.create_diagnostic()
    sz_engine = sz_abstract_factory.create_engine()

    # check_repository_performance
    with streaming_output("SzDiagnosticCheckRepositoryPerformanceResponse") as write_line:
        response = sz_diagnostic.check_repository_performance(2)
        write_line(response)

    # get_repository_info
    with streaming_output("SzDiagnosticGetRepositoryInfoResponse") as write_line:
        response = sz_diagnostic.get_repository_info()
        write_line(response)

    # get_feature — extract feature IDs from entity responses
    feature_ids = []
    for entity_id in progress(LOADED_ENTITY_IDS, "get_feature (scan entity features)"):
        with safe_iteration("get_feature (scan entity features)"):
            response = sz_engine.get_entity_by_entity_id(entity_id, ALL_FLAGS)
            response_dict = json.loads(response)
            features = response_dict.get("RESOLVED_ENTITY", {}).get("FEATURES", {})
            for feature_values in features.values():
                for feature_value in feature_values:
                    fid = feature_value.get("LIB_FEAT_ID")
                    if fid and fid not in feature_ids:
                        feature_ids.append(fid)

    with streaming_output("SzDiagnosticGetFeatureResponse") as write_line:
        for fid in progress(feature_ids, "get_feature"):
            with safe_iteration("get_feature"):
                response = sz_diagnostic.get_feature(fid)
                write_line(response)


# -----------------------------------------------------------------------------
# Phase 5: SzEngine responses (read-only queries)
# -----------------------------------------------------------------------------


def collect_szengine_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect responses from read-only SzEngine methods."""
    sz_engine = sz_abstract_factory.create_engine()
    n_entities = len(LOADED_ENTITY_IDS)
    n_records = len(LOADED_RECORD_KEYS)

    # --- find_interesting_entities_by_entity_id ---
    with streaming_output("SzEngineFindInterestingEntitiesByEntityIdResponse") as write_line:
        for entity_id in progress(LOADED_ENTITY_IDS, "find_interesting_entities_by_entity_id"):
            with safe_iteration("find_interesting_entities_by_entity_id"):
                response = sz_engine.find_interesting_entities_by_entity_id(entity_id, ALL_FLAGS)
                write_line(response)

    # --- find_interesting_entities_by_record_id ---
    with streaming_output("SzEngineFindInterestingEntitiesByRecordIdResponse") as write_line:
        for record in progress(LOADED_RECORD_KEYS, "find_interesting_entities_by_record_id"):
            with safe_iteration("find_interesting_entities_by_record_id"):
                response = sz_engine.find_interesting_entities_by_record_id(
                    record["data_source"], record["record_id"], ALL_FLAGS
                )
                write_line(response)

    # --- find_network_by_entity_id ---
    with streaming_output("SzEngineFindNetworkByEntityIdResponse") as write_line:
        for i, entity_id in enumerate(progress(LOADED_ENTITY_IDS, "find_network_by_entity_id")):
            with safe_iteration("find_network_by_entity_id"):
                entity_ids = [LOADED_ENTITY_IDS[(i + j) % n_entities] for j in range(min(5, n_entities))]
                response = sz_engine.find_network_by_entity_id(
                    entity_ids, MAX_DEGREES, BUILD_OUT_DEGREES, BUILD_OUT_MAX_ENTITIES, ALL_FLAGS
                )
                write_line(response)

    # --- find_network_by_record_id ---
    with streaming_output("SzEngineFindNetworkByRecordIdResponse") as write_line:
        for i, record in enumerate(progress(LOADED_RECORD_KEYS, "find_network_by_record_id")):
            with safe_iteration("find_network_by_record_id"):
                record_keys = [
                    (
                        LOADED_RECORD_KEYS[(i + j) % n_records]["data_source"],
                        LOADED_RECORD_KEYS[(i + j) % n_records]["record_id"],
                    )
                    for j in range(min(5, n_records))
                ]
                response = sz_engine.find_network_by_record_id(
                    record_keys, MAX_DEGREES, BUILD_OUT_DEGREES, BUILD_OUT_MAX_ENTITIES, ALL_FLAGS
                )
                write_line(response)

    # --- find_path_by_entity_id ---
    with streaming_output("SzEngineFindPathByEntityIdResponse") as write_line:
        for i in range(PATH_VARIATION_COUNT):
            if n_entities < 2:
                break
            with safe_iteration("find_path_by_entity_id"):
                start_id = LOADED_ENTITY_IDS[i % n_entities]
                end_id = LOADED_ENTITY_IDS[(i + 1) % n_entities]
                response = sz_engine.find_path_by_entity_id(start_id, end_id, MAX_DEGREES, None, None, ALL_FLAGS)
                write_line(response)

    # --- find_path_by_record_id ---
    with streaming_output("SzEngineFindPathByRecordIdResponse") as write_line:
        for i in range(PATH_VARIATION_COUNT):
            if n_records < 2:
                break
            with safe_iteration("find_path_by_record_id"):
                start = LOADED_RECORD_KEYS[i % n_records]
                end = LOADED_RECORD_KEYS[(i + 1) % n_records]
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
                write_line(response)

    # --- get_entity_by_entity_id ---
    with streaming_output("SzEngineGetEntityByEntityIdResponse") as write_line:
        for entity_id in progress(LOADED_ENTITY_IDS, "get_entity_by_entity_id"):
            with safe_iteration("get_entity_by_entity_id"):
                response = sz_engine.get_entity_by_entity_id(entity_id, ALL_FLAGS)
                write_line(response)

    # --- get_entity_by_record_id ---
    with streaming_output("SzEngineGetEntityByRecordIdResponse") as write_line:
        for record in progress(LOADED_RECORD_KEYS, "get_entity_by_record_id"):
            with safe_iteration("get_entity_by_record_id"):
                response = sz_engine.get_entity_by_record_id(record["data_source"], record["record_id"], ALL_FLAGS)
                write_line(response)

    # --- get_record ---
    with streaming_output("SzEngineGetRecordResponse") as write_line:
        for record in progress(LOADED_RECORD_KEYS, "get_record"):
            with safe_iteration("get_record"):
                response = sz_engine.get_record(record["data_source"], record["record_id"], ALL_FLAGS)
                write_line(response)

    # --- get_record_preview ---
    with streaming_output("SzEngineGetRecordPreviewResponse") as write_line:
        for record in progress(LOADED_RECORD_KEYS, "get_record_preview"):
            with safe_iteration("get_record_preview"):
                record_definition = record.get("record_definition", "")
                response = sz_engine.get_record_preview(record_definition, ALL_FLAGS)
                write_line(response)

    # --- get_stats ---
    with streaming_output("SzEngineGetStatsResponse") as write_line:
        with safe_iteration("get_stats"):
            response = sz_engine.get_stats()
            write_line(response)

    # --- get_virtual_entity_by_record_id ---
    with streaming_output("SzEngineGetVirtualEntityByRecordIdResponse") as write_line:
        for i, record in enumerate(progress(LOADED_RECORD_KEYS, "get_virtual_entity_by_record_id")):
            with safe_iteration("get_virtual_entity_by_record_id"):
                record_keys = [
                    (
                        LOADED_RECORD_KEYS[(i + j) % n_records]["data_source"],
                        LOADED_RECORD_KEYS[(i + j) % n_records]["record_id"],
                    )
                    for j in range(min(5, n_records))
                ]
                response = sz_engine.get_virtual_entity_by_record_id(record_keys, ALL_FLAGS)
                write_line(response)

    # --- how_entity_by_entity_id ---
    with streaming_output("SzEngineHowEntityByEntityIdResponse") as write_line:
        for entity_id in progress(LOADED_ENTITY_IDS, "how_entity_by_entity_id"):
            with safe_iteration("how_entity_by_entity_id"):
                response = sz_engine.how_entity_by_entity_id(entity_id, ALL_FLAGS)
                write_line(response)

    # --- search_by_attributes ---
    with streaming_output("SzEngineSearchByAttributesResponse") as write_line:
        for search_record in SEARCH_RECORDS:
            with safe_iteration("search_by_attributes"):
                attributes = json.dumps(search_record)
                response = sz_engine.search_by_attributes(attributes, ALL_FLAGS, "")
                write_line(response)

    # --- why_entities ---
    with streaming_output("SzEngineWhyEntitiesResponse") as write_line:
        for i, entity_id in enumerate(progress(LOADED_ENTITY_IDS, "why_entities")):
            with safe_iteration("why_entities"):
                entity_id_2 = LOADED_ENTITY_IDS[(i + 1) % n_entities]
                response = sz_engine.why_entities(entity_id, entity_id_2, ALL_FLAGS)
                write_line(response)

    # --- why_record_in_entity ---
    with streaming_output("SzEngineWhyRecordInEntityResponse") as write_line:
        for record in progress(LOADED_RECORD_KEYS, "why_record_in_entity"):
            with safe_iteration("why_record_in_entity"):
                response = sz_engine.why_record_in_entity(record["data_source"], record["record_id"], ALL_FLAGS)
                write_line(response)

    # --- why_records ---
    with streaming_output("SzEngineWhyRecordsResponse") as write_line:
        for i, record in enumerate(progress(LOADED_RECORD_KEYS, "why_records")):
            with safe_iteration("why_records"):
                record_2 = LOADED_RECORD_KEYS[(i + 1) % n_records]
                response = sz_engine.why_records(
                    record["data_source"],
                    record["record_id"],
                    record_2["data_source"],
                    record_2["record_id"],
                    ALL_FLAGS,
                )
                write_line(response)

    # --- why_search ---
    with streaming_output("SzEngineWhySearchResponse") as write_line:
        for entity_id in progress(LOADED_ENTITY_IDS, "why_search"):
            for search_record in SEARCH_RECORDS:
                with safe_iteration("why_search"):
                    attributes = json.dumps(search_record)
                    response = sz_engine.why_search(attributes, entity_id, ALL_FLAGS, "")
                    write_line(response)

    # --- fetch_next (via export_json_entity_report) ---
    with streaming_output("SzEngineFetchNextResponse") as write_line:
        handle = None
        with safe_iteration("export_json_entity_report"):
            handle = sz_engine.export_json_entity_report(ALL_FLAGS)
        if handle is not None:
            while True:
                try:
                    response = sz_engine.fetch_next(handle)
                    if not response:
                        break
                    write_line(response)
                except (KeyboardInterrupt, GeneratorExit):
                    raise
                except BaseException as err:
                    logger.warning("fetch_next: %s", err)
            with safe_iteration("close_export_report"):
                sz_engine.close_export_report(handle)


# -----------------------------------------------------------------------------
# Phase 6: Redo records
# -----------------------------------------------------------------------------


def collect_redo_responses(sz_abstract_factory: SzAbstractFactory):
    """Drain and process redo records, collect responses."""
    sz_engine = sz_abstract_factory.create_engine()

    # Drain all redo records
    redo_records = []
    with streaming_output("SzEngineGetRedoRecordResponse") as write_line:
        while True:
            try:
                response = sz_engine.get_redo_record()
            except (KeyboardInterrupt, GeneratorExit):
                raise
            except BaseException as err:
                logger.warning("get_redo_record: %s", err)
                continue
            if not response:
                break
            redo_records.append(response)
            write_line(response)

    # Process redo records
    with streaming_output("SzEngineProcessRedoRecordResponse") as write_line:
        for redo_record in progress(redo_records, "process_redo_record"):
            with safe_iteration("process_redo_record"):
                response = sz_engine.process_redo_record(redo_record, ALL_FLAGS)
                write_line(response)


# -----------------------------------------------------------------------------
# Phase 7: Reevaluate
# -----------------------------------------------------------------------------


def collect_reevaluate_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect reevaluate_entity and reevaluate_record responses."""
    sz_engine = sz_abstract_factory.create_engine()

    # reevaluate_entity
    with streaming_output("SzEngineReevaluateEntityResponse") as write_line:
        for entity_id in progress(LOADED_ENTITY_IDS, "reevaluate_entity"):
            with safe_iteration("reevaluate_entity"):
                response = sz_engine.reevaluate_entity(entity_id, ALL_FLAGS)
                write_line(response)

    # reevaluate_record
    with streaming_output("SzEngineReevaluateRecordResponse") as write_line:
        for record in progress(LOADED_RECORD_KEYS, "reevaluate_record"):
            with safe_iteration("reevaluate_record"):
                response = sz_engine.reevaluate_record(record["data_source"], record["record_id"], ALL_FLAGS)
                write_line(response)


# -----------------------------------------------------------------------------
# Phase 8: Delete records (captures SzEngineDeleteRecordResponse)
# -----------------------------------------------------------------------------


def delete_records(sz_abstract_factory: SzAbstractFactory):
    """Delete all loaded records, collect DeleteRecord responses."""
    sz_engine = sz_abstract_factory.create_engine()

    with streaming_output("SzEngineDeleteRecordResponse") as write_line:
        for record in progress(LOADED_RECORD_KEYS, "delete_record"):
            with safe_iteration("delete_record"):
                response = sz_engine.delete_record(record["data_source"], record["record_id"], ALL_FLAGS)
                write_line(response)


# -----------------------------------------------------------------------------
# Phase 9: SzProduct responses
# -----------------------------------------------------------------------------


def collect_szproduct_responses(sz_abstract_factory: SzAbstractFactory):
    """Collect responses from SzProduct methods."""
    sz_product = sz_abstract_factory.create_product()

    with streaming_output("SzProductGetLicenseResponse") as write_line:
        response = sz_product.get_license()
        write_line(response)

    with streaming_output("SzProductGetVersionResponse") as write_line:
        response = sz_product.get_version()
        write_line(response)


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def do_load_database():
    """Download CORD data and populate Senzing (Phase 1 only)."""

    # Fetch CORD records from senzing.com
    logger.info("Fetching CORD records from senzing.com...")
    all_cord_records = load_cord_data()
    logger.info("Fetched %d records", len(all_cord_records))

    # Create SzAbstractFactory
    the_factory = create_sz_abstract_factory()

    # Register data sources
    logger.info("Registering data sources...")
    register_datasources(the_factory)

    # Phase 1: Add records
    logger.info("Phase 1: Adding records...")
    add_records(the_factory, all_cord_records)


def do_extract_responses():
    """Query Senzing and extract responses (Phase 2 through Phase 9)."""

    # Create SzAbstractFactory
    the_factory = create_sz_abstract_factory()

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    # Populate LOADED_RECORD_KEYS from CORD URLs
    logger.info("Fetching CORD records to build LOADED_RECORD_KEYS...")
    all_cord_records = load_cord_data()
    for line_str, line_dict in all_cord_records:
        LOADED_RECORD_KEYS.append(
            {
                "data_source": line_dict.get("DATA_SOURCE"),
                "record_id": line_dict.get("RECORD_ID"),
                "record_definition": line_str,
            }
        )
    logger.info("Loaded %d record keys", len(LOADED_RECORD_KEYS))

    # Collect entity IDs from existing records
    logger.info("Collecting entity IDs...")
    LOADED_ENTITY_IDS = get_entity_ids(the_factory)
    logger.info("Found %d unique entity IDs", len(LOADED_ENTITY_IDS))
    logger.info("Found %d records", len(LOADED_RECORD_KEYS))

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


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate test data from CORD (Collections Of Relatable Data).",
    )
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser(
        "load-database",
        help="Download CORD data and populate Senzing (Phase 1 only).",
    )

    subparsers.add_parser(
        "extract-responses",
        help="Query Senzing and extract responses (Phase 2-9), then normalize output files.",
    )

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    logger.info("Begin %s %s", os.path.basename(__file__), args.command)

    if args.command == "load-database":
        do_load_database()
    elif args.command == "extract-responses":
        do_extract_responses()

    logger.info("End   %s %s", os.path.basename(__file__), args.command)
