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
def bj_main(x):      #获取所有主播的id
  for i in range(1,4):
      postData = { 'szWhich':'talkcam',    #类型
              'nPage':i,        #页数
            'szSearch':
                       ' '
                     #  'e000e77'
                         ,     #主播id ，空为查找所有主播
              'szGender':'F'  #女生属性
                      }
      url = 'http://afevent2.afreecatv.com:8120/app/rank/api.php'
      html_session = requests.Session()
      g=html_session.post(url,data = postData,headers = header).text
      loads = demjson.decode(g)   #loads = json.loads(title)           #.decode() 函数解码 JSON 数据。该函数返回 Python 字段的数据类型,即为 u'data'
      html=json.dumps(loads, indent=4, sort_keys=False, ensure_ascii=False)     #将 Python 对象编码成 JSON 字符串
      #docs = lxml.html.fromstring(html).text
      docs = html
      names=re.findall(r'"bj_nick": "(.*?)",',docs)
      ids=re.findall(r'"bj_id": "(.*?)",',docs)
      gender_rank=re.findall(r'"gender_rank": "(.*?)"',docs)
      total_rank=re.findall(r'"total_rank": "(.*?)",',docs)
      is_live=re.findall(r'"is_broad": (.*?),',docs)
      if x==1:
          for m in range(len(ids)):
              try:
                name=names[m]
                id=ids[m]
                rank_f=gender_rank[m]
                bj_url(name,id,rank_f)
              except:
                pass
      elif x==2:
          m=0
          for ss in ids:
             if look_id==ids[m]:
                 info=[ids[m],names[m],gender_rank[m],total_rank[m],is_live[m]]
                 return  bj_find(info)
             else:
                 m+=1
                 pass

def bj_find(info):
    print 'bj_mane为：%s'%(info[1].encode('utf-8'))
    print 'bj在talk女生中排名为：%s'%(str(info[2]))
    print 'bj在talk总排名为：%s'%(str(info[3]))
    print 'bj是否在直播：-------- %s'%(str(info[4]))
    if info[4]=='true':
        print "主播开始直播了，请移至浏览器观看\直播已开始n!!!!!!!!!!!!"
        time.sleep(1)
        bj_main(x)
    else:
        print "主播没有直播哦，请继续等待吧\n!!!!!!!!!!!!"
        time.sleep(5)
        bj_main(x)

def bj_url(name,id,rank_f):       #获取需要爬虫的url
    global count  #定义全局变量
    # time.sleep(0.5)
    print '获取：---',id, '---主播信息\n'
    #  time.sleep(1)
    url='http://live.afreecatv.com:8079/app/index.cgi?szBjId='+str(id)      #主页
    bj_f_rank=rank_f
    bj_info(url,bj_f_rank)
    # time.sleep(1)
    try:
         htmls=requests.post(url,  headers = header,timeout=10).text   #用post结果相同
         num=re.findall('main_content\.cgi\?nStationNo=(.*?)&szBjId',htmls)[0]
         url_0='http://live.afreecatv.com:8079/app/main_content.cgi?nStationNo='+str(num)+'&szBjId='+str(id)
         img_id=id
         bj_img(url_0,img_id,bj_f_rank)
         time.sleep(1)
         url_1='http://stbbs.afreecatv.com/app/list_ucc.cgi?nStationNo='+str(num)+'&szBbsType=REVIEW&szBjId='+str(id)+'&nPageNo=1'   #视频url
         bj_video(url_1)
        # time.sleep(1)
         url_2='http://stbbs.afreecatv.com/app/list_bbs.cgi?nStationNo='+str(num)+'&szBjId='+str(id)+'&nPageNo=1'        #文章    url
         bj_article(url_2)
         print '主播---',id,'---信息获取完毕\n======================================================'
         print '共爬取',count,'位主播信息\n======================================================'    #如果多线程爬虫，count值可能出错
         count+=1
         time.sleep(1)
    except:
        print "获取主播页面出错！！！！！！！！！！！\n======================================================"
        pass

