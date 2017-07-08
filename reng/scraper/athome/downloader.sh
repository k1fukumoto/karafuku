#!/bin/bash

while read url
do
  curl $url 2>/dev/null | python34 ../parser/main.py # -o ${url//\//_}
done < /dev/stdin
