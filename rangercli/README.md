# rangercli
Ranger command line interface to interact with the Apache Ranger REST interface.

For this short example a script is provided to get all policies of a Ranger
instance, delete all policies of another Ranger instance and add the policies
to the second instance.


## Prerequisites
* In order to connect to both of the Ranger hosts, it is required to set a few environment
variables for all of the following scripts
```
export RANGER_HOST=https://hostname.example.com
export RANGER_HOST2=https://hostname2.example.com
export RANGER_PORT=6080
export RANGER_PORT2=6080
export RANGER_USER=admin
export RANGER_USER2=admin
export RANGER_PASSWORD=admin
export RANGER_PASSWORD2=admin
export CLUSTERNAME=mastercluster
export CLUSTERNAME=replicacluster
```

* Download the scripts:
```
git clone https://github.com/Condla/dr-tools
cd dr-tools/rangercli
```

## Transfer Policy

Example: I want to transfer policy with id 4 from cluster one to cluster 2: 
```
./transfer-policy.sh 4
```

## Compare Policies
Example: I want to compare the policies of two clusters for completeness and
major differences with output on the command line.
```
./compare-policies.sh
```

## Mirror Policies
Example: I want to delete all policies on cluster 2 and force all policies on
cluster 1 to be transfered.

### Python Version
Then clone or download this project and execute the mirror-policies.py script
*Note: if you use the Python version you need to be able to install the
requests module*
```
python mirror-policies.py
```

### Bash version
If you can't install the requests module
*Note: if you use the bash version of the script, policy definitions will temporarily
be saved in the path specified by the $TEMP_POLICY_FILE variable. At the moment this is the /tmp/policy.json file
If it is a concern that policy definition might temporarily be visible to other users on the machine, you should
choose a path that is accessible by only the user executing the script.*

```
git clone https://github.com/Condla/rangercli
cd rangercli
./mirror-policies.sh
```
