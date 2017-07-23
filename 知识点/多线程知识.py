#coding=utf-8

import threading

u'理解：同个def中，如需要爬虫100个url，都是将url组成一个数组，多线程相当于同一时间每条线程执行100次（即总执行次数为线程数*数组数），多进程相当于同一时间执行相当于进程数的url（总执行次数为数组数），不同def中，多线程相当于每个线程执行不同的def，多进程相当于执行全部def，'

"""python 多线程就这么简单



　　多线程和多进程是什么自行google补脑

　　对于python 多线程的理解，我花了很长时间，搜索的大部份文章都不够通俗易懂。所以，这里力图用简单的例子，让你对多线程有个初步的认识。


多线程



　　科技在发展，时代在进步，我们的CPU也越来越快，CPU抱怨，P大点事儿占了我一定的时间，其实我同时干多个活都没问题的；于是，操作系统就进入了多任务时代。我们听着音乐吃着火锅的不在是梦想。

　　python提供了两个模块来实现多线程thread 和threading ，thread 有一些缺点，在threading 得到了弥补，为了不浪费你和时间，所以我们直接学习threading 就可以了。

继续对上面的例子进行改造，引入threadring来同时播放音乐和视频：

复制代码"""
#coding=utf-8
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print "I was listening to %s. %s" %(func,ctime())
        sleep(1)

def move(func):
    for i in range(2):
        print "I was at the %s! %s" %(func,ctime())
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    print "all over %s" %ctime()



import threading

#首先导入threading 模块，这是使用多线程的前提。



threads = []

t1 = threading.Thread(target=music,args=(u'爱情买卖',))

threads.append(t1)

"""　创建了threads数组，创建线程t1,使用threading.Thread()方法，在这个方法中调用music方法target=music，args方法对music进行传参。 把创建好的线程t1装到threads数组中。

　　接着以同样的方式创建线程t2，并把t2也装到threads数组。"""



for t in threads:

　　t.setDaemon(True)

　　t.start()

#最后通过for循环遍历数组。（数组被装载了t1和t2两个线程）



setDaemon()

　　setDaemon(True)#将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句print "all over %s" %ctime()后，没有等待子线程，直接就退出了，同时子线程也一同结束。



start()

#开始线程活动。



"""运行结果：

>>> ========================= RESTART ================================
>>>
I was listening to 爱情买卖. Thu Apr 17 12:51:45 2014 I was at the 阿凡达! Thu Apr 17 12:51:45 2014  all over Thu Apr 17 12:51:45 2014
　　从执行结果来看，子线程（muisc 、move ）和主线程（print "all over %s" %ctime()）都是同一时间启动，但由于主线程执行完结束，所以导致子线程也终止。



继续调整程序：

复制代码"""

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()

    print "all over %s" %ctime()

"""　　我们只对上面的程序加了个join()方法，用于等待线程终止。join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。

　　注意:  join()方法的位置是在for循环外的，也就是说必须等待for循环里的两个进程都结束后，才去执行主进程。

运行结果：

复制代码
>>> ========================= RESTART ================================
>>>
I was listening to 爱情买卖. Thu Apr 17 13:04:11 2014  I was at the 阿凡达! Thu Apr 17 13:04:11 2014

I was listening to 爱情买卖. Thu Apr 17 13:04:12 2014
I was at the 阿凡达! Thu Apr 17 13:04:16 2014
all over Thu Apr 17 13:04:21 2014
复制代码
　　从执行结果可看到，music 和move 是同时启动的。

　　开始时间4分11秒，直到调用主进程为4分22秒，总耗时为10秒。从单线程时减少了2秒，我们可以把music的sleep()的时间调整为4秒。

复制代码
"""
def music(func):
    for i in range(2):
        print "I was listening to %s. %s" %(func,ctime())
        sleep(4)

"""
执行结果：

复制代码
>>> ====================== RESTART ================================
>>>
I was listening to 爱情买卖. Thu Apr 17 13:11:27 2014I was at the 阿凡达! Thu Apr 17 13:11:27 2014

I was listening to 爱情买卖. Thu Apr 17 13:11:31 2014
I was at the 阿凡达! Thu Apr 17 13:11:32 2014
all over Thu Apr 17 13:11:37 2014
复制代码
　　子线程启动11分27秒，主线程运行11分37秒。

　　虽然music每首歌曲从1秒延长到了4 ，但通多程线的方式运行脚本，总的时间没变化。"""


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


threading

"""threading基于Java的线程模型设计。锁（Lock）和条件变量（Condition）在Java中是对象的基本行为（每一个对象都自带了锁和条件变量），而在Python中则是独立的对象。Python Thread提供了Java Thread的行为的子集；没有优先级、线程组，线程也不能被停止、暂停、恢复、中断。Java Thread中的部分被Python实现了的静态方法在threading中以模块方法的形式提供。

threading 模块提供的常用方法：
threading.currentThread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

threading模块提供的类：
Thread, Lock, Rlock, Condition, [Bounded]Semaphore, Event, Timer, local.

1、Thread

Thread是线程类，与Java类似，有两种使用方法，直接传入要运行的方法或从Thread继承并覆盖run()："""

# encoding: UTF-8
import threading

# 方法1：将要执行的方法作为参数传给Thread的构造方法
def func():
    print 'func() passed to Thread'

t = threading.Thread(target=func)
t.start()

# 方法2：从Thread继承，并重写run()
class MyThread(threading.Thread):
    def run(self):
        print 'MyThread extended from Thread'

t = MyThread()
t.start()


"""构造方法：
Thread(group=None, target=None, name=None, args=(), kwargs={})
group: 线程组，目前还没有实现，库引用中提示必须是None；
target: 要执行的方法；
name: 线程名；
args/kwargs: 要传入方法的参数。

实例方法：
isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。
get/setName(name): 获取/设置线程名。
is/setDaemon(bool): 获取/设置是否守护线程。初始值从创建该线程的线程继承。当没有非守护线程仍在运行时，程序将终止。
start(): 启动线程。
join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。

一个使用join()的例子："""

