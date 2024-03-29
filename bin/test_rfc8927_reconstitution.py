#! /usr/bin/env python3

"""
Requires minimum Python 3.10
"""

import builtins
import json
import logging
import os
import sys

# Tricky code:  Need to import all python.typedef.* for the "not in globals()" test
# pylint: disable=unused-wildcard-import

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from python.typedef import *  # pylint: disable=wrong-import-position disable=wildcard-import

INPUT_FILE = "bin/response-testcases.json"

DEBUG = False
ERROR_COUNT = 0
TEST_COUNT = 0

# -----------------------------------------------------------------------------
# --- Functions
# -----------------------------------------------------------------------------


def is_equal(test_name, source, target):
    """Determin if source and target are equal. Return boolean"""

    result = True

    if DEBUG:
        print(test_name)

    if target is None:
        if source is None:
            return True
        return False

    source_type = type(source)
    if source_type == builtins.dict:
        for key, value in source.items():
            if not is_equal("{0}.{1}".format(test_name, key), value, target.get(key)):
                return False
    elif source_type == builtins.list:
        source_length = len(source)
        target_length = len(target)
        if source_length != target_length:
            return False
        for item_number in range(source_length):
            if not is_equal(
                "{0}[{1}]".format(test_name, item_number),
                source[item_number],
                target[item_number],
            ):
                return False
    else:
        if source != target:
            logging.error("JSON key conflict: {0}".format(test_name))
            result = False
    return result


def remove_empty_elements(an_object):
    """Remove empty object from dictionary."""

    def empty(test_object):
        return test_object is None

    source_type = type(an_object)
    if source_type == builtins.dict:
        return {
            k: v
            for k, v in ((k, remove_empty_elements(v)) for k, v in an_object.items())
            if not empty(v)
        }
    if source_type == builtins.list:
        return [
            v for v in (remove_empty_elements(v) for v in an_object) if not empty(v)
        ]
    return an_object


# -----------------------------------------------------------------------------
# --- Main
# -----------------------------------------------------------------------------

# Set up logging.

logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO)

# Prolog.

logging.info("{0}".format("-" * 80))
logging.info("--- {0} - Begin".format(os.path.basename(__file__)))
logging.info("{0}".format("-" * 80))


# Load testcase metadata.

with open(INPUT_FILE, encoding="utf-8") as input_file:
    response_testcases = json.load(input_file)


# Process TEST_CASES.

for senzing_api_class, method_test_cases in response_testcases.items():

    metadata = method_test_cases.get("metadata", {})
    tests = method_test_cases.get("tests", {})
    pythonClass = metadata.get("pythonClass", senzing_api_class)

    # Test that class exists.

    if pythonClass not in globals():
        ERROR_COUNT += 1
        logging.error("Incorrect pythonClass: {0}".format(pythonClass))
        continue

    # Run though test cases.

    senzing_class = globals()[pythonClass]
    for testcase_name, testcase_dict in tests.items():
        TEST_COUNT += 1
        canonical_testcase_name = "{0}.{1}".format(pythonClass, testcase_name)

        # Test for similarity in key/values.

        logging.info("Testcase: {0}".format(canonical_testcase_name))
        json_struct = senzing_class.from_json_data(testcase_dict)
        reconstructed_json_string = json.dumps(json_struct.to_json_data())
        reconstructed_testcase_dict = json.loads(reconstructed_json_string)
        if not is_equal(
            canonical_testcase_name, testcase_dict, reconstructed_testcase_dict
        ):
            ERROR_COUNT += 1

        # Test for similarity in JSON string lengths.

        original_json_string_sorted = json.dumps(
            remove_empty_elements(testcase_dict), sort_keys=True
        )
        reconstructed_json_string_sorted = json.dumps(
            remove_empty_elements(json_struct.to_json_data()), sort_keys=True
        )
        len_original = len(original_json_string_sorted)
        len_reconstructed = len(reconstructed_json_string_sorted)
        if len_original != len_reconstructed:
            ERROR_COUNT += 1
            logging.error(
                "Lengths differ: Test: {0}; Original: {1}; Reconstructed: {2}".format(
                    canonical_testcase_name, len_original, len_reconstructed
                )
            )

        # Test for similarity in JSON strings.

        if original_json_string_sorted != reconstructed_json_string_sorted:
            for index in range(len_original):
                if (
                    original_json_string_sorted[index]
                    != reconstructed_json_string_sorted[index]
                ):
                    ERROR_COUNT += 1
                    logging.error(
                        "Strings differ: Test: {0}; First difference position: {1}".format(
                            canonical_testcase_name, index
                        )
                    )
                    logging.error(
                        ">>>>>>      Original: {0}".format(original_json_string_sorted)
                    )
                    logging.error(
                        ">>>>>> Reconstructed: {0}".format(
                            reconstructed_json_string_sorted
                        )
                    )
                    break

# Epilog.

logging.info("Tests: {0}; Errors: {1}".format(TEST_COUNT, ERROR_COUNT))
logging.info("{0}".format("-" * 80))
logging.info("--- {0} - End".format(os.path.basename(__file__)))
logging.info("{0}".format("-" * 80))
if ERROR_COUNT > 0:
    sys.exit(1)
