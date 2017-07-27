#coding=utf-8
import os
import json
import re
import requests
import demjson
from lxml import etree
import lxml.html
import time

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2716.5 Safari/537.36'
header = { "User-Agent" :USER_AGENT  }             #定义开头
count=0
def bj_main():      #获取所有主播的id
  for i in range(1,8):
      postData = { 'szWhich':'star',    #类型
              'nPage':i,        #页数
            'szSearch':
                       ''
                    #   'e000e77'
                         ,     #主播id ，空为查找所有主播
              'szSType':'A'
                      }
      url = 'http://afevent2.afreecatv.com:8120/app/rank/api.php'
      html_session = requests.Session()
      g=html_session.post(url,data = postData,headers = header).text
      loads = demjson.decode(g)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
      html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
      docs = lxml.html.fromstring(html).text
      names=re.findall(r'"bj_nick": "(.*?)",',docs)
      ids=re.findall(r'"bj_id": "(.*?)",',docs)
      sexs=re.findall(r'"sex": "(.*?)",',docs)
      for m in range(len(ids)):
          name=names[m]
          id=ids[m]
          sex=sexs[m]
          bj_url(name,id,sex)


def bj_url(name,id,sex):       #获取需要爬虫的url
      global count  #定义全局变量
      if sex=='F':
         print '是女生，开始爬取>>>>>>\n'
        # time.sleep(0.5)
         print '获取：---',id, '---主播信息\n'
       #  time.sleep(1)
         url='http://live.afreecatv.com:8079/app/index.cgi?szBjId='+str(id)      #主页
         bj_info(url)
        # time.sleep(1)
         htmls=requests.post(url,  headers = header).text   #用post结果相同
         num=re.findall('main_content\.cgi\?nStationNo=(.*?)&szBjId',htmls)[0]
         url_0='http://live.afreecatv.com:8079/app/main_content.cgi?nStationNo='+str(num)+'&szBjId='+str(id)
         img_id=id
         bj_img(url_0,img_id)
         time.sleep(1)
         url_1='http://stbbs.afreecatv.com/app/list_ucc.cgi?nStationNo='+str(num)+'&szBbsType=REVIEW&szBjId='+str(id)+'&nPageNo=1'   #视频url
         bj_video(url_1)
        # time.sleep(1)
         url_2='http://stbbs.afreecatv.com/app/list_bbs.cgi?nStationNo='+str(num)+'&szBjId='+str(id)+'&nPageNo=1'        #文章    url
         bj_article(url_2)
         print '主播---',id,'---信息获取完毕\n'
         print '共爬取',count,'位主播信息'    #如果多线程爬虫，count值可能出错
         count+=1
         time.sleep(1)
      else:
          print '不是女生哦，跳过吧！！！！！'
        #  time.sleep(0.5)
          pass

def bj_info(url):   #获取主播个人信息
     #   网页编码为charset=euc-kr韩语，直接用get获取不到网页，要用请求头headers
     print '主页信息--\n',url
     header = { "User-Agent" :USER_AGENT    }
     html=requests.get(url,  headers = header).text   #用post结果相同
     docs = lxml.html.fromstring(html)
     img=docs.xpath('//div[@class="header"]/p/a/img/@src')[0]
     bj_name=docs.xpath('//div[@class="user"]/text()')[0]+docs.xpath('//div[@class="user"]/span/text()')[0]
     bj_id=docs.xpath('//span[@class="tt"]/text()')[0]
     bj_follower=docs.xpath('//div[@class="my_bs_info"]/ul[1]/li[1]/span/text()')[0]
     bj_stime=docs.xpath('//div[@class="my_bs_info"]/ul[1]/li[4]/span/text()')[0]
     bj_swatch=docs.xpath('//div[@class="my_bs_info"]/ul[1]/li[5]/span/text()')[0]
     bj_last_time=docs.xpath('//div[@class="my_bs_guest"]/ul/li[1]/span/text()')[0]
     bj_last_visit=docs.xpath('//div[@class="my_bs_guest"]/ul/li[2]/span/text()')[0]
     bj_last_up=docs.xpath('//div[@class="my_bs_guest"]/ul/li[3]/span/text()')[0]
      #---------------------------保存主播信息----------------------------------------
     bj=str(count)+'|'+bj_name.encode('utf-8')+'|'+bj_id+'|'+bj_follower+'|'+bj_stime+'|'+bj_swatch+'|'+bj_last_time+'|'+bj_last_visit+'|'+bj_last_up+'|'+img+'\n'
     print '主播信息：',bj
     try:
         with open('bj.csv','a')as f:         #保存最后爬取的信息
             s=str(bj)
             f.write(s)
         print '成功保存BJ：%s 的信息\n'%(bj_name.encode('utf-8'))#韩语需进行编码
     except:
         print "BJ %s 信息保存不成功\n"%(bj_name.encode('utf-8'))


def bj_img(url_0,img_id):    #bj主页图片信息
     print '图片信息--\n',url_0
     html=requests.get(url_0).text   #用post结果相同
     doc = lxml.html.fromstring(html)
     img=doc.xpath('//img[@id="preImg"]/@src')
     img_path=img_id+'-'+str(count)
     path="D:\\meinv\\afreetv\\img\\%s"%(img_path)  #用%r，否则print "图片%s成功保存在：%s"%(file_name,path) 解析出错，或者path.encode('utf-8')人，或%r%(file_name,path)
     for i in range(len(img)):
         print img[i]
         try:
             list_name = img[i].split('/')       #分片
             file_name = list_name[len(list_name)-1]    #取最后一个字符串
             file_path='%s/%s'%(path,file_name)
             if not os.path.exists(path):           #判断路径是否存在，不存在
                os.makedirs(path)
             try:
                 r=requests.get(img[i])
                 with open(file_path,'wb')as f:
                   f.write(r.content)
                   print "图片%s成功保存在：%r\n"%(file_name,path)

             except:
                 print "图片%s保存不成功\n"%(file_name)
         except:
              i+=1
              pass

def bj_video(url_1):
    print '视频信息--\n',url_1


def bj_article(url_2):
    print '文章信息--\n',url_2


if __name__ == '__main__':
   # bj_names=raw_input('爬取的主播：\n')
    count=1
    try:
      bj='count'+'|'+'bj_name'+'|'+'bj_id'+'|'+'bj_follower'+'|'+'bj_stime'+'|'+'bj_swatch'+'|'+'bj_last_time'+'|'+'bj_last_visit'+'|'+'bj_last_up'+'|'+'img'+'\n'
      print '获取数据的字段为',bj
      with open('bj.csv','a')as f:
           s=str(bj)
           f.write(s)
      print "已写入列名>>>>"
    except:
       print "列名写入有误：请检查>>>>>\n"
    print '现在开始爬取内容：\n_______'
    time.sleep(1)
    bj_main()

