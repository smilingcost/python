# -*- coding: UTF-8 -*-
import multiprocessing
u'理解：同个def中，如需要爬虫100个url，都是将url组成一个数组，多线程相当于同一时间每条线程执行100次（即总执行次数为线程数*数组数），多进程相当于同一时间执行相当于进程数的url（总执行次数为数组数），不同def中，多线程相当于每个线程执行不同的def，多进程相当于执行全部def，'
"""

python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，在python中大部分情况需要使用多进程。Python提供了非常好用的多进程包multiprocessing，
只需要定义一个函数，Python会完成其他所有事情。借助这个包，可以轻松完成从单进程到并发执行的转换。multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，
提供了Process、Queue、Pipe、Lock等组件。



回到顶部"""
1. Process
"""
创建进程的类：Process([group [, target [, name [, args [, kwargs]]]]])，target表示调用对象，args表示调用对象的位置参数元组。kwargs表示调用对象的字典。
name为别名。group实质上不使用。
方法：is_alive()、join([timeout])、run()、start()、terminate()。其中，Process以start()启动某个进程。

属性：authkey、daemon（要通过start()设置）、exitcode(进程在运行时为None、如果为–N，表示被信号N结束）、name、pid。其中daemon是父进程终止后自动终止，
且自己不能产生新进程，必须在start()之前设置。



例1.1：创建函数并将其作为单个进程

复制代码"""
import multiprocessing
import time

def worker(interval):
    n = 5
    while n > 0:
        print("The time is {0}".format(time.ctime()))
        time.sleep(interval)
        n -= 1

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.start()
    print "p.pid:", p.pid
    print "p.name:", p.name
    print "p.is_alive:", p.is_alive()
"""复制代码
结果


p.pid: 8736
p.name: Process-1
p.is_alive: True
The time is Tue Apr 21 20:55:12 2015
The time is Tue Apr 21 20:55:15 2015
The time is Tue Apr 21 20:55:18 2015
The time is Tue Apr 21 20:55:21 2015
The time is Tue Apr 21 20:55:24 2015


例1.2：创建函数并将其作为多个进程

复制代码"""
import multiprocessing
import time

def worker_1(interval):
    print "worker_1"
    time.sleep(interval)
    print "end worker_1"

def worker_2(interval):
    print "worker_2"
    time.sleep(interval)
    print "end worker_2"

def worker_3(interval):
    print "worker_3"
    time.sleep(interval)
    print "end worker_3"

