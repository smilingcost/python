#coding=utf-8

import os
"""
1、String 操作

　　redis中的String在在内存中按照一个name对应一个value来存储

set()

复制代码
#在Redis中设置值，默认不存在则创建，存在则修改
r.set('name', 'zhangsan')
'''参数：
     set(name, value, ex=None, px=None, nx=False, xx=False)
     ex，过期时间（秒）
     px，过期时间（毫秒）
     nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
     xx，如果设置为True，则只有name存在时，当前set操作才执行'''
复制代码
setex(name, value, time)
#设置过期时间（秒）

psetex(name, time_ms, value)
#设置过期时间（豪秒）
mset()

#批量设置值
r.mset(name1='zhangsan', name2='lisi')
#或
r.mget({"name1":'zhangsan', "name2":'lisi'})
get(name)

　　获取值

mget(keys, *args)

#批量获取
print(r.mget("name1","name2"))
#或
li=["name1","name2"]
print(r.mget(li))
getset(name, value)

#设置新值，打印原值
print(r.getset("name1","wangwu")) #输出:zhangsan
print(r.get("name1")) #输出:wangwu
getrange(key, start, end)

#根据字节获取子序列
r.set("name","zhangsan")
print(r.getrange("name",0,3))#输出:zhan
setrange(name, offset, value)

#修改字符串内容，从指定字符串索引开始向后替换，如果新值太长时，则向后添加
r.set("name","zhangsan")
r.setrange("name",1,"z")
print(r.get("name")) #输出:zzangsan
r.setrange("name",6,"zzzzzzz")
print(r.get("name")) #输出:zzangszzzzzzz
setbit(name, offset, value)

复制代码
#对二进制表示位进行操作
''' name:redis的name
    offset，位的索引（将值对应的ASCII码变换成二进制后再进行索引）
    value，值只能是 1 或 0 '''

str="345"
r.set("name",str)
for i in str:
    print(i,ord(i),bin(ord(i)))#输出 值、ASCII码中对应的值、对应值转换的二进制
'''
输出:
    3 51 0b110011
    4 52 0b110100
    5 53 0b110101'''

r.setbit("name",6,0)#把第7位改为0，也就是3对应的变成了0b110001
print(r.get("name"))#输出：145
复制代码
getbit(name, offset)

#获取name对应值的二进制中某位的值(0或1)
r.set("name","3") # 对应的二进制0b110011
print(r.getbit("name",5))   #输出:0
print(r.getbit("name",6))   #输出:1
bitcount(key, start=None, end=None)

#获取对应二进制中1的个数
r.set("name","345")#0b110011 0b110100 0b110101
print(r.bitcount("name",start=0,end=1)) #输出:7
''' key:Redis的name
    start:字节起始位置
    end:字节结束位置'''
strlen(name)

#返回name对应值的字节长度（一个汉字3个字节）
r.set("name","zhangsan")
print(r.strlen("name")) #输出:8
incr(self, name, amount=1)

#自增mount对应的值，当mount不存在时，则创建mount＝amount，否则，则自增,amount为自增数(整数)
print(r.incr("mount",amount=2))#输出:2
print(r.incr("mount"))#输出:3
print(r.incr("mount",amount=3))#输出:6
print(r.incr("mount",amount=6))#输出:12
print(r.get("mount")) #输出:12
incrbyfloat(self, name, amount=1.0)

#类似 incr() 自增,amount为自增数(浮点数)
decr(self, name, amount=1)

#自减name对应的值,当name不存在时,则创建name＝amount，否则，则自减，amount为自增数(整数)
append(name, value)

#在name对应的值后面追加内容
r.set("name","zhangsan")
print(r.get("name"))    #输出:'zhangsan
r.append("name","lisi")
print(r.get("name"))    #输出:zhangsanlisi
 

2、Hash 操作

redis中的Hash 在内存中类似于一个name对应一个dic来存储 

 hset(name, key, value)

#name对应的hash中设置一个键值对（不存在，则创建，否则，修改）
r.hset("dic_name","a1","aa")
hget(name,key)

r.hset("dic_name","a1","aa")
#在name对应的hash中根据key获取value
print(r.hget("dic_name","a1"))#输出:aa
hgetall(name)

#获取name对应hash的所有键值
print(r.hgetall("dic_name"))
hmset(name, mapping)

#在name对应的hash中批量设置键值对,mapping:字典
dic={"a1":"aa","b1":"bb"}
r.hmset("dic_name",dic)
print(r.hget("dic_name","b1"))#输出:bb
hmget(name, keys, *args)

# 在name对应的hash中获取多个key的值
li=["a1","b1"]
print(r.hmget("dic_name",li))
print(r.hmget("dic_name","a1","b1"))
hlen(name)、hkeys(name)、hvals(name)

复制代码
dic={"a1":"aa","b1":"bb"}
r.hmset("dic_name",dic)

#hlen(name) 获取hash中键值对的个数
print(r.hlen("dic_name"))

#hkeys(name) 获取hash中所有的key的值
print(r.hkeys("dic_name"))

#hvals(name) 获取hash中所有的value的值
print(r.hvals("dic_name"))
复制代码
hexists(name, key)

#检查name对应的hash是否存在当前传入的key
print(r.hexists("dic_name","a1"))#输出:True
hdel(name,*keys)

#删除指定name对应的key所在的键值对
r.hdel("dic_name","a1")
hincrby(name, key, amount=1)

#自增hash中key对应的值，不存在则创建key=amount(amount为整数)
print(r.hincrby("demo","a",amount=2))
hincrbyfloat(name, key, amount=1.0)

#自增hash中key对应的值，不存在则创建key=amount(amount为浮点数)
 

hscan(name, cursor=0, match=None, count=None)

 

hscan_iter(name, match=None, count=None)

 

3、List 操作

redis中的List在在内存中按照一个name对应一个List来存储 

lpush(name,values)

# 在name对应的list中添加元素，每个新的元素都添加到列表的最左边
r.lpush("list_name",2)
r.lpush("list_name",3,4,5)#保存在列表中的顺序为5，4，3，2
rpush(name,values)

#同lpush，但每个新的元素都添加到列表的最右边
lpushx(name,value)

#在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边
rpushx(name,value)

#在name对应的list中添加元素，只有name已经存在时，值添加到列表的最右边
llen(name)

# name对应的list元素的个数
print(r.llen("list_name"))
linsert(name, where, refvalue, value))

复制代码
# 在name对应的列表的某一个值前或后插入一个新值
r.linsert("list_name","BEFORE","2","SS")#在列表内找到第一个元素2，在它前面插入SS

'''参数：
     name: redis的name
     where: BEFORE（前）或AFTER（后）
     refvalue: 列表内的值
     value: 要插入的数据'''
复制代码
r.lset(name, index, value)

#对list中的某一个索引位置重新赋值
r.lset("list_name",0,"bbb")
r.lrem(name, value, num)

复制代码
#删除name对应的list中的指定值
r.lrem("list_name","SS",num=0)

''' 参数：
    name:  redis的name
    value: 要删除的值
    num:   num=0 删除列表中所有的指定值；
           num=2 从前到后，删除2个；
           num=-2 从后向前，删除2个'''
复制代码
lpop(name)

#移除列表的左侧第一个元素，返回值则是第一个元素
print(r.lpop("list_name"))
lindex(name, index)

#根据索引获取列表内元素
print(r.lindex("list_name",1))
lrange(name, start, end)

#分片获取元素
print(r.lrange("list_name",0,-1))
ltrim(name, start, end)

#移除列表内没有在该索引之内的值
r.ltrim("list_name",0,2)
rpoplpush(src, dst)

# 从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
#src 要取数据的列表
#dst 要添加数据的列表
brpoplpush(src, dst, timeout=0)

#同rpoplpush，多了个timeout, timeout：取数据的列表没元素后的阻塞时间，0为一直阻塞
r.brpoplpush("list_name","list_name1",timeout=0)
blpop(keys, timeout)

复制代码
#将多个列表排列,按照从左到右去移除各个列表内的元素
r.lpush("list_name",3,4,5)
r.lpush("list_name1",3,4,5)

while True:
    print(r.blpop(["list_name","list_name1"],timeout=0))
    print(r.lrange("list_name",0,-1),r.lrange("list_name1",0,-1))

'''keys: redis的name的集合
   timeout: 超时时间，获取完所有列表的元素之后，阻塞等待列表内有数据的时间（秒）, 0 表示永远阻塞'''
复制代码
r.brpop(keys, timeout)

#同blpop，将多个列表排列,按照从右像左去移除各个列表内的元素
 

4、Set 操作

Set集合就是不允许重复的列表

sadd(name,values)

#给name对应的集合中添加元素
r.sadd("set_name","aa")
r.sadd("set_name","aa","bb")
smembers(name)

#获取name对应的集合的所有成员
scard(name)

#获取name对应的集合中的元素个数
r.scard("set_name")
sdiff(keys, *args)

#在第一个name对应的集合中且不在其他name对应的集合的元素集合
r.sadd("set_name","aa","bb")
r.sadd("set_name1","bb","cc")
r.sadd("set_name2","bb","cc","dd")

print(r.sdiff("set_name","set_name1","set_name2"))#输出:｛aa｝
sdiffstore(dest, keys, *args)

#相当于把sdiff获取的值加入到dest对应的集合中
sinter(keys, *args)

# 获取多个name对应集合的并集
r.sadd("set_name","aa","bb")
r.sadd("set_name1","bb","cc")
r.sadd("set_name2","bb","cc","dd")

print(r.sinter("set_name","set_name1","set_name2"))#输出:｛bb｝
sinterstore(dest, keys, *args)

#获取多个name对应集合的并集，再讲其加入到dest对应的集合中
sismember(name, value)

#检查value是否是name对应的集合内的元素
smove(src, dst, value)

#将某个元素从一个集合中移动到另外一个集合
spop(name)

#从集合的右侧移除一个元素，并将其返回
srandmember(name, numbers)

# 从name对应的集合中随机获取numbers个元素
print(r.srandmember("set_name2",2))
srem(name, values)

#删除name对应的集合中的某些值
print(r.srem("set_name2","bb","dd"))
sunion(keys, *args)

#获取多个name对应的集合的并集
r.sunion("set_name","set_name1","set_name2")
sunionstore(dest,keys, *args)

#获取多个name对应的集合的并集，并将结果保存到dest对应的集合中
有序集合：

　　在集合的基础上，为每元素排序，元素的排序需要根据另外一个值来进行比较，所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。

zadd(name, *args, **kwargs)

# 在name对应的有序集合中添加元素
r.zadd("zset_name", "a1", 6, "a2", 2,"a3",5)
#或
r.zadd('zset_name1', b1=10, b2=5)
zcard(name)

#获取有序集合内元素的数量
zcount(name, min, max)

#获取有序集合中分数在[min,max]之间的个数
print(r.zcount("zset_name",1,5))
zincrby(name, value, amount)

#自增有序集合内value对应的分数
r.zincrby("zset_name","a1",amount=2)#自增zset_name对应的有序集合里a1对应的分数
zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)

复制代码
# 按照索引范围获取name对应的有序集合的元素
aa=r.zrange("zset_name",0,1,desc=False,withscores=True,score_cast_func=int)
print(aa)
'''参数：
    name    redis的name
    start   有序集合索引起始位置
    end     有序集合索引结束位置
    desc    排序规则，默认按照分数从小到大排序
    withscores  是否获取元素的分数，默认只获取元素的值
    score_cast_func 对分数进行数据转换的函数'''
复制代码
zrevrange(name, start, end, withscores=False, score_cast_func=float)

#同zrange，集合是从大到小排序的
zrank(name, value)、zrevrank(name, value)

#获取value值在name对应的有序集合中的排行位置（从0开始）
print(r.zrank("zset_name", "a2"))

print(r.zrevrank("zset_name", "a2"))#从大到小排序
zscore(name, value)

#获取name对应有序集合中 value 对应的分数
print(r.zscore("zset_name","a1"))
zrem(name, values)

#删除name对应的有序集合中值是values的成员
r.zrem("zset_name","a1","a2")
zremrangebyrank(name, min, max)

#根据排行范围删除
zremrangebyscore(name, min, max)

#根据分数范围删除
zinterstore(dest, keys, aggregate=None)

复制代码
r.zadd("zset_name", "a1", 6, "a2", 2,"a3",5)
r.zadd('zset_name1', a1=7,b1=10, b2=5)

# 获取两个有序集合的交集并放入dest集合，如果遇到相同值不同分数，则按照aggregate进行操作
# aggregate的值为: SUM  MIN  MAX
r.zinterstore("zset_name2",("zset_name1","zset_name"),aggregate="MAX")
print(r.zscan("zset_name2"))
复制代码
zunionstore(dest, keys, aggregate=None)

#获取两个有序集合的并集并放入dest集合，其他同zinterstore，
其他常用操作

delete(*names)

#根据name删除redis中的任意数据类型
exists(name)

#检测redis的name是否存在
keys(pattern='*')

#根据* ？等通配符匹配获取redis的name
expire(name ,time)

# 为某个name设置超时时间
rename(src, dst)

# 重命名
move(name, db))

# 将redis的某个值移动到指定的db下
randomkey()

#随机获取一个redis的name（不删除）
type(name)

# 获取name对应值的类型

"""

