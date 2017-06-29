from bs4 import BeautifulSoup
import sys

# with open('athome.html','rb') as fd:
soup = BeautifulSoup(sys.stdin.buffer.read(),"lxml")

cnt = 0
for p in soup.find_all('div',attrs={'data-bukken-no':True}):
    cols = [p['data-bukken-no']]
    try:
        for location in p.find('li',attrs={'class':'info-trans'}).find_all('span'):
            cols.append(' '.join(location.text.strip().split()))
        cols.append(p.find('li',attrs={'class':'info-time'}).text.strip())
        cols.append(p.find('li',attrs={'class':'info-price'}).find('span').text)
        cols.append(p.find('li',attrs={'class':'info-floor'}).find('span').text)
        for ratio in p.find('li',attrs={'class':'info-percent'}).find_all('span'):
            cols.append(ratio.text)
    except:
        print("PARSE ERROR AT LINE " + str(cnt))

    cnt = cnt + 1
    s = u','.join(cols) + u'\n'
    sys.stdout.buffer.write(bytes(s,'utf-8'))

