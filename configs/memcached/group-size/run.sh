#!/bin/bash

DIR=group-size

for i in {1..16}
do
    python ../../../benchmark/main.py \
        -type=memcached \
        -server-conf=./memcached.$i.conf \
        -memtier-conf=./memtier.conf \
        -output=../../../results/memcached/$DIR/$i/ \
        -base-port=11120 \
        -instances=1 \
        -duration=30
done