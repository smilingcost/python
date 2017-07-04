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
print "downloading with requests"
start=time.time()
url = 'http://pcr1.pc6.com/rm/python2.7.zip'
r = requests.get(url)
with open("python2.7.2.zip", "wb") as code:
     code.write(r.content)
total_time = time.time() - start
print(u"总共耗时：%f 秒" % total_time)