if __name__ == "__main__":
    p1 = multiprocessing.Process(target = worker_1, args = (2,))
    p2 = multiprocessing.Process(target = worker_2, args = (3,))
    p3 = multiprocessing.Process(target = worker_3, args = (4,))

    p1.start()
    p2.start()
    p3.start()

    print("The number of CPU is:" + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
    print "END!!!!!!!!!!!!!!!!!"
"""复制代码
结果


The number of CPU is:4
child   p.name:Process-3    p.id7992
child   p.name:Process-2    p.id4204
child   p.name:Process-1    p.id6380
END!!!!!!!!!!!!!!!!!
worker_1
worker_3
worker_2
end worker_1
end worker_2
end worker_3


例1.3：将进程定义为类

复制代码"""
import multiprocessing
import time

class ClockProcess(multiprocessing.Process):
    def __init__(self, interval):
        multiprocessing.Process.__init__(self)
        self.interval = interval

    def run(self):
        n = 5
        while n > 0:
            print("the time is {0}".format(time.ctime()))
            time.sleep(self.interval)
            n -= 1

if __name__ == '__main__':
    p = ClockProcess(3)
    p.start()
"""复制代码
注：进程p调用start()时，自动调用run()

结果


the time is Tue Apr 21 20:31:30 2015
the time is Tue Apr 21 20:31:33 2015
the time is Tue Apr 21 20:31:36 2015
the time is Tue Apr 21 20:31:39 2015
the time is Tue Apr 21 20:31:42 2015


例1.4：daemon程序对比结果

#1.4-1 不加daemon属性

复制代码"""
import multiprocessing
import time

def worker(interval):
    print("work start:{0}".format(time.ctime()));
    time.sleep(interval)
    print("work end:{0}".format(time.ctime()));

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.start()
    print "end!"
"""复制代码
结果


end!
work start:Tue Apr 21 21:29:10 2015
work end:Tue Apr 21 21:29:13 2015
#1.4-2 加上daemon属性

复制代码"""
import multiprocessing
import time

def worker(interval):
    print("work start:{0}".format(time.ctime()));
    time.sleep(interval)
    print("work end:{0}".format(time.ctime()));

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.daemon = True
    p.start()
    print "end!"
"""复制代码
结果


end!
注：因子进程设置了daemon属性，主进程结束，它们就随着结束了。

#1.4-3 设置daemon执行完结束的方法

复制代码"""
import multiprocessing
import time

def worker(interval):
    print("work start:{0}".format(time.ctime()));
    time.sleep(interval)
    print("work end:{0}".format(time.ctime()));

if __name__ == "__main__":
    p = multiprocessing.Process(target = worker, args = (3,))
    p.daemon = True
    p.start()
    p.join()
    print "end!"
"""复制代码
结果


work start:Tue Apr 21 22:16:32 2015
work end:Tue Apr 21 22:16:35 2015
end!


回到顶部"""
2. Lock
"""
当多个进程需要访问共享资源的时候，Lock可以用来避免访问的冲突。

复制代码"""
import multiprocessing
import sys

def worker_with(lock, f):
    with lock:
        fs = open(f, 'a+')
        n = 10
        while n > 1:
            fs.write("Lockd acquired via with\n")
            n -= 1
        fs.close()

def worker_no_with(lock, f):
    lock.acquire()
    try:
        fs = open(f, 'a+')
        n = 10
        while n > 1:
            fs.write("Lock acquired directly\n")
            n -= 1
        fs.close()
    finally:
        lock.release()

if __name__ == "__main__":
    lock = multiprocessing.Lock()
    f = "file.txt"
    w = multiprocessing.Process(target = worker_with, args=(lock, f))
    nw = multiprocessing.Process(target = worker_no_with, args=(lock, f))
    w.start()
    nw.start()
    print "end"
"""复制代码
结果（输出文件）


Lockd acquired via with
Lockd acquired via with
Lockd acquired via with
Lockd acquired via with
Lockd acquired via with
Lockd acquired via with
Lockd acquired via with
Lockd acquired via with
Lockd acquired via with
Lock acquired directly
Lock acquired directly
Lock acquired directly
Lock acquired directly
Lock acquired directly
Lock acquired directly
Lock acquired directly
Lock acquired directly
Lock acquired directly


回到顶部"""
3. Semaphore
"""
Semaphore用来控制对共享资源的访问数量，例如池的最大连接数。

复制代码"""
import multiprocessing
import time

def worker(s, i):
    s.acquire()
    print(multiprocessing.current_process().name + "acquire");
    time.sleep(i)
    print(multiprocessing.current_process().name + "release\n");
    s.release()

if __name__ == "__main__":
    s = multiprocessing.Semaphore(2)
    for i in range(5):
        p = multiprocessing.Process(target = worker, args=(s, i*2))
        p.start()
"""复制代码
结果


Process-1acquire
Process-1release

Process-2acquire
Process-3acquire
Process-2release

Process-5acquire
Process-3release

Process-4acquire
Process-5release

Process-4release


回到顶部"""
4. Event
"""
Event用来实现进程间同步通信。

复制代码"""
import multiprocessing
import time

def wait_for_event(e):
    print("wait_for_event: starting")
    e.wait()
    print("wairt_for_event: e.is_set()->" + str(e.is_set()))

def wait_for_event_timeout(e, t):
    print("wait_for_event_timeout:starting")
    e.wait(t)
    print("wait_for_event_timeout:e.is_set->" + str(e.is_set()))

if __name__ == "__main__":
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(name = "block",
            target = wait_for_event,
            args = (e,))

    w2 = multiprocessing.Process(name = "non-block",
            target = wait_for_event_timeout,
            args = (e, 2))
    w1.start()
    w2.start()

    time.sleep(3)

    e.set()
    print("main: event is set")
"""复制代码
结果


wait_for_event: starting
wait_for_event_timeout:starting
wait_for_event_timeout:e.is_set->False
main: event is set
wairt_for_event: e.is_set()->True


回到顶部"""
5. Queue
"""
Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。put方法用以插入数据到队列中，put方法还有两个可选参数：blocked和timeout。如果blocked为True（默认值），
并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。

get方法可以从队列读取并且删除一个元素。同样，get方法有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，
会抛出Queue.Empty异常。如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常。Queue的一段示例代码：
复制代码"""
import multiprocessing

def writer_proc(q):
    try:
        q.put(1, block = False)
    except:
        pass

def reader_proc(q):
    try:
        print q.get(block = False)
    except:
        pass

if __name__ == "__main__":
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=writer_proc, args=(q,))
    writer.start()

    reader = multiprocessing.Process(target=reader_proc, args=(q,))
    reader.start()

    reader.join()
    writer.join()