#==========================================================================================================================





入门及使用

Python





# 导入模块
>>> import redis
# 连接到Redis服务器
>>> conn = redis.Redis(host='192.168.56.100', port=6379)
# 写入一条数据
>>> conn.set('name','ansheng')
True
# 获取一条数据
>>> conn.get('name')
b'ansheng'
>>> conn.get('url')
b'https://blog.ansheng.me'
1
2
3
4
5
6
7
8
9
10
11
12
# 导入模块
>>> import redis
# 连接到Redis服务器
>>> conn = redis.Redis(host='192.168.56.100', port=6379)
# 写入一条数据
>>> conn.set('name','ansheng')
True
# 获取一条数据
>>> conn.get('name')
b'ansheng'
>>> conn.get('url')
b'https://blog.ansheng.me'
使用连接池连接到Redis

Behind the scenes, redis-py uses a connection pool to manage connections to a Redis server. By default, each Redis instance you create will in turn create its own connection pool. You can override this behavior and use an existing connection pool by passing an already created connection pool instance to the connection_pool argument of the Redis class. You may choose to do this in order to implement client side sharding or have finer grain control of how connections are managed.
Python

>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> conn = redis.Redis(connection_pool=pool)
>>> conn.set('hello','world')
True
>>> conn.get('hello')
b'world'
1
2
3
4
5
6
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> conn = redis.Redis(connection_pool=pool)
>>> conn.set('hello','world')
True
>>> conn.get('hello')
b'world'
使用套接字连接

Python

>>> r = redis.Redis(unix_socket_path='/tmp/redis.sock')
1
>>> r = redis.Redis(unix_socket_path='/tmp/redis.sock')
API

redis-py提供的API用来操作redis

String API

set(name, value, ex=None, px=None, nx=False, xx=False)

参数	描述
ex	过期时间（秒）
px	过期时间（毫秒）
nx	如果设置为True，则只有name不存在时，当前set操作才执行
xx	如果设置为True，则只有name存在时，岗前set操作才执行
Python

>>> conn.set('k1', 'v1', ex=10, nx=True)
True
>>> conn.get('k1')
b'v1'
>>> conn.get('k1')
1
2
3
4
5
>>> conn.set('k1', 'v1', ex=10, nx=True)
True
>>> conn.get('k1')
b'v1'
>>> conn.get('k1')
setex(name, value, time)

设置过期时间/秒

Python

>>> conn.setex('k','v',1)
True
>>> conn.get('k')
1
2
3
>>> conn.setex('k','v',1)
True
>>> conn.get('k')
psetex(name, time_ms, value)

设置过期时间/毫秒

Python

>>> conn.psetex('k',10,'v')
True
>>> conn.get('k')
1
2
3
>>> conn.psetex('k',10,'v')
True
>>> conn.get('k')
setnx(name, value)

设置值，只有key不存在时，执行设置操作

Python

>>> conn.get('k1')
>>> conn.setnx('k1','v1')
True
>>> conn.get('k1')
b'v1'
>>> conn.setnx('k2','v2')
False
1
2
3
4
5
6
7
>>> conn.get('k1')
>>> conn.setnx('k1','v1')
True
>>> conn.get('k1')
b'v1'
>>> conn.setnx('k2','v2')
False
mset(*args, **kwargs)

同时设置多个key/value

Python

>>> conn.mset(k1='v1', k2='v2')
True
>>> conn.mset({'k1':'v1', 'k1':'v1'})
True
1
2
3
4
>>> conn.mset(k1='v1', k2='v2')
True
>>> conn.mset({'k1':'v1', 'k1':'v1'})
True
get(name)

获取单个值

Python

>>> conn.get('k1')
b'v1'
1
2
>>> conn.get('k1')
b'v1'
mget(keys, *args)

获取多个值

Python

>>> conn.mget('k1','k2')
[b'v1', b'v2']
# 传入列表
>>> conn.mget(['name','url'])
[b'ansheng', b'https://blog.ansheng.me']
1
2
3
4
5
>>> conn.mget('k1','k2')
[b'v1', b'v2']
# 传入列表
>>> conn.mget(['name','url'])
[b'ansheng', b'https://blog.ansheng.me']
getset(name, value)

设置新值并获取原来的值

Python

>>> conn.set('hello', 'world')
True
>>> result = conn.getset('hello', 'Linux')
>>> result
b'world'
>>> conn.get('hello')
b'Linux'
1
2
3
4
5
6
7
>>> conn.set('hello', 'world')
True
>>> result = conn.getset('hello', 'Linux')
>>> result
b'world'
>>> conn.get('hello')
b'Linux'
getrange(key, start, end)

通过索引的方式来获取value的值

Python

>>> conn.set('key','value')
True
>>> conn.getrange('key', 1, 4)
b'alue'
1
2
3
4
>>> conn.set('key','value')
True
>>> conn.getrange('key', 1, 4)
b'alue'
setrange(name, offset, value)

根据索引修改value

Python

>>> conn.set('n','123456789')
True
>>> conn.setrange('n', 0, 'a')
9
>>> conn.get('n')
b'a23456789'
1
2
3
4
5
6
>>> conn.set('n','123456789')
True
>>> conn.setrange('n', 0, 'a')
9
>>> conn.get('n')
b'a23456789'
setbit(name, offset, value)

getbit(name, offset)

获取value对应某一个索引位置对应的值0/1

Python

>>> conn.getbit('k',1)
1
1
2
>>> conn.getbit('k',1)
1
bitcount(key, start=None, end=None)

获取key对应二进制中表示1的个数

bitop(operation, dest, *keys)

将多个值进行值运算，得出的结果保存到一个新值当中

Python

>>> conn.mset(n1='abc',n2='cde',n3='adc')
True
>>> conn.bitop('AND','now_key','n1','n2','n3')
3
>>> conn.get('now_key')
b'a`a'
>>> conn.mget('n1','n2','n3')
[b'abc', b'cde', b'adc']
1
2
3
4
5
6
7
8
>>> conn.mset(n1='abc',n2='cde',n3='adc')
True
>>> conn.bitop('AND','now_key','n1','n2','n3')
3
>>> conn.get('now_key')
b'a`a'
>>> conn.mget('n1','n2','n3')
[b'abc', b'cde', b'adc']
operation支持AND(并)、OR(或)、NOT(非)、XOR(异或)
strlen(name)

