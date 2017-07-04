#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html
import os

def url_1(n):                                #定义爬取得页数
       urls1=[]
       for i in range(1,n+1):
          url = 'http://www.kzj365.com/category-9-b0-min0-max0-page-'+str(i)+'-default-DESC-pre2.html'
          print url
          yield url_2(url)     #将url返回给url_2(url)，yield在python内部是当作list处理的



def url_2(url):      #定义爬取的数据
    html = requests.get(url).content
    doc = lxml.html.fromstring(html)
    href = doc.xpath('//div[@class="goodsInfo"]/a/@href')
    m=0
    for ss in href:
      urls='http://www.kzj365.com/'+href[m]    #获取页面每个产品的url
      print urls
      htmls = requests.get(urls).content      #开始解析二级页面
      docs = lxml.html.fromstring(htmls)           #或page = etree.HTML(html)
      titles = docs.xpath('//div[@class="jqzoom"]/img/@alt')
      price=docs.xpath('//div[@class="gi-pinfo"]/div[2]/span[1]/b/text()')
      img = docs.xpath('//div[@class="jqzoom"]/img/@data-url')
      i=0
      for rr in titles:                          #保存文本
        results = titles[i]+','+price[i]+','+img[i]+'\n'  #/n 进行换行
        print results
        b=str(results)
        with open('lxml_1.csv','a') as f:
         f.write(b)

        p_url=img[i]               #保存图片
        r = requests.get(p_url)                #图片名称
        list_name = img[i].split('/')
        file_name = list_name[len(list_name)-1]            #分割取最后一组数据
        path="D:\\meinv\\kzj"
        file_path='%s/%s'%(path,file_name)
        if not os.path.exists(path):        #判断路径是否存在，不存在
           os.makedirs(path)            #就创建路径file_path
        print 'file_path',file_path
        with open(file_path,'wb') as code:
           code.write(r.content)


        i += 1
      f.close()
      m+=1
if __name__ == '__main__':
    page=raw_input("请输入页数： ")
    for yy in url_1(int(page)):    #将page转化为整数，生成器要用for循环打印出，即是将函数赋予一个变量才可以进行遍历
       print yy