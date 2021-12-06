#!/bin/bash

mkdir output/

echo "0" >./output/compilation-result

printf "#!/bin/bash \n python3 ./submission" > ./helper.sh
chmod +x ./helper.sh

for filename in tests/*; do
  [ -e "$filename" ] || continue
  name=${filename##*/}

  (/usr/bin/time -f'%S' ./helper.sh <"$filename" >./output/"$name") 2>./output/"$name"-time
done