"""复制代码
结果



回到顶部"""
6. Pipe
"""
Pipe方法返回(conn1, conn2)代表一个管道的两个端。Pipe方法有duplex参数，如果duplex参数为True(默认值)，那么这个管道是全双工模式，也就是说conn1和conn2均可收发。
duplex为False，conn1只负责接受消息，conn2只负责发送消息。

send和recv方法分别是发送和接受消息的方法。例如，在全双工模式下，可以调用conn1.send发送消息，conn1.recv接收消息。如果没有消息可接收，recv方法会一直阻塞。
如果管道已经被关闭，那么recv方法会抛出EOFError。
复制代码"""
import multiprocessing
import time

def proc1(pipe):
    while True:
        for i in xrange(10000):
            print "send: %s" %(i)
            pipe.send(i)
            time.sleep(1)

def proc2(pipe):
    while True:
        print "proc2 rev:", pipe.recv()
        time.sleep(1)

def proc3(pipe):
    while True:
        print "PROC3 rev:", pipe.recv()
        time.sleep(1)

if __name__ == "__main__":
    pipe = multiprocessing.Pipe()
    p1 = multiprocessing.Process(target=proc1, args=(pipe[0],))
    p2 = multiprocessing.Process(target=proc2, args=(pipe[1],))
    #p3 = multiprocessing.Process(target=proc3, args=(pipe[1],))

    p1.start()
    p2.start()
    #p3.start()

    p1.join()
    p2.join()
    #p3.join()
"""复制代码
结果





回到顶部"""
7. Pool
"""
在利用Python进行系统管理的时候，特别是同时操作多个文件目录，或者远程控制多台主机，并行操作可以节约大量的时间。当被操作对象数目不大时，可以直接利用multiprocessing
中的Process动态成生多个进程，十几个还好，但如果是上百个，上千个目标，手动的去限制进程数量却又太过繁琐，此时可以发挥进程池的功效。
Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；
但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来它。



例7.1：使用进程池（非阻塞）

复制代码"""
#coding: utf-8
import multiprocessing
import time

def func(msg):
    print "msg:", msg
    time.sleep(3)
    print "end"

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in xrange(4):
        msg = "hello %d" %(i)
        pool.apply_async(func, (msg, ))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print "Sub-process(es) done."
"""复制代码
一次执行结果


mMsg: hark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~ello 0

msg: hello 1
msg: hello 2
end
msg: hello 3
end
end
end
Sub-process(es) done.
函数解释：

apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞，apply(func[, args[, kwds]])是阻塞的（理解区别，看例1例2结果区别）
close()    关闭pool，使其不在接受新的任务。
terminate()    结束工作进程，不在处理未完成的任务。
join()    主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用。
执行说明：创建一个进程池pool，并设定进程的数量为3，xrange(4)会相继产生四个对象[0, 1, 2, 4]，四个对象被提交到pool中，因pool指定进程数为3，
所以0、1、2会直接送到进程中执行，当其中一个执行完事后才空出一个进程处理对象3，所以会出现输出“msg: hello 3”出现在"end"后。因为为非阻塞，
主函数会自己执行自个的，不搭理进程的执行，所以运行完for循环后直接输出“mMsg: hark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~”，主程序在pool.join（）处等待各个进程的结束。
Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到返回结果。
注意，虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。


例7.2：使用进程池（阻塞）

复制代码"""
#coding: utf-8
import multiprocessing
import time

