#coding:utf-8
import os
"""
关于用Python实现一个分布式爬虫，我曾折腾了很长一段时间，翻遍了Google十几页，和 Python 分布式 爬虫 等关键字相关的博客也就那么几篇，后来在学习Redis的时候，终于找到了实现分布式的方法。看来当现有的技术解决不了实际问题的时候，是需要学习新的技术了。

具体实现思路：利用Redis的主从数据同步，所有爬虫获取到的url都放到一个redis queue中，并且Master和Slave的爬虫都从这个redis queue中获取url。

需要用到的工具redis-py。

我有两台机器，笔记本Windows，树莓派Linux，笔记本做Master，树莓派做Slave。

爬取网站http://jandan.net/（经常写爬虫的应该不会不知道这个网站。）

以前写爬虫的时候我会把需要下载的URL放在Queue里面，而现在需要把URL放在 redis queue 中，借鉴了网上一篇博客的代码
"""
import redis  
  
class RedisQueue(object):  
    """Simple Queue with Redis Backend"""  
    def __init__(self, name, namespace='queue', **redis_kwargs):  
        """The default connection parameters are: host='localhost', port=6379, db=0"""  
        self.__db= redis.Redis(host='192.168.1.105', port=6379, db=0)  
        self.key = '%s:%s' %(namespace, name)  
  
    def qsize(self):  
        """Return the approximate size of the queue."""  
        return self.__db.llen(self.key)  
  
    def empty(self):  
        """Return True if the queue is empty, False otherwise."""  
        return self.qsize() == 0  
  
    def put(self, item):  
        """Put item into the queue."""  
        self.__db.rpush(self.key, item)  
  
    def get(self, block=True, timeout=None):  
        """Remove and return an item from the queue.  
 
        If optional args block is true and timeout is None (the default), block 
        if necessary until an item is available."""  
        if block:  
            item = self.__db.blpop(self.key, timeout=timeout)  
        else:  
            item = self.__db.lpop(self.key)  
  
        if item:  
            item = item[1]  
        return item  
  
    def get_nowait(self):  
        """Equivalent to get(False)."""  
        return self.get(False)  
    
    """
这段代码作为一个模块的形式，文件命名为RedisQueue.py，和爬虫文件放在同一个文件夹里面，具体操作和Queue差不多 

>>> from RedisQueue import RedisQueue  
>>> q = RedisQueue('test')  
>>> q.put('hello world')  
 
redis 127.0.0.1:6379> keys *  
1) "queue:test"  
redis 127.0.0.1:6379> type queue:test  
list  
redis 127.0.0.1:6379> llen queue:test  
(integer) 1  
redis 127.0.0.1:6379> lrange queue:test 0 1  
1) "hello world"  
 
>>> from RedisQueue import RedisQueue  
>>> q = RedisQueue('test')  
>>> q.get()  
'hello world' 
先用一段代码将URL放进redis queue中
"""
#coding=utf-8
from bs4 import BeautifulSoup
import urllib2
from Queue import Queue
from RedisQueue import RedisQueue
queue = Queue()
redis = RedisQueue('jandan3')
 
def user_agent(url):
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
    req_timeout = 20
    req = urllib2.Request(url,None,req_header)
    page = urllib2.urlopen(req,None,req_timeout)
    html = page
    return html
 
def next_page():
    base_url = 'http://jandan.net/ooxx/page-1006#comments'
    for i in range(3):
        html = user_agent(base_url).read()
        soup = BeautifulSoup(html)         
        next_url = soup.find('a',{'class':'next-comment-page','title':'Newer Comments'}).get('href')
        yield base_url
        base_url = next_url        
for page in next_page():
    queue.put(page)
print 'There are %d pages'%queue.qsize()
        
while not queue.empty():
    page_url = queue.get()
    html = user_agent(page_url).read()
    soup = BeautifulSoup(html)
    img_urls = soup.find_all(['img'])
    for myimg in img_urls:
        Jpgurl = myimg.get('src')
        redis.put(Jpgurl)
print 'There are %d pictures'%redis.qsize()

"""
然后在Master端可以看到：

redis 192.168.1.105:6379> keys *
1) "queue:jandan3"
redis 192.168.1.105:6379>
Slave端：

192.168.1.106:6379> keys *
1) "queue:jandan3"
192.168.1.106:6379>
现在Master和Slave都可以读取redis queue中的数据，下面的工作就是Master和Slave分别运行自己的爬虫对redis queue中的数据下载就行了。
"""
Windows爬虫代码

import urllib2
from RedisQueue import RedisQueue
redis = RedisQueue('jandan3')
 
def user_agent(url):
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
    req_timeout = 20
    req = urllib2.Request(url,None,req_header)
    page = urllib2.urlopen(req,None,req_timeout)
    html = page
    return html
 
while not redis.empty():
    down_url = redis.get()
    data = user_agent(down_url).read()
    with open('D:/Python/picture'+'/'+down_url[-11:],'wb')as code:
        code.write(data)
    print down_url

""
Linux爬虫代码：

import urllib2
from RedisQueue import RedisQueue
redis = RedisQueue('jandan3')
 
def user_agent(url):
    req_header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0'}
    req_timeout = 20
    req = urllib2.Request(url,None,req_header)
    page = urllib2.urlopen(req,None,req_timeout)
    html = page
    return html
 
while not redis.empty():
    down_url = redis.get()
    data = user_agent(down_url).read()
    with open('/mz/picture'+'/'+down_url[-11:],'wb')as code:
        code.write(data)
    print down_url


    
将这两段代码同时运行，即可对redis queue 中的URL同时下载，直到把redis queue取空为止。