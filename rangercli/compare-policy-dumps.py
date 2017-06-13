#!/usr/bin/python

import json
import pprint



DUMP_FILE1 = "/tmp/policies1.json"
DUMP_FILE2 = "/tmp/policies2.json"

COMPARE_ATTRIBUTES = {
        "totalCount": True,
        "vXPolicies": [
            "columnFamilies",
            "columnType",
            "columns",
            "description"
            "isAuditEnabled",
            "isEnabled",
            "isRecursive",
            "permMapList"
            ]
        }


dump1 = open(DUMP_FILE1).read()
dump2 = open(DUMP_FILE2).read()
data1 = json.loads(dump1)
data2 = json.loads(dump2)

policies1 = data1["vXPolicies"]
policies2 = data2["vXPolicies"]

print("################")
print("Checking policies:")
print("################")
for policy1 in policies1:
    repoType1 = policy1["repositoryType"]
    resourceName1 = policy1["resourceName"]

    replacePerm1 = policy1["replacePerm"]
    isAuditEnabled1 = policy1["isAuditEnabled"]
    isEnabled1 = policy1["isEnabled"]
    isRecursive1 = policy1["isRecursive"]
    permMapList1 = policy1["permMapList"]

    policy_found = False
    for policy2 in policies2:
        repoType2 = policy2["repositoryType"]
        resourceName2 = policy2["resourceName"]
        replacePerm2 = policy2["replacePerm"]
        isAuditEnabled2 = policy2["isAuditEnabled"]
        isEnabled2 = policy2["isEnabled"]
        isRecursive2 = policy2["isRecursive"]
        permMapList2 = policy2["permMapList"]
        if repoType2 == repoType1 and resourceName2 == resourceName1:
            print("policy {0} found".format(policy1['id']))
            policy_found = True
            policies2.remove(policy2)
            if replacePerm1 != replacePerm2:
                print("replacePerm different from policy with id {0}".format(policy1["id"]))
            if isAuditEnabled1 != isAuditEnabled2:
                print("isAuditEnabled different from policy with id {0}".format(policy1["id"]))
            if isEnabled1 != isEnabled2:
                print("isEnabled different from policy with id {0}".format(policy1["id"]))
            if isRecursive1 != isRecursive2:
                print("isRecursive different from policy with id {0}".format(policy1["id"]))
            if permMapList1 != permMapList2:
                print("permMapList different from policy with id {0}".format(policy1["id"]))
            break
    if not policy_found:
        print("policy with id {0}, was not found on cluster 2".format(policy1["id"]))

if len(policies2):
    print()
    print("################")
    print("The following policies were found on cluster 2, but are not present on cluster 1")
    print("################")
    for policy2 in policies2:
        print(policy2["id"])
