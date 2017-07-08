#!/bin/bash

URLBASE="https://www.athome.co.jp/tochi/tokyo/list/page"
STARTPAGE=$1
ENDPAGE=$2

eval echo ${URLBASE}{$STARTPAGE..$ENDPAGE} | xargs -n1