# encoding: UTF-8
import threading
import time

def context(tJoin):
    print 'in threadContext.'
    tJoin.start()

    # 将阻塞tContext直到threadJoin终止。
    tJoin.join()

    # tJoin终止后继续执行。
    print 'out threadContext.'

def join():
    print 'in threadJoin.'
    time.sleep(1)
    print 'out threadJoin.'

# tJoin和tContext分别为两个不同的线程
tJoin = threading.Thread(target=join)
tContext = threading.Thread(target=context, args=(tJoin,))

tContext.start()
"""运行结果：

 in threadContext.
 in threadJoin.
 out threadJoin.
 out threadContext."""
2、Lock

"""Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。

可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。池中的线程处于状态图中的同步阻塞状态。

构造方法：
Lock()

实例方法：
acquire([timeout]): 使线程进入同步阻塞状态，尝试获得锁定。
release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。"""

# encoding: UTF-8
import threading
import time

data = 0
lock = threading.Lock()

def func():
    global data
    print '%s acquire lock...' % threading.currentThread().getName()

    # 调用acquire([timeout])时，线程将一直阻塞，
    # 直到获得锁定或者直到timeout秒后（timeout参数可选）。
    # 返回是否获得锁。
    if lock.acquire():
        print '%s get the lock.' % threading.currentThread().getName()
        data += 1
        time.sleep(2)
        print '%s release lock...' % threading.currentThread().getName()

        # 调用release()将释放锁。
        lock.release()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()


"""多运行几次，你会看到打印的信息顺序并不一致，这就证实了线程在锁定池中谁将获得锁运行是由系统调度决定（随机，不确定）

RLock

RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。

可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。

构造方法：
RLock()

实例方法：
acquire([timeout])/release(): 跟Lock差不多。"""

# encoding: UTF-8
import threading
import time

rlock = threading.RLock()

def func():
    # 第一次请求锁定
    print '%s acquire lock...' % threading.currentThread().getName()
    if rlock.acquire():
        print '%s get the lock.' % threading.currentThread().getName()
        time.sleep(2)

        # 第二次请求锁定
        print '%s acquire lock again...' % threading.currentThread().getName()
        if rlock.acquire():
            print '%s get the lock.' % threading.currentThread().getName()
            time.sleep(2)

        # 第一次释放锁
        print '%s release lock...' % threading.currentThread().getName()
        rlock.release()
        time.sleep(2)

        # 第二次释放锁
        print '%s release lock...' % threading.currentThread().getName()
        rlock.release()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()


4、Condition

"""Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。

可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于状态图中的等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。

构造方法：
Condition([lock/rlock])

实例方法：
acquire([timeout])/release(): 调用关联的锁的相应方法。
wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。
notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。

例子是很常见的生产者/消费者模式："""

# encoding: UTF-8
import threading
import time

# 商品
product = None
# 条件变量
con = threading.Condition()

# 生产者方法
def produce():
    global product

    if con.acquire():
        while True:
            if product is None:
                print 'produce...'
                product = 'anything'

                # 通知消费者，商品已经生产
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)

# 消费者方法
def consume():
    global product

    if con.acquire():
        while True:
            if product is not None:
                print 'consume...'
                product = None

                # 通知生产者，商品已经没了
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)

t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t2.start()
t1.start()
5、Semaphore/BoundedSemaphore

"""Semaphore（信号量）是计算机科学史上最古老的同步指令之一。Semaphore管理一个内置的计数器，每当调用acquire()时-1，调用release() 时+1。计数器不能小于0；当计数器为0时，acquire()将阻塞线程至同步锁定状态，直到其他线程调用release()。

基于这个特点，Semaphore经常用来同步一些有“访客上限”的对象，比如连接池。

BoundedSemaphore 与Semaphore的唯一区别在于前者将在调用release()时检查计数器的值是否超过了计数器的初始值，如果超过了将抛出一个异常。

构造方法：
Semaphore(value=1): value是计数器的初始值。

实例方法：
acquire([timeout]): 请求Semaphore。如果计数器为0，将阻塞线程至同步阻塞状态；否则将计数器-1并立即返回。
release(): 释放Semaphore，将计数器+1，如果使用BoundedSemaphore，还将进行释放次数检查。release()方法不检查线程是否已获得 Semaphore。"""

# encoding: UTF-8
import threading
import time

# 计数器初值为2
semaphore = threading.Semaphore(2)

def func():

    # 请求Semaphore，成功后计数器-1；计数器为0时阻塞
    print '%s acquire semaphore...' % threading.currentThread().getName()
    if semaphore.acquire():

        print '%s get semaphore' % threading.currentThread().getName()
        time.sleep(4)

        # 释放Semaphore，计数器+1
        print '%s release semaphore' % threading.currentThread().getName()
        semaphore.release()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t4 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()
t4.start()

time.sleep(2)

# 没有获得semaphore的主线程也可以调用release
# 若使用BoundedSemaphore，t4释放semaphore时将抛出异常
print 'MainThread release semaphore without acquire'
semaphore.release()


6、Event

"""Event（事件）是最简单的线程通信机制之一：一个线程通知事件，其他线程等待事件。Event内置了一个初始为False的标志，当调用set()时设为True，调用clear()时重置为 False。wait()将阻塞线程至等待阻塞状态。

Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。

构造方法：
Event()

实例方法：
isSet(): 当内置标志为True时返回True。
set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。
clear(): 将标志设为False。
wait([timeout]): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()。"""

# encoding: UTF-8
import threading
import time

event = threading.Event()

def func():
    # 等待事件，进入等待阻塞状态
    print '%s wait for event...' % threading.currentThread().getName()
    event.wait()

    # 收到事件后进入运行状态
    print '%s recv event.' % threading.currentThread().getName()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()
t2.start()

time.sleep(2)

# 发送事件通知
print 'MainThread set event.'
event.set()


"""Timer

Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法。

构造方法：
Timer(interval, function, args=[], kwargs={})
interval: 指定的时间
function: 要执行的方法
args/kwargs: 方法的参数

实例方法：
Timer从Thread派生，没有增加实例方法。"""

