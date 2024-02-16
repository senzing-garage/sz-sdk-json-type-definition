#! /usr/bin/env python3

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json
import os
import pathlib

from python.typedef import (
    FeatureForAttribute,
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


def absolute_path(filename: str) -> str:
    current_path = pathlib.Path(__file__).parent.resolve()
    result = os.path.abspath("{0}/testdata/{1}".format(current_path, filename))
    return result


# -----------------------------------------------------------------------------
# Tests
# -----------------------------------------------------------------------------


def test_g2engine_add_record_with_info_01():
    with open(absolute_path("g2engine_addRecordWithInfo-01.json")) as input_file:
        response = G2engineAddRecordWithInfoResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.data_source == "TEST"
    assert response.value.record_id == "WITH_INFO_1"
    assert response.value.affected_entities[0].entity_id == 7


def test_g2engine_delete_record_with_info_01():
    with open(absolute_path("g2engine_deleteRecordWithInfo-01.json")) as input_file:
        response = G2engineDeleteRecordWithInfoResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.data_source == "TEST"
    assert response.value.record_id == "DELETE_TEST"
    assert response.value.affected_entities[0].entity_id == 100002


def test_g2engine_find_interesting_entities_by_entity_id_01():
    with open(
        absolute_path("g2engine_findInterestingEntitiesByEntityID-01.json")
    ) as input_file:
        response = G2engineFindInterestingEntitiesByEntityIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.interesting_entities.entities == []


def test_g2engine_find_interesting_entities_by_record_id_01():
    with open(
        absolute_path("g2engine_findInterestingEntitiesByRecordID-01.json")
    ) as input_file:
        response = G2engineFindInterestingEntitiesByRecordIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.interesting_entities.entities == []


def test_g2engine_find_network_by_entity_id_01():
    with open(absolute_path("g2engine_findNetworkByEntityID-01.json")) as input_file:
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
    with open(absolute_path("g2engine_findNetworkByRecordID-01.json")) as input_file:
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
    with open(absolute_path("g2engine_findPathByEntityID-01.json")) as input_file:
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
    with open(absolute_path("g2engine_findPathByRecordID-01.json")) as input_file:
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


def test_g2engine_get_entity_by_entity_id_01():
    with open(absolute_path("g2engine_getEntityByEntityID-01.json")) as input_file:
        response = G2engineGetEntityByEntityIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.related_entities == []
    assert response.value.resolved_entity.entity_id == 1
    assert response.value.resolved_entity.entity_name == "Robert Smith"
    feature_json = response.value.resolved_entity.features.get("ADDRESS")[0]
    feature = FeatureForAttribute.from_json_data(feature_json)
    assert feature.feat_desc == "1515 Adela Lane Las Vegas NV 89111"
    assert feature.feat_desc_values[0].lib_feat_id == 20


def test_g2engine_get_entity_by_record_id_01():
    with open(absolute_path("g2engine_getEntityByRecordID-01.json")) as input_file:
        response = G2engineGetEntityByRecordIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.related_entities == []
    assert response.value.resolved_entity.entity_id == 1
    assert response.value.resolved_entity.entity_name == "Robert Smith"

    feature_json = response.value.resolved_entity.features.get("ADDRESS")[0]
    feature = FeatureForAttribute.from_json_data(feature_json)
    assert feature.feat_desc == "1515 Adela Lane Las Vegas NV 89111"
    assert feature.feat_desc_values[0].lib_feat_id == 20


def test_g2engine_get_record_01():
    with open(absolute_path("g2engine_getRecord-01.json")) as input_file:
        response = G2engineGetRecordResponse.from_json_data(json.load(input_file))
    assert response.value.data_source == "CUSTOMERS"
    assert response.value.record_id == "1001"
    assert type(response.value.json_data) == dict
    assert response.value.json_data.get("DATA_SOURCE") == "CUSTOMERS"
    assert response.value.json_data.get("RECORD_ID") == "1001"


# TODO: Fix this
def test_g2engine_get_redo_record_01():
    with open(absolute_path("g2engine_getRedoRecord-01.json")) as input_file:
        response = G2engineGetRedoRecordResponse.from_json_data(json.load(input_file))
    assert response.value.value == {}


def test_g2engine_get_virtual_entity_by_record_id_01():
    with open(
        absolute_path("g2engine_getVirtualEntityByRecordID-01.json")
    ) as input_file:
        response = G2engineGetVirtualEntityByRecordIDResponse.from_json_data(
            json.load(input_file)
        )
    assert response.value.resolved_entity.entity_id == 1
    assert response.value.resolved_entity.entity_name == "Robert Smith"
    feature_json = response.value.resolved_entity.features.get("NAME")[0]
    feature = FeatureForAttribute.from_json_data(feature_json)
    assert feature.feat_desc == "Robert Smith"
    assert feature.lib_feat_id == 1
    assert feature.feat_desc_values[1].lib_feat_id == 18


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


if __name__ == "__main__":
    test_g2engine_add_record_with_info_01()
