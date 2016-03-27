#!/bin/bash

LABEL=instances
DATA_SIZE=64
mkdir $LABEL

for i in {1..4}
do
    echo "-s nsl200
-p 11120
--test-time=30
-c 5
-t 6
-P redis
--random-data
--data-size=64
--key-minimum=1
--key-maximum=$((10000000 / $i))" > $LABEL/memtier.redis.$i.conf

DATA_SIZE=$(($DATA_SIZE * 2))

done
