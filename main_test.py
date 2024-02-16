#! /usr/bin/env python3

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json

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
# Mock Senzing SDK API calls
# Use list at https://github.com/senzing-garage/knowledge-base/blob/main/proposals/SDKs-for-V4/canonical-names.md
# -----------------------------------------------------------------------------


def mock_g2engine_add_record_with_info():
    return json.dumps(
        {
            "DATA_SOURCE": "TEST",
            "RECORD_ID": "WITH_INFO_1",
            "AFFECTED_ENTITIES": [{"ENTITY_ID": 7}],
            "INTERESTING_ENTITIES": {"ENTITIES": []},
        }
    )


def mock_g2engine_delete_record_with_info():
    return json.dumps(
        {
            "DATA_SOURCE": "TEST",
            "RECORD_ID": "DELETE_TEST",
            "AFFECTED_ENTITIES": [{"ENTITY_ID": 100002}],
            "INTERESTING_ENTITIES": {"ENTITIES": []},
        }
    )


def mock_g2engine_find_interesting_entities_by_entity_id():
    return json.dumps({"INTERESTING_ENTITIES": {"ENTITIES": []}})


def mock_g2engine_find_interesting_entities_by_record_id():
    return mock_g2engine_find_interesting_entities_by_entity_id()


def mock_g2engine_find_network_by_entity_id():
    return json.dumps(
        {
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
    )


def mock_g2engine_find_network_by_record_id():
    return mock_g2engine_find_network_by_entity_id()


def mock_g2engine_find_path_by_entity_id():
    return json.dumps(
        {
            "ENTITY_PATHS": [
                {"START_ENTITY_ID": 1, "END_ENTITY_ID": 1, "ENTITIES": [1]}
            ],
            "ENTITIES": [
                {
                    "RESOLVED_ENTITY": {
                        "ENTITY_ID": 1,
                        "ENTITY_NAME": "Robert Smith",
                        "RECORD_SUMMARY": [
                            {
                                "DATA_SOURCE": "CUSTOMERS",
                                "RECORD_COUNT": 3,
                                "FIRST_SEEN_DT": "2024-02-15 22:38:57.789",
                                "LAST_SEEN_DT": "2024-02-15 22:39:02.516",
                            }
                        ],
                        "LAST_SEEN_DT": "2024-02-15 22:39:02.516",
                    },
                    "RELATED_ENTITIES": [],
                }
            ],
        }
    )


def mock_g2engine_find_path_by_record_id():
    return mock_g2engine_find_path_by_entity_id()


def mock_g2engine_get_entity_by_entity_id():
    return json.dumps(
        {
            "RESOLVED_ENTITY": {
                "ENTITY_ID": 1,
                "ENTITY_NAME": "Robert Smith",
                "FEATURES": {
                    "ADDRESS": [
                        {
                            "FEAT_DESC": "1515 Adela Lane Las Vegas NV 89111",
                            "LIB_FEAT_ID": 20,
                            "USAGE_TYPE": "HOME",
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "1515 Adela Lane Las Vegas NV 89111",
                                    "LIB_FEAT_ID": 20,
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "123 Main Street, Las Vegas NV 89132",
                            "LIB_FEAT_ID": 3,
                            "USAGE_TYPE": "MAILING",
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "123 Main Street, Las Vegas NV 89132",
                                    "LIB_FEAT_ID": 3,
                                }
                            ],
                        },
                    ],
                    "DOB": [
                        {
                            "FEAT_DESC": "12/11/1978",
                            "LIB_FEAT_ID": 2,
                            "FEAT_DESC_VALUES": [
                                {"FEAT_DESC": "12/11/1978", "LIB_FEAT_ID": 2},
                                {"FEAT_DESC": "11/12/1978", "LIB_FEAT_ID": 19},
                            ],
                        }
                    ],
                    "EMAIL": [
                        {
                            "FEAT_DESC": "bsmith@work.com",
                            "LIB_FEAT_ID": 5,
                            "FEAT_DESC_VALUES": [
                                {"FEAT_DESC": "bsmith@work.com", "LIB_FEAT_ID": 5}
                            ],
                        }
                    ],
                    "NAME": [
                        {
                            "FEAT_DESC": "Robert Smith",
                            "LIB_FEAT_ID": 1,
                            "USAGE_TYPE": "PRIMARY",
                            "FEAT_DESC_VALUES": [
                                {"FEAT_DESC": "Robert Smith", "LIB_FEAT_ID": 1},
                                {"FEAT_DESC": "Bob J Smith", "LIB_FEAT_ID": 32},
                                {"FEAT_DESC": "Bob Smith", "LIB_FEAT_ID": 18},
                            ],
                        }
                    ],
                    "PHONE": [
                        {
                            "FEAT_DESC": "702-919-1300",
                            "LIB_FEAT_ID": 4,
                            "USAGE_TYPE": "HOME",
                            "FEAT_DESC_VALUES": [
                                {"FEAT_DESC": "702-919-1300", "LIB_FEAT_ID": 4}
                            ],
                        },
                        {
                            "FEAT_DESC": "702-919-1300",
                            "LIB_FEAT_ID": 4,
                            "USAGE_TYPE": "MOBILE",
                            "FEAT_DESC_VALUES": [
                                {"FEAT_DESC": "702-919-1300", "LIB_FEAT_ID": 4}
                            ],
                        },
                    ],
                    "RECORD_TYPE": [
                        {
                            "FEAT_DESC": "PERSON",
                            "LIB_FEAT_ID": 16,
                            "FEAT_DESC_VALUES": [
                                {"FEAT_DESC": "PERSON", "LIB_FEAT_ID": 16}
                            ],
                        }
                    ],
                },
                "RECORD_SUMMARY": [
                    {
                        "DATA_SOURCE": "CUSTOMERS",
                        "RECORD_COUNT": 3,
                        "FIRST_SEEN_DT": "2024-02-15 22:38:57.789",
                        "LAST_SEEN_DT": "2024-02-15 22:39:02.516",
                    }
                ],
                "LAST_SEEN_DT": "2024-02-15 22:39:02.516",
                "RECORDS": [
                    {
                        "DATA_SOURCE": "CUSTOMERS",
                        "RECORD_ID": "1001",
                        "ENTITY_TYPE": "GENERIC",
                        "INTERNAL_ID": 1,
                        "ENTITY_KEY": "53C913F04DF04CA474389042F731333F92DCD3E7",
                        "ENTITY_DESC": "Robert Smith",
                        "MATCH_KEY": "",
                        "MATCH_LEVEL": 0,
                        "MATCH_LEVEL_CODE": "",
                        "ERRULE_CODE": "",
                        "LAST_SEEN_DT": "2024-02-15 22:38:57.789",
                    },
                    {
                        "DATA_SOURCE": "CUSTOMERS",
                        "RECORD_ID": "1002",
                        "ENTITY_TYPE": "GENERIC",
                        "INTERNAL_ID": 2,
                        "ENTITY_KEY": "E417012A90D71444C2E190FAF313DA88C5E663B9",
                        "ENTITY_DESC": "Bob Smith",
                        "MATCH_KEY": "+NAME+DOB+PHONE",
                        "MATCH_LEVEL": 1,
                        "MATCH_LEVEL_CODE": "RESOLVED",
                        "ERRULE_CODE": "CNAME_CFF_CEXCL",
                        "LAST_SEEN_DT": "2024-02-15 22:39:00.429",
                    },
                    {
                        "DATA_SOURCE": "CUSTOMERS",
                        "RECORD_ID": "1003",
                        "ENTITY_TYPE": "GENERIC",
                        "INTERNAL_ID": 3,
                        "ENTITY_KEY": "B327B02717D7515EC96319C0A0AD680FE532E27E",
                        "ENTITY_DESC": "Bob J Smith",
                        "MATCH_KEY": "+NAME+DOB+EMAIL",
                        "MATCH_LEVEL": 1,
                        "MATCH_LEVEL_CODE": "RESOLVED",
                        "ERRULE_CODE": "SF1_PNAME_CSTAB",
                        "LAST_SEEN_DT": "2024-02-15 22:39:02.516",
                    },
                ],
            },
            "RELATED_ENTITIES": [],
        }
    )


