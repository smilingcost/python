# -*- coding: utf-8 -*-
import scrapy
import re
from www80s.items import Www80SItem
import requests
from scrapy.http import Request


class www80sSpider(scrapy.Spider):
    name = "www80s"
    #allowed_domains = ["http://www.80s.tw/movie/list/"]

    start_urls = [
        'http://www.80s.tw/movie/list/'     #爬取得第一页
    ]
    def parse(self, response):

        selector = scrapy.Selector(response)
        books = selector.xpath('//ul[@class="me1 clearfix"]/li') #提取第一页属性中的所有li，组成数组
        page1=books.xpath('./h3/a/@href')                 #提取页面电影子链接
        for urls in page1:          #遍历所有子链接
          urls1=urls.extract()
          connect = 'http://www.80s.tw'+str(urls1)     #重新定义的链接只能通过回调给函数，不能直接在def中使用
          yield scrapy.http.Request(connect,callback=self.parse1)  #将子链接依次传递给回调函数parse1，每次一个链接回调

        page=int(selector.xpath('//div[@class="pager"]/strong/text()').extract()[0])   #获取当前页面的页数值
        pages=page+1                                                               #数值加1为下一页
        nextPage = 'http://www.80s.tw/movie/list/-----p'+str(pages)
        if nextPage:
                   print nextPage
                   yield scrapy.http.Request(nextPage,callback=self.parse)  #将附加数据（下一页的url）传递给回调函数parse，




    def parse1(self,response):
                 item = Www80SItem()
                 tow_url = scrapy.Selector(response)
                 each=tow_url.xpath('//div[@class="info"]')   #对子链接进行处理

                 title = each.xpath('./h1/text()').extract()[0]    #[]是将获取到的lis转化为字符串
                 score = each.xpath('./div[2]/span[1]/text()').extract()[2]   #根据实际输出的选择对应的list数据
                 time= each.xpath('./div[1]/span[7]/text()').extract()[0]

                 each2=tow_url.xpath('//div[@class="formatblock3-left"]')
                 connect_url = each2.xpath('//span[@class="xunlei dlbutton1"]/a/@href').extract()

                 title = title.replace(' ','')  #使用前必需将title的list转化为字符串，将空格替换掉
                 score = score.replace(' ','')
                 item['title'] = title
                 item['score'] = score
                 item['time'] = time
                 item['connect_url'] = connect_url
                  # print 'time:' + score
                  # print connect_url
                  # print ''
                 yield item
