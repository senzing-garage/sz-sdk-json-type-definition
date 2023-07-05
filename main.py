#! /usr/bin/env python3

"""
For more information, visit https://jsontypedef.com/docs/python-codegen/
"""

import json
from python.typedef import ConfigListDataSourcesResponse

JSON_STRING = '{"DATA_SOURCES": [{"DSRC_ID": 1, "DSRC_CODE": "TEST"}, {"DSRC_ID": 2, "DSRC_CODE": "SEARCH"}]}'
JSON_STRUCT = ConfigListDataSourcesResponse.from_json_data(json.loads(JSON_STRING))

for data_source in JSON_STRUCT.data_sources.value:
    print("ID: {0}  Code: {1}".format(data_source.dsrc_id, data_source.dsrc_code))

RECONSTRUCTED_STRING = json.dumps(JSON_STRUCT.to_json_data())
print("     Original JSON: {0}".format(JSON_STRING))
print("Reconstructed JSON: {0} - notice JSON keys have been sorted.".format(RECONSTRUCTED_STRING))
