#! /usr/bin/env python3

"""
Used to generate testdata/*.json
"""

import json
import logging
import os

from test_cases import TEST_CASES

IS_DEBUG = False
FINAL_RESULT = {}

OUTPUT_DIRECTORY = "./testdata"

# -----------------------------------------------------------------------------
# --- Helpers
# -----------------------------------------------------------------------------


def canonical_json(json_string):
    """Create compact JSON.  No spaces."""
    json_object = json.loads(json_string)
    result = json.dumps(json_object, sort_keys=True, separators=(",", ":"))
    return result


# -----------------------------------------------------------------------------
# --- Main
# -----------------------------------------------------------------------------

# Set up logging.

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

logging.info("{0}".format("-" * 80))
logging.info("--- {0} - Begin".format(os.path.basename(__file__)))
logging.info("{0}".format("-" * 80))


for senzing_api_class, method_test_cases in TEST_CASES.items():
    metadata = method_test_cases.get("metadata", {})
    tests = method_test_cases.get("tests", {})
    for test_case_name, test_case_json in tests.items():
        filename = f"{OUTPUT_DIRECTORY}/{senzing_api_class}-{test_case_name}.json"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(canonical_json(test_case_json))

# Epilog.

logging.info("{0}".format("-" * 80))
logging.info("--- {0} - End".format(os.path.basename(__file__)))
logging.info("{0}".format("-" * 80))
