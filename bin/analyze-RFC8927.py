#! /usr/bin/env python3
# For more information, visit https://jsontypedef.com/docs/python-codegen/

import json

global_keys = {}
global_key_count = {}
global_key_type = {}
global_out_of_order = []
black_list = ["description", "elements", "goType", "metadata", "properties", "ref", "optionalproperties", "type"]
exclude_list = []
senzing_json_keys = [
    "ACCT_NUM",
    "ACCOUNT_DOMAIN",
    "ACCOUNT_NUMBER",
    "ADDRESS",
    "ADDRESS_LIST",
    # "ADDR_CITY",
    # "ADDR_COUNTRY",
    # "ADDR_FROM_DATE",
    "ADDR_FULL",
    "ADDR_KEY",
    # "ADDR_LINE1",
    # "ADDR_LINE2",
    # "ADDR_LINE3",
    # "ADDR_LINE4",
    # "ADDR_LINE5",
    # "ADDR_LINE6",
    # "ADDR_POSTAL_CODE",
    # "ADDR_STATE",
    # "ADDR_THRU_DATE",
    # "ADDR_TYPE",
    "CELL_PHONE_NUMBER",
    "CITIZENSHIP",
    "COUNTRY_OF_ASSOCIATION",
    "DATA_SOURCE",
    "DATE_OF_BIRTH",
    "DATE_OF_DEATH",
    "DOB",
    "DOD",
    "DRLIC",
    "DRIVERS_LICENSE_NUMBER",
    "DRIVERS_LICENSE_STATE",
    "DUNS_NUMBER",
    "EMAIL",
    "EMAIL_ADDRESS",
    "EMAIL_KEY",
    "EMPLOYER_NAME",
    "ENTITY_TYPE",
    "FACEBOOK",
    "GENDER",
    "GROUP_ASSN_ID_NUMBER",
    "GROUP_ASSN_ID_TYPE",
    "GROUP_ASSOCIATION_ORG_NAME",
    "GROUP_ASSOCIATION_TYPE",
    "ID_KEY",
    "INSTAGRAM",
    "LEI_NUMBER",
    "LINKEDIN",
    "LOAD_ID",
    "LOGIN_ID",
    "NAME",
    # "NAME_FIRST",
    "NAME_FULL",
    "NAME_KEY",
    # "NAME_LAST",
    "NAME_LIST",
    # "NAME_MIDDLE",
    # "NAME_ORG",
    # "NAME_PREFIX",
    # "NAME_SUFFIX",
    # "NAME_TYPE",
    "NATIONALITY",
    "NATIONAL_ID",
    "NATIONAL_ID_COUNTRY",
    "NATIONAL_ID_NUMBER",
    "NIN_COUNTRY",
    "NIN_NUMBER",
    "NPI_NUMBER",
    "OTHER_ID_COUNTRY",
    "OTHER_ID_NUMBER",
    "OTHER_ID_TYPE",
    "PASSPORT",
    "PASSPORT_COUNTRY",
    "PASSPORT_NUMBER",
    "PASSPORTS",
    "PHONE",
    # "PHONE_FROM_DATE",
    "PHONE_KEY",
    # "PHONE_NUMBER",
    # "PHONE_THRU_DATE",
    # "PHONE_TYPE",
    "PHONES",
    "PLACE_OF_BIRTH",
    "PRIMARY_NAME_FIRST",
    "PRIMARY_NAME_LAST",
    "PRIMARY_NAME_MIDDLE",
    "PRIMARY_NAME_ORG",
    "PRIMARY_NAME_PREFIX",
    "PRIMARY_NAME_SUFFIX",
    "PRIMARY_PHONE_NUMBER",
    # "RECORD_ID",
    "RECORD_TYPE",
    "REGISTRATION_COUNTRY",
    "REGISTRATION_DATE",
    "REL_ANCHOR",
    "REL_ANCHOR_DOMAIN",
    "REL_ANCHOR_KEY",
    "REL_LINK",
    "REL_POINTER",
    "REL_POINTER_DOMAIN",
    "REL_POINTER_KEY",
    "REL_POINTER_ROLE",
    "SIGNAL",
    "SKYPE",
    "SOCIAL_HANDLE",
    "SOCIAL_NETWORK",
    "SOURCE_ID",
    "SSN",
    "SSN_LAST4",
    "SSN_NUMBER",
    "TANGO",
    "TAX_ID_COUNTRY",
    "TAX_ID_NUMBER",
    "TAX_ID_TYPE",
    "TELEGRAM",
    "TRUSTED_ID_NUMBER",
    "TRUSTED_ID_TYPE",
    "TWITTER",
    "VIBER",
    "WEBSITE_ADDRESS",
    "WECHAT",
    "WHATSAPP",
    "WORK_PHONE_NUMBER",
    "ZOOMROOM",
]


