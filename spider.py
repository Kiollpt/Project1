from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import requests
import shutil
import urllib.request
import os
import json
import spider_sql
import spider_mongodb

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url1='http://www.ptt.cc/bbs/Beauty/index.html'
res= requests.get(url1,verify=False)

soup=BeautifulSoup(res.text,"html.parser")
r_rent =soup.find_all('div','r-ent')
articles=[]
for i in r_rent:
    count=0

    try:
        count=int(i.find('div','nrec').string)

    except:
        pass

    if(count>=5):
        title=i.find('div','title')
        tag_a=title.contents[1]

        articles.append({
            'liked': count,
            'tilte':tag_a.string,
            'href': tag_a['href']
        })
print(articles)
url2='http://www.ptt.cc'
pic_formate=['.jpg','.jpeg','png']

for article in articles:
    res1=requests.get(url2+article['href'],verify=False)

    if res1:
        soup=BeautifulSoup(res1.text,"html.parser")
        tag_a =soup.find_all('a',rel='nofollow')
        for img_href in tag_a:
            pic=img_href['href']
            if('.jpg' in pic):
                fname=pic.split('/')[-1]
                f =open(fname, 'wb')
                res3=requests.get(pic,stream=True,verify=False)
                shutil.copyfileobj(res3.raw,f)
                f.close()
                del res3

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, indent=2, sort_keys=True, ensure_ascii=False)

spider_sql.run_sql()
spider_mongodb.run_mongo()
