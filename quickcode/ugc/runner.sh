#!/bin/bash
g++ -O3 -march=native ./submission.cpp

index=0

mkdir output/

for filename in tests/*; do
    [ -e "$filename" ] || continue
    name=${filename##*/}

    cat $filename | ./a.out > ./output/$name
    let index=$index+1
done
