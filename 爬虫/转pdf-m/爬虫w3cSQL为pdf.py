# coding=utf-8
import os
import re
import time
import logging
import pdfkit
import requests
from bs4 import BeautifulSoup

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
    body = soup.find_all(id="maincontent")[0]
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
    soup = BeautifulSoup(open('w3cSQL.html').read(), "html.parser")         #获取网页代码,提取所需代码到本地进行处理
    menu_tag = soup.find_all(id="course")[0]    #查找相应模块标签的代码，返回一个列表，[0]为提取列表的值，
    urls = []                                              #提取后的格式应该为网页html模式，否则无法下面无法识别
    for li in menu_tag.find_all("li"):
        url = "http://www.w3school.com.cn" + li.a.get('href')       #单个url，结果与parse_url_to_html(url, name)不相干
        urls.append(url)            #获取所以目录的url
    return urls          #所有组成的url，注意renturn应与for对齐，否则出错

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
    file_name = u"w3cSQLjc.pdf"
    urls = get_url_list()
    htmls = [parse_url_to_html(url, str(index) + ".html")   #将获取到的urls返回到parse_url_to_html，生成htmls页面内容
    for index, url in enumerate(urls)]   #enumerate函数用于遍历（urls）中的元素以及它们的下标，
    save_pdf(htmls, file_name)
    for html in htmls:
        os.remove(html)    #将生成的单个html文件删除

    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)

if __name__ == '__main__':
    main()                                    #pdf文件保存在此代码文件夹中
