#!/usr/bin/env python34
import io,sys,csv

ios = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

def pr(s):
    sys.stdout.buffer.write(bytes(s+'\n','utf-8'))


pr('<html><body><ul>')

reader = csv.DictReader(ios,fieldnames=['image','land'])
for row in reader:
    pr('<li><a href={}><img src={}/></a></li>'.format(row['land'],row['image']))

pr('</ul></body></html>')
