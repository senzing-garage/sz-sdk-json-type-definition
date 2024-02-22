#! /usr/bin/env python3

# pylint: disable=duplicate-code

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json
import os
import pathlib

from python.typedef import (
    G2engineAddRecordWithInfoResponse,
    G2engineDeleteRecordWithInfoResponse,
    G2engineFindInterestingEntitiesByEntityIDResponse,
    G2engineFindInterestingEntitiesByRecordIDResponse,
    G2engineFindNetworkByEntityIDResponse,
    G2engineFindNetworkByRecordIDResponse,
    G2engineFindPathByEntityIDResponse,
    G2engineFindPathByRecordIDResponse,
    G2engineGetEntityByEntityIDResponse,
    G2engineGetEntityByRecordIDResponse,
    G2engineGetRecordResponse,
    G2engineGetRedoRecordResponse,
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
# Tests
# -----------------------------------------------------------------------------


def test_g2engine_add_record_with_info_01():
    with open(
        path_to_testdata("G2EngineAddRecordWithInfoResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineAddRecordWithInfoResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.data_source == "TEST"
    assert response.value.record_id == "WITH_INFO_1"
    assert response.value.affected_entities[0].entity_id == 7


def test_g2engine_delete_record_with_info_01():
    with open(
        path_to_testdata("G2EngineDeleteRecordWithInfoResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineDeleteRecordWithInfoResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.data_source == "TEST"
    assert response.value.record_id == "DELETE_TEST"
    assert response.value.affected_entities[0].entity_id == 100002


def test_g2engine_find_interesting_entities_by_entity_id_01():
    with open(
        path_to_testdata(
            "G2EngineFindInterestingEntitiesByEntityIdResponse-test-101.json"
        ),
        encoding="utf-8",
    ) as input_file:
        response = G2engineFindInterestingEntitiesByEntityIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.interesting_entities.entities == []


def test_g2engine_find_interesting_entities_by_record_id_01():
    with open(
        path_to_testdata(
            "G2EngineFindInterestingEntitiesByRecordIdResponse-test-101.json"
        ),
        encoding="utf-8",
    ) as input_file:
        response = G2engineFindInterestingEntitiesByRecordIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.interesting_entities.entities == []


def test_g2engine_find_network_by_entity_id_01():
    with open(
        path_to_testdata("G2EngineFindNetworkByEntityIdResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineFindNetworkByEntityIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.entity_paths == []
    assert response.value.entities[0].resolved_entity.entity_id == 1
    assert response.value.entities[0].resolved_entity.entity_name == "Robert Smith"
    assert (
        response.value.entities[0].resolved_entity.record_summary[0].data_source
        == "CUSTOMERS"
    )


def test_g2engine_find_network_by_record_id_01():
    with open(
        path_to_testdata("G2EngineFindNetworkByRecordIdResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineFindNetworkByRecordIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.entity_paths == []
    assert response.value.entities[0].resolved_entity.entity_id == 1
    assert response.value.entities[0].resolved_entity.entity_name == "Robert Smith"
    assert (
        response.value.entities[0].resolved_entity.record_summary[0].data_source
        == "CUSTOMERS"
    )


def test_g2engine_find_path_by_entity_id_01():
    with open(
        path_to_testdata("G2EngineFindPathByEntityIdResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineFindPathByEntityIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.entity_paths[0].start_entity_id == 1
    assert response.value.entities[0].related_entities == []
    assert response.value.entities[0].resolved_entity.entity_id == 1
    assert response.value.entities[0].resolved_entity.entity_name == "Robert Smith"
    assert (
        response.value.entities[0].resolved_entity.record_summary[0].record_count == 3
    )


def test_g2engine_find_path_by_record_id_01():
    with open(
        path_to_testdata("G2EngineFindPathByRecordIdResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineFindPathByRecordIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.entity_paths[0].start_entity_id == 1
    assert response.value.entities[0].related_entities == []
    assert response.value.entities[0].resolved_entity.entity_id == 1
    assert response.value.entities[0].resolved_entity.entity_name == "Robert Smith"
    assert (
        response.value.entities[0].resolved_entity.record_summary[0].record_count == 3
    )


# def test_g2engine_get_entity_by_entity_id_01():
#     with open(
#         path_to_testdata("G2EngineGetEntityByEntityIdResponse-test-001.json"),
#         encoding="utf-8",
#     ) as input_file:
#         response = G2engineGetEntityByEntityIDResponse.from_json_data(
#             json.load(input_file)
#         )
#     assert response.value.related_entities == []
#     assert response.value.resolved_entity.entity_id == 1
#     assert response.value.resolved_entity.entity_name == "Robert Smith"
#     feature_json = response.value.resolved_entity.features["ADDRESS"][0].feat_desc
#     feature = FeatureForAttribute.from_json_data(feature_json)
#     assert feature.feat_desc == "1515 Adela Lane Las Vegas NV 89111"
#     assert feature.feat_desc_values[0].lib_feat_id == 20


def test_g2engine_get_entity_by_entity_id_01():
    with open(
        path_to_testdata("G2EngineGetEntityByEntityIdResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineGetEntityByEntityIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.related_entities == []
    assert response.value.resolved_entity.entity_id == 1
    assert response.value.resolved_entity.entity_name == "Robert Smith"
    assert (
        response.value.resolved_entity.features["ADDRESS"][0].feat_desc
        == "1515 Adela Lane Las Vegas NV 89111"
    )
    assert response.value.resolved_entity.features["ADDRESS"][0].lib_feat_id == 20


def test_g2engine_get_entity_by_entity_id_02():
    with open(
        path_to_testdata("G2EngineGetEntityByEntityIdResponse-test-002.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineGetEntityByEntityIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.related_entities == []
    assert response.value.resolved_entity.entity_id == 1
    assert response.value.resolved_entity.entity_name == "blank"
    assert response.value.resolved_entity.features["ADDRESS"][0].feat_desc == "blank"
    assert (
        response.value.resolved_entity.features["ADDRESS"][0]
        .feat_desc_values[0]
        .lib_feat_id
        == 1
    )


def test_g2engine_get_entity_by_record_id_01():
    with open(
        path_to_testdata("G2EngineGetEntityByRecordIdResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineGetEntityByRecordIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.related_entities == []
    assert response.value.resolved_entity.entity_id == 1
    assert response.value.resolved_entity.entity_name == "Robert Smith"
    assert (
        response.value.resolved_entity.features["ADDRESS"][0].feat_desc
        == "1515 Adela Lane Las Vegas NV 89111"
    )
    assert (
        response.value.resolved_entity.features["ADDRESS"][0]
        .feat_desc_values[0]
        .lib_feat_id
        == 20
    )


def test_g2engine_get_record_01():
    with open(
        path_to_testdata("G2EngineGetRecordResponse-test-001.json"), encoding="utf-8"
    ) as input_file:
        response = G2engineGetRecordResponse.from_json_data(json.load(input_file))
    assert response.value.data_source == "CUSTOMERS"
    assert response.value.record_id == "1001"
    assert isinstance(response.value.json_data, dict)
    assert response.value.json_data["DATA_SOURCE"] == "CUSTOMERS"
    assert response.value.json_data["RECORD_ID"] == "1001"


# TODO: Fix this
def test_g2engine_get_redo_record_01():
    with open(
        path_to_testdata("G2EngineGetRedoRecordResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineGetRedoRecordResponse.from_json_data(json.load(input_file))
    assert response.value.value == {}


def test_g2engine_get_virtual_entity_by_record_id_01():
    with open(
        path_to_testdata("G2EngineGetVirtualEntityByRecordIdResponse-test-001.json"),
        encoding="utf-8",
    ) as input_file:
        response = G2engineGetVirtualEntityByRecordIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.resolved_entity.entity_id == 1
    assert response.value.resolved_entity.entity_name == "Robert Smith"
    assert (
        response.value.resolved_entity.features["NAME"][0].feat_desc == "Robert Smith"
    )
    assert response.value.resolved_entity.features["NAME"][0].lib_feat_id == 1
    assert (
        response.value.resolved_entity.features["NAME"][0]
        .feat_desc_values[1]
        .lib_feat_id
        == 18
    )


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    test_g2engine_add_record_with_info_01()
