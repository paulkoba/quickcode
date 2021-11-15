#!/bin/bash
g++ -O3 -march=native ./submission.cpp

mkdir output/

for filename in tests/*; do
    [ -e "$filename" ] || continue
    name=${filename##*/}

    < "$filename" ./a.out > ./output/"$name"
done
