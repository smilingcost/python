#coding=utf-8
import os
"""
python之OS模块详解
^_^，步入第二个模块世界----->OS

常见函数列表
os.sep:取代操作系统特定的路径分隔符
os.name:指示你正在使用的工作平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
os.getcwd:得到当前工作目录，即当前python脚本工作的目录路径。
os.getenv()和os.putenv:分别用来读取和设置环境变量
os.listdir():返回指定目录下的所有文件和目录名
os.remove(file):删除一个文件
os.stat（file）:获得文件属性
os.chmod(file):修改文件权限和时间戳
os.mkdir(name):创建目录
os.rmdir(name):删除目录
os.removedirs（r“c：\python”）:删除多个目录
os.system():运行shell命令
os.exit():终止当前进程
os.linesep:给出当前平台的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
os.path.split():返回一个路径的目录名和文件名
os.path.isfile()和os.path.isdir()分别检验给出的路径是一个目录还是文件
os.path.existe():检验给出的路径是否真的存在
os.listdir(dirname):列出dirname下的目录和文件
os.getcwd():获得当前工作目录
os.curdir:返回当前目录（'.'）
os.chdir(dirname):改变工作目录到dirname
os.path.isdir(name):判断name是不是目录，不是目录就返回false
os.path.isfile(name):判断name这个文件是否存在，不存在返回false
os.path.exists(name):判断是否存在文件或目录name
os.path.getsize(name):或得文件大小，如果name是目录返回0L
os.path.abspath(name):获得绝对路径
os.path.isabs():判断是否为绝对路径
os.path.normpath(path):规范path字符串形式
os.path.split(name):分割文件名与目录（事实上，如果你完全使用目录，它也会将最后一个目录作为文件名而分离，同时它不会判断文件或目录是否存在）
os.path.splitext():分离文件名和扩展名
os.path.join(path,name):连接目录与文件名或目录
os.path.basename(path):返回文件名
os.path.dirname(path):返回文件路径
文件操作
os.mknod("text.txt")：创建空文件
fp = open("text.txt",w):直接打开一个文件，如果文件不存在就创建文件

关于open的模式

w 写方式
a 追加模式打开（从EOF开始，必要时创建新文件）
r+ 以读写模式打开
w+ 以读写模式打开
a+ 以读写模式打开
rb 以二进制读模式打开
wb 以二进制写模式打开 (参见 w )
ab 以二进制追加模式打开 (参见 a )
rb+ 以二进制读写模式打开 (参见 r+ )
wb+ 以二进制读写模式打开 (参见 w+ )
ab+ 以二进制读写模式打开 (参见 a+ )

关于文件的函数

fp.read([size])
size为读取的长度，以byte为单位

fp.readline([size])
读一行，如果定义了size，有可能返回的只是一行的一部分

fp.readlines([size])
把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。

fp.write(str)
把str写到文件中，write()并不会在str后加上一个换行符

fp.writelines(seq)
把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。

fp.close()
关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。 如果一个文件在关闭后还对其进行操作会产生ValueError

fp.flush()
把缓冲区的内容写入硬盘

fp.fileno()
返回一个长整型的”文件标签“

fp.isatty()
文件是否是一个终端设备文件（unix系统中的）

fp.tell()
返回文件操作标记的当前位置，以文件的开头为原点

fp.next()
返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。

fp.seek(offset[,whence])
将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。

fp.truncate([size])
把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。

目录操作
os.mkdir("file")
创建目录

复制文件:

shutil.copyfile("oldfile","newfile")
oldfile和newfile都只能是文件

shutil.copy("oldfile","newfile")
oldfile只能是文件夹，newfile可以是文件，也可以是目标目录

shutil.copytree("olddir","newdir")
复制文件夹.olddir和newdir都只能是目录，且newdir必须不存在

os.rename("oldname","newname")
重命名文件（目录）.文件或目录都是使用这条命令

shutil.move("oldpos","newpos")
移动文件（目录）

os.rmdir("dir")
只能删除空目录

shutil.rmtree("dir")
空目录、有内容的目录都可以删

os.chdir("path")
转换目录，换路径

代码演示
#!/usr/bin/env python

import os

print os.getcwd()                               #获取当前路径

print os.listdir('/mnt')                        #列出/mnt下面的所有目录和文件

print os.mkdir('lala')                          #创建目录lala和haha
print os.mkdir('haha')

print os.rmdir('haha')                          #删除haha

print os.rename('example.txt','back.txt')       #修改文件名
运行：

root@ruanyang-HP-ProDesk-680-G2-MT:/mnt/python# python os.py
/mnt/python
['proc', 'perl_bash', 'docker', 'warn', 'blog', 'python', 'hostname', 'test', 'tags', 'perl_DB', 'shell', 'perl_test', '.vimrc~', 'club.yml', 'test.c', '.vimrc']
None
None
None
None
root@ruanyang-HP-ProDesk-680-G2-MT:/mnt/python# ls
back.txt  exit.py  lala  modules.py  os_file.py  os.py  sys.py
"""





