#coding=utf-8
import redis
import time

r = redis.Redis(host='192.168.1.114', port=6379,db=0)
r.set('name', 'zhangsan')   #添加
print r.get('name')   #获取


