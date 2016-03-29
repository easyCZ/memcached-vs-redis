#!/bin/bash

DIR=zipf

for i in {1..5}
do
    python ../../../benchmark/main.py \
        -type=memcached \
        -server-conf=./memcached.conf \
        -memtier-conf=./memtier.memcached.$i.conf \
        -output=../../../results/memcached/$DIR/$i/ \
        -base-port=11120 \
        -instances=1 \
        -duration=30
done

