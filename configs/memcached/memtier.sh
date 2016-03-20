#!/bin/bash

LABEL=baseline
DATA_SIZE=2
mkdir $LABEL

for i in {1..19}
do
    echo "-s nsl200
-p 11120
--test-time=30
-c $i
-t 3
-P memcache_binary
--random-data
--key-minimum=1
--key-maximum=10000000" > $LABEL/memtier.memcached.$i.conf

DATA_SIZE=$(($DATA_SIZE * 2))

done
