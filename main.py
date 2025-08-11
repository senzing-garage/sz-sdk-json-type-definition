#! /usr/bin/env python3

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json
import os
import pathlib

from python.typedef import (
    DataSource,
    List,
    SzConfigExportResponse,
    SzConfigGetDataSourceRegistryResponse,
    SzConfigManagerGetConfigRegistryResponse,
    SzConfigRegisterDataSourceResponse,
    SzDiagnosticCheckRepositoryPerformanceResponse,
    SzDiagnosticGetFeatureResponse,
    SzDiagnosticGetRepositoryInfoResponse,
    SzEngineAddRecordResponse,
    SzEngineDeleteRecordResponse,
    SzEngineFetchNextResponse,
    SzEngineFindInterestingEntitiesByEntityIDResponse,
    SzEngineFindInterestingEntitiesByRecordIDResponse,
    SzEngineFindNetworkByEntityIDResponse,
    SzEngineFindNetworkByRecordIDRecordKeys,
    SzEngineFindNetworkByRecordIDResponse,
    SzEngineFindPathByEntityIDResponse,
    SzEngineFindPathByRecordIDResponse,
    SzEngineGetEntityByEntityIDResponse,
    SzEngineGetEntityByRecordIDResponse,
    SzEngineGetRecordResponse,
    SzEngineGetRedoRecordResponse,
    SzEngineGetVirtualEntityByRecordIDRecordKeys,
    SzEngineGetVirtualEntityByRecordIDResponse,
    SzEngineHowEntityByEntityIDResponse,
    SzEngineProcessRedoRecordResponse,
    SzEngineReevaluateEntityResponse,
    SzEngineReevaluateRecordResponse,
    SzEngineSearchByAttributesResponse,
    SzEngineWhyEntitiesResponse,
    SzEngineWhyRecordInEntityResponse,
    SzEngineWhyRecordsResponse,
    SzProductGetLicenseResponse,
    SzProductGetVersionResponse,
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


def print_fmt(
    response, value
):  # pylint: disable=redefined-outer-name eval-used, unused-argument
    """
    Tricky code:
    The "response" passed in needs to be part of the "value" string to be evaluated.
    """
    print(f"    {value} = {eval(value)}")  # pylint: disable=eval-used


# -----------------------------------------------------------------------------
# Mock functions - Simulate calls to Senzing SDK API.
# -----------------------------------------------------------------------------


def mock_szengine_add_record_with_info() -> str:
    with open(
        path_to_testdata("SzEngineAddRecordResponse-test-002.json"),
        encoding="utf-8",
    ) as input_file:
        return input_file.read()


def mock_szengine_delete_record_with_info() -> str:
    with open(
        path_to_testdata("SzEngineDeleteRecordResponse-test-002.json"),
        encoding="utf-8",
    ) as input_file:
        return input_file.read()


    def get_virtual_entity_by_record_id(
        self,
        record_keys: List[Tuple[str, str]],
        flags: int = SzEngineFlags.SZ_VIRTUAL_ENTITY_DEFAULT_FLAGS,
    ) -> str:

def mock_szengine_get_virtual_entity_by_record_id(
            record_keys: List[Tuple[str, str]],
        flags: int ,

    ) -> str:
    with open(
        path_to_testdata("SzEngineGetVirtualEntityByRecordIdResponse-test-002.json"),
        encoding="utf-8",
    ) as input_file:
        return input_file.read()


# -----------------------------------------------------------------------------
# Demonstrate creating input parameter and parsing output result.
# -----------------------------------------------------------------------------

print(
    "--- Demonstrate creating input parameter and parsing output result ------------\n\n"
)

yyy = {
    "RECORDS": [
        {"DATA_SOURCE": "DATA_SOURCE_1", "RECORD_ID": "RECORD_ID_1"},
        {"DATA_SOURCE": "DATA_SOURCE_2", "RECORD_ID": "RECORD_ID_2"},
    ]
}


xxx = SzEngineGetVirtualEntityByRecordIDRecordKeys.from_json_data(yyy)

xxx.value.records[0].data_source = "DATA_SOURCE_x"
xxx.value.records[0].record_id = "RECORD_ID_x"

print(xxx.to_json_data())


# -----------------------------------------------------------------------------
# Show transformation from "from_json_data()" to "to_json_data"
# -----------------------------------------------------------------------------

bob = SzEngineFindNetworkByRecordIDRecordKeys.from_json_data({})
ds = DataSource
ds.dsrc_code = "Bob_DS"
ds.dsrc_id = 1
records = List[ds]

bob.records = List[ds]


print(
    "\n---- Simple examples ----------------------------------------------------------\n"
)

# SzEngine add_record_with_info -----------------------------------------------

response = SzEngineAddRecordResponse.from_json_data(
    json.loads(mock_szengine_add_record_with_info())
)
print(
    f"SzEngineAddRecordResponse: DataSource: {response.value.data_source}; RecordID: {response.value.record_id}; Affected entity: {response.value.affected_entities[0].entity_id}"
)

# SzEngine delete_record_with_info --------------------------------------------

response = SzEngineDeleteRecordResponse.from_json_data(
    json.loads(mock_szengine_delete_record_with_info())
)
print(
    f"SzEngineDeleteRecordResponse: DataSource: {response.value.data_source}; RecordID: {response.value.record_id}; Affected entity: {response.value.affected_entities[0].entity_id}"
)

# SzEngine szengine_get_virtual_entity_by_record_id ------------------------------------

response = SzEngineGetVirtualEntityByRecordIDResponse.from_json_data(
    json.loads(mock_szengine_get_virtual_entity_by_record_id())
)
print(
    f"SzEngineGetVirtualEntityByRecordIDResponse: Simple  description: {response.value.resolved_entity.features['NAME'][0].feat_desc}"
)

feature_list = response.value.resolved_entity.features["NAME"]
for feature in feature_list:
    feat_desc_list = feature.feat_desc_values
    for feat_desc in feat_desc_list:
        print(
            f"SzEngineGetVirtualEntityByRecordIDResponse: Feature description: {feat_desc.feat_desc}"
        )

# Compare the use of Python objects above with the following straight JSON parsing.
# - Issue: No static checking can be done on JSON keys
# - Issue: No editor hints
response = json.loads(mock_szengine_get_virtual_entity_by_record_id())
feature_list = response.get("RESOLVED_ENTITY", {}).get("FEATURES", {}).get("NAME", [])
for feature in feature_list:
    feat_desc_list = feature.get("FEAT_DESC_VALUES")
    for feat_desc in feat_desc_list:
        print(
            f"SzEngineGetVirtualEntityByRecordIDResponse: Feature description: {feat_desc.get('FEAT_DESC')}"
        )

# -----------------------------------------------------------------------------
# Show transformation from "from_json_data()" to "to_json_data"
# -----------------------------------------------------------------------------

print(
    "\n---- Transformation example ---------------------------------------------------\n"
)

JSON_STRING = '{"DATA_SOURCES": [{"DSRC_ID": 1, "DSRC_CODE": "TEST"}, {"DSRC_ID": 2, "DSRC_CODE": "SEARCH"}]}'
JSON_STRUCT = SzConfigGetDataSourceRegistryResponse.from_json_data(
    json.loads(JSON_STRING)
)

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


response = SzConfigRegisterDataSourceResponse.from_json_data(
    file("SzConfigRegisterDataSourceResponse-test-001.json")
)
print_fmt(response, "response.value.dsrc_id")


response = SzConfigExportResponse.from_json_data(
    file("SzConfigExportResponse-test-001.json")
)
print_fmt(response, "response.value.g2_config.cfg_dfbom[0].dfcall_id")


response = SzConfigGetDataSourceRegistryResponse.from_json_data(
    file("SzConfigGetDataSourceRegistryResponse-test-001.json")
)
print_fmt(response, "response.value.data_sources[0].dsrc_id")


response = SzConfigManagerGetConfigRegistryResponse.from_json_data(
    file("SzConfigManagerGetConfigRegistryResponse-test-001.json")
)
print_fmt(response, "response.value.configs[0].config_id")


response = SzDiagnosticCheckRepositoryPerformanceResponse.from_json_data(
    file("SzDiagnosticCheckRepositoryPerformanceResponse-test-001.json")
)
print_fmt(response, "response.value.num_records_inserted")


response = SzDiagnosticGetRepositoryInfoResponse.from_json_data(
    file("SzDiagnosticGetRepositoryInfoResponse-test-001.json")
)
print_fmt(response, "response.value.data_stores[0].location")


response = SzDiagnosticGetFeatureResponse.from_json_data(
    file("SzDiagnosticGetFeatureResponse-test-001.json")
)
print_fmt(response, "response.value.lib_feat_id")


response = SzEngineAddRecordResponse.from_json_data(
    file("SzEngineAddRecordResponse-test-002.json")
)
print_fmt(response, "response.value.affected_entities[0].entity_id")


response = SzEngineDeleteRecordResponse.from_json_data(
    file("SzEngineDeleteRecordResponse-test-002.json")
)
print_fmt(response, "response.value.affected_entities[0].entity_id")


response = SzEngineFetchNextResponse.from_json_data({})
x = response.value.value  # TODO:


response = SzEngineFindInterestingEntitiesByEntityIDResponse.from_json_data(
    file("SzEngineFindInterestingEntitiesByEntityIdResponse-test-001.json")
)
print_fmt(
    response,
    "response.value.interesting_entities",
)

response = SzEngineFindInterestingEntitiesByRecordIDResponse.from_json_data(
    file("SzEngineFindInterestingEntitiesByRecordIdResponse-test-001.json")
)
print_fmt(
    response,
    "response.value.interesting_entities",
)

response = SzEngineFindNetworkByEntityIDResponse.from_json_data(
    file("SzEngineFindNetworkByEntityIdResponse-test-003.json")
)
print_fmt(
    response,
    "response.value.entities[0].related_entities[0].entity_id",
)


response = SzEngineFindNetworkByRecordIDResponse.from_json_data(
    file("SzEngineFindNetworkByRecordIdResponse-test-003.json")
)
print_fmt(
    response,
    "response.value.entities[0].related_entities[0].entity_id",
)


response = SzEngineFindPathByEntityIDResponse.from_json_data(
    file("SzEngineFindPathByEntityIdResponse-test-001.json")
)
print_fmt(
    response,
    "response.value.entities[0].resolved_entity.entity_id",
)


response = SzEngineFindPathByRecordIDResponse.from_json_data(
    file("SzEngineFindPathByRecordIdResponse-test-001.json")
)
print_fmt(
    response,
    "response.value.entities[0].resolved_entity.entity_id",
)


response = SzEngineGetEntityByEntityIDResponse.from_json_data({})
response = SzEngineGetEntityByRecordIDResponse.from_json_data({})
response = SzEngineGetRecordResponse.from_json_data({})
response = SzEngineGetRedoRecordResponse.from_json_data({})
response = SzEngineGetVirtualEntityByRecordIDResponse.from_json_data({})
response = SzEngineHowEntityByEntityIDResponse.from_json_data({})
response = SzEngineProcessRedoRecordResponse.from_json_data({})
response = SzEngineReevaluateEntityResponse.from_json_data({})
response = SzEngineReevaluateRecordResponse.from_json_data({})
response = SzEngineSearchByAttributesResponse.from_json_data({})
response = SzEngineStreamExportJSONEntityReportResponse.from_json_data({})
response = SzEngineWhyEntitiesResponse.from_json_data({})
response = SzEngineWhyRecordInEntityResponse.from_json_data({})
response = SzEngineWhyRecordsResponse.from_json_data({})
response = SzProductGetLicenseResponse.from_json_data({})
response = SzProductGetVersionResponse.from_json_data({})


# response = SzEngineGetEntityByEntityIDResponse.from_json_data({})
# x = response.value.resolved_entity

# response = SzEngineFindNetworkByEntityIDResponse.from_json_data({})
# x = response.value.entities[0].related_entities[0].record_summary[0]

# response = SzConfigManagerGetConfigRegistryResponse.from_json_data({})
# x = response.value.configs[0].


# response = SzProductLicenseResponse.from_json_data({})
# response.

# response = SzEngineGetEntityByEntityIDResponse.from_json_data({})
# x = response.value.resolved_entity.entity_id
