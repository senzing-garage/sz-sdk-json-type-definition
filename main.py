#! /usr/bin/env python3

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json
import os
import pathlib

from python.typedef import (  # G2configAddDataSourceResponse,; G2configListDataSourcesResponse,; G2configmgrGetConfigListResponse,; G2configmgrGetConfigResponse,; G2configSaveResponse,; G2diagnosticCheckDBPerfResponse,; G2diagnosticStreamEntityListBySizeResponse,; G2engineAddRecordWithInfoResponse,; G2engineDeleteRecordWithInfoResponse,; G2engineExportConfigAndConfigIdResponse,; G2engineExportConfigResponse,; G2engineFetchNextResponse,; G2engineFindInterestingEntitiesByEntityIdResponse,; G2engineFindInterestingEntitiesByRecordIdResponse,; G2engineFindNetworkByEntityIdResponse,; G2engineFindNetworkByEntityIDV2Response,; G2engineFindNetworkByRecordIdResponse,; G2engineFindNetworkByRecordIDV2Response,; G2engineFindPathByEntityIdResponse,; G2engineFindPathByEntityIDV2Response,; G2engineFindPathByRecordIdResponse,; G2engineFindPathByRecordIDV2Response,; G2engineFindPathExcludingByEntityIdResponse,; G2engineFindPathExcludingByEntityIDV2Response,; G2engineFindPathExcludingByRecordIdResponse,; G2engineFindPathExcludingByRecordIDV2Response,; G2engineFindPathIncludingSourceByEntityIdResponse,; G2engineFindPathIncludingSourceByEntityIDV2Response,; G2engineFindPathIncludingSourceByRecordIdResponse,; G2engineFindPathIncludingSourceByRecordIDV2Response,; G2engineGetEntityByEntityIdResponse,; G2engineGetEntityByEntityIDV2Response,; G2engineGetEntityByRecordIdResponse,; G2engineGetEntityByRecordIDV2Response,; G2engineGetRecordResponse,; G2engineGetRecordV2Response,; G2engineGetRedoRecordResponse,; G2engineGetVirtualEntityByRecordIdResponse,; G2engineGetVirtualEntityByRecordIDV2Response,; G2engineHowEntityByEntityIdResponse,; G2engineHowEntityByEntityIDV2Response,; G2engineProcessRedoRecordResponse,; G2engineProcessRedoRecordWithInfoResponse,; G2engineReevaluateEntityWithInfoResponse,; G2engineReevaluateRecordWithInfoResponse,; G2engineReplaceRecordWithInfoResponse,; G2engineSearchByAttributesResponse,; G2engineSearchByAttributesV2Response,; G2engineSearchByAttributesV3Response,; G2engineStreamExportJSONEntityReportResponse,; G2engineWhyEntitiesResponse,; G2engineWhyEntitiesV2Response,; G2engineWhyRecordsResponse,; G2engineWhyRecordsV2Response,; G2productLicenseResponse,; G2productVersionResponse,
    G2configAddDataSourceResponse,
    G2configListDataSourcesResponse,
    G2configmgrGetConfigListResponse,
    G2configmgrGetConfigResponse,
    G2configSaveResponse,
    G2diagnosticCheckDbperfResponse,
    G2diagnosticStreamEntityListBySizeResponse,
    G2engineAddRecordWithInfoResponse,
    G2engineDeleteRecordWithInfoResponse,
    G2engineExportConfigAndConfigIDResponse,
    G2engineExportConfigResponse,
    G2engineFetchNextResponse,
    G2engineFindInterestingEntitiesByEntityIDResponse,
    G2engineFindInterestingEntitiesByRecordIDResponse,
    G2engineFindNetworkByEntityIDResponse,
    G2engineFindNetworkByEntityIdv2response,
    G2engineFindNetworkByRecordIDResponse,
    G2engineFindNetworkByRecordIdv2response,
    G2engineFindPathByEntityIDResponse,
    G2engineFindPathByEntityIdv2response,
    G2engineFindPathByRecordIDResponse,
    G2engineFindPathByRecordIdv2response,
    G2engineFindPathExcludingByEntityIDResponse,
    G2engineFindPathExcludingByEntityIdv2response,
    G2engineFindPathExcludingByRecordIDResponse,
    G2engineFindPathExcludingByRecordIdv2response,
    G2engineFindPathIncludingSourceByEntityIDResponse,
    G2engineFindPathIncludingSourceByEntityIdv2response,
    G2engineFindPathIncludingSourceByRecordIDResponse,
    G2engineFindPathIncludingSourceByRecordIdv2response,
    G2engineGetEntityByEntityIDResponse,
    G2engineGetEntityByEntityIdv2response,
    G2engineGetEntityByRecordIDResponse,
    G2engineGetEntityByRecordIdv2response,
    G2engineGetRecordResponse,
    G2engineGetRecordV2response,
    G2engineGetRedoRecordResponse,
    G2engineGetVirtualEntityByRecordIDResponse,
    G2engineGetVirtualEntityByRecordIdv2response,
    G2engineHowEntityByEntityIDResponse,
    G2engineHowEntityByEntityIdv2response,
    G2engineProcessRedoRecordResponse,
    G2engineProcessRedoRecordWithInfoResponse,
    G2engineReevaluateEntityWithInfoResponse,
    G2engineReevaluateRecordWithInfoResponse,
    G2engineReplaceRecordWithInfoResponse,
    G2engineSearchByAttributesResponse,
    G2engineSearchByAttributesV2response,
    G2engineSearchByAttributesV3response,
    G2engineStreamExportJsonentityReportResponse,
    G2engineWhyEntitiesResponse,
    G2engineWhyEntitiesV2response,
    G2engineWhyRecordsResponse,
    G2engineWhyRecordsV2response,
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


def file(filename: str) -> dict:
    print(filename)
    absolute_file = path_to_testdata(filename)
    with open(
        absolute_file,
        encoding="utf-8",
    ) as input_file:
        return json.loads(input_file.read())


def print_fmt(response, value):
    print(f"    {value} = {eval(value)}")


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


response = G2configAddDataSourceResponse.from_json_data(
    file("G2ConfigAddDataSourceResponse-test-101.json")
)
print_fmt(response, "response.value.dsrc_id")


response = G2configListDataSourcesResponse.from_json_data(
    file("G2ConfigListDataSourcesResponse-test-105.json")
)
print_fmt(response, "response.value.data_sources[0].dsrc_id")


response = G2configmgrGetConfigListResponse.from_json_data(
    file("G2ConfigmgrGetConfigListResponse-test-101.json")
)
print_fmt(response, "response.value.configs[0].config_id")


response = G2configmgrGetConfigResponse.from_json_data(
    file("G2ConfigmgrGetConfigResponse-test-101.json")
)
print_fmt(response, "response.value.g2_config.cfg_attr[0].attr_id")


response = G2configSaveResponse.from_json_data(
    file("G2ConfigSaveResponse-test-101.json")
)
print_fmt(response, "response.value.g2_config.cfg_dfbom[0].dfcall_id")


response = G2diagnosticCheckDbperfResponse.from_json_data(
    file("G2DiagnosticCheckDBPerfResponse-test-101.json")
)
print_fmt(response, "response.value.num_records_inserted")


response = G2diagnosticStreamEntityListBySizeResponse.from_json_data({})
x = response.value  # TODO:


response = G2engineAddRecordWithInfoResponse.from_json_data(
    file("G2EngineAddRecordWithInfoResponse-test-102.json")
)
print_fmt(response, "response.value.affected_entities[0].entity_id")


response = G2engineDeleteRecordWithInfoResponse.from_json_data(
    file("G2EngineDeleteRecordWithInfoResponse-test-001.json")
)
print_fmt(response, "response.value.affected_entities[0].entity_id")


response = G2engineExportConfigAndConfigIDResponse.from_json_data(
    file("G2EngineExportConfigAndConfigIdResponse-test-101.json")
)
print_fmt(response, "response.value.g2_config.cfg_attr[0].attr_id")


response = G2engineExportConfigResponse.from_json_data(
    file("G2EngineExportConfigResponse-test-101.json")
)
print_fmt(response, "response.value.g2_config.cfg_cfbom[0].felem_id")


response = G2engineFetchNextResponse.from_json_data({})
x = response.value.value  # TODO:


response = G2engineFindInterestingEntitiesByEntityIDResponse.from_json_data(
    file("G2EngineFindInterestingEntitiesByEntityIdResponse-test-108.json")
)
print_fmt(
    response,
    "response.value.interesting_entities.entities[0].entity_id",
)


response = G2engineFindInterestingEntitiesByRecordIDResponse.from_json_data(
    file("G2EngineFindInterestingEntitiesByRecordIdResponse-test-108.json")
)
print_fmt(
    response,
    "response.value.interesting_entities.entities[0].entity_id",
)


response = G2engineFindNetworkByEntityIDResponse.from_json_data(
    file("G2EngineFindNetworkByEntityIdResponse-test-106.json")
)
print_fmt(
    response,
    "response.value.entities[0].related_entities[0].entity_id",
)


response = G2engineFindNetworkByEntityIdv2response.from_json_data(
    file("G2EngineFindNetworkByEntityIDV2Response-test-106.json")
)
print_fmt(
    response,
    "response.value.entities[0].related_entities[0].entity_id",
)


response = G2engineFindNetworkByRecordIDResponse.from_json_data(
    file("G2EngineFindNetworkByRecordIdResponse-test-102.json")
)
print_fmt(
    response,
    "response.value.entities[0].related_entities[0].entity_id",
)


response = G2engineFindNetworkByRecordIdv2response.from_json_data(
    file("G2EngineFindNetworkByRecordIDV2Response-test-102.json")
)
print_fmt(
    response,
    "response.value.entities[0].related_entities[0].entity_id",
)


response = G2engineFindPathByEntityIDResponse.from_json_data(
    file("G2EngineFindPathByEntityIdResponse-test-105.json")
)
print_fmt(
    response,
    "response.value.entities[0].resolved_entity.entity_id",
)


response = G2engineFindPathByEntityIdv2response.from_json_data(
    file("G2EngineFindPathByEntityIDV2Response-test-104.json")
)
print_fmt(
    response,
    "response.value.entities[0].resolved_entity.entity_id",
)


response = G2engineFindPathByRecordIDResponse.from_json_data(
    file("G2EngineFindPathByRecordIdResponse-test-102.json")
)
print_fmt(
    response,
    "response.value.entities[0].resolved_entity.entity_id",
)


response = G2engineFindPathByRecordIdv2response.from_json_data(
    file("G2EngineFindPathByRecordIDV2Response-test-102.json")
)
print_fmt(
    response,
    "response.value.entities[0].related_entities[0].entity_id",
)


response = G2engineFindPathExcludingByEntityIDResponse.from_json_data(
    file("G2EngineFindPathExcludingByEntityIdResponse-test-102.json")
)
print_fmt(
    response,
    "response.value.entities[0].resolved_entity.record_summary[0].record_count",
)


response = G2engineFindPathExcludingByEntityIdv2response.from_json_data({})
response = G2engineFindPathExcludingByRecordIDResponse.from_json_data({})
response = G2engineFindPathExcludingByRecordIdv2response.from_json_data({})
response = G2engineFindPathIncludingSourceByEntityIDResponse.from_json_data({})
response = G2engineFindPathIncludingSourceByEntityIdv2response.from_json_data({})
response = G2engineFindPathIncludingSourceByRecordIDResponse.from_json_data({})
response = G2engineFindPathIncludingSourceByRecordIdv2response.from_json_data({})
response = G2engineGetEntityByEntityIDResponse.from_json_data({})
response = G2engineGetEntityByEntityIdv2response.from_json_data({})
response = G2engineGetEntityByRecordIDResponse.from_json_data({})
response = G2engineGetEntityByRecordIdv2response.from_json_data({})
response = G2engineGetRecordResponse.from_json_data({})
response = G2engineGetRecordV2response.from_json_data({})
response = G2engineGetRedoRecordResponse.from_json_data({})
response = G2engineGetVirtualEntityByRecordIDResponse.from_json_data({})
response = G2engineGetVirtualEntityByRecordIdv2response.from_json_data({})
response = G2engineHowEntityByEntityIDResponse.from_json_data({})
response = G2engineHowEntityByEntityIdv2response.from_json_data({})
response = G2engineProcessRedoRecordResponse.from_json_data({})
response = G2engineProcessRedoRecordWithInfoResponse.from_json_data({})
response = G2engineReevaluateEntityWithInfoResponse.from_json_data({})
response = G2engineReevaluateRecordWithInfoResponse.from_json_data({})
response = G2engineReplaceRecordWithInfoResponse.from_json_data({})
response = G2engineSearchByAttributesResponse.from_json_data({})
response = G2engineSearchByAttributesV2response.from_json_data({})
response = G2engineSearchByAttributesV3response.from_json_data({})
response = G2engineStreamExportJsonentityReportResponse.from_json_data({})
response = G2engineWhyEntitiesResponse.from_json_data({})
response = G2engineWhyEntitiesV2response.from_json_data({})
response = G2engineWhyRecordsResponse.from_json_data({})
response = G2engineWhyRecordsV2response.from_json_data({})
response = G2productLicenseResponse.from_json_data({})
response = G2productVersionResponse.from_json_data({})


# response = G2engineGetEntityByEntityIDResponse.from_json_data({})
# x = response.value.resolved_entity

# response = G2engineFindNetworkByEntityIDResponse.from_json_data({})
# x = response.value.entities[0].related_entities[0].record_summary[0]

# response = G2configmgrGetConfigListResponse.from_json_data({})
# x = response.value.configs[0].


# response = G2productLicenseResponse.from_json_data({})
# response.

# response = G2engineGetEntityByEntityIDResponse.from_json_data({})
# x = response.value.resolved_entity.entity_id