def func(msg):
    print "msg:", msg
    time.sleep(3)
    print "end"

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes = 3)
    for i in xrange(4):
        msg = "hello %d" %(i)
        pool.apply(func, (msg, ))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去

    print "Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~"
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print "Sub-process(es) done."
"""复制代码
一次执行的结果


msg: hello 0
end
msg: hello 1
end
msg: hello 2
end
msg: hello 3
end
Mark~ Mark~ Mark~~~~~~~~~~~~~~~~~~~~~~
Sub-process(es) done.
　　

例7.3：使用进程池，并关注结果

复制代码"""
import multiprocessing
import time

def func(msg):
    print "msg:", msg
    time.sleep(3)
    print "end"
    return "done" + msg

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in xrange(3):
        msg = "hello %d" %(i)
        result.append(pool.apply_async(func, (msg, )))
    pool.close()
    pool.join()
    for res in result:
        print ":::", res.get()
    print "Sub-process(es) done."
"""复制代码
一次执行结果


msg: hello 0
msg: hello 1
msg: hello 2
end
end
end
::: donehello 0
::: donehello 1
::: donehello 2
Sub-process(es) done.


例7.4：使用多个进程池

复制代码"""
#coding: utf-8
import multiprocessing
import os, time, random

def Lee():
    print "\nRun task Lee-%s" %(os.getpid()) #os.getpid()获取当前的进程的ID
    start = time.time()
    time.sleep(random.random() * 10) #random.random()随机生成0-1之间的小数
    end = time.time()
    print 'Task Lee, runs %0.2f seconds.' %(end - start)

def Marlon():
    print "\nRun task Marlon-%s" %(os.getpid())
    start = time.time()
    time.sleep(random.random() * 40)
    end=time.time()
    print 'Task Marlon runs %0.2f seconds.' %(end - start)

def Allen():
    print "\nRun task Allen-%s" %(os.getpid())
    start = time.time()
    time.sleep(random.random() * 30)
    end = time.time()
    print 'Task Allen runs %0.2f seconds.' %(end - start)

def Frank():
    print "\nRun task Frank-%s" %(os.getpid())
    start = time.time()
    time.sleep(random.random() * 20)
    end = time.time()
    print 'Task Frank runs %0.2f seconds.' %(end - start)

if __name__=='__main__':
    function_list=  [Lee, Marlon, Allen, Frank]
    print "parent process %s" %(os.getpid())

    pool=multiprocessing.Pool(4)
    for func in function_list:
        pool.apply_async(func)     #Pool执行函数，apply执行函数,当有一个进程执行完毕后，会添加一个新的进程到pool中

    print 'Waiting for all subprocesses done...'
    pool.close()
    pool.join()    #调用join之前，一定要先调用close() 函数，否则会出错, close()执行后不会有新的进程加入到pool,join函数等待素有子进程结束
    print 'All subprocesses done.'
"""复制代码
一次执行结果


parent process 7704
 
Waiting for all subprocesses done...
Run task Lee-6948
 
Run task Marlon-2896
 
Run task Allen-7304
 
Run task Frank-3052
Task Lee, runs 1.59 seconds.
Task Marlon runs 8.48 seconds.
Task Frank runs 15.68 seconds.
Task Allen runs 18.08 seconds.
All subprocesses done.
"""

-------------------------------------------------------------------------------------------------------------------------------------------------


Process
"""先来看一段代码"""


from multiprocessing import Process, current_process
def func():
    time.sleep(1)
    proc = current_process()
    proc.name, proc.pid
sub_proc = Process(target=func, args=())
sub_proc.start()
sub_proc.join()
proc = current_process()
proc.name, proc.pid
"""这是在主进程中创建子进程，然后启动(start) 子进程，等待(join) 子进程执行完，再继续执行主进程的整个的执行流程。

那么，一个进程应该是用来做什么的，它应该保存一些什么状态，它的生命周期是什么样的呢？

一个进程需要处理一些不同任务，或者处理不同的对象。创建进程需要一个 function 和相关参数，参数可以是dictProcess(target=func, args=(), kwargs = {})，name 可以用来标识进程。

控制子进程进入不同阶段的是 start(), join(), is_alive(), terminate(), exitcode 方法。这些方法只能在创建子进程的进程中执行。

进程同步
Lock

锁是为了确保数据一致性，比如读写锁，每个进程给一个变量增加 1 ，但是如果在一个进程读取但还没有写入的时候，另外的进程也同时读取了，并写入该值，则最后写入的值是错误的，这时候就需要锁。

"""
def func(lock):
    lock.acquire()
    # do mysql query select update ...
    lock.release()

