#!/bin/bash

LABEL=object-size
DATA_SIZE=64
mkdir $LABEL

for i in {1..14}
do
    echo "-s nsl200
-p 11120
--test-time=60
-c 7
-t 3
-P memcache_binary
--random-data
--data-size=$DATA_SIZE
--key-minimum=1
--key-maximum=$((10000000 / $i))" > $LABEL/memtier.memcached.$i.conf

DATA_SIZE=$(($DATA_SIZE * 2))

done
