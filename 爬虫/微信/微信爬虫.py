#coding=utf-8

import itchat
import numpy as np
import pandas as pd
from collections import defaultdict
import re
import jieba
import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import PIL.Image as Image
import demjson
import json

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
def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable


def friend_info():
    #调用函数得到各变量，并把数据存到csv文件中，保存到桌面
    print '好友信息'
    NickName = get_var("NickName")
    Sex = get_var('Sex')
    Province = get_var('Province')
    City = get_var('City')
    Signature = get_var('Signature')
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

def main(friends,mps):
    i=0
    for a  in friends:
       print friends[i]
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

if __name__ == '__main__':
    itchat.login()
    friends = itchat.get_friends(update=True)[0:] #爬取自己好友相关信息， 返回一个json文件
    mps = itchat.get_mps(update=True)[0:]  #爬取公众号相关信息， 返回一个json文件
    main(friends,mps)
   # friend()
 #   friend_info()