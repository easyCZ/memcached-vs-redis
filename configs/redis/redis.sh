#!/bin/bash

LABEL=baseline
mkdir $LABEL

for i in {1..10}
do
    echo "--p 11120" > $LABEL/redis.$(($i + 1)).conf

done
