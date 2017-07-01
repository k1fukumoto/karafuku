from bs4 import BeautifulSoup
import sys
import re

soup = BeautifulSoup(sys.stdin.buffer.read(),"lxml")

cnt = 0
for p in soup.find_all('div',attrs={'data-bukken-no':True}):
    cols = [p['data-bukken-no']]
    try:
        locs = p.find('li',attrs={'class':'info-trans'}).find_all('span')

        # train line & station
        m = re.search(r'(.+)\/(.+)',locs[0].text)
        if m:
            cols.append(m.group(1))
            cols.append(m.group(2))
        else:
            cols.append('-')
            cols.append(locs[0].text)
        # address
        cols.append(' '.join(locs[1].text.strip().split()))

        # time to station
        m = re.search(r'(\d+)',p.find('li',attrs={'class':'info-time'}).text)
        if m:
            cols.append(m.group(1))
        else:
            cols.append('-')

        # price
        price = p.find('li',attrs={'class':'info-price'}).find('span').text
        m1 = re.search(r'(\d)[^\d]([\d,]+)',price) # more than 1 okuen
        m2 = re.search(r'([\d,]+)',price)
        if m1:
            cols.append(m1.group(1)+m1.group(2))
        elif m2:
            cols.append(m2.group(1))
        else:
            cols.append('-')

        # floor space
        m = re.search(r'([\d,\.]+)',p.find('li',attrs={'class':'info-floor'}).find('span').text)
#        cols.append(p.find('li',attrs={'class':'info-floor'})
        if m:
            cols.append(m.group(1))
        else:
            cols.append('-')

        # land/capacity ratios
        for ratio in p.find('li',attrs={'class':'info-percent'}).find_all('span'):
            cols.append(ratio.text)

        # link to property
        cols.append("https://www.athome.co.jp/tochi/{}".format(cols[0]))
        
    except Exception as e:
        print("PARSE ERROR AT LINE " + str(e))

    cols = map(lambda x: '"{}"'.format(x), cols)

    cnt = cnt + 1
    s = u','.join(cols) + u'\n'
    sys.stdout.buffer.write(bytes(s,'utf-8'))