lock = Lock()
for i in xrange(4):
    proc = Process(target=func, args=(lock))
    proc.start()
"""Lock 同时也实现了 ContextManager API, 可以结合 with 语句使用, 关于 ContextManager, 请移步 Python 学习实践笔记 装饰器 与 context 查看。

Semaphore

Semaphore 和 Lock 稍有不同，Semaphore 相当于 N 把锁，获取其中一把就可以执行了。 信号量的总数 N 在构造时传入，s = Semaphore(N)。 和 Lock 一样，如果信号量为0，则进程堵塞，直到信号大于0。
"""
Pipes

"""Pipe 是在两个进程之间通信的工具，Pipe Constructor 会返回两个端

1
conn1, conn2 = Pipe(True)
如果是全双工的(构造函数参数为True)，则双端口都可接收发送，否则前面的端口用于接收，后面的端口用于发送。"""


def proc1(pipe):
   for i in xrange(10000):
       pipe.send(i)
def proc2(pipe):
    while True:
        print "proc2 rev:", pipe.recv()
pipe = Pipe()
Process(target=proc1, args=(pipe[0],)).start()
Process(target=proc2, args=(pipe[1],)).start()
"""Pipe 的每个端口同时最多一个进程读写，否则数据会出各种问题"""

Queues

"""multiprocessing.Queue 与 Queue.Queue 非常相似。其 API 列表如下"""
-----------------------------------------------------------------------------------------
qsize()
empty()
full()
put()
put_nowait()
get()
get_nowait()
close()
join_thread()
cancel_join_thread()
-----------------------------------------------------------------------------------------
"""当 Queue 为 Queue.Full 状态时，再 put() 会堵塞，当状态为 Queue.Empty 时，再 get() 也是。当 put() 或 get() 设置了超时参数，而超时的时候，会抛出异常。

Queue 主要用于多个进程产生和消费，一般使用情况如下"""


def producer(q):
    for i in xrange(10):
        q.put(i)
def consumer(q):
    while True:
        print "consumer", q.get()
q = Queue(40)
for i in xrange(10):
    Process(target=producer, args=(q,)).start()
Process(target=consumer, args=(q,)).start()
"""十个生产者进程，一个消费者进程，共用同一个队列进行同步。

有一个简化版本的 multiprocessing.queues.SimpleQueue, 只支持3个方法 empty(), get(), put()。

也有一个强化版本的 JoinableQueue, 新增两个方法 task_done() 和 join()。 task_done() 是给消费者使用的，每完成队列中的一个任务，调用一次该方法。当所有的 tasks 都完成之后，交给调用 join() 的进程执行。

"""
def consumer(q):
    while True:
        print "consumer", q.get()
        q.task_done()
jobs = JoinableQueue()
for i in xrange(10):
        jobs.put(i)
for i in xrange(10):
    p = Process(target=consumer, args=(jobs,))
    p.daemon = True
    p.start()
jobs.join()
"""这个 join 函数等待 JoinableQueue 为空的时候，等待就结束，外面的进程可以继续执行了，但是那10个进程干嘛去了呢，他们还在等待呀，上面是设置了 p.daemon = True, 子进程才随着主进程结束的，如果没有设置，它们还是会一直等待的呢。

Lock、Pipe、Queue 和 Pipe 需要注意的是：尽量避免使用 Process.terminate 来终止程序，否则将会导致很多问题, 详情请移步python 官方文档查看。

进程间数据共享
前一节中, Pipe、Queue 都有一定数据共享的功能，但是他们会堵塞进程, 这里介绍的两种数据共享方式都不会堵塞进程, 而且都是多进程安全的。

共享内存

共享内存有两个结构，一个是 Value, 一个是 Array，这两个结构内部都实现了锁机制，因此是多进程安全的。 用法如下：
"""