获取value的长度

Python

>>> conn.set('name','安生')
True
>>> conn.strlen('name')
6
1
2
3
4
>>> conn.set('name','安生')
True
>>> conn.strlen('name')
6
incr(name, amount=1)

对name的value进行自增，如果name不存在则创建，否则自增

Python

>>> conn.get('number')
>>> conn.incr('number')
1
>>> conn.get('number')
b'1'
>>> conn.incr('number')
2
>>> conn.incr('number', 10)
12
1
2
3
4
5
6
7
8
9
>>> conn.get('number')
>>> conn.incr('number')
1
>>> conn.get('number')
b'1'
>>> conn.incr('number')
2
>>> conn.incr('number', 10)
12
incrbyfloat(name, amount=1.0)

同上，支持浮点数自增

Python

>>> conn.incrbyfloat('number', 1.5)
13.5
>>> conn.incrbyfloat('number', 1.1)
14.6
1
2
3
4
>>> conn.incrbyfloat('number', 1.5)
13.5
>>> conn.incrbyfloat('number', 1.1)
14.6
decr(name, amount=1)

自减，同自增一样，如果进行自减的value不是整数就报错

Python

>>> conn.set('n', 10)
True
>>> conn.decr('n')
9
>>> conn.decr('n', 9)
0
1
2
3
4
5
6
>>> conn.set('n', 10)
True
>>> conn.decr('n')
9
>>> conn.decr('n', 9)
0
append(key, value)

在value后面追加内容

Python

>>> conn.set('blog','https://blog.ansheng.me')
True
>>> conn.append('blog','/')
26
>>> conn.get('blog')
b'https://blog.ansheng.me/'
1
2
3
4
5
6
>>> conn.set('blog','https://blog.ansheng.me')
True
>>> conn.append('blog','/')
26
>>> conn.get('blog')
b'https://blog.ansheng.me/'
Hash API

hset(name, key, value)

设置name的键值对，有则修改，没有则创建

Python

>>> conn.hset('dic','k1','v1')
1
>>> conn.hget('dic','k1')
b'v1'
1
2
3
4
>>> conn.hset('dic','k1','v1')
1
>>> conn.hget('dic','k1')
b'v1'
hmset(name, mapping)

同时设置多个name的key/value

Python

>>> conn.hmset('dic', {'k1': 'v1', 'k2': 'v2'})
True
>>> conn.hget('dic','k2')
b'v2'
1
2
3
4
>>> conn.hmset('dic', {'k1': 'v1', 'k2': 'v2'})
True
>>> conn.hget('dic','k2')
b'v2'
hget(name, key)

获取name中key的值

Python

>>> conn.hget('dic','k2')
b'v2'
1
2
>>> conn.hget('dic','k2')
b'v2'
hmget(name, keys, *args)

同时获取多个

Python

>>> conn.hmget('dic',['k1', 'k2'])
[b'v1', b'v2']
>>> conn.hmget('dic','k1', 'k2')
[b'v1', b'v2']
1
2
3
4
>>> conn.hmget('dic',['k1', 'k2'])
[b'v1', b'v2']
>>> conn.hmget('dic','k1', 'k2')
[b'v1', b'v2']
hgetall(name)

获取name对应的所有key/value

Python

>>> conn.hgetall('dic')
{b'k1': b'v1', b'k2': b'v2'}
1
2
>>> conn.hgetall('dic')
{b'k1': b'v1', b'k2': b'v2'}
hlen(name)

获取name对应键值对的个数

Python

>>> conn.hlen('dic')
2
1
2
>>> conn.hlen('dic')
2
hkeys(name)

获取name中所有的key

Python

>>> conn.hkeys('dic')
[b'k1', b'k2']
1
2
>>> conn.hkeys('dic')
[b'k1', b'k2']
hvals(name)

获取name中所有的value

Python

>>> conn.hvals('dic')
[b'v1', b'v2']
1
2
>>> conn.hvals('dic')
[b'v1', b'v2']
hexists(name, key)

检查当前name中是否有传入的key

Python

>>> conn.hexists('dic','k1')
True
>>> conn.hexists('dic','kk')
False
1
2
3
4
>>> conn.hexists('dic','k1')
True
>>> conn.hexists('dic','kk')
False
hdel(self, name, *keys)

删除name中对应的key

Python

>>> conn.hdel('dic','k1')
1
>>> conn.hget('dic','k1')
1
2
3
>>> conn.hdel('dic','k1')
1
>>> conn.hget('dic','k1')
hincrby(name, key, amount=1)

name中key对应的value进行自增，如果不存在则创建

Python

>>> conn.hincrby('dic','number')
1
>>> conn.hincrby('dic','number',10)
11
1
2
3
4
>>> conn.hincrby('dic','number')
1
>>> conn.hincrby('dic','number',10)
11
hincrbyfloat(name, key, amount=1.0)

value自增，支持浮点数，同上

Python

>>> conn.hincrbyfloat('dic','float')
1.0
>>> conn.hincrbyfloat('dic','float',0.3)
1.3
1
2
3
4
>>> conn.hincrbyfloat('dic','float')
1.0
>>> conn.hincrbyfloat('dic','float',0.3)
1.3
hscan(name, cursor=0, match=None, count=None)

增量式迭代获取，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆

参数	描述
name	redis的name
cursor	游标（基于游标分批取获取数据）
match	匹配指定key，默认None 表示所有的key
count	每次分片最少获取个数，默认None表示采用Redis的默认分片个数
hscan_iter(name, match=None, count=None)

利用yield封装hscan创建生成器，实现分批去redis中获取数据

参数	描述
match	匹配指定key，默认None 表示所有的key
count	每次分片最少获取个数，默认None表示采用Redis的默认分片个数
如：

Python

for item in r.hscan_iter('xx'):
    print item
1
2
for item in r.hscan_iter('xx'):
    print item
expire(name, time)

设置过期时间

Python

>>> conn.hset('info','BlogUrl','https://blog.ansheng.me')
1
>>> conn.expire('info', 10)
True
>>> conn.hget('info','BlogUrl')
b'https://blog.ansheng.me'
>>> conn.hget('info','BlogUrl')
1
2
3
4
5
6
7
>>> conn.hset('info','BlogUrl','https://blog.ansheng.me')
1
>>> conn.expire('info', 10)
True
>>> conn.hget('info','BlogUrl')
b'https://blog.ansheng.me'
>>> conn.hget('info','BlogUrl')
ListAPI

lpush(name, *values)

在最左边添加值

Python

>>> conn.lpush('li', 11,22,33)
3
>>> conn.lindex('li', 0)
b'33'
1
2
3
4
>>> conn.lpush('li', 11,22,33)
3
>>> conn.lindex('li', 0)
b'33'
rpush(name, *values)

在最右边添加值

Python

>>> conn.rpush('lli', 11,22,33)
3
>>> conn.lindex('lli', 0)
b'11'
1
2
3
4
>>> conn.rpush('lli', 11,22,33)
3
>>> conn.lindex('lli', 0)
b'11'
lpushx(name, value)

只有name已经存在时，值添加到列表的最左边

Python

>>> conn.lpushx('li', 'aa')
4
>>> conn.lindex('li', 0)
b'aa'
1
2
3
4
>>> conn.lpushx('li', 'aa')
4
>>> conn.lindex('li', 0)
b'aa'
rpushx(name, value)

只有name已经存在时，值添加到列表的最右边

Python

>>> conn.rpushx('li', 'bb')
5
>>> conn.lindex('li', 0)
b'aa'
>>> conn.lindex('li', 4)
b'bb'
1
2
3
4
5
6
>>> conn.rpushx('li', 'bb')
5
>>> conn.lindex('li', 0)
b'aa'
>>> conn.lindex('li', 4)
b'bb'
llen(name)

获取name元素的个数

Python

>>> conn.llen('li')
5
1
2
>>> conn.llen('li')
5
linsert(name, where, refvalue, value)

在name的某一个值前面或者后面插入一个新值

Python

>>> conn.linsert('li','AFTER','11','cc')
6
>>> conn.lindex('li', 3)
b'11'
>>> conn.lindex('li', 4)
b'cc'
1
2
3
4
5
6
>>> conn.linsert('li','AFTER','11','cc')
6
>>> conn.lindex('li', 3)
b'11'
>>> conn.lindex('li', 4)
b'cc'
lset(name, index, value)

对name中index索引位置的值进行重新赋值

Python

>>> conn.lindex('li', 4)
b'cc'
>>> conn.lset('li', 4, 'hello')
True
>>> conn.lindex('li', 4)
b'hello'
1
2
3
4
5
6
>>> conn.lindex('li', 4)
b'cc'
>>> conn.lset('li', 4, 'hello')
True
>>> conn.lindex('li', 4)
b'hello'
lrem(name, value, num=0)

删除指定value后面或者前面的值

num=2,从前到后，删除2个；
num=-2,从后向前，删除2个
Python

>>> conn.llen('li')
6
>>> conn.lrem('li', 'hello')
1
>>> conn.llen('li')
5
>>> conn.lrem('li', '22', num=2)
2
>>> conn.llen('li')
3
1
2
3
4
5
6
7
8
9
10
>>> conn.llen('li')
6
>>> conn.lrem('li', 'hello')
1
>>> conn.llen('li')
5
>>> conn.lrem('li', '22', num=2)
2
>>> conn.llen('li')
3
lpop(name)

