#!/bin/bash

TEMP_POLICY_FILE=/tmp/policy.json


if [ -z $1 ]
then
    echo "You must set a policy id!"
    exit
else
    policy_id=$1
fi

get_policy()
{
curl -k -u $3:$4 $1:$2/service/public/v2/api/policy/$5
}


post_policy()
{
curl -k -X POST -H "Content-Type: application/json" --data @$TEMP_POLICY_FILE -u $3:$4 $1:$2/service/public/v2/api/policy/
}

policy=$(get_policy $RANGER_HOST $RANGER_PORT $RANGER_USER $RANGER_PASSWORD $policy_id)
policy=$(echo $policy | sed s/$CLUSTERNAME/$CLUSTERNAME/g)

echo $policy | grep -v xa.error.data_not_found
rc=$?

if [ "$rc" -eq "0" ]
then
    echo $policy > $TEMP_POLICY_FILE
    result=$(post_policy $RANGER_HOST2 $RANGER_PORT2 $RANGER_USER2 $RANGER_PASSWORD2)
    echo $result
fi

