#! /usr/bin/env python3

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json
import os
import pathlib

from python.typedef import (
    FeatureForAttribute,
    G2configListDataSourcesResponse,
    G2engineAddRecordWithInfoResponse,
    G2engineDeleteRecordWithInfoResponse,
    G2engineGetVirtualEntityByRecordIDResponse,
)

# -----------------------------------------------------------------------------
# Utility functions
# -----------------------------------------------------------------------------


def path_to_testdata(filename: str) -> str:
    current_path = pathlib.Path(__file__).parent.resolve()
    result = os.path.abspath("{0}/testdata/{1}".format(current_path, filename))
    return result


# -----------------------------------------------------------------------------
# Mock functions - Simulate calls to Senzing SDK API.
# -----------------------------------------------------------------------------


def mock_g2engine_add_record_with_info() -> str:
    with open(
        path_to_testdata("G2EngineAddRecordWithInfoResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        return input_file.read()


def mock_g2engine_delete_record_with_info() -> str:
    with open(
        path_to_testdata("G2EngineDeleteRecordWithInfoResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        return input_file.read()


def mock_g2engine_get_virtual_entity_by_record_id() -> str:
    with open(
        path_to_testdata("G2EngineGetVirtualEntityByRecordIdResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        return input_file.read()


# -----------------------------------------------------------------------------
# Show transformation from "from_json_data()" to "to_json_data"
# -----------------------------------------------------------------------------

print(
    "\n---- Simple examples ----------------------------------------------------------\n"
)

# G2Engine add_record_with_info -----------------------------------------------

response = G2engineAddRecordWithInfoResponse.from_json_data(
    json.loads(mock_g2engine_add_record_with_info())
)
print(
    f"G2engineAddRecordWithInfoResponse: DataSource: {response.value.data_source}; RecordID: {response.value.record_id}; Affected entity: {response.value.affected_entities[0].entity_id}"
)

# G2Engine delete_record_with_info --------------------------------------------

response = G2engineDeleteRecordWithInfoResponse.from_json_data(
    json.loads(mock_g2engine_delete_record_with_info())
)
print(
    f"G2engineDeleteRecordWithInfoResponse: DataSource: {response.value.data_source}; RecordID: {response.value.record_id}; Affected entity: {response.value.affected_entities[0].entity_id}"
)

# G2Engine g2engine_get_virtual_entity_by_record_id ------------------------------------

response = G2engineGetVirtualEntityByRecordIDResponse.from_json_data(
    json.loads(mock_g2engine_get_virtual_entity_by_record_id())
)
feature_list = response.value.resolved_entity.features.get("NAME", [])
for feature in feature_list:
    feat_desc_list = FeatureForAttribute.from_json_data(feature).feat_desc_values
    for feat_desc in feat_desc_list:
        print(
            f"G2engineGetVirtualEntityByRecordIDResponse: Feature description: {feat_desc.feat_desc}"
        )

feature_desc = response.value.resolved_entity.features["ADDRESS"][0]

# Compare the use of Python objects above with the following straight JSON parsing.
# - Issue: No static checking can be done on JSON keys
# - Issue: No editor hints
response = json.loads(mock_g2engine_get_virtual_entity_by_record_id())
feature_list = response.get("RESOLVED_ENTITY", {}).get("FEATURES", {}).get("NAME", [])
for feature in feature_list:
    feat_desc_list = feature.get("FEAT_DESC_VALUES")
    for feat_desc in feat_desc_list:
        print(
            f"G2engineGetVirtualEntityByRecordIDResponse: Feature description: {feat_desc.get('FEAT_DESC')}"
        )

# -----------------------------------------------------------------------------
# Show transformation from "from_json_data()" to "to_json_data"
# -----------------------------------------------------------------------------

print(
    "\n---- Transformation example ---------------------------------------------------\n"
)

JSON_STRING = '{"DATA_SOURCES": [{"DSRC_ID": 1, "DSRC_CODE": "TEST"}, {"DSRC_ID": 2, "DSRC_CODE": "SEARCH"}]}'
JSON_STRUCT = G2configListDataSourcesResponse.from_json_data(json.loads(JSON_STRING))

for data_source in JSON_STRUCT.data_sources:
    print("ID: {0}  Code: {1}".format(data_source.dsrc_id, data_source.dsrc_code))

RECONSTRUCTED_STRING = json.dumps(JSON_STRUCT.to_json_data())
print("     Original JSON: {0}".format(JSON_STRING))
print(
    "Reconstructed JSON: {0} - notice JSON keys have been sorted.".format(
        RECONSTRUCTED_STRING
    )
)
