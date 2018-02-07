#coding=utf-8

import itchat
import time

def filehelper():
    # 发送文本消息，发送目标是“文件传输助手”
    try:
        itchat.send('Hello, filehelper', toUserName='filehelper')  #给“文件传输助手”发送一条消息
        print '发送成功！'
    except(Exception),e:
        print e

def send_frend():
    #想给谁发信息，先查找到这个朋友,name后填微信备注即可,deepin测试成功
    for i in range(0,100):
       texts=str(raw_input("请输入信息：")).decode("utf-8")    #解码输入的信息
       users = itchat.search_friends(name=u'泽霞')    #备注,微信号, 昵称
       #获取好友全部信息,返回一个列表,列表内是一个字典
      # print users
       #获取`UserName`,用于发送消息
       userName = users[0]['UserName']
       itchat.send(texts,toUserName = userName)
    #    for i in range(1,63):
    #       itchat.send_image('./headImg/1'+' ('+str(i)+').jpg',toUserName = userName)     #发送图片
    #       print '成功发送！%s'%(i)
    #       time.sleep(2)
def send_mps():
    ## 获取名字中含有特定字符的公众号，也就是按公众号名称查找,返回值为一个字典的列表
    mps = itchat.search_mps(name='CSDN')
    print mps
    #发送方法和上面一样
    userName = mps[0]['UserName']
    itchat.send("hello",toUserName = userName)

if __name__ == '__main__':
    # 登陆
    itchat.auto_login()
  #  filehelper()
    send_frend()
 #   send_mps()