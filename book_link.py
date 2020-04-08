import json
import requests
import lxml
import os
cookies = {

}

headers = {

}

data = {

}
def changejson(thejson):
    rejosn=str(thejson['data'])
    rethejson=json.loads(rejosn)
    return rethejson
def findpas(qrCode):
    url='http://xue.bookln.cn/res/multiRes'
    thedata={
        'qrCode':qrCode
    }
    r=requests.post(url,headers=headers,cookies=cookies,data=thedata)
    r.raise_for_status()
    r.encoding='utf-8'
    thejosn=changejson(r.json())
    with open('test.txt','w',encoding='utf-8') as f:
        f.write(str(thejosn))
    thepath="booklink/"+thejosn['crName']+'/'
    if not os.path.exists(thepath):
        os.mkdir(thepath)
    for t in thejosn['ress']:
        title=t['title']+'.jpg'
        repath=thepath+title
        thumbnails=t['thumbnails']
        rpic=requests.get(thumbnails)
        with open(repath,'wb') as f:
            f.write(rpic.content)
def main():
    url="http://xue.bookln.cn/books/bookDetails"
    r=requests.post(url,headers=headers,cookies=cookies,data=data)
    print(r.url)
    r.raise_for_status()
    r.encoding='utf-8'
    thejson=r.json()
    thejson=changejson(thejson)
    all_pas=[]
    for t in thejson.get('chapters'):
        for tt in t.get('sections'):
            all_pas.append(tt['crCode'])
    all_pas=all_pas[1:]
    if not os.path.exists('booklink/'):
        os.mkdir('booklink/')
    for t in all_pas:
        findpas(t)
main()
