#!/bin/bash

get_policies()
{
curl -k -u $3:$4 $1:$2/service/public/api/policy
}

get_policies $RANGER_HOST $RANGER_PORT $RANGER_USER $RANGER_PASSWORD > /tmp/policies1.json
get_policies $RANGER_HOST2 $RANGER_PORT2 $RANGER_USER2 $RANGER_PASSWORD2 > /tmp/policies2.json

python compare-policy-dumps.py