def func(n, a):
    n.value = 50
    for i in range(len(a)):
        a[i] += 10
num = Value('d', 0.0)
ints= Array('i', range(10))
p = Process(target=func, args=(num, ints))
p.start()
p.join()
"""Value 和 Array 都需要设置其中存放值的类型，d 是 double 类型，i 是 int 类型，具体的对应关系在Python 标准库的 sharedctypes 模块中查看。

服务进程 Manager

上面的共享内存支持两种结构 Value 和 Array, 这些值在主进程中管理，很分散。 Python 中还有一统天下，无所不能的 Server process，专门用来做数据共享。 其支持的类型非常多，比如list, dict, Namespace, Lock, RLock, Semaphore, BoundedSemaphore, Condition, Event, Queue, Value 和 Array 用法如下：

"""
from multiprocessing import Process, Manager
def func(dct, lst):
    dct[88] = 88
    lst.reverse()
manager = Manager()
dct = manager.dict()
lst = manager.list(range(5,10))
p = Process(target=func, args=(dct, lst))
p.start()
p.join()
print dct, '|', lst
"""Out: {88: 88} | [9, 8, 7, 6, 5]
一个 Manager 对象是一个服务进程，推荐多进程程序中，数据共享就用一个 manager 管理。

进程管理
如果有50个任务要执行, 但是 CPU 只有4核, 你可以创建50个进程来做这个事情。但是大可不必，徒增管理开销。如果你只想创建4个进程，让他们轮流替你完成任务，不用自己去管理具体的进程的创建销毁，那 Pool 是非常有用的。

Pool 是进程池，进程池能够管理一定的进程，当有空闲进程时，则利用空闲进程完成任务，直到所有任务完成为止，用法如下

"""
def func(x):
    return x*x
pool = Pool(processes=4)
print pool.map(func, range(8))
"""Pool 进程池创建4个进程，不管有没有任务，都一直在进程池中等候，等到有数据的时候就开始执行。
Pool 的 API 列表如下："""
-----------------------------------------------------------------------------------------
apply(func[, args[, kwds]])
apply_async(func[, args[, kwds[, callback]]])
map(func, iterable[, chunksize])
map_async(func, iterable[, chunksize[, callback]])
imap(func, iterable[, chunksize])
imap_unordered(func, iterable[, chunksize])
close()
terminate()
join()
-----------------------------------------------------------------------------------------
"""异步执行

apply_async 和 map_async 执行之后立即返回，然后异步返回结果。 使用方法如下

"""
def func(x):
    return x*x
def callback(x):
    print x, 'in callback'

pool = Pool(processes=4)
result = pool.map_async(func, range(8), 8, callback)
print result.get(), 'in main'
"""Out:
[0, 1, 4, 9, 16, 25, 36, 49] in callback
[0, 1, 4, 9, 16, 25, 36, 49] in main
有两个值得提到的，一个是 callback，另外一个是 multiprocessing.pool.AsyncResult。 callback 是在结果返回之前，调用的一个函数，这个函数必须只有一个参数，它会首先接收到结果。callback 不能有耗时操作，因为它会阻塞主线程。

AsyncResult 是获取结果的对象，其 API 如下
"""
-----------------------------------------------------------------------------------------
get([timeout])
wait([timeout])
ready()
successful()
-----------------------------------------------------------------------------------------
"""如果设置了 timeout 时间，超时会抛出 multiprocessing.TimeoutError 异常。wait 是等待执行完成。 ready 测试是否已经完成，successful 是在确定已经 ready 的情况下，如果执行中没有抛出异常，则成功，如果没有ready 就调用该函数，会得到一个 AssertionError 异常。
"""
Pool 管理

"""这里不再继续讲 map 的各种变体了，因为从上面的 API 一看便知。

然后我们来看看 Pool 的执行流程，有三个阶段。第一、一个进程池接收很多任务，然后分开执行任务；第二、不再接收任务了；第三、等所有任务完成了，回家，不干了。

这就是上面的方法，close 停止接收新的任务，如果还有任务来，就会抛出异常。 join 是等待所有任务完成。 join 必须要在 close 之后调用，否则会抛出异常。terminate 非正常终止，内存不够用时，垃圾回收器调用的就是这个方法。

"""