def  bj_info(url,bj_f_rank):   #获取主播个人信息
    #   网页编码为charset=euc-kr韩语，直接用get获取不到网页，要用请求头headers
 try:
     print '主页信息--\n',url
     header = { "User-Agent" :USER_AGENT    }
     html=requests.get(url,  headers = header,timeout=10).text   #用post结果相同
     docs = lxml.html.fromstring(html)
     logo_img_url=docs.xpath('//p[@class="logo"]/a/img/@src')[0]
     img=docs.xpath('//div[@class="header"]/p/a/img/@src')[0]
     bj_name=docs.xpath('//div[@class="user"]/text()')[0]
     bj_id=docs.xpath('//span[@class="tt"]/text()')[0]
     bj_rank_all=docs.xpath('//div[@id="myranking"]/ul/li[1]/text()')[0]
     bj_follower=docs.xpath('//div[@class="my_bs_info"]/ul[1]/li[1]/span/text()')[0]
     bj_stime=docs.xpath('//div[@class="my_bs_info"]/ul[1]/li[4]/span/text()')[0]
     bj_swatch=docs.xpath('//div[@class="my_bs_info"]/ul[1]/li[5]/span/text()')[0]
     bj_last_time=docs.xpath('//div[@class="my_bs_guest"]/ul/li[1]/span/text()')[0]
     bj_last_visit=docs.xpath('//div[@class="my_bs_guest"]/ul/li[2]/span/text()')[0]
     bj_last_up=docs.xpath('//div[@class="my_bs_guest"]/ul/li[3]/span/text()')[0]
     bj_info_bs=docs.xpath('//p[@class="info_bs"]/text()')[0]
     bj_logo_img(logo_img_url,bj_f_rank)
      #---------------------------保存主播信息----------------------------------------
     bj=str(count)+'|'+str(bj_f_rank)+'|'+bj_name.encode('utf-8')+'|'+bj_id+'|'+ bj_rank_all.encode('utf-8')+'|'+bj_follower+'|'+bj_stime+'|'+bj_swatch+'|'+bj_last_time+'|'+bj_last_visit+'|'+bj_last_up+'|'+bj_info_bs.encode('utf-8')+'|'+img+'\n'
     print '主播信息：',bj
     try:
         with open('bj.csv','a')as f:         #保存最后爬取的信息
             s=str(bj)
             f.write(s)
         print '成功保存BJ：%s 的信息\n======================================================'%(bj_name.encode('utf-8'))#韩语需进行编码
     except:
         print "BJ %s 信息保存不成功\n======================================================"%(bj_name.encode('utf-8'))
 except:
       print "bj个人信息无法获取---跳过!!!\n======================================================"
       pass

def bj_logo_img(logo_img_url,bj_f_rank):
    print '主播头像图片信息--\n',logo_img_url
    path="D:\\meinv\\afreetv\\logo_img"
    list_name = logo_img_url.split('/')       #分片
    file_name = str(bj_f_rank)+'-'+list_name[len(list_name)-1]    #取最后一个字符串
    file_path='%s/%s'%(path,file_name)
    if not os.path.exists(path):           #判断路径是否存在，不存在
                os.makedirs(path)
    if not os.path.exists(file_path):     #判断文件是否存在，存在则不爬取
      try:
         r=requests.get(logo_img_url,timeout=10)
         with open(file_path,'wb')as f:
            f.write(r.content)
            print "图片%s成功保存在：%r\n======================================================"%(file_name,path)

      except:
        print "图片%s保存不成功\n======================================================"%(file_name)
    else :
        print "logo图片已存在\n======================================================"


def bj_img(url_0,img_id,bj_f_rank):    #bj主页图片信息
     print '图片信息--\n',url_0
     html=requests.get(url_0).text   #用post结果相同
     doc = lxml.html.fromstring(html)
     img=doc.xpath('//img[@id="preImg"]/@src')
     img_path=str(bj_f_rank)+'-'+img_id
     path="D:\\meinv\\afreetv\\img\\%s"%(img_path)  #用%r，否则print "图片%s成功保存在：%s"%(file_name,path) 解析出错，或者path.encode('utf-8')人，或%r%(file_name,path)
     for i in range(len(img)):
         print img[i]
         try:
             list_name = img[i].split('/')       #分片
             file_name = list_name[len(list_name)-1]    #取最后一个字符串
             file_path='%s/%s'%(path,file_name)
             if not os.path.exists(path):           #判断路径是否存在，不存在
                os.makedirs(path)
             if not os.path.exists(file_path):
                try:
                   r=requests.get(img[i],timeout=10)
                   with open(file_path,'wb')as f:
                     f.write(r.content)
                     print "图片%s成功保存在：%r\n======================================================"%(file_name,path)

                except:
                     print "图片%s保存不成功\n======================================================"%(file_name)
             else :
                 print "图片信息已存在\n======================================================"
         except:
              i+=1
              pass

def bj_video(url_1):
    print '视频信息--\n======================================================',url_1


def bj_article(url_2):
    print '文章信息--\n======================================================',url_2



if __name__ == '__main__':
    x=int(raw_input('请输入执行的代码: \n'))

    if x==1:                 #用if 来执行不同的代码
      count=1
      try:
        bj='count'+'|'+'bj_f_rank'+'|'+'bj_name'+'|'+'bj_id'+'|'+'bj_rank_all'+'|'+'bj_follower'+'|'+'bj_stime'+'|'+'bj_swatch'+'|'+'bj_last_time'+'|'+'bj_last_visit'+'|'+'bj_last_up'+'|'+'bj_info_bs'+'|'+'img'+'\n'
        print '获取数据的字段为',bj
        with open('bj.csv','a')as f:
           s=str(bj)
           f.write(s)
        print "已写入列名>>>>"
      except:
         print "列名写入有误：请检查>>>>>\n"
      print '现在开始爬取内容：\n_______'
      time.sleep(1)
      bj_main(x)
    elif x==2:         #查询某位bj的简单信息
      #  look_id=raw_input('请输入要查询的bj的id号：\n')
        look_id='e000e77'
        bj_main(x)


