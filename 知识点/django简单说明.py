#coding=utf-8
import re


创建第一个项目----------------------------------------------------------------------------------------
使用 django-admin.py 来创建 HelloWorld 项目：

django-admin.py startproject HelloWorld

创建完成后我们可以查看下项目的目录结构：
$ cd HelloWorld/
$ tree
.
|-- HelloWorld
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
`-- manage.py
目录说明：
HelloWorld: 项目的容器。
manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
HelloWorld/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
HelloWorld/settings.py: 该 Django 项目的设置/配置。
HelloWorld/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
HelloWorld/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。
接下来我们进入 HelloWorld 目录输入以下命令，启动服务器：

python manage.py runserver 0.0.0.0:8000

0.0.0.0 让其它电脑可连接到开发服务器，8000 为端口号。如果不说明，那么端口号默认为 8000。


视图和 URL 配置
在先前创建的 HelloWorld 目录下的 HelloWorld 目录新建一个 view.py 文件，并输入代码：
HelloWorld/HelloWorld/view.py 文件代码：
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world ! ")
接着，绑定 URL 与视图函数。打开 urls.py 文件，删除原来代码，将以下代码复制粘贴到 urls.py 文件中：
HelloWorld/HelloWorld/urls.py 文件代码：
from django.conf.urls import url

from . import view

urlpatterns = [
    url(r'^$', view.hello),
]
整个目录结构如下：
$ tree
.
|-- HelloWorld
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- settings.py
|   |-- settings.pyc
|   |-- urls.py              # url 配置
|   |-- urls.pyc
|   |-- view.py              # 添加的视图文件
|   |-- view.pyc             # 编译后的视图文件
|   |-- wsgi.py
|   `-- wsgi.pyc
`-- manage.py
完成后，启动 Django 开发服务器，并在浏览器访问打开浏览器并访问：

我们也可以修改以下规则：
HelloWorld/HelloWorld/urls.py 文件代码：
from django.conf.urls import url

from . import view

urlpatterns = [
    url(r'^hello$', view.hello),
]
通过浏览器打开 http://127.0.0.1:8000/hello，输出结果如下：

注意：项目中如果代码有改动，服务器会自动监测代码的改动并自动重新载入，所以如果你已经启动了服务器则不需手动重启。
url() 函数
Django url() 可以接收四个参数，分别是两个必选参数：regex、view 和两个可选参数：kwargs、name，接下来详细介绍这四个参数。
regex: 正则表达式，与之匹配的 URL 会执行对应的第二个参数 view。
view: 用于执行与正则表达式匹配的 URL 请求。
kwargs: 视图使用的字典类型的参数。
name: 用来反向获取 URL。

"""
Django 模板-------------------------------------------------------------------------------------------------------------------------------------------------

        在上一章节中我们使用 django.http.HttpResponse() 来输出 "Hello World！"。该方式将数据与视图混合在一起，不符合 Django 的 MVC 思想。
本章节我们将为大家详细介绍 Django 模板的应用，模板是一个文本，用于分离文档的表现形式和内容。
模板应用实例
我们接着上一章节的项目将在 HelloWorld 目录底下创建 templates 目录并建立 hello.html文件，整个目录结构如下：
HelloWorld/
|-- HelloWorld
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- settings.py
|   |-- settings.pyc
|   |-- urls.py
|   |-- urls.pyc
|   |-- view.py
|   |-- view.pyc
|   |-- wsgi.py
|   `-- wsgi.pyc
|-- manage.py
`-- templates
    `-- hello.html
hello.html 文件代码如下：
HelloWorld/templates/hello.html 文件代码：
<h1>{{ hello }}</h1>
从模板中我们知道变量使用了双括号。
接下来我们需要向Django说明模板文件的路径，修改HelloWorld/settings.py，修改 TEMPLATES 中的 DIRS 为 [BASE_DIR+"/templates",]，如下所示:
HelloWorld/HelloWorld/settings.py 文件代码：
...TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+"/templates",],       # 修改位置
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
...
我们现在修改 view.py，增加一个新的对象，用于向模板提交数据：
HelloWorld/HelloWorld/view.py 文件代码：
# -*- coding: utf-8 -*-

#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
可以看到，我们这里使用 render 来替代之前使用的 HttpResponse。render 还使用了一个字典 context 作为参数。
context 字典中元素的键值 "hello" 对应了模板中的变量 "{{ hello }}"。
再访问访问 http://127.0.0.1:8000/hello，可以看到页面：