# encoding: UTF-8
import threading

def func():
    print 'hello timer!'

timer = threading.Timer(5, func)
timer.start()


8、local

"""local是一个小写字母开头的类，用于管理 thread-local（线程局部的）数据。对于同一个local，线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换。

可以把local看成是一个“线程-属性字典”的字典，local封装了从自身使用线程作为 key检索对应的属性字典、再使用属性名作为key检索属性值的细节。"""

# encoding: UTF-8
import threading

local = threading.local()
local.tname = 'main'

def func():
    local.tname = 'notmain'
    print local.tname

t1 = threading.Thread(target=func)
t1.start()
t1.join()

print local.tname


"""熟练掌握Thread、Lock、Condition就可以应对绝大多数需要使用线程的场合，某些情况下local也是非常有用的东西。本文的最后使用这几个类展示线程基础中提到的场景："""

# encoding: UTF-8
import threading

alist = None
condition = threading.Condition()

def doSet():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in range(len(alist))[::-1]:
            alist[i] = 1
        condition.release()

def doPrint():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in alist:
            print i,
        print
        condition.release()

def doCreate():
    global alist
    if condition.acquire():
        if alist is None:
            alist = [0 for i in range(10)]
            condition.notifyAll()
        condition.release()

tset = threading.Thread(target=doSet,name='tset')
tprint = threading.Thread(target=doPrint,name='tprint')
tcreate = threading.Thread(target=doCreate,name='tcreate')
tset.start()
tprint.start()
tcreate.start()

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

python--threading多线程总结
threading用于提供线程相关的操作，线程是应用程序中工作的最小单元。python当前版本的多线程库没有实现优先级、线程组，线程也不能被停止、暂停、恢复、中断。

threading模块提供的类：
　　Thread, Lock, Rlock, Condition, [Bounded]Semaphore, Event, Timer, local。

threading 模块提供的常用方法：
　　threading.currentThread(): 返回当前的线程变量。
　　threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
　　threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。

threading 模块提供的常量：

　　threading.TIMEOUT_MAX 设置threading全局超时时间。



Thread类



Thread是线程类，有两种使用方法，直接传入要运行的方法或从Thread继承并覆盖run()：


复制代码
# coding:utf-8
import threading
import time
#方法一：将要执行的方法作为参数传给Thread的构造方法
def action(arg):
    time.sleep(1)
    print 'the arg is:%s\r' %arg

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.start()

print 'main thread end!'

#方法二：从Thread继承，并重写run()
class MyThread(threading.Thread):
    def __init__(self,arg):
        super(MyThread, self).__init__()#注意：一定要显式的调用父类的初始化函数。
        self.arg=arg
    def run(self):#定义每个线程要运行的函数
        time.sleep(1)
        print 'the arg is:%s\r' % self.arg

for i in xrange(4):
    t =MyThread(i)
    t.start()

print 'main thread end!'
复制代码


构造方法：
Thread(group=None, target=None, name=None, args=(), kwargs={})

　　group: 线程组，目前还没有实现，库引用中提示必须是None；
　　target: 要执行的方法；
　　name: 线程名；
　　args/kwargs: 要传入方法的参数。

实例方法：
　　isAlive(): 返回线程是否在运行。正在运行指启动后、终止前。
　　get/setName(name): 获取/设置线程名。

　　start():  线程准备就绪，等待CPU调度
　　is/setDaemon(bool): 获取/设置是后台线程（默认前台线程（False））。（在start之前设置）

　　　　如果是后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程和后台线程均停止
       　　如果是前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
　　start(): 启动线程。
　　join([timeout]): 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）。



使用例子一(未设置setDeamon)：




复制代码
# coding:utf-8
import threading
import time

def action(arg):
    time.sleep(1)
    print  'sub thread start!the thread name is:%s\r' % threading.currentThread().getName()
    print 'the arg is:%s\r' %arg
    time.sleep(1)

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.start()

print 'main_thread end!'
复制代码



复制代码
main_thread end!
sub thread start!the thread name is:Thread-2
the arg is:1
the arg is:0
sub thread start!the thread name is:Thread-4
the arg is:2
the arg is:3
Process finished with exit code 0
可以看出，创建的4个“前台”线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，程序停止
复制代码
验证了serDeamon(False)(默认)前台线程，主线程执行过程中，前台线程也在进行，主线程执行完毕后，等待前台线程也执行完成后，主线程停止。



使用例子二（setDeamon=True）


复制代码
# coding:utf-8
import threading
import time

def action(arg):
    time.sleep(1)
    print  'sub thread start!the thread name is:%s\r' % threading.currentThread().getName()
    print 'the arg is:%s\r' %arg
    time.sleep(1)

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.setDaemon(True)#设置线程为后台线程
    t.start()

print 'main_thread end!'
复制代码

main_thread end!

Process finished with exit code 0

可以看出，主线程执行完毕后，后台线程不管是成功与否，主线程均停止
验证了serDeamon(True)后台线程，主线程执行过程中，后台线程也在进行，主线程执行完毕后，后台线程不论成功与否，主线程均停止。



使用例子三（设置join）


复制代码
#coding:utf-8
import threading
import time

def action(arg):
    time.sleep(1)
    print  'sub thread start!the thread name is:%s    ' % threading.currentThread().getName()
    print 'the arg is:%s   ' %arg
    time.sleep(1)

thread_list = []    #线程存放列表
for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.setDaemon(True)
    thread_list.append(t)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()
复制代码
 运行结果
验证了 join()阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout，即使设置了setDeamon（True）主线程依然要等待子线程结束。

使用例子四（join不妥当的用法，使多线程编程顺序执行）


复制代码
#coding:utf-8
import threading
import time

def action(arg):
    time.sleep(1)
    print  'sub thread start!the thread name is:%s    ' % threading.currentThread().getName()
    print 'the arg is:%s   ' %arg
    time.sleep(1)


for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.setDaemon(True)
    t.start()
    t.join()

print 'main_thread end!'
复制代码

