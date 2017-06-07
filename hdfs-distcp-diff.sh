#!/bin/bash

# specify the cluster names and don't forget the last "/" (!)
FULL_PATH1="hdfs://cluster1:8020/path/to/source/dir/"
FULL_PATH2="hdfs://cluster2:8020/target/dir/"

# count dashes in path
dash="/"
i1=$(( $(grep -o "$dash" <<< "$FULL_PATH1" | wc -l) + 1 ))
i2=$(( $(grep -o "$dash" <<< "$FULL_PATH2" | wc -l) + 1 ))

# dump paths and compare them.
# output indicates differing paths/files
# output is empty if no difference
hdfs dfs -ls -R $FULL_PATH1 | cut -d/ -f${i1}- | sort > /tmp/filelist1
hdfs dfs -ls -R $FULL_PATH2 | cut -d/ -f${i2}- | sort > /tmp/filelist2
diff /tmp/filelist1 /tmp/filelist2 | grep -v .staging | grep -v 1a2,3