删除name中左侧第一个元素

Python

>>> conn.lindex('li', 0)
b'11'
>>> conn.lpop('li')
b'11'
1
2
3
4
>>> conn.lindex('li', 0)
b'11'
>>> conn.lpop('li')
b'11'
rpop(name)

删除name中右侧第一个元素

Python

>>> conn.rpop('li')
b'33'
1
2
>>> conn.rpop('li')
b'33'
lindex(name, index)

获取name中对应索引的值

Python

>>> conn.lindex('li', 0)
b'aa'
1
2
>>> conn.lindex('li', 0)
b'aa'
lrange(name, start, end)

使用切片获取数据

Python

>>> conn.llen('li')
8
>>> conn.lrange('li',0,5)
[b'3', b'23', b'34', b'235', b'2', b'1']
1
2
3
4
>>> conn.llen('li')
8
>>> conn.lrange('li',0,5)
[b'3', b'23', b'34', b'235', b'2', b'1']
ltrim(name, start, end)

在name对应的列表中移除没有在start-end索引之间的值

Python

>>> conn.ltrim('li',0,5)
True
>>> conn.llen('li')
6
1
2
3
4
>>> conn.ltrim('li',0,5)
True
>>> conn.llen('li')
6
rpoplpush(src, dst)

从src列表中取出最右边的元素，同时将其添加至dst列表的最左边

Python

>>> conn.lpush('li1', 1,2,3)
3
>>> conn.lpush('li2', 'a','b','c')
3
>>> conn.rpoplpush('li1','li2')
b'1'
1
2
3
4
5
6
>>> conn.lpush('li1', 1,2,3)
3
>>> conn.lpush('li2', 'a','b','c')
3
>>> conn.rpoplpush('li1','li2')
b'1'
blpop(keys, timeout=0)
brpop(keys, timeout=0)

brpoplpush(src, dst, timeout=0)

从src列表的右侧移除一个元素并将其添加到dst列表的左侧

Python

>>> conn.lpush('ll', 'a','b','c')
3
>>> conn.lpush('aa', 'a','b','c')
3
>>> conn.brpoplpush('ll','aa')
b'a'
1
2
3
4
5
6
>>> conn.lpush('ll', 'a','b','c')
3
>>> conn.lpush('aa', 'a','b','c')
3
>>> conn.brpoplpush('ll','aa')
b'a'
timeout，当src对应的列表中没有数据时，阻塞等待其有数据的超时时间（秒），0 表示永远阻塞
自定义增量迭代

由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要：

获取name对应的所有列表
循环列表
但是，如果列表非常大，那么就有可能在第一步时就将程序的内容撑爆，所有有必要自定义一个增量迭代的功能：

Python

def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in xrange(list_count):
        yield r.lindex(name, index)
1
2
3
4
5
6
7
8
9
def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in xrange(list_count):
        yield r.lindex(name, index)
使用

Python

for item in list_iter('pp'):
    print item
1
2
for item in list_iter('pp'):
    print item
SET API

sadd(name, *values)

为name添加值，如果存在则不添加

Python

>>> conn.sadd('s1', 1)
1
>>> conn.sadd('s1', 1)
0
1
2
3
4
>>> conn.sadd('s1', 1)
1
>>> conn.sadd('s1', 1)
0
scard(name)

返回name的元素数量

Python

>>> conn.scard('s1')
1
1
2
>>> conn.scard('s1')
1
sdiff(keys, *args)

在keys集合中不在其他集合中的数据

Python

>>> conn.sdiff('s1','s2')
{b'c', b'v', b'a'}
1
2
>>> conn.sdiff('s1','s2')
{b'c', b'v', b'a'}
sdiffstore(dest, keys, *args)

在keys集合中不在其他集合中的数据保存到dest集合中

Python

>>> conn.sdiffstore('news','s1','s2')
3
>>> conn.scard('news')
3
1
2
3
4
>>> conn.sdiffstore('news','s1','s2')
3
>>> conn.scard('news')
3
sinter(keys, *args)

获取keys集合中与其他集合中的并集

Python

>>> conn.sinter('s1','s2')
{b'2', b'3', b'1'}
1
2
>>> conn.sinter('s1','s2')
{b'2', b'3', b'1'}
sinterstore(dest, keys, *args)

获取keys集合中与其他集合中的并集数据并保存到dest集合中

Python

>>> conn.sinterstore('news1','s1','s2')
3
1
2
>>> conn.sinterstore('news1','s1','s2')
3
sismember(name, value)

获取value是否是name集合中的成员

Python

>>> conn.sismember('news1','1')
True
>>> conn.sismember('news1','aa1')
False
1
2
3
4
>>> conn.sismember('news1','1')
True
>>> conn.sismember('news1','aa1')
False
smembers(name)

获取name集合中所有的成员

Python

>>> conn.smembers('news1')
{b'2', b'3', b'1'}
1
2
>>> conn.smembers('news1')
{b'2', b'3', b'1'}
smove(src, dst, value)

将src中的value移动到dst中

Python

>>> conn.smembers('s1')
{b'c', b'2', b'v', b'1', b'3', b'a'}
>>> conn.smembers('s2')
{b'2', b'3', b'1'}
>>> conn.smove('s1','s2','v')
True
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
1
2
3
4
5
6
7
8
9
10
>>> conn.smembers('s1')
{b'c', b'2', b'v', b'1', b'3', b'a'}
>>> conn.smembers('s2')
{b'2', b'3', b'1'}
>>> conn.smove('s1','s2','v')
True
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
spop(name)

删除并返回name中的随机成员

Python

>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
>>> conn.spop('s2')
b'3'
>>> conn.smembers('s2')
{b'2', b'v', b'1'}
>>> conn.spop('s2')
b'2'
>>> conn.smembers('s2')
{b'v', b'1'}
>>> conn.spop('s2')
b'1'
>>> conn.smembers('s2')
{b'v'}
1
2
3
4
5
6
7
8
9
10
11
12
13
14
>>> conn.smembers('s2')
{b'2', b'v', b'3', b'1'}
>>> conn.spop('s2')
b'3'
>>> conn.smembers('s2')
{b'2', b'v', b'1'}
>>> conn.spop('s2')
b'2'
>>> conn.smembers('s2')
{b'v', b'1'}
>>> conn.spop('s2')
b'1'
>>> conn.smembers('s2')
{b'v'}
srandmember(name, number=None)

随机获取name集合中的number个成员，默认number=1

Python

>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srandmember('s1')
b'1'
>>> conn.srandmember('s1')
b'a'
>>> conn.srandmember('s1',number=2)
[b'3', b'a']
>>> conn.srandmember('s1',number=2)
[b'1', b'2']
1
2
3
4
5
6
7
8
9
10
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srandmember('s1')
b'1'
>>> conn.srandmember('s1')
b'a'
>>> conn.srandmember('s1',number=2)
[b'3', b'a']
>>> conn.srandmember('s1',number=2)
[b'1', b'2']
srem(name, *values)

删除name集合中的values数据

Python

>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srem('s1','1','2')
2
>>> conn.smembers('s1')
{b'c', b'a', b'3'}
1
2
3
4
5
6
>>> conn.smembers('s1')
{b'c', b'2', b'a', b'3', b'1'}
>>> conn.srem('s1','1','2')
2
>>> conn.smembers('s1')
{b'c', b'a', b'3'}
sunion(keys, *args)

获取keys集合与其他集合的并集

Python

>>> conn.sadd('a1',1,2,3)
3
>>> conn.sadd('a2',1,2,3,4,5,6,7)
7
>>> conn.sunion('a2','a1')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
1
2
3
4
5
6
>>> conn.sadd('a1',1,2,3)
3
>>> conn.sadd('a2',1,2,3,4,5,6,7)
7
>>> conn.sunion('a2','a1')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
sunionstore(dest, keys, *args)

获取keys集合与其他集合的并集并保存到dest中

Python

>>> conn.sunionstore('a3', 'a2','a1')
7
>>> conn.smembers('a3')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
1
2
3
4
>>> conn.sunionstore('a3', 'a2','a1')
7
>>> conn.smembers('a3')
{b'2', b'7', b'1', b'3', b'6', b'5', b'4'}
Ordered set API

zadd(name, *args, **kwargs)

Python

>>> conn.zadd('h1','n1',11,'n2',22)
2
>>> conn.zadd('h2',n1=11,n2=22)
2
1
2
3
4
>>> conn.zadd('h1','n1',11,'n2',22)
2
>>> conn.zadd('h2',n1=11,n2=22)
2
zcard(name)

返回有序集合name元素的数量

Python

>>> conn.zcard('h1')
2
1
2
>>> conn.zcard('h1')
2
zcount(name, min, max)

返回在name中值在min与max之间的值个数

Python

>>> conn.zcount('h1',10,30)
2
1
2
>>> conn.zcount('h1',10,30)
2
zincrby(name, value, amount=1)

name中让value的值加上amount

Python

>>> conn.zincrby('h1','n1',10)
21.0
1
2
>>> conn.zincrby('h1','n1',10)
21.0
zinterstore(dest, keys, aggregate=None)
zlexcount(name, min, max)

zrange(name, start, end, desc=False, withscores=False, score_cast_func=float)

参数	描述
name	redis的name
start	有序集合索引起始位置（非分数）
end	有序集合索引结束位置（非分数）
desc	排序规则，默认按照分数从小到大排序
withscores	是否获取元素的分数，默认只获取元素的值
score_cast_func	对分数进行数据转换的函数
Python

