#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html
import os
import time
import threading

def url_1(n):                                #定义爬取得页数
       urls=[]
       for i in range(1,n+1):
          url = 'http://www.kzj365.com/category-9-b0-min0-max0-page-'+str(i)+'-default-DESC-pre2.html'
          print url
          urls.append(url)
       return urls


def url_2(url):      #定义爬取的数据
    html = requests.get(url).content
    doc = lxml.html.fromstring(html)
    href = doc.xpath('//div[@class="goods-lists clearfix"]/ul/li/a/@href')
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
    star=time.time()
    for url in url_1(int(page)):
        t = threading.Thread(target=url_2(url),args=(url,))    #创建了threads数组，创建线程t1，# target: 要执行的方法；name: 线程名；args/kwargs: 要传入方法的参数。
        t.start()        #开始线程活动。
    t.join()  #join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
    end=time.time()-star
print '文件下载完成,耗时：%f秒'%(end)
