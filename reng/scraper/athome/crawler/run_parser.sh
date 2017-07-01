#!/bin/bash

for f in *.html
do 
  cat $f | python34 ../parser/main.py
done
