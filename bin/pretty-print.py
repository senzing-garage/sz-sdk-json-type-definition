#! /usr/bin/env python3

import json

black_list = ["description", "elements", "goType", "metadata", "properties", "ref", "optionalproperties", "type"]


# -----------------------------------------------------------------------------
# --- Helpers
# -----------------------------------------------------------------------------

def recurse(prefix, an_object):
    for key, value in an_object.items():
        if isinstance(value, dict):
            recurse("{0}.{1}".format(prefix, key), value)
            if key not in black_list:
                if not "metadata" in value:
                    value["metadata"] = {}
                if "description" not in value.get("metadata"):
                    value["metadata"]["description"] = "No description."
                if "goType" not in value.get("metadata"):
                    if value.get("type") == "int32":
                        value["metadata"]["goType"] = "int64"


# -----------------------------------------------------------------------------
# --- Main
# -----------------------------------------------------------------------------

# Read JSON from file.

input_filename = "./senzingapi-RFC8927.json"
with open(input_filename, "r") as input_file:
    data = json.load(input_file)

# Recurse through dictionary.

recurse("definitions", data.get("definitions"))

# Write JSON to file.

output_filename = "./senzingapi-RFC8927-pretty.json"
with open(output_filename, "w") as output_file:
    json.dump(data, output_file, indent=4, sort_keys=True)