>>> conn.zrange('h1', 1, 2, desc=True, withscores=True, score_cast_func=float)
[(b'n1', 21.0)]
>>> conn.zrange('h1', 1, 2, desc=False, withscores=True, score_cast_func=float)
[(b'n2', 22.0)]
1
2
3
4
>>> conn.zrange('h1', 1, 2, desc=True, withscores=True, score_cast_func=float)
[(b'n1', 21.0)]
>>> conn.zrange('h1', 1, 2, desc=False, withscores=True, score_cast_func=float)
[(b'n2', 22.0)]
Python

# 从大到小排序
zrevrange(name, start, end, withscores=False, score_cast_func=float)
# 按照分数范围获取name对应的有序集合的元素
zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
# 从大到小排序
zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
1
2
3
4
5
6
# 从大到小排序
zrevrange(name, start, end, withscores=False, score_cast_func=float)
# 按照分数范围获取name对应的有序集合的元素
zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
# 从大到小排序
zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
zrangebylex(name, min, max, start=None, num=None)

当有序集合的所有成员都具有相同的分值时，有序集合的元素会根据成员的 值 （lexicographical ordering）来进行排序，而这个命令则可以返回给定的有序集合键 key 中， 元素的值介于 min 和 max 之间的成员

对集合中的每个成员进行逐个字节的对比（byte-by-byte compare）， 并按照从低到高的顺序， 返回排序后的集合成员。 如果两个字符串有一部分内容是相同的话， 那么命令会认为较长的字符串比较短的字符串要大

