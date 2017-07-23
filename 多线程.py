#coding=utf-8
import threading
from time import ctime,sleep


def music(func):
    for i in range(100):
        print "I was listening to %s. %s" %(func,ctime())
        sleep(1)

def move(func):
    for i in range(100):
        print "I was at the %s! %s" %(func,ctime())
        sleep(1)

threads = []
t1 = threading.Thread(target=music,args=(u'hello 你好',))    #创建了threads数组，创建线程t1，# target: 要执行的方法；name: 线程名；args/kwargs: 要传入方法的参数。
threads.append(t1)                        #把创建好的线程t1装到threads数组中
t2 = threading.Thread(target=move,args=(u'word 世界',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:    #for循环遍历数组。（数组被装载了t1和t2两个线程）
        t.setDaemon(True) #设置是后台线程，将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
        t.start()        #开始线程活动。
    t.join()  #join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
    print "all over %s" %ctime()

"""
# -*- coding: UTF-8 -*-

import time, threading

# 假定这是你的银行存款:
balance = 0
def change_it(n):
  # 先存后取，结果应该为0:
  global balance
  balance = balance + n
  balance = balance - n
#  print "%s %s %s: %s" % ('balance',balance, n, time.ctime(time.time()) )

def run_thread(n):
  for i in range(100000):
    change_it(n)

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance,t1.getName()
"""