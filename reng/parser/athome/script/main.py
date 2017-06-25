from bs4 import BeautifulSoup

# import requests
# r = requests.get("http://www.athome.co.jp/tochi/tokyo/list")
#              headers={'User-Agent': user_agent})

import sys,codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

with codecs.open('athome.html','r','utf-8') as f:
    soup = BeautifulSoup(f.read(),"html.parser")

for p in soup.find_all('div',attrs={'class':'object-detail'}):
    row = []

    try:
        for location in p.find('li',attrs={'class':'info-trans'}).find_all('span'):
            row.append(u' '.join(location.text.strip().split()))
        row.append(p.find('li',attrs={'class':'info-time'}).text.strip())
        row.append(p.find('li',attrs={'class':'info-price'}).find('span').text)
        row.append(p.find('li',attrs={'class':'info-floor'}).find('span').text)
        for ratio in p.find('li',attrs={'class':'info-percent'}).find_all('span'):
            row.append(ratio.text)
    except:
        True
#        print u"PARSE ERROR:" + id

    print u','.join(row)
