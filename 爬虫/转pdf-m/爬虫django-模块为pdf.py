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
     url='http://python.usyiyi.cn/documents/django_182/py-modindex.html#cap-a'
     urls=[]
     urls.append(url)
     response = requests.get(url)
     for i in range(7,232):
        body =re.findall(r'class="yiyi-st" id="yiyi-%s"><a href="(.*?)"><tt class="xref"'%(str(i)),response.text)
        if body==[]:
          pass
        else:
          r='http://python.usyiyi.cn/documents/django_182/'+str(body[0])
          print r
          urls.append(r)
     return urls

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
    file_name = u"django-模块.pdf"
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


