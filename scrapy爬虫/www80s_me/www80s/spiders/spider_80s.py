# -*- coding: utf-8 -*-
import scrapy
import re
from www80s.items import Www80SItem
import requests
from scrapy.http import Request

class www80sSpider(scrapy.Spider):
    name = "www80s"
    #allowed_domains = ["http://www.80s.tw/movie/list/"]
    #def start_requests(self):
        #一共有6页
    #    for i in range(1,7): #遍历条件的url，如果满足条件，继续爬取
    #        url='http://www.80s.tw/movie/list/-----p'+str(i)
     #       yield Request(url,callback=self.parse)  ——————  此方法遍历是为无序抓取
    start_urls = [
        'http://www.80s.tw/movie/list/'
    ]
    def parse(self, response):
        #print response.body
        item = Www80SItem()
        selector = scrapy.Selector(response)
        books = selector.xpath('//ul[@class="me1 clearfix"]/li') #提取属性中的所有li，组成数组

        for each in books:    #遍历所有li
            title = each.xpath('./h3/a/text()').extract()[0]
            score = each.xpath('./a/span[2]/text()').extract()
            connect_url = each.xpath('./h3/a/@href').extract()
            title = title.replace(' ','')  #使用前必需将title的list转化为字符串
            #connect_url = connect_url.replace(' ','').replace('\n','')
            item['title'] = title
            item['score'] = score
            item['connect_url'] = connect_url
            # print 'time:' + score
           # print connect_url
            #print ''
            yield item
            page=int(selector.xpath('//div[@class="pager"]/strong/text()').extract()[0])   #获取当前页面的页数值
            pages=page+1   #数值加1为下一页
            nextPage = 'http://www.80s.tw/movie/list/-----p'+str(pages)
            if nextPage:
                print nextPage
                yield scrapy.http.Request(nextPage,callback=self.parse)  #将附加数据传递给回调函数parse