# -*- encoding:utf-8 -*-

import requests
from lxml import etree
import re
import math
import datetime
import pymongo
import time
start_url='http://www.qianfanedu.cn/search.php?'
db=pymongo.MongoClient().SchoolReview
para={'mod':'forum',
'searchid':41458,
'orderby':'lastpost',
'ascdesc':'desc',
'searchsubmit':'yes',
'kw':'幼儿园怎么样',
'page' :1
}
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

def start():
    resp=requests.get(start_url,params=para,headers=headers)
    parse(resp)

def parse(resp):
    html = etree.HTML(resp.content)
    total_number=''.join([line.strip() for line in html.xpath('//h2/em/text()')])
    total_number=float(re.search('\d+',total_number).group())
    total_page=int(math.ceil(total_number/50))
    urls=html.xpath('//h3[@class="xs3"]/a/@href')
    for url in urls:
        if list(db.qf.find({'_id': url})):
            continue
        try:
            response=requests.get(url,headers=headers)
        except Exception as e:
            print e
        parse_detail(response)
        time.sleep(20)
    para['page']= para['page'] +1
    para.pop('kw','')
    if para['page']<=total_page:
        response=requests.get(start_url,params=para,headers=headers)
        parse(response)

def parse_detail(resp):
    html = etree.HTML(resp.content)
    try:
        title = html.xpath('//span[@id="thread_subject"]/text()')[0]
    except Exception as e:
        print e
        return
    address=html.xpath('//h1[@class="ts"]/a/text()')[0].strip()[1:-1]
    url = resp.url
    allcontent = html.xpath('//div[@id="postlist"]/div[contains(@id,"post_")]')
    ask_content = ' '.join([line.strip() for line in allcontent[0].xpath('.//td[@class="t_f"]/text()')])
    comments = []
    try:
        for item in allcontent[1:]:
            comment = item.xpath('.//td[@class="t_f"]/text()')
            if comment:
                comment = ' '.join([line.strip() for line in comment])
                comment_time = item.xpath('.//div[@class="authi"]/em/text()')[0].strip()[4:]
                nick_name = item.xpath('.//td[contains(@class,"pls")]//div[@class="authi"]/a/text()')[0].strip()
                img_url = item.xpath('.//div[@class="avatar"]/a/img/@src')[0]
                result = {'origin': url, 'commentTime': comment_time,
                          'fetchTime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          'content': comment, 'avatar': img_url, 'originName': '千帆', 'nickName': nick_name}
                comments.append(result)
    except Exception as e:
        print e
    db.qf.insert({'_id': url, 'title': title, 'comments': comments, 'ask_content': ask_content,'address':address})


start()