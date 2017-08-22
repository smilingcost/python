#coding=utf-8

import re
import requests
from lxml import etree
import lxml.html
import os
import redis
import time

headers={ 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36' }

def push_redis_list(n):
      r = redis.Redis(host='192.168.1.114', port=6379,db=0)
      print r.keys('*')           # KEYS * 匹配数据库中所有 key
      for i in range(1,n+1):#定义爬取得页数
          url = 'https://list.jd.com/list.html?cat=9192,12632&page='+str(i)+'&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main'
          print url
          push_redis_lists(url,r)
          time.sleep(0.5)

def push_redis_lists(url,r):
  html = requests.get(url,headers=headers).content
  doc = lxml.html.fromstring(html)
  href = doc.xpath('//div[@class="p-name"]/a/@href')   #获取页面商品页面url
  i=0
  for ss in href:                       #
     urls='https:'+href[i]
   #  print urls
     htmls = requests.get(urls).content
     docs = lxml.html.fromstring(htmls)           #或page = etree.HTML(html)
     pic_url = docs.xpath('//li[@class="img-hover"]/img/@src')
     m=0
     for rr in  pic_url:
        p_url='https:'+pic_url[m]
        l = len(re.findall('limg',p_url))
        print l
        if(l == 0):
                print "url: ",p_url
                r.lpush('jd',p_url)     #在name对应的list中添加元素，每个新的元素都添加到列表的最左边
        m+= 1
     print r.llen('jd')  # name对应的list元素的个数
     print '---------------------------------------'
     i+=1
  return 0

def get_big_img_url():
    r = redis.Redis(host='192.168.1.114', port=6379,db=0)
    print r.keys('*')
    while (1):
      try:
            url = r.lpop('jd')  # 在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
            download(url,r)
            time.sleep(1)
            print url,r.llen('jd')
            list=r.llen('jd')
            if int(list)==int('0'):
                break
      except:
            print "请求求发送失败重试"
            time.sleep(10)
            pass
    return 0
def download(url,r):
  list=r.llen('jd')   # name对应的list元素的个数
  if int(list)>=int('0'):
     try:                   #保存图片
        html = requests.get(url,headers=headers)
        list_name = url.split('/')
        file_name = list_name[len(list_name)-1]            #图片名称
        path="D:\\meinv\\jd"
        file_path='%s/%s'%(path,file_name)
        if not os.path.exists(path):           #判断路径是否存在，不存在
           os.makedirs(path)                     #就创建路径file_path
        print 'file_path',file_path
        with open(file_path,'wb') as code:
            code.write(html.content)
        code.close()
        print '成功保存图片---------\n剩余url个数：',r.llen('jd')
     except Exception,e:
        print Exception,":",e
  else:
      return 0
if __name__ == '__main__':
    page=raw_input("请输入页数： ")
    push_redis_list(int(page))#开启则加任务队列。不过是用于计算页码的
    get_big_img_url()#开启则运行爬取任务
    print '爬虫结束'