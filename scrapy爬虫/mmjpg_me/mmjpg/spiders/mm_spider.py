#coding=utf-8
import scrapy
from mmjpg.items import MmjpgItem
from scrapy.http import Request
import requests
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Myspider(scrapy.Spider):
    name='mmjpg'
    allowed_domains=['mmjpg.com']
    base=r'D:/meinv/mmjpg/'


    def start_requests(self):
        #一共有6页
        for i in range(1,7):
            url='http://www.mmjpg.com/tag/meixiong/'+str(i)    #一级页面
            yield Request(url,callback=self.parse_one)


    def parse_one(self,response):    #创建一个大的list存储所有的item ，获取每个girl的个人页面
        items=[]
        pattern=re.compile(r'<span class="title"><a href="(.*?)" target="_blank">(.*?)</a></span>',re.S)
        mains=re.findall(pattern,response.text)
        for main in mains:
            #创建实例,并转化为字典
            item=MmjpgItem()
            item['siteURL']=main[0]              #每个girl的页面url，二级页面
            item['title']=main[1]
            item['fileName']=self.base+item['title']
            items.append(item)

        for item in items:
            #创建文件夹
            fileName=item['fileName']
            if not os.path.exists(fileName):
                os.makedirs(fileName)
            #用meta传入下一层
            yield Request(url=item['siteURL'],meta={'item1':item},callback=self.parse_two)



    def parse_two(self,response):  #传入上面的item1，获取每个girl页面的所有图片信息
        item2=response.meta['item1']
        source=requests.get(response.url)
        html=source.text.encode('utf-8')
        pattern=re.compile(r'</a><i></i><a href=".*?">(.*?)</a><em class="ch all" id="opic" onclick=".*?">',re.S)
        Num=re.search(pattern,html).group(1)
        items=[]
        for i in range(1,int(Num)+1):
         item=MmjpgItem()
         item['fileName']=item2['fileName']
         item['path']=item['fileName']+'/'+str(i)+'.jpg'   #构造每一个图片的存储路径
         item['pageURL']=response.url+'/'+str(i)   #构造每一个图片入口链接，以获取源码中的原图链接，三级页面，response.url[:-5]切片为选择倒数第五个之前的字符串
         items.append(item)
        for item in items:
            yield Request(url=item['pageURL'],meta={'item2':item},callback=self.parse_three)





    def parse_three(self,response):   #获取要保存的每张图片的信息
        item=MmjpgItem()
        #传入上面的item2
        item3=response.meta['item2']
        pattern=re.compile(r'<div class="content" id="content"><a href=".*?"><img src="(.*?)" alt=".*?" /></a></div>',re.S)
        URL=re.search(pattern,response.text).group(1)     #获取页面每张图片的img地址
        item['detailURL']=URL
        item['path']=item3['path']
        item['fileName']=item3['fileName']
        yield item










