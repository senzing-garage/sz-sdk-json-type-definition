#! /usr/bin/env python3

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json
import os
import pathlib

from python.typedef import (
    G2configListDataSourcesResponse,
    G2engineAddRecordWithInfoResponse,
    G2engineDeleteRecordWithInfoResponse,
    G2engineGetEntityByEntityIDResponse,
    G2engineGetVirtualEntityByRecordIDResponse,
    G2engineFindNetworkByEntityIDResponse,
    G2configmgrGetConfigListResponse,
    G2productLicenseResponse,

 G2configAddDataSourceResponse,
         G2configListDataSourcesResponse,
         G2configmgrGetConfigListResponse,
         G2configmgrGetConfigResponse,
         G2configSaveResponse,
         G2diagnosticCheckDBPerfResponse,
         G2diagnosticStreamEntityListBySizeResponse,
         G2engineAddRecordWithInfoResponse,
         G2engineDeleteRecordWithInfoResponse,
         G2engineExportConfigAndConfigIdResponse,
         G2engineExportConfigResponse,
         G2engineFetchNextResponse,
         G2engineFindInterestingEntitiesByEntityIdResponse,
         G2engineFindInterestingEntitiesByRecordIdResponse,
         G2engineFindNetworkByEntityIdResponse,
         G2engineFindNetworkByEntityIDV2Response,
         G2engineFindNetworkByRecordIdResponse,
         G2engineFindNetworkByRecordIDV2Response,
         G2engineFindPathByEntityIdResponse,
         G2engineFindPathByEntityIDV2Response,
         G2engineFindPathByRecordIdResponse,
         G2engineFindPathByRecordIDV2Response,
         G2engineFindPathExcludingByEntityIdResponse,
         G2engineFindPathExcludingByEntityIDV2Response,
         G2engineFindPathExcludingByRecordIdResponse,
         G2engineFindPathExcludingByRecordIDV2Response,
         G2engineFindPathIncludingSourceByEntityIdResponse,
         G2engineFindPathIncludingSourceByEntityIDV2Response,
         G2engineFindPathIncludingSourceByRecordIdResponse,
         G2engineFindPathIncludingSourceByRecordIDV2Response,
         G2engineGetEntityByEntityIdResponse,
         G2engineGetEntityByEntityIDV2Response,
         G2engineGetEntityByRecordIdResponse,
         G2engineGetEntityByRecordIDV2Response,
         G2engineGetRecordResponse,
         G2engineGetRecordV2Response,
         G2engineGetRedoRecordResponse,
         G2engineGetVirtualEntityByRecordIdResponse,
         G2engineGetVirtualEntityByRecordIDV2Response,
         G2engineHowEntityByEntityIdResponse,
         G2engineHowEntityByEntityIDV2Response,
         G2engineProcessRedoRecordResponse,
         G2engineProcessRedoRecordWithInfoResponse,
         G2engineReevaluateEntityWithInfoResponse,
         G2engineReevaluateRecordWithInfoResponse,
         G2engineReplaceRecordWithInfoResponse,
         G2engineSearchByAttributesResponse,
         G2engineSearchByAttributesV2Response,
         G2engineSearchByAttributesV3Response,
         G2engineStreamExportJSONEntityReportResponse,
         G2engineWhyEntitiesResponse,
 G2engineWhyEntitiesV2Response,
         G2engineWhyRecordsResponse,
         G2engineWhyRecordsV2Response,
         G2productLicenseResponse,
         G2productVersionResponse,


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
print(
    f"G2engineGetVirtualEntityByRecordIDResponse: Simple  description: {response.value.resolved_entity.features['NAME'][0].feat_desc}"
)

feature_list = response.value.resolved_entity.features["NAME"]
for feature in feature_list:
    feat_desc_list = feature.feat_desc_values
    for feat_desc in feat_desc_list:
        print(
            f"G2engineGetVirtualEntityByRecordIDResponse: Feature description: {feat_desc.feat_desc}"
        )

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

for data_source in JSON_STRUCT.value.data_sources:
    print("ID: {0}  Code: {1}".format(data_source.dsrc_id, data_source.dsrc_code))

RECONSTRUCTED_STRING = json.dumps(JSON_STRUCT.to_json_data())
print("     Original JSON: {0}".format(JSON_STRING))
print(
    "Reconstructed JSON: {0} - notice JSON keys have been sorted.".format(
        RECONSTRUCTED_STRING
    )
)

# -----------------------------------------------------------------------------
# test area
# -----------------------------------------------------------------------------



response = G2configAddDataSourceResponse.from_json_data({})
response =         G2configListDataSourcesResponse.from_json_data({})
response =         G2configmgrGetConfigListResponse.from_json_data({})
response =         G2configmgrGetConfigResponse.from_json_data({})
response =         G2configSaveResponse.from_json_data({})
response =         G2diagnosticCheckDBPerfResponse.from_json_data({})
response =         G2diagnosticStreamEntityListBySizeResponse.from_json_data({})
response =         G2engineAddRecordWithInfoResponse.from_json_data({})
response =         G2engineDeleteRecordWithInfoResponse.from_json_data({})
response =         G2engineExportConfigAndConfigIdResponse.from_json_data({})
response =         G2engineExportConfigResponse.from_json_data({})
response =         G2engineFetchNextResponse.from_json_data({})
response =         G2engineFindInterestingEntitiesByEntityIdResponse.from_json_data({})
response =         G2engineFindInterestingEntitiesByRecordIdResponse.from_json_data({})
response =         G2engineFindNetworkByEntityIdResponse.from_json_data({})
response =         G2engineFindNetworkByEntityIDV2Response.from_json_data({})
response =         G2engineFindNetworkByRecordIdResponse.from_json_data({})
response =         G2engineFindNetworkByRecordIDV2Response.from_json_data({})
response =         G2engineFindPathByEntityIdResponse.from_json_data({})
response =         G2engineFindPathByEntityIDV2Response.from_json_data({})
response =         G2engineFindPathByRecordIdResponse.from_json_data({})
response =         G2engineFindPathByRecordIDV2Response.from_json_data({})
response =         G2engineFindPathExcludingByEntityIdResponse.from_json_data({})
response =         G2engineFindPathExcludingByEntityIDV2Response.from_json_data({})
response =         G2engineFindPathExcludingByRecordIdResponse.from_json_data({})
response =         G2engineFindPathExcludingByRecordIDV2Response.from_json_data({})
response =         G2engineFindPathIncludingSourceByEntityIdResponse.from_json_data({})
response =         G2engineFindPathIncludingSourceByEntityIDV2Response.from_json_data({})
response =         G2engineFindPathIncludingSourceByRecordIdResponse.from_json_data({})
response =         G2engineFindPathIncludingSourceByRecordIDV2Response.from_json_data({})
response =         G2engineGetEntityByEntityIdResponse.from_json_data({})
response =         G2engineGetEntityByEntityIDV2Response.from_json_data({})
response =         G2engineGetEntityByRecordIdResponse.from_json_data({})
response =         G2engineGetEntityByRecordIDV2Response.from_json_data({})
response =         G2engineGetRecordResponse.from_json_data({})
response =         G2engineGetRecordV2Response.from_json_data({})
response =         G2engineGetRedoRecordResponse.from_json_data({})
response =         G2engineGetVirtualEntityByRecordIdResponse.from_json_data({})
response =         G2engineGetVirtualEntityByRecordIDV2Response.from_json_data({})
response =         G2engineHowEntityByEntityIdResponse.from_json_data({})
response =         G2engineHowEntityByEntityIDV2Response.from_json_data({})
response =         G2engineProcessRedoRecordResponse.from_json_data({})
response =         G2engineProcessRedoRecordWithInfoResponse.from_json_data({})
response =         G2engineReevaluateEntityWithInfoResponse.from_json_data({})
response =         G2engineReevaluateRecordWithInfoResponse.from_json_data({})
response =         G2engineReplaceRecordWithInfoResponse.from_json_data({})
response =         G2engineSearchByAttributesResponse.from_json_data({})
response =         G2engineSearchByAttributesV2Response.from_json_data({})
response =         G2engineSearchByAttributesV3Response.from_json_data({})
response =         G2engineStreamExportJSONEntityReportResponse.from_json_data({})
response =         G2engineWhyEntitiesResponse.from_json_data({})
response = G2engineWhyEntitiesV2Response.from_json_data({})
response =         G2engineWhyRecordsResponse.from_json_data({})
response =         G2engineWhyRecordsV2Response.from_json_data({})
response =         G2productLicenseResponse.from_json_data({})
response =         G2productVersionResponse.from_json_data({})



response = G2engineGetEntityByEntityIDResponse.from_json_data({})
x = response.value.resolved_entity

response = G2engineFindNetworkByEntityIDResponse.from_json_data({})
x = response.value.entities[0].related_entities[0].record_summary[0]

response = G2configmgrGetConfigListResponse.from_json_data({})
x = response.value.configs[0].


response = G2productLicenseResponse.from_json_data({})
response.billing