def mock_g2engine_get_entity_by_record_id():
    return mock_g2engine_get_entity_by_entity_id()


def mock_g2engine_get_record():
    return json.dumps(
        {
            "DATA_SOURCE": "CUSTOMERS",
            "RECORD_ID": "1001",
            "JSON_DATA": {
                "DATA_SOURCE": "CUSTOMERS",
                "RECORD_ID": "1001",
                "RECORD_TYPE": "PERSON",
                "PRIMARY_NAME_LAST": "Smith",
                "PRIMARY_NAME_FIRST": "Robert",
                "DATE_OF_BIRTH": "12/11/1978",
                "ADDR_TYPE": "MAILING",
                "ADDR_LINE1": "123 Main Street, Las Vegas NV 89132",
                "PHONE_TYPE": "HOME",
                "PHONE_NUMBER": "702-919-1300",
                "EMAIL_ADDRESS": "bsmith@work.com",
                "DATE": "1/2/18",
                "STATUS": "Active",
                "AMOUNT": "100",
            },
        }
    )


def mock_g2engine_get_redo_record():
    return json.dumps({})


def mock_g2engine_get_virtual_entity_by_record_id():
    return json.dumps(
        {
            "RESOLVED_ENTITY": {
                "ENTITY_ID": 1,
                "ENTITY_NAME": "Robert Smith",
                "FEATURES": {
                    "ADDRESS": [
                        {
                            "FEAT_DESC": "1515 Adela Lane Las Vegas NV 89111",
                            "LIB_FEAT_ID": 20,
                            "USAGE_TYPE": "HOME",
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "1515 Adela Lane Las Vegas NV 89111",
                                    "LIB_FEAT_ID": 20,
                                    "USED_FOR_CAND": "N",
                                    "USED_FOR_SCORING": "Y",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "123 Main Street, Las Vegas NV 89132",
                            "LIB_FEAT_ID": 3,
                            "USAGE_TYPE": "MAILING",
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "123 Main Street, Las Vegas NV 89132",
                                    "LIB_FEAT_ID": 3,
                                    "USED_FOR_CAND": "N",
                                    "USED_FOR_SCORING": "Y",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                    ],
                    "ADDR_KEY": [
                        {
                            "FEAT_DESC": "123|MN||89132",
                            "LIB_FEAT_ID": 14,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "123|MN||89132",
                                    "LIB_FEAT_ID": 14,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "123|MN||LS FKS",
                            "LIB_FEAT_ID": 13,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "123|MN||LS FKS",
                                    "LIB_FEAT_ID": 13,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "1515|ATL||89111",
                            "LIB_FEAT_ID": 30,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "1515|ATL||89111",
                                    "LIB_FEAT_ID": 30,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "1515|ATL||LS FKS",
                            "LIB_FEAT_ID": 31,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "1515|ATL||LS FKS",
                                    "LIB_FEAT_ID": 31,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                    ],
                    "DOB": [
                        {
                            "FEAT_DESC": "12/11/1978",
                            "LIB_FEAT_ID": 2,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "12/11/1978",
                                    "LIB_FEAT_ID": 2,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "Y",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                },
                                {
                                    "FEAT_DESC": "11/12/1978",
                                    "LIB_FEAT_ID": 19,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "Y",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                },
                            ],
                        }
                    ],
                    "EMAIL": [
                        {
                            "FEAT_DESC": "bsmith@work.com",
                            "LIB_FEAT_ID": 5,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "bsmith@work.com",
                                    "LIB_FEAT_ID": 5,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "Y",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        }
                    ],
                    "EMAIL_KEY": [
                        {
                            "FEAT_DESC": "bsmith@WORK.COM",
                            "LIB_FEAT_ID": 17,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "bsmith@WORK.COM",
                                    "LIB_FEAT_ID": 17,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        }
                    ],
                    "NAME": [
                        {
                            "FEAT_DESC": "Robert Smith",
                            "LIB_FEAT_ID": 1,
                            "USAGE_TYPE": "PRIMARY",
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "Robert Smith",
                                    "LIB_FEAT_ID": 1,
                                    "USED_FOR_CAND": "N",
                                    "USED_FOR_SCORING": "Y",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                },
                                {
                                    "FEAT_DESC": "Bob Smith",
                                    "LIB_FEAT_ID": 18,
                                    "USED_FOR_CAND": "N",
                                    "USED_FOR_SCORING": "Y",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                },
                            ],
                        }
                    ],
                    "NAME_KEY": [
                        {
                            "FEAT_DESC": "BB|SM0",
                            "LIB_FEAT_ID": 22,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "BB|SM0",
                                    "LIB_FEAT_ID": 22,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "BB|SM0|ADDRESS.CITY_STD=LS FKS",
                            "LIB_FEAT_ID": 26,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "BB|SM0|ADDRESS.CITY_STD=LS FKS",
                                    "LIB_FEAT_ID": 26,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "BB|SM0|DOB.MMDD_HASH=1211",
                            "LIB_FEAT_ID": 24,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "BB|SM0|DOB.MMDD_HASH=1211",
                                    "LIB_FEAT_ID": 24,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "BB|SM0|DOB.MMYY_HASH=1178",
                            "LIB_FEAT_ID": 28,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "BB|SM0|DOB.MMYY_HASH=1178",
                                    "LIB_FEAT_ID": 28,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "BB|SM0|DOB=71211",
                            "LIB_FEAT_ID": 21,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "BB|SM0|DOB=71211",
                                    "LIB_FEAT_ID": 21,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "BB|SM0|PHONE.PHONE_LAST_5=91300",
                            "LIB_FEAT_ID": 29,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "BB|SM0|PHONE.PHONE_LAST_5=91300",
                                    "LIB_FEAT_ID": 29,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "BB|SM0|POST=89111",
                            "LIB_FEAT_ID": 25,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "BB|SM0|POST=89111",
                                    "LIB_FEAT_ID": 25,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "RBRT|SM0",
                            "LIB_FEAT_ID": 7,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "RBRT|SM0",
                                    "LIB_FEAT_ID": 7,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "RBRT|SM0|ADDRESS.CITY_STD=LS FKS",
                            "LIB_FEAT_ID": 8,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "RBRT|SM0|ADDRESS.CITY_STD=LS FKS",
                                    "LIB_FEAT_ID": 8,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "RBRT|SM0|DOB.MMDD_HASH=1211",
                            "LIB_FEAT_ID": 11,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "RBRT|SM0|DOB.MMDD_HASH=1211",
                                    "LIB_FEAT_ID": 11,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "RBRT|SM0|DOB.MMYY_HASH=1178",
                            "LIB_FEAT_ID": 23,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "RBRT|SM0|DOB.MMYY_HASH=1178",
                                    "LIB_FEAT_ID": 23,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "RBRT|SM0|DOB.MMYY_HASH=1278",
                            "LIB_FEAT_ID": 6,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "RBRT|SM0|DOB.MMYY_HASH=1278",
                                    "LIB_FEAT_ID": 6,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "RBRT|SM0|DOB=71211",
                            "LIB_FEAT_ID": 12,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "RBRT|SM0|DOB=71211",
                                    "LIB_FEAT_ID": 12,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "RBRT|SM0|PHONE.PHONE_LAST_5=91300",
                            "LIB_FEAT_ID": 10,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "RBRT|SM0|PHONE.PHONE_LAST_5=91300",
                                    "LIB_FEAT_ID": 10,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "RBRT|SM0|POST=89111",
                            "LIB_FEAT_ID": 27,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "RBRT|SM0|POST=89111",
                                    "LIB_FEAT_ID": 27,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "RBRT|SM0|POST=89132",
                            "LIB_FEAT_ID": 9,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "RBRT|SM0|POST=89132",
                                    "LIB_FEAT_ID": 9,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                    ],
                    "PHONE": [
                        {
                            "FEAT_DESC": "702-919-1300",
                            "LIB_FEAT_ID": 4,
                            "USAGE_TYPE": "HOME",
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "702-919-1300",
                                    "LIB_FEAT_ID": 4,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "Y",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                        {
                            "FEAT_DESC": "702-919-1300",
                            "LIB_FEAT_ID": 4,
                            "USAGE_TYPE": "MOBILE",
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "702-919-1300",
                                    "LIB_FEAT_ID": 4,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "Y",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        },
                    ],
                    "PHONE_KEY": [
                        {
                            "FEAT_DESC": "7029191300",
                            "LIB_FEAT_ID": 15,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "7029191300",
                                    "LIB_FEAT_ID": 15,
                                    "USED_FOR_CAND": "Y",
                                    "USED_FOR_SCORING": "N",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        }
                    ],
                    "RECORD_TYPE": [
                        {
                            "FEAT_DESC": "PERSON",
                            "LIB_FEAT_ID": 16,
                            "FEAT_DESC_VALUES": [
                                {
                                    "FEAT_DESC": "PERSON",
                                    "LIB_FEAT_ID": 16,
                                    "USED_FOR_CAND": "N",
                                    "USED_FOR_SCORING": "Y",
                                    "ENTITY_COUNT": 1,
                                    "CANDIDATE_CAP_REACHED": "N",
                                    "SCORING_CAP_REACHED": "N",
                                    "SUPPRESSED": "N",
                                }
                            ],
                        }
                    ],
                },
                "RECORD_SUMMARY": [
                    {
                        "DATA_SOURCE": "CUSTOMERS",
                        "RECORD_COUNT": 2,
                        "FIRST_SEEN_DT": "2024-02-15 22:38:57.789",
                        "LAST_SEEN_DT": "2024-02-15 22:39:00.429",
                    }
                ],
                "LAST_SEEN_DT": "2024-02-15 22:39:00.429",
                "RECORDS": [
                    {
                        "DATA_SOURCE": "CUSTOMERS",
                        "RECORD_ID": "1001",
                        "ENTITY_TYPE": "GENERIC",
                        "INTERNAL_ID": 1,
                        "ENTITY_KEY": "53C913F04DF04CA474389042F731333F92DCD3E7",
                        "ENTITY_DESC": "Robert Smith",
                        "LAST_SEEN_DT": "2024-02-15 22:38:57.789",
                        "FEATURES": [
                            {"LIB_FEAT_ID": 1, "USAGE_TYPE": "PRIMARY"},
                            {"LIB_FEAT_ID": 2},
                            {"LIB_FEAT_ID": 3, "USAGE_TYPE": "MAILING"},
                            {"LIB_FEAT_ID": 4, "USAGE_TYPE": "HOME"},
                            {"LIB_FEAT_ID": 5},
                            {"LIB_FEAT_ID": 6},
                            {"LIB_FEAT_ID": 7},
                            {"LIB_FEAT_ID": 8},
                            {"LIB_FEAT_ID": 9},
                            {"LIB_FEAT_ID": 10},
                            {"LIB_FEAT_ID": 11},
                            {"LIB_FEAT_ID": 12},
                            {"LIB_FEAT_ID": 13},
                            {"LIB_FEAT_ID": 14},
                            {"LIB_FEAT_ID": 15},
                            {"LIB_FEAT_ID": 16},
                            {"LIB_FEAT_ID": 17},
                        ],
                    },
                    {
                        "DATA_SOURCE": "CUSTOMERS",
                        "RECORD_ID": "1002",
                        "ENTITY_TYPE": "GENERIC",
                        "INTERNAL_ID": 2,
                        "ENTITY_KEY": "E417012A90D71444C2E190FAF313DA88C5E663B9",
                        "ENTITY_DESC": "Bob Smith",
                        "LAST_SEEN_DT": "2024-02-15 22:39:00.429",
                        "FEATURES": [
                            {"LIB_FEAT_ID": 4, "USAGE_TYPE": "MOBILE"},
                            {"LIB_FEAT_ID": 7},
                            {"LIB_FEAT_ID": 8},
                            {"LIB_FEAT_ID": 10},
                            {"LIB_FEAT_ID": 11},
                            {"LIB_FEAT_ID": 12},
                            {"LIB_FEAT_ID": 15},
                            {"LIB_FEAT_ID": 16},
                            {"LIB_FEAT_ID": 18, "USAGE_TYPE": "PRIMARY"},
                            {"LIB_FEAT_ID": 19},
                            {"LIB_FEAT_ID": 20, "USAGE_TYPE": "HOME"},
                            {"LIB_FEAT_ID": 21},
                            {"LIB_FEAT_ID": 22},
                            {"LIB_FEAT_ID": 23},
                            {"LIB_FEAT_ID": 24},
                            {"LIB_FEAT_ID": 25},
                            {"LIB_FEAT_ID": 26},
                            {"LIB_FEAT_ID": 27},
                            {"LIB_FEAT_ID": 28},
                            {"LIB_FEAT_ID": 29},
                            {"LIB_FEAT_ID": 30},
                            {"LIB_FEAT_ID": 31},
                        ],
                    },
                ],
            }
        }
    )


