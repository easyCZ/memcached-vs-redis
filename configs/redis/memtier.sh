#!/bin/bash

LABEL=zipf
STDDEV=10
mkdir $LABEL

for i in {1..6}
do
    echo "-s nsl200
-p 11120
--test-time=30
-c 5
-t 1
-P redis
--random-data
--key-minimum=1
--data-size=64
--key-maximum=10000000
--key-pattern=G:G
--key-stddev=$STDDEV
--key-median=1" > $LABEL/memtier.redis.$i.conf

STDDEV=$(($STDDEV * 10))

done
