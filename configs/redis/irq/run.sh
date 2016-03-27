#!/bin/bash

DIR=irq

python ../../../benchmark/main.py \
    -type=redis \
    -server-conf=./redis.1.conf \
    -memtier-conf=./memtier.redis.1.conf \
    -output=../../../results/redis/irq/1/ \
    -base-port=11120 \
    -instances=1 \
    -duration=30

python ../../../benchmark/main.py \
    -type=redis \
    -server-conf=./redis.2.conf \
    -memtier-conf=./memtier.redis.2.conf \
    -output=../../../results/redis/irq/2/ \
    -base-port=11120 \
    -instances=2 \
    -duration=30

python ../../../benchmark/main.py \
    -type=redis \
    -server-conf=./redis.3.conf \
    -memtier-conf=./memtier.redis.3.conf \
    -output=../../../results/redis/irq/3/ \
    -base-port=11120 \
    -instances=3 \
    -duration=30

python ../../../benchmark/main.py \
    -type=redis \
    -server-conf=./redis.4.conf \
    -memtier-conf=./memtier.redis.4.conf \
    -output=../../../results/redis/irq/4/ \
    -base-port=11120 \
    -instances=6 \
    -duration=30
