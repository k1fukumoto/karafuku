#!/usr/bin/env python34

from bs4 import BeautifulSoup
import sys
import re

soup = BeautifulSoup(sys.stdin.buffer.read(),"lxml")
cnt = 0

try:
    p = soup.find('meta',attrs={'property':'og:url'})
    if p is None:
        sys.exit()
    propid = p['content']

    for p in soup.find_all('div',attrs={'class':'thumb-view'}):
        for img in p.find_all('img'):
            print(",".join([img['src'],propid]))
        
except Exception as e:
    sys.stderr.write("parser_land.py PARSE ERROR AT LINE {}".format(cnt) + str(e))
cnt = cnt + 1

