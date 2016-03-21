#!/bin/bash

LABEL=baseline
mkdir $LABEL

for i in {1..20}
do
    echo "-s nsl200
-p 11120
--test-time=30
-c $i
-t 2
-P redis
--random-data
--key-minimum=1
--key-maximum=100000
" > $LABEL/memtier.redis.$i.conf

done