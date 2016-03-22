#!/bin/bash

DIR=threads-coalesce-off

for i in {1..12}
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
