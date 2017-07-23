# -*- coding:utf-8 -*-
#1
u'示例1'
import re
import urllib
import threading
import time
import Queue

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getUrl(html):
    reg = r"(http://.*?\.jpg!mid)"  #这是根据我要爬的图片写的正则，根据自己情况要改一下
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    return imglist

class getImg(threading.Thread):
    """
    """
    def __init__(self, q):
        threading.Thread.__init__(self)
        self.q = q

    def run(self):   #使用队列实现进程通信
        global count
        while True:
            imgurl = self.q.get()
            # print self.getName()
            urllib.urlretrieve(imgurl, '/home/pein/Pictures/%s.jpg' % count)
            print "%s.jpg done"%count
            count += 1
            if self.q.empty():
                break
            self.q.task_done()

def main():
    global mutex, count
    # url = raw_input("please input a url:\n-->")
    url = "http://girl-atlas.com/a/10130205170100000231"  #要爬的网页地址
    html = getHtml(url)
    imglist = getUrl(html)
    threads = []
    count = 0
    q = Queue.Queue()  #建立消息队列

    for i in range(len(imglist)):
        q.put(imglist[i])

    for i in range(10):
        thread = getImg(q)
        # thread.setName("%s"%i)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
main()


"""------------------------------------------------------------------------"""
u'示例2'
# -*- coding:utf-8 -*-
import time
import threading


def print_nums(s):
    for i in range(5):
        time.sleep(1)
        print "线程", s, ":", i


class MyThread(threading.Thread):
    def __init__(self, s):                     #构造函数
        threading.Thread.__init__(self)
        self.s = s

    def run(self):                             #执行函数
        print_nums(self.s)
if __name__ == "__main__":
    thread = []
    start = time.time()
    for j in range(5):
        t = MyThread(j)   #创建进程
        thread.append(t)

    for t in thread:
        t.start()       #启动线程

    for t in thread:
        t.join()       # 主线程等待子线程

    end = time.time()
    print "运行时间：", end - start, "s"


----------------------------------------------------------------------------------------------
u'示例3'
"""
程序功能大概就是爬取每个网页中的图片，并根据标题，分文件保存至指定目录，使用threading实现多线程。
主要流程为每访问一个网页，将此网页中的图片链接依次放入队列，根据图片数量依次开启下载线程，传入队列和编号，
然后启动线程开始下载，主线程查询当前正在活动的线程数量，当数量为1的时候，即只剩主线程的时候，表示所有图片下载完毕，开始下一个网页。"""
import re
import requests
from lxml import etree
import lxml.html
import os
import time
import threading

class threadDownload(threading.Thread):
    def __init__(self,que,no):
        threading.Thread.__init__(self)
        self.que = que
        self.no = no
    def run(self):
        while True:
            if not self.que.empty():
                saveImg(self.que.get(),'os'+str(self.no)+'.jpg')
            else:
                break

def saveToFile(FileName,srcList):
    a=0
    srcTuple = (srcList)
    FileName = 'os'+FileName.strip()
    res = mkdir(FileName)
    if res == False:
        return False
    #os.mkdir(FileName)
    os.chdir(FileName)
    que = Queue.Queue()
    for sl in srcList:
        que.put(sl)
    for a in range(0,srcList.__len__()):
        threadD = threadDownload(que,a)
        threadD.start()
        #print threading.enumerate()
    while threading.active_count() != 0:
        if threading.active_count() == 1:
            print FileName+"  is Done"
            return True

def saveImg(imgUrl,fileName):
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'
    headers = {'User-Agent':user_agent}
    try:
        req = urllib2.Request(imgUrl,headers=headers)
        res = urllib2.urlopen(req,timeout=5)
        data = res.read()
    except socket.timeout as e:
        print "saveImgTimeOut"
        return False
    f = open(fileName,'wb')
    f.write(data)
    f.close()


----------------------------------------------------------------------------------------------
u'示例4'
# -*- coding: UTF-8 -*-

import Queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"