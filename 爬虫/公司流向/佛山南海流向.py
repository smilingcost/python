# -*- coding:utf-8 -*-
# python-version: 3.51
import requests, time
from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
}


def login(email, password):
    login_url='http://www.fsnhyyjt.com/'
    #实例化出一个Firefox浏览器
    driver = webdriver.Chrome()
    #设置浏览器窗口的位置和大小
    driver.set_window_position(20, 40)
    driver.set_window_size(1100,700)
    #打开一个页面（QQ空间登录页）
    driver.get(login_url)
    driver.find_element_by_id('userId').clear()             #使用 clear 方法去清除input或者textarea元素中的内容
    driver.find_element_by_id('userId').send_keys(email)
    driver.find_element_by_id('pwd').clear()
    driver.find_element_by_id('pwd').send_keys(password)
   # time.sleep(5)
  #  driver.find_element_by_id('submit').click()    # 选择click函数还是submit函数。推荐每个都试一下，总会有一个成功的。
    print '佛山南海%s销售流向查询'%(email)
    print '佛山南海%s库存查询'%(email)
 #   exp(driver)




def main1():
    email = '7gzqx'
    password = '111111'
    login(email, password)


def main():
    x=int(raw_input('请输入序号: '))
    if x==1:
       main1()
       main()
    elif x==2:
       main()
if __name__ == '__main__':
    main()







