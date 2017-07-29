# coding=utf-8
import urllib
import time
print "downloading with urllib"
url = 'http://pcr1.pc6.com/rm/python2.7.zip'
start=time.time()
urllib.urlretrieve(url, "python2.7.zip")
total_time = time.time() - start
print(u"总共耗时：%f 秒" % total_time)

import urllib2
import time
print "downloading with urllib2"
url = 'http://pcr1.pc6.com/rm/python2.7.zip'
f = urllib2.urlopen(url)
start=time.time()
with open("python2.7.1.zip", "wb") as code:
    code.write(f.read())
total_time = time.time() - start
print(u"总共耗时：%f 秒" % total_time)


import requests
import time
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0'  #模拟浏览器，有些需要才能下载
print "downloading with requests"
start=time.time()
url = 'http://pcr1.pc6.com/rm/python2.7.zip'
r = requests.get(url)
with open("python2.7.2.zip", "wb") as code:
     code.write(r.content)
total_time = time.time() - start
print(u"总共耗时：%f 秒" % total_time)


#coding=utf-8
import requests
import time
import urllib

#判断网页是否可用，然后进行递归重新下载
url =  'http://videofile-hls-ko-vod-cf.afreecatv.com/video/_definst_/mp4:highlight/20161218/355/9ACAE219_186261355_1_1_A.mp4/media_w2116937822_.ts'
r = requests.get(url)
filename="w2116937822_.ts"

def auto_down(url,filename):
    try:
        print r.status_code  #返回响应状态码
        print r.raise_for_status()  #抛出异常
        urllib.urlretrieve(url,filename)
        time.sleep(0.5)
    except :
        print 'url解析错误，将重新进行下载>>>'
        time.sleep(0.5)
        auto_down(url,filename)
print auto_down(url,filename)