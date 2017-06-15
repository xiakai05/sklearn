# -*- encoding:utf-8 -*-

import requests
from lxml import etree
import pymongo
import datetime
db=pymongo.MongoClient().SchoolReview
session=requests.session()
headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
start_url='http://jzb.com/bbs/sh/'
search_url='http://jzb.com/bbs/search.php?'
base_url='http://jzb.com/bbs/'
data = {'mod': 'forum',
        'fid': 0,
        'hashCode': '',
        'srchtxt': '幼儿园怎么样',
        'searchsubmit': 'true',
        'page': 1}
def start(url):
    resp = session.get(start_url)
    parse(resp)

def parse(resp) :
    html = etree.HTML(resp.content)
    hashcode = html.xpath('//input[@name="hashCode"]/@value')
    data['hashCode']=hashcode
    response=session.post(search_url,data=data,headers=headers)
    parse_list(response)

def parse_list(resp):
    html = etree.HTML(resp.content)
    url=html.xpath('//h3[@class="title1"]/a/@href')
    for detail_url in url:
        detail_url=base_url+detail_url
        if list(db.jzb.find({'_id':detail_url})):
            continue
        response=session.get(detail_url)
        parse_detail(response)
    hashcode = html.xpath('//input[@name="hashCode"]/@value')[0]
    data['hashCode']=hashcode
    data['page']=data['page']+1
    if data['page']<=17:
        response_list=session.post(search_url,data=data,headers=headers)
        parse_list(response_list)


def parse_detail(resp):
    html = etree.HTML(resp.content)
    title=html.xpath('//a[@id="thread_subject"]/@title')[0]
    url=resp.url
    allcontent=html.xpath('//table[@summary]')
    ask_content=''.join([line.strip() for line in allcontent[0].xpath('.//td[@class="t_f"]/text()')])
    comments=[]
    try:
        for item in allcontent[1:]:
            comment= item.xpath('.//td[@class="t_f"]/text()')
            if comment:
                comment=comment[0].strip()
                comment_time=item.xpath('.//div[@class="eduu_rept_rt"]/em/text()')[0].strip()
                nick_name=item.xpath('.//a[contains(@class,"Tt_ifo_name")]/text()')[0].strip()
                img_url=item.xpath('.//div[contains(@class,"avatar z eduu_pr")]/a/img/@src')[0]
                result={'origin':url,'commentTime':comment_time,'fetchTime':datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'content':comment,'avatar':img_url,'originName':'家长帮','nickName':nick_name}
                comments.append(result)
    except Exception as e:
        print e
    db.jzb.insert({'_id':url,'title':title,'comments':comments,'ask_content':ask_content})
start(start_url)