复制代码
sub thread start!the thread name is:Thread-1
the arg is:0
sub thread start!the thread name is:Thread-2
the arg is:1
sub thread start!the thread name is:Thread-3
the arg is:2
sub thread start!the thread name is:Thread-4
the arg is:3
main_thread end!

Process finished with exit code 0
可以看出此时，程序只能顺序执行，每个线程都被上一个线程的join阻塞，使得“多线程”失去了多线程意义。
复制代码




Lock、Rlock类



　　由于线程之间随机调度：某线程可能在执行n条后，CPU接着执行其他线程。为了多个线程同时操作一个内存中的资源时不产生混乱，我们使用锁。

Lock（指令锁）是可用的最低级的同步指令。Lock处于锁定状态时，不被特定的线程拥有。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。

可以认为Lock有一个锁定池，当线程请求锁定时，将线程至于池中，直到获得锁定后出池。池中的线程处于状态图中的同步阻塞状态。

RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。

可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。

简言之：Lock属于全局，Rlock属于线程。

构造方法：
Lock()，Rlock（）,推荐使用Rlock()

实例方法：
　　acquire([timeout]): 尝试获得锁定。使线程进入同步阻塞状态。
　　release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。

例子一（未使用锁）：


复制代码
#coding:utf-8
import threading
import time

gl_num = 0

def show(arg):
    global gl_num
    time.sleep(1)
    gl_num +=1
    print gl_num

for i in range(10):
    t = threading.Thread(target=show, args=(i,))
    t.start()

print 'main thread stop'
复制代码

复制代码
main thread stop
12

 3
4
568
 9

910


Process finished with exit code 0

多次运行可能产生混乱。这种场景就是适合使用锁的场景。
复制代码


例子二（使用锁）:


复制代码
# coding:utf-8

import threading
import time

gl_num = 0

lock = threading.RLock()


# 调用acquire([timeout])时，线程将一直阻塞，
# 直到获得锁定或者直到timeout秒后（timeout参数可选）。
# 返回是否获得锁。
def Func():
    lock.acquire()
    global gl_num
    gl_num += 1
    time.sleep(1)
    print gl_num
    lock.release()


for i in range(10):
    t = threading.Thread(target=Func)
    t.start()
复制代码

复制代码
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

Process finished with exit code 0
可以看出，全局变量在在每次被调用时都要获得锁，才能操作，因此保证了共享数据的安全性
复制代码


Lock对比Rlock

#coding:utf-8

import threading
lock = threading.Lock() #Lock对象
lock.acquire()
lock.acquire()  #产生了死锁。
lock.release()
lock.release()
print lock.acquire()


import threading
rLock = threading.RLock()  #RLock对象
rLock.acquire()
rLock.acquire() #在同一线程内，程序不会堵塞。
rLock.release()
rLock.release()


Condition类



　　Condition（条件变量）通常与一个锁关联。需要在多个Contidion中共享一个锁时，可以传递一个Lock/RLock实例给构造方法，否则它将自己生成一个RLock实例。

　　可以认为，除了Lock带有的锁定池外，Condition还包含一个等待池，池中的线程处于等待阻塞状态，直到另一个线程调用notify()/notifyAll()通知；得到通知后线程进入锁定池等待锁定。

构造方法：
Condition([lock/rlock])

实例方法：
　　acquire([timeout])/release(): 调用关联的锁的相应方法。
　　wait([timeout]): 调用这个方法将使线程进入Condition的等待池等待通知，并释放锁。使用前线程必须已获得锁定，否则将抛出异常。
　　notify(): 调用这个方法将从等待池挑选一个线程并通知，收到通知的线程将自动调用acquire()尝试获得锁定（进入锁定池）；其他线程仍然在等待池中。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。
　　notifyAll(): 调用这个方法将通知等待池中所有的线程，这些线程都将进入锁定池尝试获得锁定。调用这个方法不会释放锁定。使用前线程必须已获得锁定，否则将抛出异常。



例子一：生产者消费者模型


复制代码
# encoding: UTF-8
import threading
import time

# 商品
product = None
# 条件变量
con = threading.Condition()


# 生产者方法
def produce():
    global product

    if con.acquire():
        while True:
            if product is None:
                print 'produce...'
                product = 'anything'

                # 通知消费者，商品已经生产
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


# 消费者方法
def consume():
    global product

    if con.acquire():
        while True:
            if product is not None:
                print 'consume...'
                product = None

                # 通知生产者，商品已经没了
                con.notify()

            # 等待通知
            con.wait()
            time.sleep(2)


t1 = threading.Thread(target=produce)
t2 = threading.Thread(target=consume)
t2.start()
t1.start()
复制代码

复制代码
produce...
consume...
produce...
consume...
produce...
consume...
produce...
consume...
produce...
consume...

Process finished with exit code -1
程序不断循环运行下去。重复生产消费过程。
复制代码
例子二：生产者消费者模型


复制代码
import threading
import time

condition = threading.Condition()
products = 0

class Producer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products < 10:
                    products += 1;
                    print "Producer(%s):deliver one, now products:%s" %(self.name, products)
                    condition.notify()#不释放锁定，因此需要下面一句
                    condition.release()
                else:
                    print "Producer(%s):already 10, stop deliver, now products:%s" %(self.name, products)
                    condition.wait();#自动释放锁定
                time.sleep(2)

class Consumer(threading.Thread):
    def run(self):
        global products
        while True:
            if condition.acquire():
                if products > 1:
                    products -= 1
                    print "Consumer(%s):consume one, now products:%s" %(self.name, products)
                    condition.notify()
                    condition.release()
                else:
                    print "Consumer(%s):only 1, stop consume, products:%s" %(self.name, products)
                    condition.wait();
                time.sleep(2)

if __name__ == "__main__":
    for p in range(0, 2):
        p = Producer()
        p.start()

    for c in range(0, 3):
        c = Consumer()
        c.start()
复制代码
例子三：


复制代码
import threading

alist = None
condition = threading.Condition()

def doSet():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in range(len(alist))[::-1]:
            alist[i] = 1
        condition.release()

