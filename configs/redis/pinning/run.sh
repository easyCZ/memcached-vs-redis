#!/bin/bash

DIR=pinning

for i in {1..9}
do
    python ../../../benchmark/main.py \
        -type=redis \
        -server-conf=./redis.conf \
        -memtier-conf=./memtier.redis.$i.conf \
        -output=../../../results/redis/$DIR/$i/ \
        -base-port=11120 \
        -instances=$i \
        -duration=30
done
