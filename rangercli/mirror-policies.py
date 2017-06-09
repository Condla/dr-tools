import logging
from client import RangerClient
from env import (RANGER_HOST, RANGER_HOST2,
                 RANGER_USER, RANGER_USER2,
                 RANGER_PASSWORD, RANGER_PASSWORD2,
                 RANGER_PORT, RANGER_PORT2,
                 CLUSTER_NAME, CLUSTER_NAME2,
                 RANGER_SECURE)


logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.WARN)
requests_log.propagate = True


if __name__ ==  "__main__":
    if not RANGER_HOST:
        raise Exception("Ranger hostname was not set! (RANGER_HOST environment)")

    ### connect to Ranger of cluster 1
    ranger = RangerClient(ranger_fqdn=RANGER_HOST, ranger_port=RANGER_PORT,
                          ranger_user=RANGER_USER,
                          ranger_password=RANGER_PASSWORD)
    policies = ranger.get_all_policies()

    ### Change name and print policy name.
    policies2 = []
    for policy in policies:
        policy['repositoryName'] = policy['repositoryName'].replace(CLUSTER_NAME, CLUSTER_NAME2)
        logging.info("Got policy '{}'.".format(policy["policyName"]))
        policies2.append(policy)

    ### connect to Ranger of cluster 2
    ranger = RangerClient(ranger_fqdn=RANGER_HOST2, ranger_port=RANGER_PORT2,
                          ranger_user=RANGER_USER2,
                          ranger_password=RANGER_PASSWORD2)
    ranger.delete_all_policies()
    ranger.add_policies(policies2)