def doPrint():
    if condition.acquire():
        while alist is None:
            condition.wait()
        for i in alist:
            print i,
        print
        condition.release()

def doCreate():
    global alist
    if condition.acquire():
        if alist is None:
            alist = [0 for i in range(10)]
            condition.notifyAll()
        condition.release()

tset = threading.Thread(target=doSet,name='tset')
tprint = threading.Thread(target=doPrint,name='tprint')
tcreate = threading.Thread(target=doCreate,name='tcreate')
tset.start()
tprint.start()
tcreate.start()
复制代码


Event类



　　Event（事件）是最简单的线程通信机制之一：一个线程通知事件，其他线程等待事件。Event内置了一个初始为False的标志，当调用set()时设为True，调用clear()时重置为 False。wait()将阻塞线程至等待阻塞状态。

　　Event其实就是一个简化版的 Condition。Event没有锁，无法使线程进入同步阻塞状态。

构造方法：
Event()

实例方法：
　　isSet(): 当内置标志为True时返回True。
　　set(): 将标志设为True，并通知所有处于等待阻塞状态的线程恢复运行状态。
　　clear(): 将标志设为False。
　　wait([timeout]): 如果标志为True将立即返回，否则阻塞线程至等待阻塞状态，等待其他线程调用set()。



例子一


复制代码
# encoding: UTF-8
import threading
import time

event = threading.Event()


def func():
    # 等待事件，进入等待阻塞状态
    print '%s wait for event...' % threading.currentThread().getName()
    event.wait()

    # 收到事件后进入运行状态
    print '%s recv event.' % threading.currentThread().getName()


t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t1.start()
t2.start()

time.sleep(2)

# 发送事件通知
print 'MainThread set event.'
event.set()
复制代码



复制代码
Thread-1 wait for event...
Thread-2 wait for event...

#2秒后。。。
MainThread set event.
Thread-1 recv event.
 Thread-2 recv event.

Process finished with exit code 0
复制代码


timer类



　　Timer（定时器）是Thread的派生类，用于在指定时间后调用一个方法。

构造方法：
Timer(interval, function, args=[], kwargs={})
　　interval: 指定的时间
　　function: 要执行的方法
　　args/kwargs: 方法的参数

实例方法：
Timer从Thread派生，没有增加实例方法。

例子一：


复制代码
# encoding: UTF-8
import threading


def func():
    print 'hello timer!'


timer = threading.Timer(5, func)
timer.start()
复制代码
线程延迟5秒后执行。



local类





　　local是一个小写字母开头的类，用于管理 thread-local（线程局部的）数据。对于同一个local，线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换。

　　可以把local看成是一个“线程-属性字典”的字典，local封装了从自身使用线程作为 key检索对应的属性字典、再使用属性名作为key检索属性值的细节。


复制代码
# encoding: UTF-8
import threading

local = threading.local()
local.tname = 'main'

def func():
    local.tname = 'notmain'
    print local.tname

t1 = threading.Thread(target=func)
t1.start()
t1.join()

print local.tname
复制代码

notmain
main

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Python 多线程

多线程类似于同时执行多个不同程序，多线程运行有如下优点：
使用线程可以把占据长时间的程序中的任务放到后台去处理。
用户界面可以更加吸引人，这样比如用户点击了一个按钮去触发某些事件的处理，可以弹出一个进度条来显示处理的进度
程序的运行速度可能加快
在一些等待的任务实现上如用户输入、文件读写和网络收发数据等，线程就比较有用了。在这种情况下我们可以释放一些珍贵的资源如内存占用等等。
线程在执行过程中与进程还是有区别的。每个独立的线程有一个程序运行的入口、顺序执行序列和程序的出口。但是线程不能够独立执行，必须依存在应用程序中，由应用程序提供多个线程执行控制。
每个线程都有他自己的一组CPU寄存器，称为线程的上下文，该上下文反映了线程上次运行该线程的CPU寄存器的状态。
指令指针和堆栈指针寄存器是线程上下文中两个最重要的寄存器，线程总是在进程得到上下文中运行的，这些地址都用于标志拥有线程的进程地址空间中的内存。
线程可以被抢占（中断）。
在其他线程正在运行时，线程可以暂时搁置（也称为睡眠） -- 这就是线程的退让。

开始学习Python线程
Python中使用线程有两种方式：函数或者用类来包装线程对象。
函数式：调用thread模块中的start_new_thread()函数来产生新线程。语法如下:
thread.start_new_thread ( function, args[, kwargs] )
参数说明:
function - 线程函数。
args - 传递给线程函数的参数,他必须是个tuple类型。
kwargs - 可选参数。
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time

# 为线程定义一个函数
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print "%s: %s" % ( threadName, time.ctime(time.time()) )

# 创建两个线程
try:
   thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass
执行以上程序输出结果如下：
Thread-1: Thu Jan 22 15:42:17 2009
Thread-1: Thu Jan 22 15:42:19 2009
Thread-2: Thu Jan 22 15:42:19 2009
Thread-1: Thu Jan 22 15:42:21 2009
Thread-2: Thu Jan 22 15:42:23 2009
Thread-1: Thu Jan 22 15:42:23 2009
Thread-1: Thu Jan 22 15:42:25 2009
Thread-2: Thu Jan 22 15:42:27 2009
Thread-2: Thu Jan 22 15:42:31 2009
Thread-2: Thu Jan 22 15:42:35 2009
线程的结束一般依靠线程函数的自然结束；也可以在线程函数中调用thread.exit()，他抛出SystemExit exception，达到退出线程的目的。
线程模块
Python通过两个标准库thread和threading提供对线程的支持。thread提供了低级别的、原始的线程以及一个简单的锁。
thread 模块提供的其他方法：
threading.currentThread(): 返回当前的线程变量。
threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
run(): 用以表示线程活动的方法。
start():启动线程活动。
join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
isAlive(): 返回线程是否活动的。
getName(): 返回线程名。
setName(): 设置线程名。
使用Threading模块创建线程
使用Threading模块创建线程，直接从threading.Thread继承，然后重写__init__方法和run方法：
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

