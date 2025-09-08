#!/bin/bash

duration=10
bar_length=30

echo -n "["

for ((i=0; i<=bar_length; i++));
do
        sleep_time=$(echo "$duration / $bar_length" | bc -l)
        sleep $sleep_time
        echo -n "#"
done
echo "]"
echo "Chargement terminé"
