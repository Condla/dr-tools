#!/bin/bash

TEMP_POLICY_FILE=/tmp/policy.json

delete_policy()
{
curl -k -u $3:$4 $1:$2/service/public/v2/api/policy/$5 -X DELETE
}

get_policy()
{
curl -k -u $3:$4 $1:$2/service/public/v2/api/policy/$5
}

post_policy()
{
curl -k -X POST -H "Content-Type: application/json" --data @$TEMP_POLICY_FILE -u $3:$4 $1:$2/service/public/v2/api/policy/
}


delete_policies()
{
i=0
number_not_found=0
first_found=0
for (( ; ; ))
do
    i=$((i+1)) 
    out=$(delete_policy $1 $2 $3 $4 $i) 
    echo $out | grep -v "xa.error.data_not_found"
    rc=$?
    echo $out | grep -v "KMS"
    rc2=$?

    if ([ "$rc" -eq "1" ] || [ "$rc2" -eq "1" ]) && [ "$first_found" -eq "1" ]
     then
         number_not_found=$((number_not_found+1))
     fi
     echo "number not found: $number_not_found"
     echo $rc
     if [ "$rc" -ne "1" ] && [ "$rc2" -ne "1" ]
     then
         first_found=1
     fi

     if [ "$number_not_found" -eq "10" ]
     then
         break
     fi
done
}

copy_policies()
{
i=0
number_not_found=0
first_found=0

for (( ; ; ))

do
    i=$((i+1)) 
    policy=$(get_policy $1 $2 $3 $4 $i)

    policy=$(echo $policy | sed s/$9/${10}/g)
    echo "\n\n\n\n\n\n"
    echo "$policy"
    echo "\n\n\n\n\n\n"

    echo $policy | grep -v xa.error.data_not_found
    rc=$?
    echo $policy | grep -v "KMS"
    rc2=$?
    echo return code: $rc

    if ([ "$rc" -eq "1" ] || [ "$rc2" -eq "1" ]) && [ "$first_found" -eq "1" ]
    then
        number_not_found=$((number_not_found+1))
    fi

    if [ "$rc" -eq "0" ] && [ "$rc2" -eq "0" ]
    then
        echo make request:
        first_found=1
        echo $policy > $TEMP_POLICY_FILE
        result=$(post_policy $5 $6 $7 $8)
        echo "result is $result"
    fi

    echo $number_not_found
    if [ "$number_not_found" -eq "10" ]
    then
        break
    fi

done
}


delete_policies $RANGER_HOST2 $RANGER_PORT2 $RANGER_USER2 $RANGER_PASSWORD2
copy_policies $RANGER_HOST $RANGER_PORT $RANGER_USER $RANGER_PASSWORD $RANGER_HOST2 $RANGER_PORT2 $RANGER_USER2 $RANGER_PASSWORD2 $CLUSTERNAME $CLUSTERNAME2