exitFlag = 0

class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        print "Starting " + self.name
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threading.Thread.exit()
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

print "Exiting Main Thread"
以上程序执行结果如下；
Starting Thread-1
Starting Thread-2
Exiting Main Thread
Thread-1: Thu Mar 21 09:10:03 2013
Thread-1: Thu Mar 21 09:10:04 2013
Thread-2: Thu Mar 21 09:10:04 2013
Thread-1: Thu Mar 21 09:10:05 2013
Thread-1: Thu Mar 21 09:10:06 2013
Thread-2: Thu Mar 21 09:10:06 2013
Thread-1: Thu Mar 21 09:10:07 2013
Exiting Thread-1
Thread-2: Thu Mar 21 09:10:08 2013
Thread-2: Thu Mar 21 09:10:10 2013
Thread-2: Thu Mar 21 09:10:12 2013
Exiting Thread-2
线程同步
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
使用Thread对象的Lock和Rlock可以实现简单的线程同步，这两个对象都有acquire方法和release方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到acquire和release方法之间。如下：
多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。
考虑这样一种情况：一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。
那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。
锁有两种状态——锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；如果已经有别的线程比如"print"获得锁定了，那么就让线程"set"暂停，也就是同步阻塞；等到线程"print"访问完毕，释放锁以后，再让线程"set"继续。
经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import threading
import time

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print "Starting " + self.name
       # 获得锁，成功获得锁定后返回True
       # 可选的timeout参数不填时将一直阻塞直到获得锁定
       # 否则超时后将返回False
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁
        threadLock.release()

def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

threadLock = threading.Lock()
threads = []

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"
线程优先级队列（ Queue）
Python的Queue模块中提供了同步的、线程安全的队列类，包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列PriorityQueue。这些队列都实现了锁原语，能够在多线程中直接使用。可以使用队列来实现线程间的同步。
Queue模块中的常用方法:
Queue.qsize() 返回队列的大小
Queue.empty() 如果队列为空，返回True,反之False
Queue.full() 如果队列满了，返回True,反之False
Queue.full 与 maxsize 大小对应
Queue.get([block[, timeout]])获取队列，timeout等待时间
Queue.get_nowait() 相当Queue.get(False)
Queue.put(item) 写入队列，timeout等待时间
Queue.put_nowait(item) 相当Queue.put(item, False)
Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
Queue.join() 实际上意味着等到队列为空，再执行别的操作
实例(Python 2.0+)
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Queue
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print "Starting " + self.name
        process_data(self.name, self.q)
        print "Exiting " + self.name

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)
threads = []
threadID = 1

# 创建新线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print "Exiting Main Thread"
以上程序执行结果：
Starting Thread-1
Starting Thread-2
Starting Thread-3
Thread-1 processing One
Thread-2 processing Two
Thread-3 processing Three
Thread-1 processing Four
Thread-2 processing Five
Exiting Thread-3
Exiting Thread-1
Exiting Thread-2
Exiting Main Thread


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
多线程爬虫涉及到的知识点：
其实对于任何软件项目而言，我们凡是想知道编写这个项目需要什么知识点，我们都可以观察一下这个项目的主要入口文件都导入了哪些包。

