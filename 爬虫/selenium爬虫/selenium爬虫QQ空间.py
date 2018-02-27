#coding=utf-8
from selenium import webdriver
import requests
import time


def main(login_url):
    #实例化出一个Firefox浏览器
    driver = webdriver.Chrome()
    #设置浏览器窗口的位置和大小
    driver.set_window_position(20, 40)
    driver.set_window_size(1100,700)
    #打开一个页面（QQ空间登录页）
    driver.get(login_url)
    #登录表单在页面的框架中，所以要切换到该框架
    driver.switch_to.frame('login_frame')
    #通过使用选择器选择到表单元素进行模拟输入和点击按钮提交
    driver.find_element_by_id('switcher_plogin').click()
    driver.find_element_by_id('u').clear()             #使用 clear 方法去清除input或者textarea元素中的内容
    driver.find_element_by_id('u').send_keys('3127006878')
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys('****')
    driver.find_element_by_id('login_button').click()    # 选择click函数还是submit函数。推荐每个都试一下，总会有一个成功的。
    time.sleep(10)                     #等待Cookies完全加载，很重要
    qq_kj(driver)
    time.sleep(10)
    driver.quit()      #退出窗口

def  qq_kj(driver):
    url ='https://user.qzone.qq.com/3127006878'                      #driver.current_url     #验证登录成功与否，若currenturl发生变化，则认为登录成功：
    cookies = driver.get_cookies()   #调出Cookies
  #  print cookies
    req = requests.Session()
    for cookie in cookies:
        req.cookies.set(cookie['name'],cookie['value'])
    headers = {'User-agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
    test = req.get(url,headers = headers)
    print test.content



if __name__ == '__main__':
    login_url='http://qzone.qq.com'
    main(login_url)

