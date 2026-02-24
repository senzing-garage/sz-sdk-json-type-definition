#! /usr/bin/env python3

"""
Validate senzingsdk-RFC8927.json against JSONL testdata responses.

Bidirectional validation:
  1. Data -> Schema: keys/types in data that the schema doesn't describe
  2. Schema -> Data: properties in the schema that never appear in any data

Streams through JSONL files line-by-line to keep memory bounded.
"""

import argparse
import json
import logging
import os
import pathlib
import sys

# Logging.

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Global variables.

CURRENT_PATH = pathlib.Path(__file__).parent.resolve()
DEFAULT_INPUT_DIRECTORY = os.path.abspath(f"{CURRENT_PATH}/../testdata/responses_cord_raw")
DEFAULT_SCHEMA_FILE = os.path.abspath(f"{CURRENT_PATH}/../senzingsdk-RFC8927.json")

DEFINITIONS = {}
VARIABLE_JSON_KEY = "<user_defined_json_key>"


# -----------------------------------------------------------------------------
# Functions to process RFC8927.json and create schema structures.
# Reused from test_using_testdata_responses.py
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
            logger.error("Error: Bad 'pythonType:' %s", python_type)
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
# Schema path enumeration
# -----------------------------------------------------------------------------


def enumerate_schema_paths(schema_node, prefix=""):
    """Recursively enumerate all possible paths defined in the schema."""
    paths = set()
    if isinstance(schema_node, dict):
        for key, value in schema_node.items():
            path = f"{prefix}.{key}" if prefix else key
            paths.add(path)
            paths.update(enumerate_schema_paths(value, path))
    elif isinstance(schema_node, list) and schema_node:
        # List element schema — use [] to indicate array traversal.
        path = f"{prefix}.[]"
        paths.add(path)
        paths.update(enumerate_schema_paths(schema_node[0], path))
    # Scalar type strings (e.g. "int32", "string") are leaf nodes — no sub-paths.
    return paths


# -----------------------------------------------------------------------------
# Validation walker
# -----------------------------------------------------------------------------


def walk(path, schema_node, data_node, extra_keys, type_mismatches, schema_keys_seen):
    """Recursively walk data alongside schema, accumulating findings."""

    if data_node is None:
        return

    if isinstance(data_node, dict):
        if isinstance(schema_node, dict):
            for key, value in data_node.items():
                child_path = f"{path}.{key}"
                if key in schema_node:
                    schema_keys_seen.add(child_path)
                    walk(child_path, schema_node[key], value, extra_keys, type_mismatches, schema_keys_seen)
                elif VARIABLE_JSON_KEY in schema_node:
                    # Variable key (map type) — mark the variable key pattern as seen.
                    var_path = f"{path}.{VARIABLE_JSON_KEY}"
                    schema_keys_seen.add(var_path)
                    walk(child_path, schema_node[VARIABLE_JSON_KEY], value, extra_keys, type_mismatches, schema_keys_seen)
                else:
                    # Key in data not in schema.
                    type_name = type(value).__name__
                    if child_path not in extra_keys:
                        extra_keys[child_path] = {"types": set(), "count": 0}
                    extra_keys[child_path]["types"].add(type_name)
                    extra_keys[child_path]["count"] += 1
        elif schema_node in ("object", "****"):
            # Schema says opaque object — anything goes.
            return
        elif isinstance(schema_node, str):
            # Schema expected a scalar but got a dict.
            mismatch_path = path
            if mismatch_path not in type_mismatches:
                type_mismatches[mismatch_path] = {"schema_type": schema_node, "actual_types": set()}
            type_mismatches[mismatch_path]["actual_types"].add("dict")
        return

    if isinstance(data_node, list):
        if isinstance(schema_node, list) and schema_node:
            arr_path = f"{path}.[]"
            schema_keys_seen.add(arr_path)
            for item in data_node:
                walk(arr_path, schema_node[0], item, extra_keys, type_mismatches, schema_keys_seen)
        elif schema_node in ("object", "****"):
            return
        else:
            if path not in type_mismatches:
                type_mismatches[path] = {"schema_type": str(schema_node), "actual_types": set()}
            type_mismatches[path]["actual_types"].add("list")
        return

    # Scalar types.
    if isinstance(data_node, bool):
        actual_type = "boolean"
    elif isinstance(data_node, int):
        actual_type = "int32"
    elif isinstance(data_node, float):
        actual_type = "float32"
    elif isinstance(data_node, str):
        actual_type = "string"
    else:
        actual_type = type(data_node).__name__

    if isinstance(schema_node, str):
        compatible = {
            "int32": ("int32", "object", "****"),
            "float32": ("float32", "float64", "object", "****"),
            "string": ("string", "timestamp", "object", "****"),
            "boolean": ("boolean", "object", "****"),
        }
        allowed = compatible.get(actual_type, (actual_type, "object", "****"))
        if schema_node not in allowed:
            if path not in type_mismatches:
                type_mismatches[path] = {"schema_type": schema_node, "actual_types": set()}
            type_mismatches[path]["actual_types"].add(actual_type)
    elif isinstance(schema_node, dict) and schema_node:
        # Schema expected a dict but got a scalar.
        if path not in type_mismatches:
            type_mismatches[path] = {"schema_type": "dict", "actual_types": set()}
        type_mismatches[path]["actual_types"].add(actual_type)


# -----------------------------------------------------------------------------
# Schema loading
# -----------------------------------------------------------------------------


