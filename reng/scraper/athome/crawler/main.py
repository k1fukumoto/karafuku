import requests
import re

URLBASE = "http://www.athome.co.jp/tochi/tokyo/list/page{}"

for i in range(1,11):
    url = URLBASE.format(i)
    print ("Get {}...".format(url))
    r = requests.get(url)

    fname = url.replace('/','_') + '.html'
    with open(fname,'wb') as fd:
        for chunk in r.iter_content(chunk_size=128):
            fd.write(chunk)

