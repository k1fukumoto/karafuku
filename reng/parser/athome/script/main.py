from bs4 import BeautifulSoup
import re

# import requests
# r = requests.get("http://www.athome.co.jp/tochi/tokyo/list/page")
#              headers={'User-Agent': user_agent})

import sys,codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

with codecs.open('athome.html','r','utf-8') as f:
    soup = BeautifulSoup(f.read(),"lxml")

for p in soup.find_all('div',attrs={'data-bukken-no':True}):
    cols = [p['data-bukken-no']]
    cnt = 0
    try:
        for location in p.find('li',attrs={'class':'info-trans'}).find_all('span'):
            cols.append(' '.join(location.text.strip().split()))
        cols.append(p.find('li',attrs={'class':'info-time'}).text.strip())
        cols.append(p.find('li',attrs={'class':'info-price'}).find('span').text)
        cols.append(p.find('li',attrs={'class':'info-floor'}).find('span').text)
        for ratio in p.find('li',attrs={'class':'info-percent'}).find_all('span'):
            cols.append(ratio.text)
    except:
        print "PARSE ERROR:" + str(cnt)

    cnt += 1
    print ','.join(cols)
