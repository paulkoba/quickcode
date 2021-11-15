#!/bin/bash

mkdir output/

if g++ -O3 -march=native ./submission.cpp; then
  echo "$?" >./output/compilation-result
else
  echo "$?" >./output/compilation-result

  for filename in tests/*; do
    name=${filename##*/}
    touch ./output/"$name"
    touch ./output/"$name"-time
  done

  exit 0
fi

for filename in tests/*; do
  [ -e "$filename" ] || continue
  name=${filename##*/}

  (/usr/bin/time -f'%S' ./a.out <"$filename" >./output/"$name") 2>./output/"$name"-time
done
