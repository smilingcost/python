#coding=utf-8

import requests
import sys
import time
from bs4 import BeautifulSoup
from lxml import etree
import lxml.html

def main(s_page):   #处理登陆信息

     #登录后才能访问的网页
      url = 'https://www.douyu.com/room/follow'

      #浏览器登录后得到的cookie，也就是刚才复制的字符串，浏览器不能关闭
      cookie_str = r'OUTFOX_SEARCH_USER_ID_NCOO=1891286289.35384; dy_did=8895439718030865f214d8a600021501; _dys_lastPageCode=page_studio_v,page_studio_v; _dys_refer_action_code=init_page_studio_v; dys_del_log=0d7d55d09HytC%2F%2FcHfJ1GeKmIP3FUnWkgGf6HeTxXiRM%2FevIRhVL0; acf_ditchName=uc123; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1514303637,1514305404,1514306883,1514373758; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1514376947; smidV2=201712272015474651ee321a4c21b3ca38bbca4307d69e00cf98f298c9e9c50'

      #把cookie字符串处理成字典，以便接下来使用
      cookies = {}
      for line in cookie_str.split(';'):
        key, value = line.split('=', 1)
        cookies[key] = value

      #设置请求头
      headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

      #在发送get请求时带上请求头和cookies
      html = requests.get(url, headers = headers, cookies = cookies).content
      print html
      run_lx(html)


def run_lx(html):
    print '开始爬取流向信息：'


if __name__ == '__main__':
   print '现在开始爬取内容：\n_______'
   time.sleep(1)
   s_page=raw_input("请输入需要爬取得页数：")
   star=time.time()

   main(s_page)
   last=time.time()-star
   print u'共耗时：%f 秒'%(last)
