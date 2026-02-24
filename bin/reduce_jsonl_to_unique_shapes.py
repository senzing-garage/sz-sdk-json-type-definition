#! /usr/bin/env python3

# pylint: disable=duplicate-code

"""
reduce_jsonl_to_unique_shapes.py

Reduce JSONL files to one representative line per unique JSON "shape"
(structural fingerprint).

A shape is defined recursively:
  - dict  -> frozenset of (key, value_shape) pairs
  - list  -> frozenset of unique element shapes (empty list is distinct)
  - scalar -> type name (str, int, float, bool, null)

Two JSON lines have the same shape iff they have identical key structures
at every nesting level and identical value types everywhere.

Usage:
    python bin/reduce_jsonl_to_unique_shapes.py
    python bin/reduce_jsonl_to_unique_shapes.py --input-dir path/in --output-dir path/out
"""

import argparse
import contextlib
import hashlib
import json
import logging
import os
import pathlib
import subprocess
import sys
import tempfile

# Logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Global constants

CURRENT_PATH = pathlib.Path(__file__).parent.resolve()
TESTDATA_DIRECTORY = os.path.abspath(f"{CURRENT_PATH}/../testdata")
DEFAULT_INPUT_DIRECTORY = f"{TESTDATA_DIRECTORY}/responses_cord_raw"
DEFAULT_OUTPUT_DIRECTORY = f"{TESTDATA_DIRECTORY}/responses_cord"


# -----------------------------------------------------------------------------
# Shape fingerprinting
# -----------------------------------------------------------------------------


def compute_shape(obj):
    """Compute a recursive structural fingerprint of a JSON value.

    Returns a hashable, canonical representation capturing:
    - For dicts: the full set of (key, value_shape) pairs at every nesting level
    - For lists: the set of unique element shapes (empty vs non-empty distinguished)
    - For scalars: just the type name
    """
    if isinstance(obj, dict):
        return ("dict", frozenset((k, compute_shape(v)) for k, v in obj.items()))
    if isinstance(obj, list):
        if not obj:
            return ("list_empty",)
        element_shapes = frozenset(compute_shape(item) for item in obj)
        return ("list", element_shapes)
    if isinstance(obj, bool):  # Must precede int check; bool is subclass of int
        return ("bool",)
    if isinstance(obj, int):
        return ("int",)
    if isinstance(obj, float):
        return ("float",)
    if isinstance(obj, str):
        return ("str",)
    if obj is None:
        return ("null",)
    return (type(obj).__name__,)


def shape_hash(obj):
    """Compute a hex digest of the shape for efficient set operations."""
    sig = compute_shape(obj)
    return hashlib.sha256(str(sig).encode()).hexdigest()


# -----------------------------------------------------------------------------
# File reduction
# -----------------------------------------------------------------------------


def reduce_file(input_filepath, output_filepath):
    """Reduce a single JSONL file to one representative line per unique shape.

    Reads streaming (one line at a time) to handle very large files.
    Representatives are written to a temp file immediately to avoid
    holding all representative JSON strings in memory (critical for files
    like FindNetworkByRecordId where each line can be hundreds of KB and
    there can be hundreds of thousands of unique shapes).

    Final output is sorted with sort_keys=True.
    Always ensures {} sentinel line is present.
    """
    seen_shapes = set()
    shape_count = 0

    os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

    # Pass 1: stream through input, write unique-shape representatives to temp file
    tmpfd, tmppath = tempfile.mkstemp(suffix=".jsonl", dir=os.path.dirname(output_filepath))
    try:
        line_count = 0
        with os.fdopen(tmpfd, "w", encoding="utf-8") as tmpfile, open(
            input_filepath, "r", encoding="utf-8"
        ) as infile:
            for line in infile:
                line = line.strip()
                if not line:
                    continue
                line_count += 1

                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    logger.warning("Skipping invalid JSON at line %d in %s", line_count, input_filepath)
                    continue

                h = shape_hash(obj)
                if h not in seen_shapes:
                    seen_shapes.add(h)
                    tmpfile.write(f"{json.dumps(obj, sort_keys=True)}\n")

                if line_count % 50000 == 0:
                    print(
                        f"\r  {os.path.basename(input_filepath)}: {line_count} lines, "
                        f"{len(seen_shapes)} unique shapes",
                        end="",
                        flush=True,
                        file=sys.stderr,
                    )

        if line_count >= 50000:
            print(file=sys.stderr)

        # Ensure {} sentinel is in temp file
        empty_h = shape_hash({})
        if empty_h not in seen_shapes:
            with open(tmppath, "a", encoding="utf-8") as tmpfile:
                tmpfile.write("{}\n")

        # Pass 2: sort temp file using external sort (memory-efficient)
        subprocess.run(["sort", "-o", output_filepath, tmppath], check=True)  # noqa: S603, S607

        # Count output lines
        shape_count = 0
        with open(output_filepath, "r", encoding="utf-8") as f:
            for _ in f:
                shape_count += 1
    finally:
        with contextlib.suppress(OSError):
            os.unlink(tmppath)

    reduction = (1 - shape_count / max(line_count, 1)) * 100
    logger.info(
        "%s: %d lines -> %d unique shapes (%.1f%% reduction)",
        os.path.basename(input_filepath),
        line_count,
        shape_count,
        reduction,
    )


def reduce_directory(input_directory, output_directory):
    """Process all .jsonl files in input_directory, writing reduced versions to output_directory."""
    os.makedirs(output_directory, exist_ok=True)

    jsonl_files = sorted(f for f in os.listdir(input_directory) if f.endswith(".jsonl"))

    if not jsonl_files:
        logger.warning("No .jsonl files found in %s", input_directory)
        return

    logger.info("Processing %d files from %s -> %s", len(jsonl_files), input_directory, output_directory)

    for filename in jsonl_files:
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)

        # Skip empty files -- still create output with just {} sentinel
        if os.path.getsize(input_path) == 0:
            with open(output_path, "w", encoding="utf-8") as outfile:
                outfile.write("{}\n")
            logger.info("%s: empty input -> sentinel only", filename)
            continue

        reduce_file(input_path, output_path)


# -----------------------------------------------------------------------------
# CLI
# -----------------------------------------------------------------------------


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Reduce JSONL files to unique structural shapes. "
            "Keeps one representative line per unique JSON structure, "
            "where structure is defined by the recursive key/type hierarchy."
        ),
    )
    parser.add_argument(
        "--input-dir",
        default=DEFAULT_INPUT_DIRECTORY,
        help=f"Input directory containing .jsonl files (default: {DEFAULT_INPUT_DIRECTORY})",
    )
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIRECTORY,
        help=f"Output directory for reduced .jsonl files (default: {DEFAULT_OUTPUT_DIRECTORY})",
    )
    return parser.parse_args()


if __name__ == "__main__":

    args = parse_args()

    logger.info("Begin %s", os.path.basename(__file__))
    reduce_directory(args.input_dir, args.output_dir)
    logger.info("End   %s", os.path.basename(__file__))
