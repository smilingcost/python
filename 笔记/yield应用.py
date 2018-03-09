#coding=utf-8

import requests
import lxml.html


def h():
 for i in range(1,2):   #返回f()次数
  print 'To be brave'
  yield f()

def f():
    t=raw_input("请输入一个数：")
    if int(t)%2==0:
        print "该数为偶数"
    else:
        print "该数为奇数"
for x in h():
     print x