# coding=utf-8
import os
import re
import time
import logging
import pdfkit
import requests
from bs4 import BeautifulSoup
import lxml.html

def parse_url_to_html(url, name):
    """
    解析URL，返回HTML内容
    :param url:解析的url
    :param name: 保存的html文件名
    :return: html
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # 正文
    body = soup.find_all(id="yui-main")[0]
    html = str(body)        #参数必须转换为缓冲区，而不是标签
      #html = html.encode("utf-8")
    with open(name, 'wb') as f:      #写入html文件
        f.write(html)
        return name

def get_url_list():
     """
     获取所有URL目录列表   ，将生成html文件保存在此代码文件夹下
     :return:
    """
     url='http://python.usyiyi.cn/documents/django_182/ref/index.html'

     response = requests.get(url)
     soup = BeautifulSoup(response.content, 'html.parser')
    # 正文
     body = soup.find_all(id="yui-main")[0]
     urls=[]
     t=body.find_all("h1")[0].span.a.get('href')
     url='http://python.usyiyi.cn/documents/django_182/ref/index.html'+t
     urls.append(url)
  # print url
     for li in body.find_all("li"):
       r='http://python.usyiyi.cn/documents/django_182/ref/'+li.a.get('href')
       title=re.findall(r'(.*?).html',li.a.get('href'))[0]
       urll(r,urls,title)
     return urls
     # print urls


def urll(r,urls,title):  #判断是否有二级连接
    print title
    urls.append(r)
  #  print r
    if 'index' in title:
       print  '有二级链接：继续获取----'
       list_name = title.split('/')
       file_name = list_name[0]
       print file_name
       try:
          html = requests.get(r).content
          doc = lxml.html.fromstring(html)
          href = doc.xpath('//li[@class="toctree-l1"]/a/@href')
          if href==[] :
              hrefs = doc.xpath('//li[@class="toctree-l1"]/span/a/@href')
              for lis in hrefs:
                  r2='http://python.usyiyi.cn/documents/django_182/ref/'+file_name+'/'+lis
               #   print r2
                  urls.append(r2)
          else:
              for li in href:
                 r1='http://python.usyiyi.cn/documents/django_182/ref/'+file_name+'/'+li
              #   print r1
                 urls.append(r1)
       except(Exception),e:
           print e
           pass
    else:
      pass
    print urls

def save_pdf(htmls, file_name):
    """
    把所有html文件保存到pdf文件
    :param htmls:  html文件列表
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    pdfkit.from_file(htmls, file_name, options=options)

def main():
    start = time.time()
    file_name = u"django-api.pdf"
    urls = get_url_list()
    htmls = [parse_url_to_html(url, str(index) + ".html")   #将获取到的urls返回到parse_url_to_html，生成htmls页面内容
    for index, url in enumerate(urls)]   #enumerate函数用于遍历（urls）中的元素以及它们的下标，
    print htmls
    save_pdf(htmls, file_name)
    for html in htmls:
        os.remove(html)    #将生成的单个html文件删除

    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)

if __name__ == '__main__':
    main()                                    #pdf文件保存在此代码文件夹中