参数	描述
name	redis的name
min	左区间(值) + 表示正无限； – 表示负无限； ( 表示开区间； [ 则表示闭区间
min	右区间（值）
start	对结果进行分片处理，索引位置
num	对结果进行分片处理，索引后面的num个元素
如：

Python

ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
# r.zrangebylex('myzset', "-", "[ca") 结果为：['aa', 'ba', 'ca']
1
2
ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
# r.zrangebylex('myzset', "-", "[ca") 结果为：['aa', 'ba', 'ca']
更多：

Python

# 从大到小排序
zrevrangebylex(name, max, min, start=None, num=None)
1
2
# 从大到小排序
zrevrangebylex(name, max, min, start=None, num=None)
zrevrangebylex(name, max, min, start=None, num=None)

zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)**

zrank(name, value)

返回基于0的值，指示在排序集名称的值排名

Python

>>> conn.zrank('h1','n1')
0
>>> conn.zrank('h1','n2')
1
1
2
3
4
>>> conn.zrank('h1','n1')
0
>>> conn.zrank('h1','n2')
1
zrevrank(name, value)，从大到小排序
zrem(name, *values)

删除name中对应的values

Python

>>> conn.zrem('h1','n2')
1
>>> conn.zrem('h2',['n1','n2'])
2
1
2
3
4
>>> conn.zrem('h1','n2')
1
>>> conn.zrem('h2',['n1','n2'])
2
zremrangebyrank(name, min, max)

根据排行范围进行删除

Python

>>> conn.zremrangebyrank('h1',1,2)
1
1
2
>>> conn.zremrangebyrank('h1',1,2)
1
zremrangebyscore(name, min, max)

根据分数范围进行删除

Python

>>> conn.zremrangebyscore('h1',10,20)
2
1
2
>>> conn.zremrangebyscore('h1',10,20)
2
zscore(name, value)

返回指定value的值是多少

Python

>>> conn.zscore('h1','n1')
11.0
1
2
>>> conn.zscore('h1','n1')
11.0
zunionstore(dest, keys, aggregate=None)

Global API

delete(*names)

在redis中删除names

Python

>>> conn.delete('ooo')
1
1
2
>>> conn.delete('ooo')
1
exists(name)

检测name是否存在

Python

>>> conn.exists('iii')
False
>>> conn.exists('h1')
True
1
2
3
4
>>> conn.exists('iii')
False
>>> conn.exists('h1')
True
keys(pattern=’*’)

Python

# 匹配数据库中所有 key
>>> conn.keys(pattern='*')
[b'h2', b'kasd1', b'n2', b'url', b'name', b'n', b'li1', b'n1', b's1', b'now_key', b'l', b's2', b'number', b'numbers', b'a2', b'dic', b'a1', b'news', b'news1', b'aa', b'key', b'lli', b'll', b'k', b'li', b'k2', b'h1', b'li2', b'ccc', b'k1', b'blog', b'kaasdsd1', b'a3', b'l1', b'l2', b'n3', b'a']
1
2
3
# 匹配数据库中所有 key
>>> conn.keys(pattern='*')
[b'h2', b'kasd1', b'n2', b'url', b'name', b'n', b'li1', b'n1', b's1', b'now_key', b'l', b's2', b'number', b'numbers', b'a2', b'dic', b'a1', b'news', b'news1', b'aa', b'key', b'lli', b'll', b'k', b'li', b'k2', b'h1', b'li2', b'ccc', b'k1', b'blog', b'kaasdsd1', b'a3', b'l1', b'l2', b'n3', b'a']
Python

# 匹配hello，hallo和hxllo等
conn.keys(pattern='h?llo')
# 匹配hllo和heeeeello 等
conn.keys(pattern='h*llo')
# 匹配hello和hallo，但不匹配 hillo
conn.keys(pattern='h[ae]llo')
1
2
3
4
5
6
# 匹配hello，hallo和hxllo等
conn.keys(pattern='h?llo')
# 匹配hllo和heeeeello 等
conn.keys(pattern='h*llo')
# 匹配hello和hallo，但不匹配 hillo
conn.keys(pattern='h[ae]llo')
rename(src, dst)

把src重命名成dst

Python

>>> conn.set('k','v')
True
>>> conn.get('k')
b'v'
>>> conn.rename('k', 'kk')
True
>>> conn.get('k')
>>> conn.get('kk')
b'v'
1
2
3
4
5
6
7
8
9
>>> conn.set('k','v')
True
>>> conn.get('k')
b'v'
>>> conn.rename('k', 'kk')
True
>>> conn.get('k')
>>> conn.get('kk')
b'v'
move(name, db)

将redis的某个值移动到指定的db下

randomkey()

随机获取一个redis的name，不进行删除

Python

>>> conn.randomkey()
b'll'
>>> conn.randomkey()
b'news1'
1
2
3
4
>>> conn.randomkey()
b'll'
>>> conn.randomkey()
b'news1'
type(name)

查看name的类型

Python

>>> conn.type('kk')
b'string'
1
2
>>> conn.type('kk')
b'string'
管道

redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作(MySQL中的事务)。

Python

>>> import redis
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> r = redis.Redis(connection_pool=pool)
# 创建一个通道支持事务
>>> pipe = r.pipeline(transaction=True)
#
>>> r.set('hello', 'world')
True
>>> r.set('blog', 'ansheng.me')
True
# 如果在设置上面两个值的过程中出错了，那么这次提交就不会执行
>>> pipe.execute()
[]
1
2
3
4
5
6
7
8
9
10
11
12
13
>>> import redis
>>> pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
>>> r = redis.Redis(connection_pool=pool)
# 创建一个通道支持事务
>>> pipe = r.pipeline(transaction=True)
#
>>> r.set('hello', 'world')
True
>>> r.set('blog', 'ansheng.me')
True
# 如果在设置上面两个值的过程中出错了，那么这次提交就不会执行
>>> pipe.execute()
[]
发布订阅

Python

# monitor.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.56.100')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'
    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
# subscriber.py 订阅者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
redis_sub = obj.subscribe()
while True:
    msg = redis_sub.parse_response()
    print(msg)
# announcer.py 发布者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
obj.public('hello')
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
# monitor.py
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
class RedisHelper:
    def __init__(self):
        self.__conn = redis.Redis(host='192.168.56.100')
        self.chan_sub = 'fm104.5'
        self.chan_pub = 'fm104.5'
    def public(self, msg):
        self.__conn.publish(self.chan_pub, msg)
        return True
    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub
# subscriber.py 订阅者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
redis_sub = obj.subscribe()
while True:
    msg = redis_sub.parse_response()
    print(msg)
# announcer.py 发布者
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from monitor import RedisHelper
obj = RedisHelper()
obj.public('hello')
实例

让redis缓存tornado页面

Python

# _*_coding:utf-8 _*_
import tornado.ioloop
import tornado.web
import time
import redis
poll = redis.ConnectionPool(host='192.168.56.100', port=6379)
conn = redis.Redis(connection_pool=poll)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        CurrentTim = conn.get('CurrentTim')
        if CurrentTim:
            self.write(CurrentTim)
        else:
            CurrentTim = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            conn.set('CurrentTim', CurrentTim, ex=5)
            self.write(CurrentTim)
settings = {
    "tempalte_path": "template",
}
application = tornado.web.Application([
    (r'/', MainHandler),
], **settings)
if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
# _*_coding:utf-8 _*_
import tornado.ioloop
import tornado.web
import time
import redis
poll = redis.ConnectionPool(host='192.168.56.100', port=6379)
conn = redis.Redis(connection_pool=poll)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        CurrentTim = conn.get('CurrentTim')
        if CurrentTim:
            self.write(CurrentTim)
        else:
            CurrentTim = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            conn.set('CurrentTim', CurrentTim, ex=5)
            self.write(CurrentTim)
settings = {
    "tempalte_path": "template",
}
application = tornado.web.Application([
    (r'/', MainHandler),
], **settings)
if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
数据缓存5秒，如图所示



基于Redis的Session存储

app.py

Python

# _*_coding:utf-8 _*_
import tornado.ioloop
import tornado.web
import RedisToSession
class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = RedisToSession.Session(self)
class MainHandler(BaseHandler):
    def get(self):
        Info = self.session.GetAll()
        self.render("template/index.html", Data=Info)
    def post(self, *args, **kwargs):
        # 获取传过来的值
        Key = self.get_argument('key')
        Val = self.get_argument('val')
        action = self.get_argument('action')
        if action == 'set':
            # 设置值
            self.session[Key] = Val
        elif action == 'del':
            del self.session[Key]
        # 获取所有信息
        Info = self.session.GetAll()
        # 返回给前端渲染
        self.render("template/index.html", Data=Info)
settings = {
    "tempalte_path": "template",
    "cookie_secret": "508CE6152CB93994628D3E99934B83CC",
}
application = tornado.web.Application([
    (r'/', MainHandler),
], **settings)
if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
# _*_coding:utf-8 _*_
import tornado.ioloop
import tornado.web
import RedisToSession
class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.session = RedisToSession.Session(self)
class MainHandler(BaseHandler):
    def get(self):
        Info = self.session.GetAll()
        self.render("template/index.html", Data=Info)
    def post(self, *args, **kwargs):
        # 获取传过来的值
        Key = self.get_argument('key')
        Val = self.get_argument('val')
        action = self.get_argument('action')
        if action == 'set':
            # 设置值
            self.session[Key] = Val
        elif action == 'del':
            del self.session[Key]
        # 获取所有信息
        Info = self.session.GetAll()
        # 返回给前端渲染
        self.render("template/index.html", Data=Info)
settings = {
    "tempalte_path": "template",
    "cookie_secret": "508CE6152CB93994628D3E99934B83CC",
}
application = tornado.web.Application([
    (r'/', MainHandler),
], **settings)
if __name__ == "__main__":
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()
template\index.html

XHTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<form action="/" method="post">
    set/del：<input type="text" name="action" value="set"/>
    Key: <input type="text" name="key"/>
    Val: <input type="text" name="val"/>
    <input type="submit" value="设置"/>
</form>
{{ Data }}
</body>
</html>
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
<form action="/" method="post">
    set/del：<input type="text" name="action" value="set"/>
    Key: <input type="text" name="key"/>
    Val: <input type="text" name="val"/>
    <input type="submit" value="设置"/>
</form>
{{ Data }}
</body>
</html>
RedisToSession.py

Python

# _*_ coding: utf-8 _*_
import redis
import hashlib
import uuid
import json
# 连接memcached
pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
conn = redis.Redis(connection_pool=pool)
class Session:
    CookieID = 'uc'
    ExpiresTime = 60 * 20
    def __init__(self, handler):
        """
        用于创建用户session在redis中的字典
        :param handler: 请求头
        """
        self.handler = handler
        # 从客户端获取随机字符串
        SessionID = self.handler.get_secure_cookie(Session.CookieID, None)
        # 客户端存在并且在服务端也存在
        if SessionID and conn.exists(SessionID):
            self.SessionID = SessionID
        else:
            # 获取随机字符串
            self.SessionID = self.SessionKey()
            # 把随机字符串写入memcached,时间是20分钟
            conn.hset(self.SessionID, None, None)
        # 每次访问超时时间就加20分钟
        conn.expire(self.SessionID, Session.ExpiresTime)
        # 设置Cookie
        self.handler.set_secure_cookie('uc', self.SessionID)
    def SessionKey(self):
        """
        :return: 生成随机字符串
        """
        UUID = str(uuid.uuid1()).replace('-', '')
        MD5 = hashlib.md5()
        MD5.update(bytes(UUID, encoding='utf-8'))
        SessionKey = MD5.hexdigest()
        return SessionKey
    def __setitem__(self, key, value):
        """
        :param key: session信息中的key
        :param value: 对应的Value
        """
        conn.hset(self.SessionID, key, value)
    def __getitem__(self, item):
        """
        :param item: Session信息中对应的Key
        :return: 获取的Session信息
        """
        # 获取对应的数据
        ResultData = conn.hget(self.SessionID, item)
        return ResultData
    def __delitem__(self, key):
        """
        :param key: 要删除的Key
        """
        conn.hdel(self.SessionID, key)
    def GetAll(self):
        # 获取Session中所有的信息，仅用于测试
        SessionData = conn.hgetall(self.SessionID)
        return SessionData
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
# _*_ coding: utf-8 _*_
import redis
import hashlib
import uuid
import json
# 连接memcached
pool = redis.ConnectionPool(host='192.168.56.100', port=6379)
conn = redis.Redis(connection_pool=pool)
class Session:
    CookieID = 'uc'
    ExpiresTime = 60 * 20
    def __init__(self, handler):
        """
        用于创建用户session在redis中的字典
        :param handler: 请求头
        """
        self.handler = handler
        # 从客户端获取随机字符串
        SessionID = self.handler.get_secure_cookie(Session.CookieID, None)
        # 客户端存在并且在服务端也存在
        if SessionID and conn.exists(SessionID):
            self.SessionID = SessionID
        else:
            # 获取随机字符串
            self.SessionID = self.SessionKey()
            # 把随机字符串写入memcached,时间是20分钟
            conn.hset(self.SessionID, None, None)
        # 每次访问超时时间就加20分钟
        conn.expire(self.SessionID, Session.ExpiresTime)
        # 设置Cookie
        self.handler.set_secure_cookie('uc', self.SessionID)
    def SessionKey(self):
        """
        :return: 生成随机字符串
        """
        UUID = str(uuid.uuid1()).replace('-', '')
        MD5 = hashlib.md5()
        MD5.update(bytes(UUID, encoding='utf-8'))
        SessionKey = MD5.hexdigest()
        return SessionKey
    def __setitem__(self, key, value):
        """
        :param key: session信息中的key
        :param value: 对应的Value
        """
        conn.hset(self.SessionID, key, value)
    def __getitem__(self, item):
        """
        :param item: Session信息中对应的Key
        :return: 获取的Session信息
        """
        # 获取对应的数据
        ResultData = conn.hget(self.SessionID, item)
        return ResultData
    def __delitem__(self, key):
        """
        :param key: 要删除的Key
        """
        conn.hdel(self.SessionID, key)
    def GetAll(self):
        # 获取Session中所有的信息，仅用于测试
        SessionData = conn.hgetall(self.SessionID)
        return SessionData


_------------------------------------------------_------------------------------------------------_------------------------------------------------_------------------------------------------------_------------------------------------------------_------------------------------------------------
"""

Redis

  redis是一个key-value存储系统。和Memcached类似，它支持存储的value类型相对更多，包括string(字符串)、list(链表)、set(集合)、zset(sorted set --有序集合)和hash（哈希类型）。这些数据类型都 支持push/pop、add/remove及取交集并集和差集及更丰富的操作，而且这些操作都是原子性的。在此基础上，redis支持各种不同方式的排 序。与memcached一样，为了保证效率，数据都是缓存在内存中。区别的是redis会周期性的把更新的数据写入磁盘或者把修改操作写入追加的记录文 件，并且在此基础上实现了master-slave(主从)同步。

一、Redis安装和基本使用

1
2
3
4
wget http://download.redis.io/releases/redis-3.0.6.tar.gz
tar xzf redis-3.0.6.tar.gz
cd redis-3.0.6
make
 启动服务端

src/redis-server
启动客户端

src/redis-cli
redis> set foo bar
OK
redis> get foo
"bar"
二、Python操作Redis

复制代码
sudo pip install redis
or
sudo easy_install redis
or
源码安装

详见：https://github.com/WoLpH/redis-py
复制代码
API使用

redis-py 的API的使用可以分类为：

连接方式
连接池
操作
String 操作
Hash 操作
List 操作
Set 操作
Sort Set 操作
管道
发布订阅
1、操作模式

redis-py提供两个类Redis和StrictRedis用于实现Redis的命令，StrictRedis用于实现大部分官方的命令，并使用官方的语法和命令，Redis是StrictRedis的子类，用于向后兼容旧版本的redis-py。

复制代码
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

r = redis.Redis(host='192.168.1.113', port=6379)
r.set('foo', 'Bar')
print r.get('foo')
复制代码
2、连接池

redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。可以直接建立一个连接池，然后作为参数 Redis，这样就可以实现多个Redis实例共享一个连接池。

复制代码
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

pool = redis.ConnectionPool(host='192.168.1.113', port=6379)

r = redis.Redis(connection_pool=pool)
r.set('foo', 'Bar')
print r.get('foo')
复制代码
"""
3、操作

String操作，redis中的String在在内存中按照一个name对应一个value来存储。如图：





set(name, value, ex=None, px=None, nx=False, xx=False)

复制代码
在Redis中设置值，默认，不存在则创建，存在则修改
参数：
     ex，过期时间（秒）
     px，过期时间（毫秒）
     nx，如果设置为True，则只有name不存在时，当前set操作才执行
     xx，如果设置为True，则只有name存在时，岗前set操作才执行

r.get("name")  # 获取字段
b'haha'
r.set("name", "hehe", ex=5)  # 保留时长 5秒
r.get("name")
b'hehe'
r.get("name")
r.set({'k1': 'v1', 'k2': 'v2'})  # 支持字典格式
r.get("k1")
b'v1'
复制代码
mset(*args, **kwargs)

复制代码
# 批量设置
r.mset(name="xixi", age=18)
r.get("name")
b'xixi'
r.get("age")
b'18'
复制代码
mget(keys, *args)

# 批量获取
r.mset(name="xixi", age=18)
r.mget("name", "age")
[b'xixi', b'18']
r.set("name", "koka")
getset(name, value)

# 设置新值并获取原来的值
r.getset("name", "akok")
b'koka'
r.get("name")
b'akok'
getrange(key, start, end)

复制代码
# 获取子序列（根据字节获取，非字符）
# 参数：
    # name，Redis 的 name
    # start，起始位置（字节）
    # end，结束位置（字节）
# 如： "武沛齐" ，0-2表示 "武"

r.set("parter", "柴少")
r.getrange("parter", 0, 2).decode()
'柴'
复制代码
setrange(name, offset, value)

复制代码
# 修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
# 参数：
    # offset，字符串的索引，字节（一个汉字三个字节）
    # value，要设置的值

r.set("name", 'ok')
# 修改字符串内容，从指定字符串索引开始向后替换
r.setrange("name", 0, "ko")
r.get("name")
b'ko'
复制代码
setbit(name, offset, value)

复制代码
# 对name对应值的二进制表示的位进行操作

# 参数：
    # name，redis的name
    # offset，位的索引（将值变换成二进制后再进行索引）
    # value，值只能是 1 或 0

ord('k')  # 107
ord('o')  # 111
# 107 => 0 1 1 0 1 0 1 1
# 111 => 0 1 1 0 1 1 1 1
r.setbit("name", 7, 0)
# 0 1 1 0 1 0 1 1 => 0 1 1 0 1 0 1 0  106 => j
r.get("name")
b'jo'
r.setbit("name", 15, 0)
# 0 1 1 0 1 1 1 1 => 0 1 1 0 1 1 1 0  110 => n
r.get("name")
b'jn'
复制代码
getbit(name, offset)

复制代码
# 获取name对应的值的二进制表示中的某位的值 （0或1）
bin(ord('j')).replace('b', '')
'01101010'
bin(ord('n')).replace('b', '')
'01101110'
r.set("name", "jn")
r.getbit("name", "2")
1
复制代码
bitcount(key, start=None, end=None)

复制代码
# 获取name对应的值的二进制表示中 1 的个数
# 参数：
    # key，Redis的name
    # start，位起始位置
    # end，位结束位置
r.bitcount("name", 0, 1)
9
str(bin(ord('j')) + bin(ord('n'))).replace('b', '').count("1")
9
复制代码
incr(self, name, amount=1)

复制代码
# 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。

# 参数：
    # name,Redis的name
    # amount,自增数（必须是整数）

# 注：同incrby

r.set('n', 1)
r.incr("n", '3')
4
复制代码
incrbyfloat(self, name, amount=1.0)

复制代码
# 自增 name对应的值，当name不存在时，则创建name＝amount，否则，则自增。

# 参数：
    # name,Redis的name
    # amount,自增数（浮点型)

r.incrbyfloat('n', 1)
3.0
复制代码
decr(self, name, amount=1)

复制代码
# 自减 name对应的值，当name不存在时，则创建name＝amount，否则，则自减。

# 参数：
    # name,Redis的name
    # amount,自减数（整数）

r.set('n', '2')
r.decr('n', 1)
1
复制代码
append(key, value)

复制代码
# 在redis name对应的值后面追加内容

# 参数：
    key, redis的name
    value, 要追加的字符串
r.append('n', 'a')
2
r.get("n")
b'1a'
复制代码
Hash操作，redis中Hash在内存中的存储格式如下图：





hset(name, key, value)

复制代码
# name对应的hash中设置一个键值对（不存在，则创建；否则，修改）

# 参数：
    # name，redis的name
    # key，name对应的hash中的key
    # value，name对应的hash中的value

# 注：
    # hsetnx(name, key, value),当name对应的hash中不存在当前key时则创建（相当于添加）

r.hset("h1", "name", "koka")
1
r.hget("h1", "name")
b'koka'
复制代码
hmset(name, mapping)

复制代码
# 在name对应的hash中批量设置键值对

# 参数：
    # name，redis的name
    # mapping，字典，如：{'k1':'v1', 'k2': 'v2'}

# 如：
    # r.hmset('xx', {'k1':'v1', 'k2': 'v2'})

r.hmset('n1', {'k1': 'v1', 'k2': 'v2'})
r.hmget("n1", "k1", "k2")
[b'v1', b'v2']
复制代码
hgetall(name)

# 获取name对应hash的所有键值
r.hgetall("n1")
{b'k2': b'v2', b'k1': b'v1'}
hlen(name)

# 获取name对应的hash中键值对的个数
r.hlen("n1")
2
hkeys(name)

# 获取name对应的hash中所有的key的值
r.hkeys("n1")
[b'k2', b'k1']
hvals(name)

# 获取name对应的hash中所有的value的值
r.hvals("n1")
[b'v2', b'v1']
hexists(name, key)

# 检查name对应的hash是否存在当前传入的key
r.hexists("n1", "k1")
hdel(name,*keys)

# 将name对应的hash中指定key的键值对删除
r.hdel("n1", "k1")
1
hincrby(name, key, amount=1)

复制代码
# 自增name对应的hash中的指定key的值，不存在则创建key=amount
# 参数：
    # name，redis中的name
    # key， hash对应的key
    # amount，自增数（整数）

r.hincrby("n1", "k1", 1)
1
复制代码
hincrbyfloat(name, key, amount=1.0)

复制代码
# 自增name对应的hash中的指定key的值，不存在则创建key=amount

# 参数：
    # name，redis中的name
    # key， hash对应的key
    # amount，自增数（浮点数）

# 自增name对应的hash中的指定key的值，不存在则创建key=amount

r.hincrbyfloat("n1", "k1", 1)
2.0
复制代码
hscan(name, cursor=0, match=None, count=None)

复制代码
# 增量式迭代获取，对于数据大的数据非常有用，hscan可以实现分片的获取数据，并非一次性将数据全部获取完，从而放置内存被撑爆

# 参数：
    # name，redis的name
    # cursor，游标（基于游标分批取获取数据）
    # match，匹配指定key，默认None 表示所有的key
    # count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数

# 如：
    # 第一次：cursor1, data1 = r.hscan('xx', cursor=0, match=None, count=None)
    # 第二次：cursor2, data1 = r.hscan('xx', cursor=cursor1, match=None, count=None)
    # ...
    # 直到返回值cursor的值为0时，表示数据已经通过分片获取完毕

r.hscan("n1")
(0, {b'k2': b'v2', b'k1': b'3'})
复制代码
hscan_iter(name, match=None, count=None)

复制代码
# 利用yield封装hscan创建生成器，实现分批去redis中获取数据

# 参数：
    # match，匹配指定key，默认None 表示所有的key
    # count，每次分片最少获取个数，默认None表示采用Redis的默认分片个数

for i in r.hscan_iter("n1", match=None, count=None):print(i)
(b'k2', b'v2')
(b'k1', b'3')
复制代码
List操作，redis中的List在在内存中按照一个name对应一个List来存储。如图：





lpush(name,values)

复制代码
# 在name对应的list中添加元素，每个新的元素都添加到列表的最左边

# 如：
    # r.lpush('oo', 11,22,33)
    # 保存顺序为: 33,22,11

# 扩展：
    # rpush(name, values) 表示从右向左操作

r.lpush("l1", [11, 22, 33, 44])
1
r.lpush("l1", [11, 22, 33, 44])
2
r.lrange("l1", '0', '3')
[b'[11, 22, 33, 44]', b'[11, 22, 33, 44]']

r.lpush("l3", "AA", "BB", "CC", "DD")
1
r.lrange("l3",0,2)
[b'CC', b'BB', b'AA']
复制代码
lpushx(name,value)

复制代码
# 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边

# 更多：
    # rpushx(name, value) 表示从右向左操作

r.lpushx("l2", "33")
0
r.lrange("l2",0,1)
[]
复制代码
llen(name)

# name对应的list元素的个数
r.llen("l1")
2
linsert(name, where, refvalue, value))