"""
python os.path模块

os.path.abspath(path) #返回绝对路径
os.path.basename(path) #返回文件名
os.path.commonprefix(list) #返回list(多个路径)中，所有path共有的最长的路径。
os.path.dirname(path) #返回文件路径
os.path.exists(path)  #路径存在则返回True,路径损坏返回False
os.path.lexists  #路径存在则返回True,路径损坏也返回True
os.path.expanduser(path)  #把path中包含的"~"和"~user"转换成用户目录
os.path.expandvars(path)  #根据环境变量的值替换path中包含的”$name”和”${name}”
os.path.getatime(path)  #返回最后一次进入此path的时间。
os.path.getmtime(path)  #返回在此path下最后一次修改的时间。
os.path.getctime(path)  #返回path的大小
os.path.getsize(path)  #返回文件大小，如果文件不存在就返回错误
os.path.isabs(path)  #判断是否为绝对路径
os.path.isfile(path)  #判断路径是否为文件
os.path.isdir(path)  #判断路径是否为目录
os.path.islink(path)  #判断路径是否为链接
os.path.ismount(path)  #判断路径是否为挂载点（）
os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径
os.path.normcase(path)  #转换path的大小写和斜杠
os.path.normpath(path)  #规范path字符串形式
os.path.realpath(path)  #返回path的真实路径
os.path.relpath(path[, start])  #从start开始计算相对路径
os.path.samefile(path1, path2)  #判断目录或文件是否相同
os.path.sameopenfile(fp1, fp2)  #判断fp1和fp2是否指向同一文件
os.path.samestat(stat1, stat2)  #判断stat tuple stat1和stat2是否指向同一个文件
os.path.split(path)  #把路径分割成dirname和basename，返回一个元组
os.path.splitdrive(path)   #一般用在windows下，返回驱动器名和路径组成的元组
os.path.splitext(path)  #分割路径，返回路径名和文件扩展名的元组
os.path.splitunc(path)  #把路径分割为加载点与文件
os.path.walk(path, visit, arg)  #遍历path，进入每个目录都调用visit函数，visit函数必须有
3个参数(arg, dirname, names)，dirname表示当前目录的目录名，names代表当前目录下的所有
文件名，args则为walk的第三个参数
os.path.supports_unicode_filenames  #设置是否支持unicode路径名
"""



python os.path模块常用方法详解（1）
"""

os.path模块主要用于文件的属性获取，在编程中经常用到，以下是该模块的几种常用方法。更多的方法可以去查看官方文档：http://docs.python.org/library/os.path.html


1.os.path.abspath(path)
返回path规范化的绝对路径。

>>> os.path.abspath('test.csv')
'C:\\Python25\\test.csv'

>>> os.path.abspath('c:\\test.csv')
'c:\\test.csv'

>>> os.path.abspath('../csv\\test.csv')
'C:\\csv\\test.csv'

2.os.path.split(path)
将path分割成目录和文件名二元组返回。

>>> os.path.split('c:\\csv\\test.csv')
('c:\\csv', 'test.csv')
>>> os.path.split('c:\\csv\\')
('c:\\csv', '')

3.os.path.dirname(path)
返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素。

>>> os.path.basename('c:\\test.csv')
'test.csv'
>>> os.path.basename('c:\\csv')
'csv' （这里csv被当作文件名处理了）
>>> os.path.basename('c:\\csv\\')
''

5.os.path.commonprefix(list)
返回list中，所有path共有的最长的路径。

如：


>>> os.path.commonprefix(['/home/td','/home/td/ff','/home/td/fff'])
'/home/td'

6.os.path.exists(path)
如果path存在，返回True；如果path不存在，返回False。


>>> os.path.exists('c:\\')
True
>>> os.path.exists('c:\\csv\\test.csv')
False

7.os.path.isabs(path)
如果path是绝对路径，返回True。


8.os.path.isfile(path)
如果path是一个存在的文件，返回True。否则返回False。


>>> os.path.isfile('c:\\boot.ini')
True
>>> os.path.isfile('c:\\csv\\test.csv')
False
>>> os.path.isfile('c:\\csv\\')
False

9.os.path.isdir(path)

python os.path模块常用方法详解（2）

如果path是一个存在的目录，则返回True。否则返回False。


>>> os.path.isdir('c:\\')
True
>>> os.path.isdir('c:\\csv\\')
False
>>> os.path.isdir('c:\\windows\\test.csv')
False

10.os.path.join(path1[, path2[, ...]])
将多个路径组合后返回，第一个绝对路径之前的参数将被忽略。


>>> os.path.join('c:\\', 'csv', 'test.csv')
'c:\\csv\\test.csv'
>>> os.path.join('windows\temp', 'c:\\', 'csv', 'test.csv')
'c:\\csv\\test.csv'
>>> os.path.join('/home/aa','/home/aa/bb','/home/aa/bb/c')
'/home/aa/bb/c'

11.os.path.normcase(path)
在Linux和Mac平台上，该函数会原样返回path，在windows平台上会将路径中所有字符转换为小写，并将所有斜杠转换为饭斜杠。


>>> os.path.normcase('c:/windows\\system32\\')
'c:\\windows\\system32\\'

12.os.path.normpath(path)
规范化路径。


>>> os.path.normpath('c://windows\\System32\\../Temp/')
'c:\\windows\\Temp'

12.os.path.splitdrive(path)
返回（drivername，fpath）元组。


>>> os.path.splitdrive('c:\\windows')
('c:', '\\windows')

13.os.path.splitext(path)
分离文件名与扩展名；默认返回(fname,fextension)元组，可做分片操作。


>>> os.path.splitext('c:\\csv\\test.csv')
('c:\\csv\\test', '.csv')

14.os.path.getsize(path)
返回path的文件的大小（字节）。


>>> os.path.getsize('c:\\boot.ini')
299L

15.os.path.getatime(path)
返回path所指向的文件或者目录的最后存取时间。


16.os.path.getmtime(path)
返回path所指向的文件或者目录的最后修改时间。"""