# -----------------------------------------------------------------------------
# TestCases
# -----------------------------------------------------------------------------

response = G2engineAddRecordWithInfoResponse.from_json_data(
    json.loads(mock_g2engine_add_record_with_info())
)
print(
    f"G2engineAddRecordWithInfoResponse: DataSource: {response.value.data_source}; RecordID: {response.value.record_id}; Affected entity: {response.value.affected_entities.value[0].entity_id}"
)

response = G2engineDeleteRecordWithInfoResponse.from_json_data(
    json.loads(mock_g2engine_delete_record_with_info())
)
print(
    f"G2engineDeleteRecordWithInfoResponse: DataSource: {response.value.data_source}; RecordID: {response.value.record_id}; Affected entity: {response.value.affected_entities.value[0].entity_id}"
)

response = G2engineFindInterestingEntitiesByEntityIDResponse.from_json_data(
    json.loads(mock_g2engine_find_interesting_entities_by_entity_id())
)
print(
    f"G2engineFindInterestingEntitiesByEntityIDResponse: Entities: {response.value.interesting_entities.entities}"
)

response = G2engineFindInterestingEntitiesByRecordIDResponse.from_json_data(
    json.loads(mock_g2engine_find_interesting_entities_by_record_id())
)
print(
    f"G2engineFindInterestingEntitiesByRecordIDResponse: Entities: {response.value.interesting_entities.entities}"
)


