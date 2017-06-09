'''
This is a python wrapper tool module for Ranger REST calls. It mainly
consists of the RangerClient. The RangerClient object gets
initialized with the main Ranger parameters.

* Example usage in python code:
    ranger.RangerClient(ranger_fqdn = 'example.rangerserver.com')
    ranger.get_policy(1)

* Example usage from the command line:
    rangercli policy get 1
'''

import requests 
import logging
from utils import return_response
import json
DATA_JSON = '/tmp/rangercli_data.json'

class RangerClient(object):
    '''
    Client to access Ranger REST API 
    '''
    HTTP = 'http://'
    HTTPS = 'https://'
    HEADER = {"Content-Type": "application/json"}
    API_V1_CLUSTERS = '/api/v1/clusters/'
    SERVICES = '/services/'
    COMPONENTS = '/components/'
    SUCCESSFULLY_INITIALIZED_INFO = 'Successfully initialized ' + \
            'RangerClient!'
   
    def __init__(self, ranger_fqdn='localhost',
            ranger_port = '6080',
            ranger_user='admin',
            ranger_password='admin',
            secure = False,
            ):
        '''
        Initialisation of wrapper class. In order to make requests to 
        Ranger admin server the FQDN of the server need to be known. 
        The ranger_port defaults to 6080. The default user name/password 
        combination of Ranger server is admin/admin. This is hopefully 
        not the case in a production cluster.
        '''
        self.ranger_fqdn = ranger_fqdn
        self.ranger_port = ranger_port
        self.ranger_user = ranger_user
        self.ranger_password = ranger_password
        self.AUTH = (self.ranger_user, self.ranger_password)
        http = self.HTTP
        if secure:
            http = self.HTTPS
        self.URL_BASE = '{http}{fqdn}:{port}/'.format(
                http = http, fqdn = self.ranger_fqdn,
                port = self.ranger_port)
        self.URL_REPO = self.URL_BASE + \
                'service/public/api/repository/{repo_id}'
        self.URL_POLICY = self.URL_BASE + \
                'service/public/api/policy/{policy_id}'
        self.URL_POLICY_SEARCH = self.URL_BASE + \
                'service/public/api/policy?policyName={p_name}'
        logging.info("Connecting to ranger of {}".format(self.URL_BASE))
        try:
            self.get_policy(1)
        except:
            raise Exception('Could not connect to Ranger host. Check hostname, user, password and port!')
        logging.debug(self.SUCCESSFULLY_INITIALIZED_INFO)

    def get_base_url(self):
        return self.URL_BASE

    def ranger_get(self, url):
        '''
        Generic ranger get request!
        '''
        response = requests.get(url, auth=self.AUTH)
        return return_response(response)
        
    def ranger_post(self, url, data):
        '''
        Generic ranger put request!
        '''
        data = json.dumps(data)
        response = requests.post(url, auth=self.AUTH,
                data = data, headers = self.HEADER)
        return return_response(response)
    
    def ranger_put(self, url, data):
        '''
        Generic ranger put request!
        '''
        #data = json.dumps(data)
        response = requests.put(url, auth=self.AUTH, 
                data = data)
        return return_response(response)
    
    def ranger_delete(self, url):
        '''
        Generic ranger delete request!
        '''
        response = requests.delete(url, auth=self.AUTH)
        return return_response(response)
   
    def get_policy(self, policy_id):
        '''
        REST call to get policy!
        '''
        url = self.URL_POLICY.format(policy_id=policy_id)
        logging.debug(url)
        return self.ranger_get(url)
 
    def get_all_policies(self):
        '''
        REST call to get all policies
        '''
        logging.info("Get all policies.")
        policies = []
        i = 0
        j = 0
        while True:
            i += 1
            policy = self.get_policy(i)
            if "id" in policy:
                policies.append(self.get_policy(i))
            elif "statusCode" in policy and policy["statusCode"] == 1 and not "KMS" in policy["msgDesc"]:
                j+=1
                # break the loop if the last 10 subsequent requests couldn't
                # find a policy
                if j == 10:
                    break
        logging.info("All policies obtained.")
        return policies

    def create_policy(self, policy):
        '''
        creating a policy by POST
        the policy_id parameter must be empty in order to post a new policy
        '''
        from pprint import pprint
        url = self.URL_POLICY.format(policy_id='')  # empty string
        import json
        return self.ranger_post(url, policy)

    def add_policies(self, policies):
        '''
        add a list of policies to Ranger
        '''
        logging.info("Adding policies.")
        for policy in policies:
            self.create_policy(policy)
        logging.info("Policies added.")
    
    def delete_policy(self, policy_id):
        '''
        REST call to delete policy!
        '''
        url = self.URL_POLICY.format(policy_id=policy_id)
        logging.debug(url)
        return self.ranger_delete(url)

    def delete_all_policies(self):
        '''
        REST call to delete all policies
        '''
        logging.info("Deleting all policies.")
        first_policy_found = False
        i = 0
        j = 0
        while True:
            i += 1
            policy = self.delete_policy(i)
            if not policy.ok:
                if first_policy_found:
                    j += 1
                if j == 20: 
                    break
            else:
                first_policy_found = True
        logging.info("Policies deleted.")

if __name__ == '__main__':
    print('is module')
