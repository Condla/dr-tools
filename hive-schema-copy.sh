#!/usr/bin/bash

export DUMP_PATH=/tmp

mysqldump -u$HIVE_USER -p$HIVE_PASSWORD -h $MYSQL_HOST hive > $DUMP_PATH/hive.dump
sed -i s/$CLUSTERNAME/$CLUSTERNAME2/g $DUMP_PATH/hive.dump
echo 'DROP DATABASE hive; CREATE DATABASE hive; USE hive;' | cat - $DUMP_PATH/hive.dump > $DUMP_PATH/temp && mv $DUMP_PATH/temp $DUMP_PATH/hive.dump
mysql -u$HIVE_USER2 -p$HIVE_PASSWORD2 -h $MYSQL_HOST2 hive < $DUMP_PATH/hive.dump
rm $DUMP_PATH/hive.dump