response = G2engineFindNetworkByEntityIDResponse.from_json_data(
    json.loads(mock_g2engine_find_network_by_entity_id())
)
print(
    f"G2engineFindNetworkByEntityIDResponse: Entity name: {response.value.entities.value[0].resolved_entity.entity_name}"
)

response = G2engineFindNetworkByRecordIDResponse.from_json_data(
    json.loads(mock_g2engine_find_network_by_record_id())
)
print(
    f"G2engineFindNetworkByRecordIDResponse: Record summary: {response.value.entities.value[0].resolved_entity.record_summary}"
)

response = G2engineFindPathByEntityIDResponse.from_json_data(
    json.loads(mock_g2engine_find_path_by_entity_id())
)
print(
    f"G2engineFindPathByEntityIDResponse: Entity name: {response.value.entities.value[0].resolved_entity.entity_name}"
)

response = G2engineFindPathByRecordIDResponse.from_json_data(
    json.loads(mock_g2engine_find_path_by_record_id())
)
print(
    f"G2engineFindPathByRecordIDResponse: Is ambiguous: {response.value.entities.value[0].resolved_entity.is_ambiguous}"
)

# TODO:  response.value.resolved_entity.features needs to be fixed.
response = G2engineGetEntityByEntityIDResponse.from_json_data(
    json.loads(mock_g2engine_get_entity_by_entity_id())
)
print(
    f"G2engineGetEntityByEntityIDResponse: Data source: {response.value.resolved_entity.record_summary.value[0].data_source}"
)