这样我们就完成了使用模板来输出数据，从而实现数据与视图分离。
接下来我们将具体介绍模板中常用的语法规则。
Django 模板标签
if/else 标签
基本语法格式如下：
{% if condition %}
     ... display
{% endif %}
或者：
{% if condition1 %}
   ... display 1
{% elif condition2 %}
   ... display 2
{% else %}
   ... display 3
{% endif %}
根据条件判断是否输出。if/else 支持嵌套。
{% if %} 标签接受 and ， or 或者 not 关键字来对多个变量做判断 ，或者对变量取反（ not )，例如：
{% if athlete_list and coach_list %}
     athletes 和 coaches 变量都是可用的。
{% endif %}
for 标签
{% for %} 允许我们在一个序列上迭代。
与Python的 for 语句的情形类似，循环语法是 for X in Y ，Y是要迭代的序列而X是在每一个特定的循环中使用的变量名称。
每一次循环中，模板系统会渲染在 {% for %} 和 {% endfor %} 之间的所有内容。
例如，给定一个运动员列表 athlete_list 变量，我们可以使用下面的代码来显示这个列表：
<ul>
{% for athlete in athlete_list %}
    <li>{{ athlete.name }}</li>
{% endfor %}
</ul>
给标签增加一个 reversed 使得该列表被反向迭代：
{% for athlete in athlete_list reversed %}
...
{% endfor %}
可以嵌套使用 {% for %} 标签：
{% for athlete in athlete_list %}
    <h1>{{ athlete.name }}</h1>
    <ul>
    {% for sport in athlete.sports_played %}
        <li>{{ sport }}</li>
    {% endfor %}
    </ul>
{% endfor %}
ifequal/ifnotequal 标签
{% ifequal %} 标签比较两个值，当他们相等时，显示在 {% ifequal %} 和 {% endifequal %} 之中所有的值。
下面的例子比较两个模板变量 user 和 currentuser :
{% ifequal user currentuser %}
    <h1>Welcome!</h1>
{% endifequal %}
和 {% if %} 类似， {% ifequal %} 支持可选的 {% else%} 标签：8
{% ifequal section 'sitenews' %}
    <h1>Site News</h1>
{% else %}
    <h1>No News Here</h1>
{% endifequal %}
注释标签
Django 注释使用 {# #}。
{# 这是一个注释 #}
过滤器
模板过滤器可以在变量被显示前修改它，过滤器使用管道字符，如下所示：
{{ name|lower }}
{{ name }} 变量被过滤器 lower 处理后，文档大写转换文本为小写。
过滤管道可以被* 套接* ，既是说，一个过滤器管道的输出又可以作为下一个管道的输入：
{{ my_list|first|upper }}
以上实例将第一个元素并将其转化为大写。
有些过滤器有参数。 过滤器的参数跟随冒号之后并且总是以双引号包含。 例如：
{{ bio|truncatewords:"30" }}
这个将显示变量 bio 的前30个词。
其他过滤器：
addslashes : 添加反斜杠到任何反斜杠、单引号或者双引号前面。
date : 按指定的格式字符串参数格式化 date 或者 datetime 对象，实例：
{{ pub_date|date:"F j, Y" }}
length : 返回变量的长度。
include 标签
{% include %} 标签允许在模板中包含其它的模板的内容。
下面这个例子都包含了 nav.html 模板：
{% include "nav.html" %}
模板继承
模板可以用继承的方式来实现复用。
接下来我们先创建之前项目的 templates 目录中添加 base.html 文件，代码如下：
HelloWorld/templates/base.html 文件代码：
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>菜鸟教程 Django 测试。</p>
    {% block mainbody %}
       <p>original</p>
    {% endblock %}
</body>
</html>
以上代码中，名为 mainbody 的 block 标签是可以被继承者们替换掉的部分。
所有的 {% block %} 标签告诉模板引擎，子模板可以重载这些部分。
hello.html 中继承 base.html，并替换特定 block，hello.html 修改后的代码如下：
HelloWorld/templates/hello.html 文件代码：
{% extends "base.html" %}

{% block mainbody %}<p>继承了 base.html 文件</p>
{% endblock %}
第一行代码说明 hello.html 继承了 base.html 文件。可以看到，这里相同名字的 block 标签用以替换 base.html 的相应 block。


"""
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Django 模型
Django 对各种数据库提供了很好的支持，包括：PostgreSQL、MySQL、SQLite、Oracle。
Django 为这些数据库提供了统一的调用API。 我们可以根据自己业务需求选择不同的数据库。
MySQL 是 Web 应用中最常用的数据库。本章节我们将以 Mysql 作为实例进行介绍。你可以通过本站的 MySQL 教程 了解更多Mysql的基础知识。
如果你没安装 mysql 驱动，可以执行以下命令安装：
sudo pip install mysqlclient
数据库配置
我们在项目的 settings.py 文件中找到 DATABASES 配置项，将其信息修改为：
HelloWorld/HelloWorld/settings.py: 文件代码：
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 或者使用 mysql.connector.django
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test123',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
这里添加了中文注释，所以你需要在 HelloWorld/settings.py 文件头部添加 # -*- coding: UTF-8 -*-。
上面包含数据库名称和用户的信息，它们与 MySQL 中对应数据库和用户的设置相同。Django 根据这一设置，与 MySQL 中相应的数据库和用户连接起来。
定义模型
创建 APP
Django规定，如果要使用模型，必须要创建一个app。我们使用以下命令创建一个 TestModel 的 app:
django-admin.py startapp TestModel
目录结构如下：
HelloWorld
|-- TestModel
|   |-- __init__.py
|   |-- admin.py
|   |-- models.py
|   |-- tests.py
|   `-- views.py
我们修改 TestModel/models.py 文件，代码如下：
HelloWorld/TestModel/models.py: 文件代码：
# models.py
from django.db import models

class Test(models.Model):
    name = models.CharField(max_length=20)
以上的类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。
接下来在settings.py中找到INSTALLED_APPS这一项，如下：
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'TestModel',               # 添加此项
)
在命令行中运行：
$ python manage.py migrate   # 创建表结构

$ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate TestModel   # 创建表结构
看到几行 "Creating table…" 的字样，你的数据表就创建好了。
Creating tables ...
……
Creating table TestModel_test  #我们自定义的表
……
表名组成结构为：应用名_类名（如：TestModel_test）。
注意：尽管我们没有在models给表设置主键，但是Django会自动添加一个id作为主键。
数据库操作
接下来我们在 HelloWorld 目录中添加 testdb.py 文件（下面介绍），并修改 urls.py：
HelloWorld/HelloWorld/urls.py: 文件代码：
from django.conf.urls import *
from . import view,testdb

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
]
添加数据
添加数据需要先创建对象，然后再执行 save 函数，相当于SQL中的INSERT：
HelloWorld/HelloWorld/testdb.py: 文件代码：
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
    test1 = Test(name='runoob')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
访问 http://127.0.0.1:8000/testdb 就可以看到数据添加成功的提示。
输出结果如下：

获取数据
Django提供了多种方式来获取数据库的内容，如下代码所示：
HelloWorld/HelloWorld/testdb.py: 文件代码：
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
    # 初始化
    response = ""
    response1 = ""


    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = Test.objects.all()

    # filter相当于SQL中的WHERE，可设置条件过滤结果
    response2 = Test.objects.filter(id=1)

    # 获取单个对象
    response3 = Test.objects.get(id=1)

    # 限制返回的数据 相当于 SQL 中的 OFFSET 0 LIMIT 2;
    Test.objects.order_by('name')[0:2]

    #数据排序
    Test.objects.order_by("id")

    # 上面的方法可以连锁使用
    Test.objects.filter(name="runoob").order_by("id")

    # 输出所有数据
    for var in list:
        response1 += var.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")
输出结果如下图所示：

更新数据
修改数据可以使用 save() 或 update():
HelloWorld/HelloWorld/testdb.py: 文件代码：
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    test1 = Test.objects.get(id=1)
    test1.name = 'Google'
    test1.save()

    # 另外一种方式
    #Test.objects.filter(id=1).update(name='Google')

    # 修改所有的列
    # Test.objects.all().update(name='Google')

    return HttpResponse("<p>修改成功</p>")
删除数据
删除数据库中的对象只需调用该对象的delete()方法即可：
HelloWorld/HelloWorld/testdb.py: 文件代码：
# -*- coding: utf-8 -*-

from django.http import HttpResponse

from TestModel.models import Test

# 数据库操作
def testdb(request):
    # 删除id=1的数据
    test1 = Test.objects.get(id=1)
    test1.delete()

    # 另外一种方式
    # Test.objects.filter(id=1).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除成功</p>")




"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Django 表单
HTML表单是网站交互性的经典方式。 本章将介绍如何用Django对用户提交的表单数据进行处理。
HTTP 请求
HTTP协议以"请求－回复"的方式工作。客户发送请求时，可以在请求中附加数据。服务器通过解析请求，就可以获得客户传来的数据，并根据URL来提供特定的服务。
GET 方法
我们在之前的项目中创建一个 search.py 文件，用于接收用户的请求：
/HelloWorld/HelloWorld/search.py 文件代码：
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

# 表单
def search_form(request):
    return render_to_response('search_form.html')

# 接收请求数据
def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
在模板目录 templates 中添加 search_form.html 表单：
/HelloWorld/templates/search_form.html 文件代码：
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <form action="/search" method="get">
        <input type="text" name="q">
        <input type="submit" value="搜索">
    </form>
</body>
</html>
urls.py 规则修改为如下形式：
/HelloWorld/HelloWorld/urls.py 文件代码：
from django.conf.urls import url
from . import view,testdb,search

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
]
访问地址 http://127.0.0.1:8000/search-form 并搜索，结果如下所示:

POST 方法
上面我们使用了GET方法。视图显示和请求处理分成两个函数处理。
提交数据时更常用POST方法。我们下面使用该方法，并用一个URL和处理函数，同时显示视图和处理请求。
我们在tmplate 创建 post.html：
/HelloWorld/tmplates/post.html 文件代码：
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <form action="/search-post" method="post">
        {% csrf_token %}
        <input type="text" name="q">
        <input type="submit" value="Submit">
    </form>

    <p>{{ rlt }}</p>
</body>
</html>
在模板的末尾，我们增加一个 rlt 记号，为表格处理结果预留位置。
表格后面还有一个{% csrf_token %}的标签。csrf 全称是 Cross Site Request Forgery。这是Django提供的防止伪装提交请求的功能。POST 方法提交的表格，必须有此标签。
在HelloWorld目录下新建 search2.py 文件并使用 search_post 函数来处理 POST 请求：
/HelloWorld/HelloWorld/search2.py 文件代码：
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf

# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
urls.py 规则修改为如下形式：
/HelloWorld/HelloWorld/urls.py 文件代码：
from django.conf.urls import url
from . import view,testdb,search,search2

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
]
访问 http://127.0.0.1:8000/search-post 显示结果如下：

完成以上实例后，我们的目录结构为：
HelloWorld
|-- HelloWorld
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- search.py
|   |-- search.pyc
|   |-- search2.py
|   |-- search2.pyc
|   |-- settings.py
|   |-- settings.pyc
|   |-- testdb.py
|   |-- testdb.pyc
|   |-- urls.py
|   |-- urls.pyc
|   |-- view.py
|   |-- view.pyc
|   |-- wsgi.py
|   `-- wsgi.pyc
|-- TestModel
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- admin.py
|   |-- admin.pyc
|   |-- apps.py
|   |-- migrations
|   |   |-- 0001_initial.py
|   |   |-- 0001_initial.pyc
|   |   |-- __init__.py
|   |   `-- __init__.pyc
|   |-- models.py
|   |-- models.pyc
|   |-- tests.py
|   `-- views.py
|-- db.sqlite3
|-- manage.py
`-- templates
    |-- base.html
    |-- hello.html
    |-- post.html
    `-- search_form.html
Request 对象
每个 view 函数的第一个参数是一个 HttpRequest 对象，就像下面这个 hello() 函数:
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")
HttpRequest对象包含当前请求URL的一些信息：
属性
描述
path
请求页面的全路径,不包括域名—例如, "/hello/"。
method
请求中使用的HTTP方法的字符串表示。全大写表示。例如:
if request.method == 'GET':
    do_something()
elif request.method == 'POST':
    do_something_else()
GET
包含所有HTTP GET参数的类字典对象。参见QueryDict 文档。
POST
包含所有HTTP POST参数的类字典对象。参见QueryDict 文档。
服务器收到空的POST请求的情况也是有可能发生的。也就是说，表单form通过HTTP POST方法提交请求，但是表单中可以没有数据。因此，不能使用语句if request.POST来判断是否使用HTTP POST方法；应该使用if request.method == "POST" (参见本表的method属性)。
注意: POST不包括file-upload信息。参见FILES属性。
REQUEST
为了方便，该属性是POST和GET属性的集合体，但是有特殊性，先查找POST属性，然后再查找GET属性。借鉴PHP's $_REQUEST。
例如，如果GET = {"name": "john"} 和POST = {"age": '34'},则 REQUEST["name"] 的值是"john", REQUEST["age"]的值是"34".
强烈建议使用GET and POST,因为这两个属性更加显式化，写出的代码也更易理解。
COOKIES
包含所有cookies的标准Python字典对象。Keys和values都是字符串。参见第12章，有关于cookies更详细的讲解。
FILES
包含所有上传文件的类字典对象。FILES中的每个Key都是<input type="file" name="" />标签中name属性的值. FILES中的每个value 同时也是一个标准Python字典对象，包含下面三个Keys:
filename: 上传文件名,用Python字符串表示
content-type: 上传文件的Content type
content: 上传文件的原始内容
注意：只有在请求方法是POST，并且请求页面中<form>有enctype="multipart/form-data"属性时FILES才拥有数据。否则，FILES 是一个空字典。
META
包含所有可用HTTP头部信息的字典。 例如:
CONTENT_LENGTH
CONTENT_TYPE
QUERY_STRING: 未解析的原始查询字符串
REMOTE_ADDR: 客户端IP地址
REMOTE_HOST: 客户端主机名
SERVER_NAME: 服务器主机名
SERVER_PORT: 服务器端口
META 中这些头加上前缀HTTP_最为Key, 例如:
HTTP_ACCEPT_ENCODING
HTTP_ACCEPT_LANGUAGE
HTTP_HOST: 客户发送的HTTP主机头信息
HTTP_REFERER: referring页
HTTP_USER_AGENT: 客户端的user-agent字符串
HTTP_X_BENDER: X-Bender头信息
user
是一个django.contrib.auth.models.User 对象，代表当前登录的用户。
如果访问用户当前没有登录，user将被初始化为django.contrib.auth.models.AnonymousUser的实例。
你可以通过user的is_authenticated()方法来辨别用户是否登录：
if request.user.is_authenticated():
    # Do something for logged-in users.
else:
    # Do something for anonymous users.
只有激活Django中的AuthenticationMiddleware时该属性才可用
session
唯一可读写的属性，代表当前会话的字典对象。只有激活Django中的session支持时该属性才可用。 参见第12章。
raw_post_data
原始HTTP POST数据，未解析过。 高级处理时会有用处。
Request对象也有一些有用的方法：
方法	描述
__getitem__(key)	返回GET/POST的键值,先取POST,后取GET。如果键不存在抛出 KeyError。
这是我们可以使用字典语法访问HttpRequest对象。
例如,request["foo"]等同于先request.POST["foo"] 然后 request.GET["foo"]的操作。
has_key()	检查request.GET or request.POST中是否包含参数指定的Key。
get_full_path()	返回包含查询字符串的请求路径。例如， "/music/bands/the_beatles/?print=true"
is_secure()	如果请求是安全的，返回True，就是说，发出的是HTTPS请求。
QueryDict对象
在HttpRequest对象中, GET和POST属性是django.http.QueryDict类的实例。
QueryDict类似字典的自定义类，用来处理单键对应多值的情况。
QueryDict实现所有标准的词典方法。还包括一些特有的方法：
方法	描述
__getitem__
和标准字典的处理有一点不同，就是，如果Key对应多个Value，__getitem__()返回最后一个value。
__setitem__
设置参数指定key的value列表(一个Python list)。注意：它只能在一个mutable QueryDict 对象上被调用(就是通过copy()产生的一个QueryDict对象的拷贝).
get()
如果key对应多个value，get()返回最后一个value。
update()
参数可以是QueryDict，也可以是标准字典。和标准字典的update方法不同，该方法添加字典 items，而不是替换它们:
>>> q = QueryDict('a=1')

>>> q = q.copy() # to make it mutable

>>> q.update({'a': '2'})

>>> q.getlist('a')

 ['1', '2']

>>> q['a'] # returns the last

['2']
items()
和标准字典的items()方法有一点不同,该方法使用单值逻辑的__getitem__():
>>> q = QueryDict('a=1&a=2&a=3')

>>> q.items()

[('a', '3')]
values()
和标准字典的values()方法有一点不同,该方法使用单值逻辑的__getitem__():
此外, QueryDict也有一些方法，如下表：
方法	描述
copy()
返回对象的拷贝，内部实现是用Python标准库的copy.deepcopy()。该拷贝是mutable(可更改的) — 就是说，可以更改该拷贝的值。
getlist(key)
返回和参数key对应的所有值，作为一个Python list返回。如果key不存在，则返回空list。 It's guaranteed to return a list of some sort..
setlist(key,list_)
设置key的值为list_ (unlike __setitem__()).
appendlist(key,item)
添加item到和key关联的内部list.
setlistdefault(key,list)
和setdefault有一点不同，它接受list而不是单个value作为参数。
lists()
和items()有一点不同, 它会返回key的所有值，作为一个list, 例如:
>>> q = QueryDict('a=1&a=2&a=3')

>>> q.lists()

[('a', ['1', '2', '3'])]

urlencode()
返回一个以查询字符串格式进行格式化后的字符串(e.g., "a=2&b=3&b=5").

"""



=-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Django 表单

HTML表单是网站交互性的经典方式。 本章将介绍如何用Django对用户提交的表单数据进行处理。
HTTP 请求
HTTP协议以"请求－回复"的方式工作。客户发送请求时，可以在请求中附加数据。服务器通过解析请求，就可以获得客户传来的数据，并根据URL来提供特定的服务。
GET 方法
我们在之前的项目中创建一个 search.py 文件，用于接收用户的请求：
/HelloWorld/HelloWorld/search.py 文件代码：
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response

# 表单
def search_form(request):
    return render_to_response('search_form.html')

# 接收请求数据
def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
在模板目录 templates 中添加 search_form.html 表单：
/HelloWorld/templates/search_form.html 文件代码：
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <form action="/search" method="get">
        <input type="text" name="q">
        <input type="submit" value="搜索">
    </form>
</body>
</html>
urls.py 规则修改为如下形式：
/HelloWorld/HelloWorld/urls.py 文件代码：
from django.conf.urls import url
from . import view,testdb,search

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
]
访问地址 http://127.0.0.1:8000/search-form 并搜索，结果如下所示:

POST 方法
上面我们使用了GET方法。视图显示和请求处理分成两个函数处理。
提交数据时更常用POST方法。我们下面使用该方法，并用一个URL和处理函数，同时显示视图和处理请求。
我们在tmplate 创建 post.html：
/HelloWorld/tmplates/post.html 文件代码：
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>菜鸟教程(runoob.com)</title>
</head>
<body>
    <form action="/search-post" method="post">
        {% csrf_token %}
        <input type="text" name="q">
        <input type="submit" value="Submit">
    </form>

    <p>{{ rlt }}</p>
</body>
</html>
在模板的末尾，我们增加一个 rlt 记号，为表格处理结果预留位置。
表格后面还有一个{% csrf_token %}的标签。csrf 全称是 Cross Site Request Forgery。这是Django提供的防止伪装提交请求的功能。POST 方法提交的表格，必须有此标签。
在HelloWorld目录下新建 search2.py 文件并使用 search_post 函数来处理 POST 请求：
/HelloWorld/HelloWorld/search2.py 文件代码：
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf

# 接收POST请求数据
def search_post(request):
    ctx ={}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
urls.py 规则修改为如下形式：
/HelloWorld/HelloWorld/urls.py 文件代码：
from django.conf.urls import url
from . import view,testdb,search,search2

urlpatterns = [
    url(r'^hello$', view.hello),
    url(r'^testdb$', testdb.testdb),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
]
访问 http://127.0.0.1:8000/search-post 显示结果如下：

完成以上实例后，我们的目录结构为：
HelloWorld
|-- HelloWorld
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- search.py
|   |-- search.pyc
|   |-- search2.py
|   |-- search2.pyc
|   |-- settings.py
|   |-- settings.pyc
|   |-- testdb.py
|   |-- testdb.pyc
|   |-- urls.py
|   |-- urls.pyc
|   |-- view.py
|   |-- view.pyc
|   |-- wsgi.py
|   `-- wsgi.pyc
|-- TestModel
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- admin.py
|   |-- admin.pyc
|   |-- apps.py
|   |-- migrations
|   |   |-- 0001_initial.py
|   |   |-- 0001_initial.pyc
|   |   |-- __init__.py
|   |   `-- __init__.pyc
|   |-- models.py
|   |-- models.pyc
|   |-- tests.py
|   `-- views.py
|-- db.sqlite3
|-- manage.py
`-- templates
    |-- base.html
    |-- hello.html
    |-- post.html
    `-- search_form.html
Request 对象
每个 view 函数的第一个参数是一个 HttpRequest 对象，就像下面这个 hello() 函数:
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello world")
HttpRequest对象包含当前请求URL的一些信息：
属性
描述
path
请求页面的全路径,不包括域名—例如, "/hello/"。
method
请求中使用的HTTP方法的字符串表示。全大写表示。例如:
if request.method == 'GET':
    do_something()
elif request.method == 'POST':
    do_something_else()
GET
包含所有HTTP GET参数的类字典对象。参见QueryDict 文档。
POST
包含所有HTTP POST参数的类字典对象。参见QueryDict 文档。
服务器收到空的POST请求的情况也是有可能发生的。也就是说，表单form通过HTTP POST方法提交请求，但是表单中可以没有数据。因此，不能使用语句if request.POST来判断是否使用HTTP POST方法；应该使用if request.method == "POST" (参见本表的method属性)。
注意: POST不包括file-upload信息。参见FILES属性。
REQUEST
为了方便，该属性是POST和GET属性的集合体，但是有特殊性，先查找POST属性，然后再查找GET属性。借鉴PHP's $_REQUEST。
例如，如果GET = {"name": "john"} 和POST = {"age": '34'},则 REQUEST["name"] 的值是"john", REQUEST["age"]的值是"34".
强烈建议使用GET and POST,因为这两个属性更加显式化，写出的代码也更易理解。
COOKIES
包含所有cookies的标准Python字典对象。Keys和values都是字符串。参见第12章，有关于cookies更详细的讲解。
FILES
包含所有上传文件的类字典对象。FILES中的每个Key都是<input type="file" name="" />标签中name属性的值. FILES中的每个value 同时也是一个标准Python字典对象，包含下面三个Keys:
filename: 上传文件名,用Python字符串表示
content-type: 上传文件的Content type
content: 上传文件的原始内容
注意：只有在请求方法是POST，并且请求页面中<form>有enctype="multipart/form-data"属性时FILES才拥有数据。否则，FILES 是一个空字典。
META
包含所有可用HTTP头部信息的字典。 例如:
CONTENT_LENGTH
CONTENT_TYPE
QUERY_STRING: 未解析的原始查询字符串
REMOTE_ADDR: 客户端IP地址
REMOTE_HOST: 客户端主机名
SERVER_NAME: 服务器主机名
SERVER_PORT: 服务器端口
META 中这些头加上前缀HTTP_最为Key, 例如:
HTTP_ACCEPT_ENCODING
HTTP_ACCEPT_LANGUAGE
HTTP_HOST: 客户发送的HTTP主机头信息
HTTP_REFERER: referring页
HTTP_USER_AGENT: 客户端的user-agent字符串
HTTP_X_BENDER: X-Bender头信息
user
是一个django.contrib.auth.models.User 对象，代表当前登录的用户。
如果访问用户当前没有登录，user将被初始化为django.contrib.auth.models.AnonymousUser的实例。
你可以通过user的is_authenticated()方法来辨别用户是否登录：
if request.user.is_authenticated():
    # Do something for logged-in users.
else:
    # Do something for anonymous users.
只有激活Django中的AuthenticationMiddleware时该属性才可用
session
唯一可读写的属性，代表当前会话的字典对象。只有激活Django中的session支持时该属性才可用。 参见第12章。
raw_post_data
原始HTTP POST数据，未解析过。 高级处理时会有用处。
Request对象也有一些有用的方法：
方法	描述
__getitem__(key)	返回GET/POST的键值,先取POST,后取GET。如果键不存在抛出 KeyError。
这是我们可以使用字典语法访问HttpRequest对象。
例如,request["foo"]等同于先request.POST["foo"] 然后 request.GET["foo"]的操作。
has_key()	检查request.GET or request.POST中是否包含参数指定的Key。
get_full_path()	返回包含查询字符串的请求路径。例如， "/music/bands/the_beatles/?print=true"
is_secure()	如果请求是安全的，返回True，就是说，发出的是HTTPS请求。
QueryDict对象
在HttpRequest对象中, GET和POST属性是django.http.QueryDict类的实例。
QueryDict类似字典的自定义类，用来处理单键对应多值的情况。
QueryDict实现所有标准的词典方法。还包括一些特有的方法：
方法	描述
__getitem__
和标准字典的处理有一点不同，就是，如果Key对应多个Value，__getitem__()返回最后一个value。
__setitem__
设置参数指定key的value列表(一个Python list)。注意：它只能在一个mutable QueryDict 对象上被调用(就是通过copy()产生的一个QueryDict对象的拷贝).
get()
如果key对应多个value，get()返回最后一个value。
update()
参数可以是QueryDict，也可以是标准字典。和标准字典的update方法不同，该方法添加字典 items，而不是替换它们:
>>> q = QueryDict('a=1')

>>> q = q.copy() # to make it mutable

>>> q.update({'a': '2'})

>>> q.getlist('a')

 ['1', '2']

>>> q['a'] # returns the last

['2']
items()
和标准字典的items()方法有一点不同,该方法使用单值逻辑的__getitem__():
>>> q = QueryDict('a=1&a=2&a=3')

>>> q.items()

[('a', '3')]
values()
和标准字典的values()方法有一点不同,该方法使用单值逻辑的__getitem__():
此外, QueryDict也有一些方法，如下表：
方法	描述
copy()
返回对象的拷贝，内部实现是用Python标准库的copy.deepcopy()。该拷贝是mutable(可更改的) — 就是说，可以更改该拷贝的值。
getlist(key)
返回和参数key对应的所有值，作为一个Python list返回。如果key不存在，则返回空list。 It's guaranteed to return a list of some sort..
setlist(key,list_)
设置key的值为list_ (unlike __setitem__()).
appendlist(key,item)
添加item到和key关联的内部list.
setlistdefault(key,list)
和setdefault有一点不同，它接受list而不是单个value作为参数。
lists()
和items()有一点不同, 它会返回key的所有值，作为一个list, 例如:
>>> q = QueryDict('a=1&a=2&a=3')

>>> q.lists()

[('a', ['1', '2', '3'])]

urlencode()
返回一个以查询字符串格式进行格式化后的字符串(e.g., "a=2&b=3&b=5").


"""

----------------------------------------------------------------------------------------------------------------------------------------------------------------

Django Admin 管理工具
Django 提供了基于 web 的管理工具。
Django 自动管理工具是 django.contrib 的一部分。你可以在项目的 settings.py 中的 INSTALLED_APPS 看到它：
/HelloWorld/HelloWorld/settings.py 文件代码：
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
django.contrib是一套庞大的功能集，它是Django基本代码的组成部分。
激活管理工具
通常我们在生成项目时会在 urls.py 中自动设置好，我们只需去掉注释即可。
配置项如下所示：
/HelloWorld/HelloWorld/urls.py 文件代码：
# urls.py
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
当这一切都配置好后，Django 管理工具就可以运行了。
使用管理工具
启动开发服务器，然后在浏览器中访问 http://127.0.0.1:8000/admin/，得到如下界面：

你可以通过命令 python manage.py createsuperuser 来创建超级用户，如下所示：
# python manage.py createsuperuser
Username (leave blank to use 'root'): admin
Email address: admin@runoob.com
Password:
Password (again):
Superuser created successfully.
[root@solar HelloWorld]#
之后输入用户名密码登录，界面如下：

为了让 admin 界面管理某个数据模型，我们需要先注册该数据模型到 admin。比如，我们之前在 TestModel 中已经创建了模型 Test 。修改 TestModel/admin.py:
HelloWorld/TestModel/admin.py: 文件代码：
from django.contrib import admin
from TestModel.models import Test

# Register your models here.
admin.site.register(Test)
刷新后即可看到 Testmodel 数据表:

复杂模型
管理页面的功能强大，完全有能力处理更加复杂的数据模型。
先在 TestModel/models.py 中增加一个更复杂的数据模型：
HelloWorld/TestModel/models.py: 文件代码：
from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)

class Contact(models.Model):
    name   = models.CharField(max_length=200)
    age    = models.IntegerField(default=0)
    email  = models.EmailField()
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name    = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name
这里有两个表。Tag 以 Contact 为外部键。一个 Contact 可以对应多个 Tag。
我们还可以看到许多在之前没有见过的属性类型，比如 IntegerField 用于存储整数。

在 TestModel/admin.py 注册多个模型并显示：
HelloWorld/TestModel/admin.py: 文件代码：
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
admin.site.register([Test, Contact, Tag])
刷新管理页面，显示结果如下：

在以上管理工具我们就能进行复杂模型操作。
如果你之前还未创建表结构，可使用以下命令创建：
$ python manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
$ python manage.py migrate TestModel   # 创建表结构
自定义表单
我们可以自定义管理页面，来取代默认的页面。比如上面的 "add" 页面。我们想只显示 name 和 email 部分。修改 TestModel/admin.py:
HelloWorld/TestModel/admin.py: 文件代码：
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fields = ('name', 'email')

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
以上代码定义了一个 ContactAdmin 类，用以说明管理页面的显示格式。
里面的 fields 属性定义了要显示的字段。
由于该类对应的是 Contact 数据模型，我们在注册的时候，需要将它们一起注册。显示效果如下：

我们还可以将输入栏分块，每个栏也可以定义自己的格式。修改 TestModel/admin.py为：
HelloWorld/TestModel/admin.py: 文件代码：
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test, Tag])
上面的栏目分为了 Main 和 Advance 两部分。classes 说明它所在的部分的 CSS 格式。这里让 Advance 部分隐藏：

Advance 部分旁边有一个 Show 按钮，用于展开，展开后可点击 Hide 将其隐藏，如下图所示：

内联(Inline)显示
上面的 Contact 是 Tag 的外部键，所以有外部参考的关系。
而在默认的页面显示中，将两者分离开来，无法体现出两者的从属关系。我们可以使用内联显示，让 Tag 附加在 Contact 的编辑页面上显示。
修改TestModel/admin.py：
HelloWorld/TestModel/admin.py: 文件代码：
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
显示效果如下：

列表页的显示
在 Contact 输入数条记录后，Contact 的列表页看起来如下:

我们也可以自定义该页面的显示，比如在列表中显示更多的栏目，只需要在 ContactAdmin 中增加 list_display 属性:
HelloWorld/TestModel/admin.py: 文件代码：
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
刷新页面显示效果如下：

搜索功能在管理大量记录时非常有，我们可以使用 search_fields 为该列表页增加搜索栏：
HelloWorld/TestModel/admin.py: 文件代码：
from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'email') # list
    search_fields = ('name',)
    inlines = [TagInline]  # Inline
    fieldsets = (
        ['Main',{
            'fields':('name','email'),
        }],
        ['Advance',{
            'classes': ('collapse',),
            'fields': ('age',),
        }]

    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
在本实例中我们搜索了 name 为 runoob 的记录，显示结果如下：

Django Admin 管理工具还有非常多实用的功能，感兴趣的同学可以深入研究下。