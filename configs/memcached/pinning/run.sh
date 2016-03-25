#!/bin/bash

DIR=pinning

for i in {1..10}
do
    python ../../../benchmark/main.py \
        -type=memcached \
        -server-conf=./memcached.$i.conf \
        -memtier-conf=./memtier.memcached.conf \
        -output=../../../results/memcached/$DIR/$i/ \
        -base-port=11120 \
        -instances=1 \
        -duration=30 \
        -pin=true
done
