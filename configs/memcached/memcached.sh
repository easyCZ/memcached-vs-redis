#!/bin/bash

LABEL=threads

mkdir $LABEL

for i in {1..12}
do
    echo "-d
-p 11120
-m 6144
-t $i" > $LABEL/memcached.$i.conf
done
