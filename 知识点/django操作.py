# -*- coding: utf-8 -*-

"""
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
"""

tae\django\HelloWorld

使用 django-admin.py 来创建 HelloWorld 项目：""" django-admin.py startproject HelloWorld """

启动服务器： """ python manage.py runserver 0.0.0.0:8000  """

HelloWorld 目录底下创建 templates 目录建立 .html文件


创建一个 TestModel 的 app:  """ django-admin.py startapp TestModel """

            """  python manage.py migrate   """# 创建表结构

            """  python manage.py makemigrations TestModel  """# 让 Django 知道我们在我们的模型有一些变更
          """    python manage.py migrate TestModel  """ # 创建表结构


命令 """ python manage.py createsuperuser """来创建超级用户



模块索引
"""
a
django.apps
c
django.conf
django.conf.urls
django.conf.urls.i18n
django.contrib
django.contrib.admin	Django的管理网站。
django.contrib.admindocs	Django的管理文档生成器。
django.contrib.auth	Django的验证框架。
django.contrib.auth.backends	Django的内置认证后端类。
django.contrib.auth.forms
django.contrib.auth.hashers
django.contrib.auth.middleware	身份验证中间件。
django.contrib.auth.signals
django.contrib.auth.views
django.contrib.contenttypes	为已安装的模块提供通用接口。
django.contrib.contenttypes.admin
django.contrib.contenttypes.fields
django.contrib.contenttypes.forms
django.contrib.flatpages	一个管理简单扁平的框架？数据库中的HTML内容。
django.contrib.gis	Django的地理信息系统（GIS）扩展
django.contrib.gis.admin	GeoDjango对管理网站的扩展。
django.contrib.gis.db.backends	GeoDjango的空间数据库后端。
django.contrib.gis.db.models	GeoDjango模型和字段API。
django.contrib.gis.feeds	GeoDjango的用于生成空间Feed的框架。
django.contrib.gis.forms	GeoDjango表单API。
django.contrib.gis.gdal	GeoDjango与GDAL库的高级接口。
django.contrib.gis.geoip	MaxMind的GeoIP C库的高级Python接口。
django.contrib.gis.geos	GeoDjango到GEOS库的高级接口。
django.contrib.gis.measure	GeoDjango的距离和面积测量对象。
django.contrib.gis.serializers.geojson	GeoJSON格式的GeoDjango模型的序列化。
django.contrib.gis.utils	GeoDjango的实用程序集合
django.contrib.gis.utils.layermapping	GeoDjango模型的空间数据导入实用程序。
django.contrib.gis.utils.ogrinspect	用于检查OGR数据源的实用程序。
django.contrib.gis.widgets	GeoDjango widgets API。
django.contrib.humanize	一组用于向数据添加“人性化”的Django模板过滤器。
django.contrib.messages	提供基于cookie和基于会话的临时邮件存储。
django.contrib.messages.middleware	消息中间件。
django.contrib.postgres	PostgreSQL特定字段和功能
django.contrib.postgres.validators
django.contrib.redirects	用于管理重定向的框架
django.contrib.sessions	为Django项目提供会话管理。
django.contrib.sessions.middleware	会话中间件。
django.contrib.sitemaps	用于生成Google sitemap XML文件的框架。
django.contrib.sites	允许您从同一数据库和Django项目操作多个网站
django.contrib.sites.middleware	网站中间件。
django.contrib.staticfiles	用于处理静态文件的应用程序。
django.contrib.syndication	用于在RSS和Atom中生成联合供稿的框架非常容易。
django.contrib.webdesign	主要面向Web *设计师*而不是Web *开发人员*的帮助者和实用程序。
django.core
django.core.checks
django.core.exceptions	Django核心异常
django.core.files	文件处理和存储
django.core.files.storage
django.core.files.uploadedfile	表示上传的文件的类。
django.core.files.uploadhandler	Django的文件上传处理程序。
django.core.mail	帮助者可以轻松发送电子邮件。
django.core.management
django.core.paginator	课程可帮助您轻松管理分页数据。
django.core.signals	请求/响应系统发送的核心信号。
django.core.signing	Django的签名框架。
django.core.urlresolvers
django.core.validators	验证实用程序和基类
d
django.db
django.db.backends	数据库包装程序发送的核心信号。
django.db.backends.base.schema
django.db.migrations	Django模型的模式迁移支持
django.db.migrations.operations
django.db.models
django.db.models.fields	内置字段类型。
django.db.models.fields.related	相关字段类型
django.db.models.functions	数据库函数
django.db.models.lookups	Lookups API
django.db.models.options	模型元类层
django.db.models.signals	由模型系统发送的信号。
django.db.transaction
django.dispatch	信号分派
f
django.forms
django.forms.fields	Django的内置表单字段。
django.forms.formsets	在同一页面上使用多个表单的抽象。
django.forms.models	ModelForm和ModelFormset。
django.forms.widgets	Django的内置窗体小部件。
h
django.http	处理HTTP请求和响应的类。
m
django.middleware	Django的内置中间件类。
django.middleware.cache	网站级缓存的中间件。
django.middleware.clickjacking	Clickjacking protection
django.middleware.common	中间件为完美主义者添加“常见”便利。
django.middleware.csrf	中间件添加防护跨站点请求伪造。
django.middleware.gzip	中间件为GZipped内容提供性能。
django.middleware.http	中间件处理高级HTTP功能。
django.middleware.locale	中间件，根据请求启用语言选择。
django.middleware.security	安全中间件。
s
django.shortcuts	方便快捷方式跨越Django的多个MVC堆栈。
t
django.template	Django的范本系统
django.template.backends
django.template.backends.django
django.template.backends.jinja2
django.template.loader
django.template.response	处理延迟呈现的HTTP响应的类。
django.test	Django应用程序的测试工具。
django.test.signals	测试期间发送的信号。
django.test.utils	帮助者编写自定义测试运行器。
u
django.utils	Django的内置实用程序。
django.utils.cache	用于控制缓存的帮助函数。
django.utils.datastructures	不在Python标准库中的数据结构。
django.utils.dateparse	解析datetime对象的函数。
django.utils.decorators	有助于为视图创建装饰器的函数。
django.utils.encoding	一系列辅助函数，用于管理字符编码。
django.utils.feedgenerator	整合Feed生成库 - 用于生成RSS等。
django.utils.functional	功能编程工具。
django.utils.html	HTML帮助函数
django.utils.http	HTTP帮助函数。 （网址编码，Cookie处理，...）
django.utils.log	Django应用程序日志记录工具
django.utils.module_loading	使用Python模块的函数
django.utils.safestring	用于处理可以安全显示的字符串的函数和类，无需在HTML中进一​​步转义。
django.utils.six
django.utils.text	文本处理。
django.utils.timezone	时区支持。
django.utils.translation
django.utils.tzinfo	与``datetime.datetime``一起使用的``tzinfo``类的实现。
v
django.views	Django的内置视图。
django.views.decorators.csrf
django.views.decorators.gzip
django.views.decorators.http
django.views.decorators.vary
django.views.generic.dates
django.views.i18n


"""