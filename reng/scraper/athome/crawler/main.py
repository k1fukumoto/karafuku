import requests

r = requests.get("http://www.athome.co.jp/tochi/tokyo/list/page1")
with open('athome.html','wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

