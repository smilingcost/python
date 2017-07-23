#coding=utf-8
import requests
import time
import os
import threading
from time import ctime,sleep

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36'
def auto_down(file_name,file_path,r,start):
    try:
       # print r.status_code        #返回响应状态码
        r.raise_for_status()         #抛出异常
        time.sleep(0.2)
        with open(file_path, "wb") as code:
          code.write(r.content)
        total_time = time.time() - start
        print file_name,u"总共耗时：%f 秒" % total_time
    except :
        time.sleep(1)
        print 'url解析错误，将重新进行下载>>>'

        afree(url)
def afree(url):
 try:
    start=time.time()
    r = requests.get(url) #设置超时时间，防止程序假死，即超过时间时执行下次循环
    list_name = url.split('/')       #分片
    file_name = list_name[len(list_name)-1]     #取最后一个字符串
    path="D:\\meinv\\afree"
    file_path='%s/%s'%(path,file_name)
    if not os.path.exists(path):           #判断路径是否存在，不存在
     os.makedirs(path)
    auto_down(file_name,file_path,r,start)
 except:
     pass


def urlu():
     urls=[]
     for i in range(0 ,10):
       url= 'http://videofile-hls-ko-vod-cf.afreecatv.com/video/_definst_/mp4:vod/20170714/881/70BF265D_194105881_1.mp4/media_w2133732653_'+str(i)+'.ts'
       urls.append(url)
     return urls

if __name__=='__main__':
    print "开始下载文件>>>>>\n"
    for url in urlu():
       t = threading.Thread(target=afree,args=(url,))    #创建了threads数组，创建线程t1，# target: 要执行的方法；name: 线程名；args/kwargs: 要传入方法的参数。
       t.start()        #开始线程活动。
    t.join()  #join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。
print '文件下载完成'