现在来看一下我们这个项目，作为一个刚接触python的人，可能有一些包几乎都没有用过，那么我们在本小节就来简单的说说这些包起什么作用，要掌握他们分别会涉及到什么知识点，这些知识点的关键词是什么。这篇文章并不会花费长篇大论来从基础讲起，因此我们要学会善用百度，搜索这些知识点的关键词来自学。下面就来一一分析一下这些知识点。
HTTP协议：
我们的爬虫抓取数据本质上就是不停的发起http请求，获取http响应，将其存入我们的电脑中。了解http协议有助于我们在抓取数据的时候对一些能够加速抓取速度的参数能够精准的控制，比如说keep-alive等。
threading模块（多线程）：
我们平时编写的程序都是单线程程序，我们写的代码都在主线程里面运行，这个主线程又运行在python进程中。关于线程和进程的解释可以参考阮一峰的博客：进程与线程的一个简单解释 – 阮一峰的网络日志
在python中实现多线程是通过一个名字叫做threading的模块来实现。之前还有thread模块，但是threading对于线程的控制更强，因此我们后来都改用threading来实现多线程编程了。
关于threading多线程的一些用法，我觉得这篇文章不错：[python] 专题八.多线程编程之thread和threading 大家可以参考参考。
简单来说，使用threading模块编写多线程程序，就是先自己定义一个类，然后这个类要继承threading.Thread，并且把每个线程要做的工作代码写到一个类的run方法中，当然如果线程本身在创建的时候如果要做一些初始化工作，那么就要在他的__init__方法中编写好初始化工作所要执行的代码，这个方法就像php，java中的构造方法一样。
这里还要额外讲的一点就是线程安全这个概念。通常情况下我们单线程情况下每个时刻只有一个线程在对资源（文件，变量）操作，所以不可能会出现冲突。但是当多线程的情况下，可能会出现同一个时刻两个线程在操作同一个资源，导致资源损坏，所以我们需要一种机制来解决这种冲突带来的破坏，通常有加锁等操作，比如说mysql数据库的innodb表引擎有行级锁等，文件操作有读取锁等等，这些都是他们的程序底层帮我们完成了。所以我们通常只要知道那些操作，或者那些程序对于线程安全问题做了处理，然后就可以在多线程编程中去使用它们了。而这种考虑到线程安全问题的程序一般就叫做“线程安全版本”，比如说php就有TS版本，这个TS就是Thread Safety线程安全的意思。下面我们要讲到的Queue模块就是一种线程安全的队列数据结构，所以我们可以放心的在多线程编程中使用它。
最后我们就要来讲讲至关重要的线程阻塞这个概念了。当我们详细学习完threading模块之后，大概就知道如何创建和启动线程了。但是如果我们把线程创建好了，然后调用了start方法，那么我们会发现好像整个程序立马就结束了，这是怎么回事呢？其实这是因为我们在主线程中只有负责启动子线程的代码，也就意味着主线程只有启动子线程的功能，至于子线程执行的那些代码，他们本质上只是写在类里面的一个方法，并没在主线程里面真正去执行他，所以主线程启动完子线程之后他的本职工作就已经全部完成了，已经光荣退场了。既然主线程都退场了，那么python进程就跟着结束了，那么其他线程也就没有内存空间继续执行了。所以我们应该是要让主线程大哥等到所有的子线程小弟全部执行完毕再光荣退场，那么在线程对象中有什么方法能够把主线程卡住呢？thread.sleep嘛？这确实是个办法，但是究竟应该让主线程sleep多久呢？我们并不能准确知道执行完一个任务要多久时间，肯定不能用这个办法。所以我们这个时候应该上网查询一下有什么办法能够让子线程“卡住”主线程呢？“卡住”这个词好像太粗鄙了，其实说专业一点，应该叫做“阻塞”，所以我们可以查询“python 子线程阻塞主线程”，如果我们会正确使用搜索引擎的话，应该会查到一个方法叫做join()，没错，这个join()方法就是子线程用于阻塞主线程的方法，当子线程还未执行完毕的时候，主线程运行到含有join()方法的这一行就会卡在那里，直到所有线程都执行完毕才会执行join()方法后面的代码。
Queue模块（队列）：
假设有一个这样的场景，我们需要抓取一个人的博客，我们知道这个人的博客有两个页面，一个list.php页面显示的是此博客的所有文章链接，还有一个view.php页面显示的是一篇文章的具体内容。
如果我们要把这个人的博客里面所有文章内容抓取下来，编写单线程爬虫的思路是：先用正则表达式把这个list.php页面的所有链接a标签的href属性抓取下来，存入一个名字叫做article_list的数组（在python中不叫数组，叫做list，中文名列表），然后再用一个for循环遍历这个article_list数组，用各种抓取网页内容的函数把内容抓取下来然后存入数据库。
如果我们要编写一个多线程爬虫来完成这个任务的话，就假设我们的程序用10个线程把，那么我们就要想办法把之前抓取的article_list平均分成10份，分别把每一份分配给其中一个子线程。
但是问题来了，如果我们的article_list数组长度不是10的倍数，也就是文章数量并不是10的整数倍，那么最后一个线程就会比别的线程少分配到一些任务，那么它将会更快的结束。
如果仅仅是抓取这种只有几千字的博客文章这看似没什么问题，但是如果我们一个任务（不一定是抓取网页的任务，有可能是数学计算，或者图形渲染等等耗时任务）的运行时间很长，那么这将造成极大地资源和时间浪费。我们多线程的目的就是尽可能的利用一切计算资源并且计算时间，所以我们要想办法让任务能够更加科学合理的分配。
并且我还要考虑一种情况，就是文章数量很大的情况下，我们要既能快速抓取到文章内容，又能尽快的看到我们已经抓取到的内容，这种需求在很多CMS采集站上经常会体现出来。
比如说我们现在要抓取的目标博客，有几千万篇文章，通常这种情况下博客都会做分页处理，那么我们如果按照上面的传统思路先抓取完list.php的所有页面起码就要几个小时甚至几天，老板如果希望你能够尽快显示出抓取内容，并且尽快将已经抓取到的内容展现到我们的CMS采集站上，那么我们就要实现一边抓取list.php并且把已经抓取到的数据丢入一个article_list数组，一边用另一个线程从article_list数组中提取已经抓取到的文章URL地址，然后这个线程再去对应的URL地址中用正则表达式取到博客文章内容。如何实现这个功能呢？
我们就需要同时开启两类线程，一类线程专门负责抓取list.php中的url然后丢入article_list数组，另外一类线程专门负责从article_list中提取出url然后从对应的view.php页面中抓取出对应的博客内容。
但是我们是否还记得前面提到过线程安全这个概念？前一类线程一边往article_list数组中写入数据，另外那一类的线程从article_list中读取数据并且删除已经读取完毕的数据。但是python中list并不是线程安全版本的数据结构，因此这样操作会导致不可预料的错误。所以我们可以尝试使用一个更加方便且线程安全的数据结构，这就是我们的子标题中所提到的Queue队列数据结构。
同样Queue也有一个join()方法，这个join()方法其实和上一个小节所讲到的threading中join()方法差不多，只不过在Queue中，join()的阻塞条件是当队列不为空空的时候才阻塞，否则继续执行join()后面的代码。在这个爬虫中我便使用了这种方法来阻塞主线程而不是直接通过线程的join方式来阻塞主线程，这样的好处是可以不用写一个死循环来判断当前任务队列中是否还有未执行完的任务，让程序运行更加高效，也让代码更加优雅。
还有一个细节就是在python2.7中队列模块的名字是Queue，而在python3.x中已经改名为queue，就是首字母大小写的区别，大家如果是复制网上的代码，要记得这个小区别。
getopt模块：
如果大家学过c语言的话，对这个模块应该会很熟悉，他就是一个负责从命令行中的命令里面提取出附带参数的模块。比如说我们通常在命令行中操作mysql数据库，就是输入mysql -h127.0.0.1 -uroot -p，其中mysql后面的“-h127.0.0.1 -uroot -p”就是可以获取的参数部分。
我们平时在编写爬虫的时候，有一些参数是需要用户自己手动输入的，比如说mysql的主机IP，用户名密码等等。为了让我们的程序更加友好通用，有一些配置项是不需要硬编码在代码里面，而是在执行他的时候我们动态传入，结合getopt模块我们就可以实现这个功能。
hashlib（哈希）：
哈希本质上就是一类数学算法的集合，这种数学算法有个特性就是你给定一个参数，他能够输出另外一个结果，虽然这个结果很短，但是他可以近似认为是独一无二的。比如说我们平时听过的md5，sha-1等等，他们都属于哈希算法。他们可以把一些文件，文字经过一系列的数学运算之后变成短短不到一百位的一段数字英文混合的字符串。
python中的hashlib模块就为我们封装好了这些数学运算函数，我们只需要简单的调用它就可以完成哈希运算。
为什么在我这个爬虫中用到了这个包呢？因为在一些接口请求中，服务器需要带上一些校验码，保证接口请求的数据没有被篡改或者丢失，这些校验码一般都是hash算法，所以我们需要用到这个模块来完成这种运算。
json：
很多时候我们抓取到的数据不是html，而是一些json数据，json本质上只是一段含有键值对的字符串，如果我们需要提取出其中特定的字符串，那么我们需要json这个模块来将这个json字符串转换为dict类型方便我们操作。
re（正则表达式）：
有的时候我们抓取到了一些网页内容，但是我们需要将网页中的一些特定格式的内容提取出来，比如说电子邮箱的格式一般都是前面几位英文数字字母加一个@符号加http://xxx.xxx的域名，而要像计算机语言描述这种格式，我们可以使用一种叫做正则表达式的表达式来表达出这种格式，并且让计算机自动从一大段字符串中将符合这种特定格式的文字匹配出来。
sys：
这个模块主要用于处理一些系统方面的事情，在这个爬虫中我用他来解决输出编码问题。
time：
稍微学过一点英语的人都能够猜出来这个模块用于处理时间，在这个爬虫中我用它来获取当前时间戳，然后通过在主线程末尾用当前时间戳减去程序开始运行时的时间戳，得到程序的运行时间。

