#!/bin/bash

DIR=instances3

for i in {1..8}
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
