#coding=utf-8
import os
"""
一、前言

献给和我一样懵懂中不断汲取知识，进步的人们。

霓虹闪烁，但人们真正需要的，只是一个可以照亮前路的烛光

二、必要的前提

2.1 准备知识

django
一个基于python的开源web框架，请确保自己熟悉它的框架目录结构。
1
uWSGI
一个基于自有的uwsgi协议、wsgi协议和http服务协议的web网关
1
nginx
常用高性能代理服务器
1
wsgi.py
django项目携带的一个wsgi接口文件
如果项目名叫destiny的话，此文件就位于[destiny/destiny/wsgi.py]
1
2
2.2 相关资料

wsgi：一种实现python解析的通用接口标准/协议，是一种通用的接口标准或者接口协议，实现了python web程序与服务器之间交互的通用性。
利用它，web.py或bottle或者django等等的python web开发框架，就可以轻松地部署在不同的web server上了；

uwsgi:同WSGI一样是一种通信协议
uwsgi协议是一个uWSGI服务器自有的协议，它用于定义传输信息的类型，它与WSGI相比是两样东西。

uWSGI :一种python web server或称为Server/Gateway
uWSGI类似tornadoweb或者flup，是一种python web server，uWSGI是实现了uwsgi和WSGI两种协议的Web服务器，负责响应python 的web请求。
因为apache、nginx等，它们自己都没有解析动态语言如php的功能，而是分派给其他模块来做，比如apache就可以说内置了php模块，让人感觉好像apache就支持php一样。
uWSGI实现了wsgi协议、uwsgi协议、http等协议。 Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。
2.3 项目流程
其实网上很多教程，都是关于uwsgi+nginx部署django的，StackOverflow也有一些解决常见错误的方法，但是部署还是容易出问题，新手难解决。
归根到底是自己不了解整个项目的流程。教程都只教方法，但为什么这样部署，这样部署有什么好处，每个组件都起什么作用却只字不提。致使只要部署稍微有那么一点不同，就无可是从了。
所以说，项目流程和每个组件的用途才是此次部署最重要的部分。

首先客户端请求服务资源，
nginx作为直接对外的服务接口,接收到客户端发送过来的http请求,会解包、分析，
如果是静态文件请求就根据nginx配置的静态文件目录，返回请求的资源，
如果是动态的请求,nginx就通过配置文件,将请求传递给uWSGI；uWSGI 将接收到的包进行处理，并转发给wsgi，
wsgi根据请求调用django工程的某个文件或函数，处理完后django将返回值交给wsgi，
wsgi将返回值进行打包，转发给uWSGI，
uWSGI接收后转发给nginx,nginx最终将返回值返回给客户端(如浏览器)。
*注:不同的组件之间传递信息涉及到数据格式和协议的转换
1
2
3
4
5
6
7
8
作用:
1. 第一级的nginx并不是必须的，uwsgi完全可以完成整个的和浏览器交互的流程；
2. 在nginx上加上安全性或其他的限制，可以达到保护程序的作用；
3. uWSGI本身是内网接口，开启多个work和processes可能也不够用，而nginx可以代理多台uWSGI完成uWSGI的负载均衡；
4. django在debug=False下对静态文件的处理能力不是很好，而用nginx来处理更加高效。

三、安装与配置

首先，确保你已经安装好了nginx并可以正常使用。
其次，确保自己安装完成了python，并已经完成了pip的安装。如果没有，请先安装。
接着，别忘了确认自己项目所需的django已经完成安装并正常工作。
没有的话参考以下命令安装django , 建立一个工程或利用已经写好的工程，打开浏览器，输入部署地址(如:http://127.0.0.1:8000/)(或http://内网ip:8000、或http://外网ip:8000)测试，确认是否可正常打开浏览。
"""
安装:sudo pip install django==1.10
测试:python manage.py runserver 0.0.0.0:8000
"""
上面的工作都完成了，接着安装uWSGI
"""
sudo pip install uwsgi
"""
测试uWSGI: 新建文件test.py，写入以下内容
"""
def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return "Hello World"
"""
运行
"""
sudo uwsgi --http 0.0.0.0:8000 --wsgi-file test.py
"""
如果端口占用，使用
"""
lsof -i :8000
"""
列出占用端口的程序的pid号，并使用以下命令杀掉所有占用端口的程序
"""
sudo kill -9 pid
"""
然后浏览 http://127.0.0.1:8000(或http://内网ip:8000、或http://外网ip:8000)查看效果，有”Hello World”输出即安装成功。

下一步，建立工程单独的nginx配置文件
首先确认自己准确的知道nginx的默认配置文件目录(nginx.conf)的路径，如果不清楚，请使用如下命令获取:
"""
nginx -t
"""
大概会列出以下类似信息:
"""
nginx: the configuration file /etc/nginx/conf/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/conf/nginx.conf test is successful
"""
里面说明了nginx默认配置文件的路径是:/etc/nginx/conf/nginx.conf；

然后，确保nginx.conf的同目录下有uwsgi_params文件(/etc/nginx/conf/uwsgi_params)，没有的话根据链接获取， 后面要用到。

在自己的工程目录下，建立如destiny.conf（/wwwroot/destiny/destiny.conf）的配置文件；复制nginx.conf里面全部的内容，全部写入destiny.conf中。
然后按照下面写的，把destiny.conf配置文件中的server段部分全部替换掉。
"""
server {
    listen 80;
    server_name localhost;
    charset     utf-8;
    access_log      /wwwroot/destiny/nginx_access.log;
    error_log       /wwwroot/destiny/nginx_error.log;
    client_max_body_size 75M;


    location /static {
        alias /wwwroot/destiny/destiny/static;
    }

    location / {
        include     /etc/nginx/conf/uwsgi_params;
        uwsgi_pass  127.0.0.1:9090;
    }
}
"""
其中的 listen 80代表服务器开放80端口；
location [目录名]代表项目路径的引导;
access_log 和error_log是定义nginx访问日志和错误日志的存放路径。
“location /static”中的”/static”是自己定义的项目引用静态文件时，浏览器中显示的静态资源所在的根目录名;这样的话，用户在浏览器中查看到的所有image、css或js资源都是处在http://127.0.0.1/static下的。
django静态文件的绝对路径是根据自己的实际情况来确定的，一般在自己的django的app名/static目录下,或自己python manage.py collectstatic后的路径下。像我的是在/wwwroot/destiny/destiny/static根目录下。
“location /”是指访问项目根目录时，nginx要做的事。其中需要指定 uwsgi_params文件的绝对路径，上面已经提到了；如果还有media文件之类的静态目录，仿照static的写法，自己补充。
127.0.0.1:9090是指uWSGI绑定的监听地址，这里使用了9090端口。
需要注意的是，请确认自己django的静态文件目录所有者是www用户，如果不是，请用以下命令更改静态目录权限归属者:
"""
sudo chown -R www:www /wwwroot/destiny/destiny/static
"""
下面接着建立uWSGI的配置文件，在自己工程目录下创建uwsgi.ini文件,写入以下内容
"""
[uwsgi]
socket = 127.0.0.1:9090
chdir=/wwwroot/destiny
module=destiny.wsgi
master = true
processes=2
threads=2
max-requests=2000
chmod-socket=664
vacuum=true
daemonize = /wwwroot/destiny/uwsgi.log
"""
其中的socket字段值”127.0.0.1:9090”必须要和上面写的density.conf配置文件中的uWSGI监听地址完全一样;
chdir指自己工程的绝对路径;
module指的是wsgi.py在自己工程中的相对路径，”.”指代一层目录;我的django工程的wsgi.py文件是在”/wwwroot/destiny/destiny/wsgi.py”，所以写成destiny.wsgi;
daemonize指定uWSGI日志的存储路径。

好了，现在理一下路径:
"""
工程路径:                  /wwwroot/destiny
工程静态文件路径:            /wwwroot/destiny/destiny/static
wsgi.py的路径:             /wwwroot/destiny/destiny/wsgi.py
uwsgi.ini的路径:           /wwwroot/destiny/uwsgi.ini
uwsgi日志路径:             /wwwroot/destiny/uwsgi.log
destiny.conf的路径:        /wwwroot/destiny/destiny.conf
uwsgi_params的路径:        /etc/nginx/conf/uwsgi_params
nginx访问日志路径:          /wwwroot/destiny/nginx_access.log
nginx错误日志路径:          /wwwroot/destiny/nginx_error.log
"""
可以发现，我几乎把所有有关工程的配置文件和日志文件都放在工程目录下了，方便后期维护与查错。
启动uWSGI
"""
sudo uwsgi --ini /wwwroot/destiny/destiny.ini
"""
启动nginx
在这之前，我们要先去nginx配置文件的根目录拷贝mime.types(/etc/nginx/conf/mime.types)到工程目录(/wwwroot/destiny/mime.types)，和destiny.conf放在一起。
否则用配置文件启动nginx会报错:
"""
nginx: [emerg] open() "/**/**/**/mime.types" failed (2: No such file or directory)
"""
当然，如果不想拷贝mime.types文件，也可以将配置文件中“include mime.types;”一项，改成绝对路径“include /etc/nginx/conf/mime.types;”
如果nginx已经开启，先关闭nginx(service nginx stop或nginx -s stop)，再执行以下命令:
"""
nginx -c /wwwroot/destiny/destiny.conf
"""
这里的-c 表示加载配置文件启动

四、后记

到这里，工作基本就做完了，可以打开浏览器，输入自己项目的IP地址，如http://127.0.0.1/查看效果了。

example

如果启动时就报错，查看终端信息，解决错误。
如果终端没有报错，但是浏览时出现500、502等错误，就去项目目录查看nginx日志和uWSGI日志，解决错误。

自己在部署时，遇到很多坑，网上的教程大多附带virtualenv和supervisor的部署，但是连最基本的部署都说不明白，部署出来的东西性能再好也没指导意义。基于自己踩坑脱坑的过程，写下此文。

正如以上所说，我只是用单独的一个conf文件，在nginx上部署了一个工程，没有说明部署多个工程的问题；也没有使用virtualenv开发环境、使用supervisor来管理进程等。请根据个人爱好和需要去实践扩展。
"""
