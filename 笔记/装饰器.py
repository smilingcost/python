#coding=utf-8

import time

def outer(func):
    def log():
        for x in range(0,10):
           print x
           time.sleep(1)
           func(x)  # func是参数，此时 func 等于 f1
    return log  # 返回的 log，log代表的是函数，非执行函数

@outer
def f1(x):
    print '函数f1=%s'%(x)+'\n'


print f1()


