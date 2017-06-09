# dr-tools
Tools for Hadoop disaster recovery

## Rangercli

This is a set of scripts that interacts with the Ranger REST API to transfer
and compare policies of two clusters.

## Hive Schema Copy Script

This is simple sample script that does the following:

* connects to MySQL server
* dumps content of "hive" database on disk (per default in /tmp/ directory)
* changes cluster name
* imports dump to backup MySQL server
* clean up

### Prerequisites

* Environment variables must be set
  ```
  CLUSTERNAME, HIVE_USER, HIVE_PASSWORD, MYSQL_HOST,
  CLUSTERNAME2, HIVE_USER2, HIVE_PASSWORD2, MYSQL_HOST2
  ```
* Network connectivity to both hosts on port 3306 must be given.
* User need to be allowed to connect to hive database on both servers from
  server the script is executed from.

### Usage
Make sure script has execute permissions.
```
./hive-schema-copy.sh
```