def add_to_key_count(key):
    global global_key_count
    if key not in black_list:
        if key not in global_key_count:
            global_key_count[key] = 1
        else:
            global_key_count[key] += 1


def add_to_key_type(key, value):
    global global_key_type
    if key not in black_list:
        if isinstance(value, dict):
            if key not in global_key_type:
                global_key_type[key] = []
            if "type" in value:
                the_type = value.get("type")
                if the_type not in global_key_type[key]:
                    global_key_type[key] += [the_type]
            if "ref" in value:
                the_ref = value.get("ref")
                if the_ref not in global_key_type[key]:
                    global_key_type[key] += [the_ref]


def is_sorted(prefix, list):
    global global_out_of_order
    last_key = ""
    for key in list:
        if not key > last_key:
            global_out_of_order += ["Key out of order: {0}.{1} > {2}".format(prefix, last_key, key)]
        last_key = key


def add_to_list(prefix, list):
    global global_keys
    key_list = [x for x in list.keys() if x not in black_list]
    if len(key_list) > 0:
        key_list.sort()
        global_keys[prefix] = key_list


def recurse(prefix, list):
    is_sorted(prefix, list)
    add_to_list(prefix, list)
    for key, value in list.items():
        add_to_key_count(key)
        add_to_key_type(key, value)
        if isinstance(value, dict):
            recurse("{0}.{1}".format(prefix, key), value)


def search_list(search_term):
    global global_keys
    global exclude_list
    results = []
    search_value = global_keys.get(search_term)
    for key, value in global_keys.items():
        if key not in exclude_list:
            if value == search_value:
                exclude_list.append(key)
                results.append(key)
    return results


# -----------------------------------------------------------------------------
# --- Main
# -----------------------------------------------------------------------------

# Read JSON from file.

input_filename = "./senzingapi-RFC8927.json"
with open(input_filename, "r") as input_file:
    data = json.load(input_file)

# Recurse through dictionary.

recurse("definitions", data.get("definitions"))

# Print "out of order" messages.

print("-"*80)
print("\nVerify that the JSON keys are in sorted order.\n")
if len(global_out_of_order) > 0:
    for message in global_out_of_order:
        print(message)
else:
    print("Everything is sorted properly.")

# Print missing JSON keys.

lists = {
    "definitions.Features": data.get("definitions", {}).get("Features", {}).get("properties", {}),
    "definitions.FeatureScores": data.get("definitions", {}).get("FeatureScores", {}).get("properties", {}),
    "definitions.JsonData": data.get("definitions", {}).get("JsonData", {}).get("properties", {}),
    "definitions.MatchInfoCandidateKeys": data.get("definitions", {}).get("MatchInfoCandidateKeys", {}).get("properties", {}),
    "definitions.MatchScores": data.get("definitions", {}).get("MatchScores", {}).get("properties", {}),
}

print("")
print("-"*80)
print("\nDetect lists not containing mandatory JSON keys.\n")
for key, value in lists.items():
    for senzing_json_key in senzing_json_keys:
        if senzing_json_key not in value:
            print("Missing {0}.{1}".format(key, senzing_json_key))

print("")
print("-"*80)
print("\nDetect JSON keys not in mandatory list.\n")
for key, value in lists.items():
    for key2, value2 in value.items():
        if key2 not in senzing_json_keys:
            print("Key not in master list: {0}.{1}".format(key, key2))

# Print result of test for similar lists.

print("")
print("-"*80)
print("\nDetect lists containing same properties.\n")

for key, value in global_keys.items():
    exclude_list.append(key)
    results = search_list(key)
    if len(results) > 0:
        print("\n{0}:".format(key))
        for result in results:
            print("  - {0}".format(result))

# Print JSON key count results.

print("")
print("-"*80)
print("\nCount occurance of JSON keys")
print("\nCOUNT  KEY")
print("-----  -----------------------------")
sorted_key_counts = sorted(global_key_count.items(), key=lambda x: x[1], reverse=True)
for key, value in sorted_key_counts:
    if value > 1:
        print("{0:5d}  {1}".format(value, key))

# Print type/ref variances.

print("")
print("-"*80)
print("\nCheck for JSON keys having different types\n")
sorted_global_key_type = dict(sorted(global_key_type.items()))
for key, value in sorted_global_key_type.items():
    if len(value) > 1:
        print("{0:30s}  {1}".format(key, sorted(value)))


# Epilog.

print("")
print("-"*80)