def load_schema(schema_file):
    """Load and process the RFC8927 schema file."""
    global DEFINITIONS

    with open(schema_file, "r", encoding="utf-8") as f:
        rfc8927 = json.load(f)

    DEFINITIONS = rfc8927.get("definitions", {})

    schemas = {}
    for key in DEFINITIONS:
        json_value = DEFINITIONS.get(key)
        if json_value is not None:
            schemas[key] = recurse_json(json_value)

    return schemas


# -----------------------------------------------------------------------------
# Main validation
# -----------------------------------------------------------------------------


def validate_file(filepath, schema_node):
    """Validate a single JSONL file against its schema definition."""

    all_schema_paths = enumerate_schema_paths(schema_node)
    extra_keys = {}
    type_mismatches = {}
    schema_keys_seen = set()
    line_count = 0
    root_name = pathlib.Path(filepath).stem

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            line_count += 1
            try:
                data = json.loads(line)
            except json.JSONDecodeError as exc:
                logger.warning("%s line %d: JSON parse error: %s", root_name, line_count, exc)
                continue
            walk(root_name, schema_node, data, extra_keys, type_mismatches, schema_keys_seen)

            if line_count % 100_000 == 0:
                logger.info("  %s: %d lines processed...", root_name, line_count)

    # Compute schema paths never seen in data.
    # Normalize: schema_keys_seen uses full paths from root (e.g. "RootName.KEY"),
    # but all_schema_paths are relative (e.g. "KEY"). Add root prefix to schema paths.
    all_schema_paths_full = set()
    for p in all_schema_paths:
        all_schema_paths_full.add(f"{root_name}.{p}")

    missing_keys = sorted(all_schema_paths_full - schema_keys_seen)

    return {
        "line_count": line_count,
        "extra_keys": extra_keys,
        "type_mismatches": type_mismatches,
        "missing_keys": missing_keys,
    }


def print_report(name, results):
    """Print a summary report for one file."""

    line_count = results["line_count"]
    extra_keys = results["extra_keys"]
    type_mismatches = results["type_mismatches"]
    missing_keys = results["missing_keys"]

    print(f"\n=== {name} ({line_count:,} lines) ===")

    # Extra keys.
    print(f"\nKeys in data NOT in schema ({len(extra_keys)}):")
    if extra_keys:
        for path in sorted(extra_keys.keys()):
            info = extra_keys[path]
            types_str = ", ".join(sorted(info["types"]))
            print(f"  {path}  ({types_str}, seen in {info['count']:,} lines)")
    else:
        print("  (none)")

    # Missing keys.
    print(f"\nKeys in schema NEVER seen in data ({len(missing_keys)}):")
    if missing_keys:
        for path in missing_keys:
            print(f"  {path}")
    else:
        print("  (none)")

    # Type mismatches.
    print(f"\nType mismatches ({len(type_mismatches)}):")
    if type_mismatches:
        for path in sorted(type_mismatches.keys()):
            info = type_mismatches[path]
            actual_str = ", ".join(sorted(info["actual_types"]))
            print(f"  {path}  (schema: {info['schema_type']}, actual: {actual_str})")
    else:
        print("  (none)")


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------


def main():
    """Main entry point."""

    parser = argparse.ArgumentParser(
        description="Validate senzingsdk-RFC8927.json against JSONL testdata responses."
    )
    parser.add_argument(
        "--input-dir",
        default=DEFAULT_INPUT_DIRECTORY,
        help=f"Directory containing JSONL files (default: {DEFAULT_INPUT_DIRECTORY})",
    )
    parser.add_argument(
        "--schema",
        default=DEFAULT_SCHEMA_FILE,
        help=f"RFC8927 schema file (default: {DEFAULT_SCHEMA_FILE})",
    )
    args = parser.parse_args()

    logger.info("Begin %s", os.path.basename(__file__))
    logger.info("Schema: %s", args.schema)
    logger.info("Input dir: %s", args.input_dir)

    # Load schema.

    schemas = load_schema(args.schema)
    logger.info("Loaded %d schema definitions", len(schemas))

    # Process each JSONL file.

    jsonl_files = sorted(
        f for f in os.listdir(args.input_dir) if f.endswith(".jsonl")
    )
    logger.info("Found %d JSONL files", len(jsonl_files))

    total_extra = 0
    total_missing = 0
    total_mismatches = 0
    files_processed = 0
    files_skipped = 0

    for jsonl_file in jsonl_files:
        name = pathlib.Path(jsonl_file).stem
        schema_node = schemas.get(name)

        if schema_node is None:
            logger.warning("No schema definition found for: %s", name)
            files_skipped += 1
            continue

        filepath = os.path.join(args.input_dir, jsonl_file)
        logger.info("Validating %s ...", name)

        results = validate_file(filepath, schema_node)
        print_report(name, results)

        total_extra += len(results["extra_keys"])
        total_missing += len(results["missing_keys"])
        total_mismatches += len(results["type_mismatches"])
        files_processed += 1

    # Summary.

    print(f"\n{'=' * 60}")
    print(f"TOTALS: {files_processed} files processed, {files_skipped} skipped")
    print(f"  Extra keys (data not in schema):    {total_extra}")
    print(f"  Missing keys (schema not in data):  {total_missing}")
    print(f"  Type mismatches:                     {total_mismatches}")
    print(f"{'=' * 60}")

    logger.info("End   %s", os.path.basename(__file__))

    if total_mismatches > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
