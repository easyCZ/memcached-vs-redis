#!/bin/bash
#!/bin/bash

DIR=object-size
for i in {1..14}
do
    python ../../../benchmark/main.py \
        -type=redis \
        -server-conf=./redis.conf \
        -memtier-conf=./memtier.redis.$i.conf \
        -output=../../../results/redis/$DIR/$i/ \
        -base-port=11120 \
        -instances=6 \
        -duration=60
done
