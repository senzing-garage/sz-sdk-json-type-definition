#! /usr/bin/env python3

"""
Used to generate go/typedef_test.go
"""

import logging
import json
import os
import re
from test_cases import TEST_CASES

IS_DEBUG = False
FINAL_RESULT = {}

OUTPUT_FILE = "./go/typedef/typedef_test.go"


# -----------------------------------------------------------------------------
# --- Helpers
# -----------------------------------------------------------------------------

def canonical_json(json_string):
    """Create compact JSON.  No spaces."""
    json_object = json.loads(json_string)
    result = json.dumps(json_object, sort_keys=True, separators=(',', ':'))
    return result


# -----------------------------------------------------------------------------
# --- Main
# -----------------------------------------------------------------------------

# Set up logging.

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

logging.info("{0}".format("-" * 80))
logging.info("--- {0} - Begin".format(os.path.basename(__file__)))
logging.info("{0}".format("-" * 80))

# Create multi-line strings for output.

OUTPUT_HEADER = """// Code generated by generate-go-typedef_test.py. DO NOT EDIT.

package typedef

import (
    "context"
    "testing"
	"encoding/json"
	"github.com/stretchr/testify/assert"
)

func testError(test *testing.T, ctx context.Context, err error) {
	if err != nil {
		test.Log("Error:", err.Error())
		assert.FailNow(test, err.Error())
	}
}

// ----------------------------------------------------------------------------
// --- Test cases
// ----------------------------------------------------------------------------

"""

TEST_FUNCTION_TEMPLATE = f"""
    ctx := context.TODO()
	jsonString := `{{json}}`
	jsonStruct := {{struct}}{{parens}}
	err := json.Unmarshal([]byte(jsonString), &jsonStruct)
	testError(test, ctx, err)
	_, err = json.Marshal(jsonStruct)
	testError(test, ctx, err)
    // assert.Equal(test, jsonString, string(reconstructedString))
    // assert.JSONEq(test, jsonString, string(reconstructedString))
"""

OUTPUT_FOOTER = """
"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write(OUTPUT_HEADER)
    for senzing_api_class, method_test_cases in TEST_CASES.items():
        for test_case_name, test_case_json in method_test_cases.items():
            better_test_case_name = re.sub('[^0-9a-zA-Z]+', '', test_case_name).capitalize()
            canonical_test_case_json = canonical_json(test_case_json)
            file.write("func Test{0}{1}(test *testing.T) {{".format(senzing_api_class, better_test_case_name))
            file.write(TEST_FUNCTION_TEMPLATE.format(json=canonical_test_case_json, struct=senzing_api_class, parens="{}"))
            file.write("}\n\n")
    file.write(OUTPUT_FOOTER)

# Epilog.

logging.info("{0}".format("-" * 80))
logging.info("--- {0} - End".format(os.path.basename(__file__)))
logging.info("{0}".format("-" * 80))
