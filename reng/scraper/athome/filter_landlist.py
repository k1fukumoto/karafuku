#!/usr/bin/env python34

import sys, io
import csv

ios = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

def print_line(s):
    sys.stdout.buffer.write(bytes(s+'\n','utf-8'))

#with open(sys.argv[1],encoding='utf-8') as f:

reader = csv.DictReader(ios,fieldnames=['id','station','line','addr',
                                          'tts','price','floor','ratio1','ratio2','url'])
for row in reader:
    if(row['tts'] != "-" and int(row['tts']) <= 10 and
       row['floor'] != "-" and float(row['floor'].replace(',','')) >=100 and
       row['ratio2'] != "-" and int(row['ratio2'].replace('%','')) >=200 and
       row['addr'] != "-" and (row['addr'].find('区') >=0 or row['addr'].find('ＪＲ中央線') >=0)):
        print_line(row['url'])