# TODO:  response.value.resolved_entity.features needs to be fixed.
response = G2engineGetEntityByRecordIDResponse.from_json_data(
    json.loads(mock_g2engine_get_entity_by_record_id())
)
print(
    f"G2engineGetEntityByRecordIDResponse: Record count: {response.value.resolved_entity.record_summary.value[0].record_count}"
)

# TODO:  response.value.json_data needs to be fixed.
response = G2engineGetRecordResponse.from_json_data(
    json.loads(mock_g2engine_get_record())
)
print(f"G2engineGetRecordResponse: Data source: {response.value.data_source}")


# TODO: Fix
response = G2engineGetRedoRecordResponse.from_json_data(
    json.loads(mock_g2engine_get_redo_record())
)
print(f"G2engineGetRedoRecordResponse: Value: {response.value}")


response = G2engineGetVirtualEntityByRecordIDResponse.from_json_data(
    json.loads(mock_g2engine_get_virtual_entity_by_record_id())
)
address_feature_json = response.value.resolved_entity.features.value.get("ADDRESS")[0]
address_feature = FeatureForAttribute.from_json_data(address_feature_json)
print(
    f"G2engineGetVirtualEntityByRecordIDResponse: Address Feature Description: {address_feature.feat_desc_values.value[0].feat_desc}"
)


response = G2engineGetVirtualEntityByRecordIDResponse.from_json_data(
    json.loads(mock_g2engine_get_virtual_entity_by_record_id())
)
feature_list = response.value.resolved_entity.features.value.get("NAME", [])
for feature in feature_list:
    feat_desc_list = FeatureForAttribute.from_json_data(feature).feat_desc_values.value
    for feat_desc in feat_desc_list:
        print(
            f"G2engineGetVirtualEntityByRecordIDResponse: Feature description: {feat_desc.feat_desc}"
        )

# Using straight JSON parsing.
# - No static checking can be done on JSON keys
# - No editor hints
response = mock_g2engine_get_virtual_entity_by_record_id()
response_dict = json.loads(response)
feature_list = (
    response_dict.get("RESOLVED_ENTITY", {}).get("FEATURES", {}).get("NAME", [])
)
for feature in feature_list:
    feat_desc_list = feature.get("FEAT_DESC_VALUES")
    for feat_desc in feat_desc_list:
        print(
            f"G2engineGetVirtualEntityByRecordIDResponse: Feature description: {feat_desc.get('FEAT_DESC')}"
        )