复制代码
# 在name对应的列表的某一个值前或后插入一个新值

# 参数：
    # name，redis的name
    # where，BEFORE或AFTER
    # refvalue，标杆值，即：在它前后插入数据
    # value，要插入的数据

r.lpush("l3", "AA", "BB", "CC", "DD")
r.lrange("l3", 0, 2)
[b'CC', b'BB', b'AA']

r.linsert("l3", "AFTER", "CC", "cc")
r.lrange("l3", 0, 3)
[b'CC', b'cc', b'BB', b'AA']
复制代码
r.lset(name, index, value)

复制代码
# 对name对应的list中的某一个索引位置重新赋值

# 参数：
    # name，redis的name
    # index，list的索引位置
    # value，要设置的值

r.lset("l3", '2', 'Cc')
r.lrange("l3", '0', '5')
[b'DD', b'CC', b'Cc', b'BB', b'AA']
复制代码
r.lrem(name, value, num)

复制代码
# 在name对应的list中删除指定的值

# 参数：
    # name，redis的name
    # value，要删除的值
    # num，  num=0，删除列表中所有的指定值；
           # num=2,从前到后，删除2个；
           # num=-2,从后向前，删除2个

r.lrem("l3", 'Cc')
1
r.lrange("l3", '0', '4')
[b'DD', b'CC', b'BB', b'AA']
复制代码
lpop(name)

复制代码
# 在name对应的列表的左侧获取第一个元素并在列表中移除，返回值则是第一个元素
# 更多：
    # rpop(name) 表示从右向左操作
r.lpop("l3")
b'DD'
r.lrange("l3", '0', '2')
[b'CC', b'BB', b'AA']
复制代码
ltrim(name, start, end)

复制代码
# 在name对应的列表中移除没有在start-end索引之间的值
# 参数：
    # name，redis的name
    # start，索引的起始位置
    # end，索引结束位置

r.ltrim("l3", "0", "1")
True
r.lrange("l3", '0', '3')
[b'CC', b'BB']
复制代码
rpoplpush(src, dst)

复制代码
# 从一个列表取出最右边的元素，同时将其添加至另一个列表的最左边
# 参数：
    # src，要取数据的列表的name
    # dst，要添加数据的列表的name