如图所示，开50个线程抓取100页（每页30个帖子，相当于抓取了3000个帖子）贴吧帖子内容并且从中提取出手机邮箱这个步骤共耗时330秒。
urllib和urllib2：
这两个模块都是用于处理一些http请求，以及url格式化方面的事情。我的爬虫http请求部分的核心代码就是使用这个模块完成的。
MySQLdb：
这是一个第三方模块，用于在python中操作mysql数据库。
这里我们要注意一个细节问题：mysqldb模块并不是线程安全版本，意味着我们不能在多线程中共享同一个mysql连接句柄。所以大家可以在我的代码中看到，我在每个线程的构造函数中都传入了一个新的mysql连接句柄。因此每个子线程只会用自己独立的mysql连接句柄。
cmd_color_printers：
这也是一个第三方模块，网上能够找到相关代码，这个模块主要用于向命令行中输出彩色字符串。比如说我们通常爬虫出现错误，要输出红色的字体会比较显眼，就要使用到这个模块。
自动化爬虫的错误处理：

如果大家在网络质量不是很好的环境下使用该爬虫，会发现有的时候会报如图所示的异常，这是我为了偷懒并没有写各种异常处理的逻辑。
通常情况下我们如果要编写高度自动化的爬虫，那么就需要预料到我们的爬虫可能会遇到的所有异常情况，针对这些异常情况做处理。
比如说如图所示的错误，我们就应该把当时正在处理的任务重新塞入任务队列，否则我们就会出现遗漏信息的情况。这也是爬虫编写的一个复杂点。"""



--------------------------------------------------------------------------------------
Queue模块学习
"""前面了解了一下threading，发现一般都是和queue模块配合使用的，queue产生一个队列，队列模式有3种，针对这三种队列分别有三个构造函数:

    1 FIFO队列先进先出：class Queue.Queue(maxsize)

    2 LIFO类似于堆,即先进后出：class Queue.LifoQueue(maxsize)

    3 优先级队列级别越低越先出来：class Queue.PriorityQueue(maxsize)

    队列长度可为无限或者有限。可通过Queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。调用队列对象的put()方法在队尾插入一个项目。put()有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数， 默认为1。如果队列当前为空且block为1，put()方法就使调用线程暂停,直到空出一个数据单元。如果block为0，put方法将引发Full异常。调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为1。如果队列为空且block为1，get()就使调用线程暂停，直至有项目可用。如果block为0，队列将引发Empty异常。join()保持阻塞状态，直到处理了队列中的所有项目为止。在将一个项目添加到该队列时，未完成的任务的总数就会增加。当使用者线程调用task_done()以表示检索了该项目、并完成了所有的工作时，那么未完成的任务的总数就会减少。当未完成的任务的总数减少到零时，join() 就会结束阻塞状态。



   队列实例分别有以下操作方法：

    Queue.qsize() 返回队列的大小
    Queue.empty() 如果队列为空，返回True,反之False
    Queue.full() 如果队列满了，返回True,反之False
    Queue.full 与 maxsize 大小对应
    Queue.get([block[, timeout]]) 获取/取出队列，timeout等待时间
    Queue.get_nowait() 相当Queue.get(False)
    Queue.put(item) 写入队列，timeout等待时间
    Queue.put_nowait(item) 相当Queue.put(item, False)
    Queue.task_done() 在完成一项工作之后，Queue.task_done() 函数向任务已经完成的队列发送一个信号
    Queue.join() 实际上意味着等到队列为空，再执行别的操作


下面是一个生产者消费者模型，抄的改改代码就可以用了，主要是了解过程。
"""
#!/usr/bin/python
import Queue
import time
import threading

q=Queue.Queue()

class producer(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self,name="producer Thread-%d" % i)
    def run(self):
        global q
        count=9
        while True:
            for i in range(3):
                if q.qsize() > 12:
                    pass
                else:
                    count=count+1
                    msg=str(count)
                    q.put(msg)
                    print self.name+' '+'producer'+msg+' '+'Queue Size:'+str(q.qsize())

            time.sleep(2)

class consumer(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self,name="consumer Thread-%d" % i)
    def run(self):
        global q
        while True:
            for i in range(3):
                if q.qsize() < 1:
                    pass
                else:
                    msg=q.get()
                    print self.name+' '+'consumer'+msg+' '+'Queue Size:'+str(q.qsize())
            time.sleep(2)


def test():
    for i in range(10):
        q.put(str(i))
        print 'Init producer  '+str(i)
    for i in range(2):
        p=producer(i)
        p.start()
    for i in range(3):
        c=consumer(i)
        c.start()

if __name__ == '__main__':
    test()