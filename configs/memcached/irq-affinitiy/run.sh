#!/bin/bash

DIR=irq-affinity

for i in {1..10}
do
    python ../../../benchmark/main.py \
        -type=memcached \
        -server-conf=./memcached.$i.conf \
        -memtier-conf=./memtier.memcached.conf \
        -output=../../../results/memcached/$DIR/$i/ \
        -base-port=11120 \
        -instances=1 \
        -duration=30
done

git add ../../../
git commit -m "Memcached Threads Results"
git push
