#coding=utf-8

import itchat
import numpy as np
import pandas as pd
import re
import os
import matplotlib.pyplot as plt
import PIL.Image as Image
import demjson
import json
import time
import math

def friend():
    #初始化计数器
    male = female = other = 0
    #friends[0]是自己的信息，所以要从friends[1]开始
    for i in friends[1:]:
      sex = i["Sex"]
      if sex == 1:
          male += 1
      elif sex == 2:
          female += 1
      else:
          other +=1
    #计算朋友总数
    total = len(friends[1:])
    print '你的好友总数：%s'%(total)
    #打印出自己的好友性别比例
    print "男性好友：%s"%(male)+ "\n" +"女性好友：%s"%(female)+ "\n" +"不明性别好友：%s"%(other)+ "\n"
    print"男性好友： %.2f%%" % (float(male)/total*100) + "\n" +"女性好友： %.2f%%" % (float(female) / total * 100) + "\n" +"不明性别好友： %.2f%%" % (float(other) / total * 100)
    df_friends = pd.DataFrame(friends)
    Sex = df_friends.Sex
   # Sex_count = get_count(Sex )
    Sex_count = Sex.value_counts() #defaultdict(int, {0: 31, 1: 292, 2: 245}) #pandas为Series提供了一个value_counts()方法，可以更方便统计各项出现的次数
    Sex_count.plot(kind = 'bar')
    plt.show()

#定义一个函数，用来爬取各个变量
def get_friends(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


def friend_info():
    #调用函数得到各变量，并把数据存到csv文件中，保存到桌面
    print '好友信息'
    NickName = get_friends("NickName")
    Sex = get_friends('Sex')
    Province = get_friends('Province')
    City = get_friends('City')
    Signature = get_friends('Signature')
    i=0
    for a in NickName:
       if int(Sex[i])==int('1'):
           sex='男'
       elif int(Sex[i])==int('2'):
           sex='女'
       else:
           sex='未知'
       try:
          Signatures=Signature[i]
       except:
          Signatures=''
       data="%s,%s,%s,%s,%s"%(NickName[i].encode("utf-8"),sex,Province[i].encode("utf-8"),City[i].encode("utf-8"),Signatures.encode("utf-8"))
       count=i+1
       print '第%s位好友信息：'%(count),data
       print '--------------------------'
       i+=1
       time.sleep(0.2)

#定义一个函数，用来爬取各个变量
def get_mps(var):
    variable = []
    for i in mps:
        value = i[var]
        variable.append(value)
    return variable

def mps_info():
    #调用函数得到各变量，并把数据存到csv文件中，保存到桌面
    print '公众号信息'
    NickName = get_mps("NickName")
    Province = get_mps('Province')
    City = get_mps('City')
    Signature = get_mps('Signature')
    i=0
    for a in NickName:
       try:
          Signatures=Signature[i]
       except:
          Signatures=''
       data="%s,%s,%s,%s"%(NickName[i].encode("utf-8"),Province[i].encode("utf-8"),City[i].encode("utf-8"),Signatures.encode("utf-8"))
       count=i+1
       print '第%s个公众号信息：'%(count),data
       print '--------------------------'
       i+=1
       time.sleep(0.2)

def main(friends,mps):
    i=0
    for a  in mps:
      # print friends[i]
       print mps[i]
   # title1=re.findall(r'User: (.*)>]',str(friends))[0]
   # title2=re.findall(r'MassivePlatform: (.*)>]',str(mps))[0]

    with open('friends.json','a')as f:         #保存最后爬取的信息
           s=str(friends)
           f.write(s)
    print '成功保存！'
    with open('mps.json','a')as f:         #保存最后爬取的信息
           s=str(mps)
           f.write(s)
    print '成功保存！'


def img_friend():
    print '拼接头像：'
    #下载所有好友的头像图片
    num = 0
    files=[]
    for i in friends:
      img = itchat.get_head_img(i["UserName"])
      user =itchat.search_friends(userName=i["UserName"])
    #  print user
      file_name=user['NickName']   #获取微信好友昵称
      path="./headImg"
      file_path='%s/%s'%(path,file_name)
      files.append(file_path)    #将图片标题保存在元祖里，拼接图片时引用
      if not os.path.exists(path):        #判断路径是否存在，不存在
           os.makedirs(path)            #就创建路径file_path
      with open(file_path + ".jpg",'wb') as f:
        f.write(img)
        f.close()
        num += 1
      time.sleep(0.2)
      print '成功保存图像：%s.jpg'%(file_path.encode("utf-8"))
    #获取文件夹内的文件个数
   # print files
    length = len(os.listdir('./headImg'))
    #根据总面积求每一个的大小
    each_size = int(math.sqrt(float(810*810)/length))
    #每一行可以放多少个
    lines = int(810/each_size)
    #生成白色背景新图片
    image = Image.new('RGBA', (810, 810),'white')
    x = 0
    y = 0
    for i in range(0,length):
      try:
         img = Image.open(files[i] + ".jpg")
      except IOError:
         print(i)
         print("Error")
      else:
         img = img.resize((each_size, each_size), Image.ANTIALIAS) #缩放图片
         image.paste(img, (x * each_size, y * each_size))     #将缩放的图片黏贴到白色背景上面，x，y为横纵坐标的相对位置，即图片放置的位置
         x += 1
         if x == lines:
           x = 0
           y += 1
    image.save("all.jpg")
    print '图片合并完成！'
    time.sleep(0.1)
    #通过文件传输助手发送到自己微信中
    itchat.send_image( "all.jpg",'filehelper')
    print '发送完成！'
    time.sleep(0.3)
    image.show()


if __name__ == '__main__':
    itchat.login()
    friends = itchat.get_friends(update=True)[0:] #爬取自己好友相关信息， 返回一个json文件
    mps = itchat.get_mps(update=True)[0:]  #爬取公众号相关信息， 返回一个json文件
   # main(friends,mps)
    friend()
    friend_info()
    mps_info()
    img_friend()