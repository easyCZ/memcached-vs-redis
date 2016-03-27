#!/bin/bash

DIR=object-size-30

for i in {1..14}
do
    python ../../../benchmark/main.py \
        -type=memcached \
        -server-conf=./memcached.conf \
        -memtier-conf=./memtier.memcached.$i.conf \
        -output=../../../results/memcached/$DIR/$i/ \
        -base-port=11120 \
        -instances=1 \
        -duration=60 \
        -pin=true
done
