#!/bin/bash

LABEL=instances
mkdir $LABEL

for i in {1..4}
do
    echo "--p 11120 --maxmemory " > $LABEL/redis.$(($i + 1)).conf

done
