#!/bin/bash

LABEL=zipf
STDDEV=10
mkdir $LABEL

for i in {1..5}
do
    echo "-s nsl200
-p 11120
--test-time=30
-c 5
-t 6
-P memcache_binary
--random-data
--key-minimum=1
--data-size=64
--key-maximum=10000000
--key-pattern=G:G
--key-stddev=$STDDEV
--key-median=2" > $LABEL/memtier.memcached.$i.conf

STDDEV=$(($STDDEV * 10))

done
