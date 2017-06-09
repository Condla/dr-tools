# rangercli
Ranger command line interface to interact with the Apache Ranger REST interface.

For this short example a script is provided to get all policies of a Ranger
instance, delete all policies of another Ranger instance and add the policies
to the second instance.


## Prerequisites
In order to connect to both of the Ranger hosts, it is required to set a few environment
variables:
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

## Python version
Then clone or download this project and execute the mirror-policies.py script
*Note: if you use the Python version you need to be able to install the
requests module*
```
git clone https://github.com/Condla/rangercli
cd rangercli
python mirror-policies.py
```


## Bash version
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
