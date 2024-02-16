#! /usr/bin/env python3

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json

from python.typedef import (
    G2EngineAddRecordWithInfoResponse,
    G2EngineDeleteRecordWithInfoResponse,
)

# -----------------------------------------------------------------------------
# Mock Senzing SDK API calls
# -----------------------------------------------------------------------------


def add_record_with_info():
    return json.dumps(
        {
            "DATA_SOURCE": "TEST",
            "RECORD_ID": "WITH_INFO_1",
            "AFFECTED_ENTITIES": [{"ENTITY_ID": 7}],
            "INTERESTING_ENTITIES": {"ENTITIES": []},
        }
    )


def delete_record_with_info():
    return json.dumps(
        {
            "DATA_SOURCE": "TEST",
            "RECORD_ID": "DELETE_TEST",
            "AFFECTED_ENTITIES": [{"ENTITY_ID": 100002}],
            "INTERESTING_ENTITIES": {"ENTITIES": []},
        }
    )


def find_interesting_entities_by_entity_id():
    return json.dumps({"INTERESTING_ENTITIES": {"ENTITIES": []}})


def find_interesting_entities_by_record_id():
    return json.dumps({"INTERESTING_ENTITIES": {"ENTITIES": []}})


FindNetworkByEntityIDResult = {
    "ENTITY_PATHS": [],
    "ENTITIES": [
        {
            "RESOLVED_ENTITY": {
                "ENTITY_ID": 1,
                "ENTITY_NAME": "Robert Smith",
                "RECORD_SUMMARY": [
                    {
                        "DATA_SOURCE": "CUSTOMERS",
                        "RECORD_COUNT": 3,
                        "FIRST_SEEN_DT": "2024-02-15 20:47:57.792",
                        "LAST_SEEN_DT": "2024-02-15 20:48:02.513",
                    }
                ],
                "LAST_SEEN_DT": "2024-02-15 20:48:02.513",
            },
            "RELATED_ENTITIES": [],
        }
    ],
}


# -----------------------------------------------------------------------------
# TestCases
# -----------------------------------------------------------------------------

response = G2EngineAddRecordWithInfoResponse.from_json_data(
    json.loads(add_record_with_info())
)
print(
    f"EngineAddRecordWithInfoResponse: DataSource: {response.value.data_source}; RecordID: {response.value.record_id}; Affected entity: {response.value.affected_entities.value[0].entity_id}"
)

response = G2EngineDeleteRecordWithInfoResponse.from_json_data(
    json.loads(delete_record_with_info())
)
print(
    f"EngineDeleteRecordWithInfoResponse: DataSource: {response.value.data_source}; RecordID: {response.value.record_id}; Affected entity: {response.value.affected_entities.value[0].entity_id}"
)

response = G2EngineFindInterestingEntitiesByEntityIDResponse.from_json_data(
    json.loads(delete_record_with_info(find_interesting_entities_by_entity_id))
)
print(
    f"EngineDeleteRecordWithInfoResponse: DataSource: {response.value.data_source}; RecordID: {response.value.record_id}; Affected entity: {response.value.affected_entities.value[0].entity_id}"
)
