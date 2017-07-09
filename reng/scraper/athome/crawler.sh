#!/bin/bash

cnt=0

download_and_parse() {
    while read url
    do
	curl $url 2>/dev/null | \
	    ./parser_landlist.py | \
	    ./filter_landlist.py | \
	    download_land | \
	    ./parser_land.py
    done < /dev/stdin
}

download_land() {
    while read url
    do
	curl $url # -o ${url//\//_}.html
    done < /dev/stdin
}

load_and_parse() {
    for f in *[0-9].html
    do
	cat $f | ./parser_land.py | ./indexgen_image.py
	exit
    done
}


if [ -n "$TEST" ]; then
    load_and_parse
else
    download_and_parse | ./indexgen_image.py | tee /var/www/html/index.html
fi


# download_jpeg() {
#     while read line
#     do
# 	download_jpeg_one $line
#     done < /dev/stdin
# }

# download_jpeg_one() {
#     curl $1 -o .archive/${2//\//_}$cnt.jpeg
#     ((cnt++))
# }

