#!/bin/bash

DIR=baseline

for i in {1..20}
do
    python ../../../benchmark/main.py \
        -type=redis \
        -server-conf=./redis.conf \
        -memtier-conf=./memtier.redis.$i.conf \
        -output=../../../results/redis/$DIR/$i/ \
        -base-port=11120 \
        -instances=1 \
        -duration=30
done
