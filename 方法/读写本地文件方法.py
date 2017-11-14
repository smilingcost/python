#-*- coding:utf-8 -*-
import requests
import re
r=open('sta.txt')
x=r.read()
z1=re.findall('([A-Z]+)\|([a-z]+)',x) #中文名称加u
print z1

from bs4 import BeautifulSoup
soup = BeautifulSoup(open('w3cSQL.html'))
print soup.prettify()

import urllib2
response = urllib2.urlopen('https://www.douban.com/doulist/1264675/?start=25&sort=seq&sub_type=')
html = response.read()
f=open('douban.txt','wb')
f.write(html)
print html         #写入文件

#r或rt 默认模式，文本模式读
#rb   二进制文件

#w或wt 文本模式写，打开前文件存储被清空
#wb  二进制写，文件存储同样被清空

#a  追加模式，只能写在文件末尾
#a+ 可读写模式，写只能写在文件末尾

#w+ 可读写，与a+的区别是要清空文件内容
#r+ 可读写，与a+的区别是可以写到文件任何位置
"""
读写模式的类型有：

rU 或 Ua 以读方式打开, 同时提供通用换行符支持 (PEP 278)
w     以写方式打开，
a     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+     以读写模式打开
w+     以读写模式打开 (参见 w )
a+     以读写模式打开 (参见 a )
rb     以二进制读模式打开
wb     以二进制写模式打开 (参见 w )
ab     以二进制追加模式打开 (参见 a )
rb+    以二进制读写模式打开 (参见 r+ )
wb+    以二进制读写模式打开 (参见 w+ )
ab+    以二进制读写模式打开 (参见 a+ )"""