r.lpush("l4", '11', '22', '33')
r.lpush("l5", '44', '55', '66')
r.rpoplpush("l4", "l5")
b'11'
r.lrange("l4", '0', '3')
[b'33', b'22']
r.lrange("l5", '0', '3')
[b'11', b'66', b'55', b'44']
复制代码
blpop(keys, timeout)

复制代码
# 将多个列表排列，按照从左到右去pop对应列表的元素

# 参数：
    # keys，redis的name的集合
    # timeout，超时时间，当元素所有列表的元素获取完之后，阻塞等待列表内有数据的时间（秒）, 0 表示永远阻塞

# 更多：
    # r.brpop(keys, timeout)，从右向左获取数据

r.blpop("l5", timeout=1)
(b'l5', b'11')
r.lrange("l5",0,3)
[b'66', b'55', b'44']
复制代码
lindex(name, index)

#在name对应的列表中根据索引获取列表元素
>>> r.lrange("l3",0,3)
[b'CC', b'cc', b'BB', b'AA']
>>> r.lindex("l3","0")
b'CC'
自定义增量迭代

复制代码
# 由于redis类库中没有提供对列表元素的增量迭代，如果想要循环name对应的列表的所有元素，那么就需要：
    # 1、获取name对应的所有列表
    # 2、循环列表
# 但是，如果列表非常大，那么就有可能在第一步时就将程序的内容撑爆，所有有必要自定义一个增量迭代的功能：

def list_iter(name):
    """
    自定义redis列表增量迭代
    :param name: redis中的name，即：迭代name对应的列表
    :return: yield 返回 列表元素
    """
    list_count = r.llen(name)
    for index in range(list_count):
        yield r.lindex(name, index)

# 使用
for item in list_iter('l3'):
    print(item)
复制代码
Set操作，Set集合就是不允许重复的列表

sadd(name,values)

# name对应的集合中添加元素
scard(name)

# 获取name对应的集合中元素个数
sdiff(keys, *args)

# 在第一个name对应的集合中且不在其他name对应的集合的元素集合
sdiffstore(dest, keys, *args)

# 获取第一个name对应的集合中且不在其他name对应的集合，再将其新加入到dest对应的集合中
sinter(keys, *args)

# 获取多一个name对应集合的并集
sinterstore(dest, keys, *args)

# 获取多一个name对应集合的并集，再讲其加入到dest对应的集合中
sismember(name, value)

# 检查value是否是name对应的集合的成员
smembers(name)

# 获取name对应的集合的所有成员
smove(src, dst, value)

# 将某个成员从一个集合中移动到另外一个集合
spop(name)

# 从集合的右侧（尾部）移除一个成员，并将其返回
srandmember(name, numbers)

# 从name对应的集合中随机获取 numbers 个元素
srem(name, values)

# 在name对应的集合中删除某些值
sunion(keys, *args)

# 获取多一个name对应的集合的并集
sunionstore(dest,keys, *args)

# 获取多一个name对应的集合的并集，并将结果保存到dest对应的集合中
sscan(name, cursor=0, match=None, count=None)
sscan_iter(name, match=None, count=None)

# 同字符串的操作，用于增量迭代分批获取元素，避免内存消耗太大
有序集合，在集合的基础上，为每元素排序；元素的排序需要根据另外一个值来进行比较，所以，对于有序集合，每一个元素有两个值，即：值和分数，分数专门用来做排序。

zadd(name, *args, **kwargs)

# 在name对应的有序集合中添加元素
# 如：
     # zadd('zz', 'n1', 1, 'n2', 2)
     # 或
     # zadd('zz', n1=11, n2=22)
zcard(name)

# 获取name对应的有序集合元素的数量
zcount(name, min, max)

# 获取name对应的有序集合中分数 在 [min,max] 之间的个数
zincrby(name, value, amount)

# 自增name对应的有序集合的 name 对应的分数
r.zrange( name, start, end, desc=False, withscores=False, score_cast_func=float)

复制代码
# 按照索引范围获取name对应的有序集合的元素

# 参数：
    # name，redis的name
    # start，有序集合索引起始位置（非分数）
    # end，有序集合索引结束位置（非分数）
    # desc，排序规则，默认按照分数从小到大排序
    # withscores，是否获取元素的分数，默认只获取元素的值
    # score_cast_func，对分数进行数据转换的函数

# 更多：
    # 从大到小排序
    # zrevrange(name, start, end, withscores=False, score_cast_func=float)

    # 按照分数范围获取name对应的有序集合的元素
    # zrangebyscore(name, min, max, start=None, num=None, withscores=False, score_cast_func=float)
    # 从大到小排序
    # zrevrangebyscore(name, max, min, start=None, num=None, withscores=False, score_cast_func=float)
复制代码
zrank(name, value)

# 获取某个值在 name对应的有序集合中的排行（从 0 开始）

# 更多：
    # zrevrank(name, value)，从大到小排序
zrangebylex(name, min, max, start=None, num=None)

复制代码
# 当有序集合的所有成员都具有相同的分值时，有序集合的元素会根据成员的 值 （lexicographical ordering）来进行排序，而这个命令则可以返回给定的有序集合键 key 中， 元素的值介于 min 和 max 之间的成员
# 对集合中的每个成员进行逐个字节的对比（byte-by-byte compare）， 并按照从低到高的顺序， 返回排序后的集合成员。 如果两个字符串有一部分内容是相同的话， 那么命令会认为较长的字符串比较短的字符串要大

# 参数：
    # name，redis的name
    # min，左区间（值）。 + 表示正无限； - 表示负无限； ( 表示开区间； [ 则表示闭区间
    # min，右区间（值）
    # start，对结果进行分片处理，索引位置
    # num，对结果进行分片处理，索引后面的num个元素

# 如：
    # ZADD myzset 0 aa 0 ba 0 ca 0 da 0 ea 0 fa 0 ga
    # r.zrangebylex('myzset', "-", "[ca") 结果为：['aa', 'ba', 'ca']

# 更多：
    # 从大到小排序
    # zrevrangebylex(name, max, min, start=None, num=None)
复制代码
zrem(name, values)

# 删除name对应的有序集合中值是values的成员

# 如：zrem('zz', ['s1', 's2'])
zremrangebyrank(name, min, max)

# 根据排行范围删除
zremrangebyscore(name, min, max)

# 根据分数范围删除
zremrangebylex(name, min, max)

# 根据值返回删除
zscore(name, value)

# 获取name对应有序集合中 value 对应的分数
zinterstore(dest, keys, aggregate=None)

# 获取两个有序集合的交集，如果遇到相同值不同分数，则按照aggregate进行操作
# aggregate的值为:  SUM  MIN  MAX
zunionstore(dest, keys, aggregate=None)

# 获取两个有序集合的并集，如果遇到相同值不同分数，则按照aggregate进行操作
# aggregate的值为:  SUM  MIN  MAX
zscan(name, cursor=0, match=None, count=None, score_cast_func=float)
zscan_iter(name, match=None, count=None,score_cast_func=float)

# 同字符串相似，相较于字符串新增score_cast_func，用来对分数进行操作
其他常用操作

delete(*names)

复制代码
# 根据删除redis中的任意数据类型
r.set("test","123")
r.get('test')
b'123'
r.delete("test")
1
r.get("test")
None
复制代码
exists(name)

复制代码
# 根据删除redis中的任意数据类型
r.set("test","123")
r.get('test')
b'123'
r.delete("test")
1
r.exists("test")
False
复制代码
keys(pattern='*')

复制代码
# 根据模型获取redis的name

# 更多：
    # KEYS * 匹配数据库中所有 key 。
    # KEYS h?llo 匹配 hello ， hallo 和 hxllo 等。
    # KEYS h*llo 匹配 hllo 和 heeeeello 等。
    # KEYS h[ae]llo 匹配 hello 和 hallo ，但不匹配 hillo

r.keys(pattern="*")
[b'l5', b'parter', b'name', b'l3', b'l4', b'foo']
复制代码
expire(name ,time)

# 为某个redis的某个name设置超时时间
r.set("t","ok")
r.expire("t",3)
r.get("t")  # 隔3秒后取值
None
rename(src, dst)

# 对redis的name重命名为
r.set('rn','123')
r.rename('rn','rename')
r.get('rename')
b'123'
move(name, db))

# 将redis的某个值移动到指定的db下
randomkey()

# 随机获取一个redis的name（不删除）
type(name)

# 获取name对应值的类型
r.get("name")
b'jn'
r.type("name")
b'string'
scan(cursor=0, match=None, count=None)
scan_iter(match=None, count=None)

# 同字符串操作，用于增量迭代获取key
4、管道

redis-py默认在执行每次请求都会创建（连接池申请连接）和断开（归还连接池）一次连接操作，如果想要在一次请求中指定多个命令，则可以使用pipline实现一次请求指定多个命令，并且默认情况下一次pipline 是原子性操作。

复制代码
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis

pool = redis.ConnectionPool(host='10.211.55.4', port=6379)

r = redis.Redis(connection_pool=pool)

# pipe = r.pipeline(transaction=False)
pipe = r.pipeline(transaction=True)

r.set('username', 'koka')
r.set('passwd', '123')

pipe.execute()
复制代码
5、发布订阅



发布者：服务器

订阅者：Dashboad和数据处理

Demo如下：

 RedisHelper
订阅者：

复制代码
# !/usr/bin/env python
# -*- coding:utf-8 -*-

from monitor.RedisHelper import RedisHelper

obj = RedisHelper()
redis_sub = obj.subscribe()

while True:
    msg= redis_sub.parse_response()
    print(msg)
复制代码
发布者：

复制代码
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from monitor.RedisHelper import RedisHelper

obj = RedisHelper()
obj.public('hello')