# coding=utf-8
import os
import re
import time
import logging
import pdfkit
import requests
from bs4 import BeautifulSoup

html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>

"""


def parse_url_to_html(url, name):
    """
    解析URL，返回HTML内容
    :param url:解析的url
    :param name: 保存的html文件名
    :return: html
    """
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # 正文
        body = soup.find_all(class_="rst-content")[0]
        # 标题
        title = soup.find('h1').get_text()

        # 标题加入到正文的最前面，居中显示
        center_tag = soup.new_tag("center")
        title_tag = soup.new_tag('h2')
        title_tag.string = title
        center_tag.insert(1, title_tag)
        body.insert(1, center_tag)
        html = str(body)          #参数必须转换为缓冲区，而不是标签
        # body中的img标签的src相对路径的改成绝对路径
        pattern = "(<img .*?src=\")(.*?)(\")"

        def func(m):
            if not m.group(3).startswith("http"):
                rtn = m.group(1) + "http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0" + m.group(2) + m.group(3)
                return rtn
            else:
                return m.group(1)+m.group(2)+m.group(3)
        html = re.compile(pattern).sub(func, html)
        html = html_template.format(content=html)
                                                        #上面为保存img标签，可以去除
      #html = html.encode("utf-8")
        with open(name, 'wb') as f:     #写入文件：wb或w
            f.write(html)
        return name

    except Exception as e:

        logging.error("解析错误", exc_info=True)


def get_url_list():
    """
    获取所有URL目录列表   ，将生成html文件保存在此代码文件夹下
    :return:
    """
    soup = BeautifulSoup(open('beautifulsoup.html'),"lxml")         #获取网页代码,提取所需代码到本地进行处理
    menu_tag = soup.find_all(class_="local-toc")[0]    #查找相应模块标签的代码，返回一个列表，[0]为提取列表的值，
    urls = []                                              #提取后的格式应该为网页html模式，否则无法下面无法识别
    for li in menu_tag.find_all("li"):
        url = "http://beautifulsoup.readthedocs.io/zh_CN/v4.4.0" + li.a.get('href')       #单个url
        urls.append(url)            #获取所以目录的url
        return urls         #所有组成的url，注意renturn应与for对齐，否则出错（在里面只循环一次）


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
    urls = get_url_list()
    file_name = u"BeautifulSoup4.4.0.pdf"
    htmls = [parse_url_to_html(url, str(index) + ".html")
             for index, url in enumerate(urls)]   #enumerate函数用于遍历（urls）中的元素以及它们的下标，
    save_pdf(htmls, file_name)                                                                #生成单个html文件

    for html in htmls:
        os.remove(html)    #将生成的单个html文件删除

    total_time = time.time() - start
    print(u"总共耗时：%f 秒" % total_time)


if __name__ == '__main__':
    main()                                    #pdf文件保存在此代码文件夹中
