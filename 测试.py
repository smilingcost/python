#coding=utf-8
import os
import re
import time
import logging
import pdfkit
import requests
import lxml.html
from bs4 import BeautifulSoup
import lxml.html

def main():

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
if __name__ == '__main__':
    main()                                    #pdf文件保存在此代码文件夹中
