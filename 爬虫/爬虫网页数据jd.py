#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html
import os
def url_1(n):                                #定义爬取得页数
      for i in range(1,n+1):
          url = 'https://list.jd.com/list.html?cat=9192,12632&page='+str(i)+'&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
          print url
          yield url_2(url)     #将url返回给url_2(url)，yield在python内部是当作list处理的


def url_2(url):
  html = requests.get(url).content
  doc = lxml.html.fromstring(html)
  href = doc.xpath('//div[@class="p-name"]/a/@href')   #获取页面商品页面url
  i=0
  for ss in href:                       #
     urls='https:'+href[i]
     print urls
     htmls = requests.get(urls).content
     docs = lxml.html.fromstring(htmls)           #或page = etree.HTML(html)
     titles = docs.xpath('//li[@class="img-hover"]/img/@alt')
     pic_url = docs.xpath('//li[@class="img-hover"]/img/@src')
     m=0
     for rr in titles:
        results = titles[m]+','+'https:'+pic_url[m]+'\n'  #/n 进行换行
        print results
        b=str(results)
        with open('lxml_2.csv','a') as f:              #保存文本
          f.write(b)

        p_url='https:'+pic_url[m]               #保存图片
        r = requests.get(p_url)
        list_name = pic_url[m].split('/')
        file_name = list_name[len(list_name)-1]            #图片名称
        path="D:\\meinv\\jd"
        file_path='%s/%s'%(path,file_name)
        if not os.path.exists(path):
           os.makedirs(path)
        print 'file_path',file_path
        with open(file_path,'wb') as code:
           code.write(r.content)

        m+= 1
     f.close()
     i+=1
if __name__ == '__main__':
    page=raw_input("请输入页数： ")
    for yy in url_1(int(page)):    #将page转化为整数，生成器要用for循环打印出，即是将函数赋予一个变量才可以进行遍历
       print yy