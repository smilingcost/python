#coding=utf-8
import os
"""
IIS-Apache-Tomcat的区别
IIS与Tomcat的区别

IIS是微软公司的Web服务器。主要支持ASP语言环境.
Tomcat是Java Servlet 2.2和JavaServer Pages 1.1技术的标准实现，是基于Apache许可证下开发的SJP语言环境容器,严格得说不能算是一个WEB服务器,而是Apache服务适配器。
tomcat主要的任务不是WEB服务,而是支持JSP语言环境.
IIS就是也款WEB服务器,支持ASP语言环境

Apache与Tomcat的区别

APACHE是一个web服务器环境程序 启用他可以作为web服务器使用 不过只支持静态网页. 但asp,php,cgi,jsp等动态网页的就不行.
如果要在APACHE环境下运行jsp 的话就需要一个解释器来执行jsp网页, 而这个jsp解释器就是TOMCAT, 为什么还要JDK呢？因为jsp需要连接数据库的话就要jdk来提供连接数据库的驱程，所以要运行jsp的web服务器平台就需要APACHE+TOMCAT+JDK 整合的好处是：如果客户端请求的是静态页面，则只需要Apache服务器响应请求如果客户端请求动态页面，则是Tomcat服务器响应请求因为jsp是服务器端解释代码的，这样整合就可以减少Tomcat的服务开销 .
apache是web服务器，tomcat是应用（java）服务器，它只是一个servlet(jsp也翻译成servlet)容器，可以认为是apache的扩展。
Apache:普通服务器，本身只支持html即普通网页,它是html容器，功能像IIS一样
tomcat:解释java程序（jsp,serverlet），它是是jsp/servlet容器，用于发布JSP及JAVA的
apache是一辆卡车，上面可以装一些东西如html等。但是不能装水，要装水必须要有容器（桶），tomcat就是一个桶（装像JAVA这样的水），而这个桶也可以不放在卡车上。

IIS与 Apache的区别

对于中小企业来说建立自己的网站，对外展示自己的页面是最平常不过的事情了。目前最流行的建立WWW服务工具就要属Apache与IIS了。那么他们之间都有什么区别呢?到底哪个工具才是最适合我们的呢?今天就来讨论下这个问题。

一、免费与收费之争:

虽然很多用户都使用IIS建立网站，他是集成于Windows操作系统中的组件。不过要想合法使用IIS就要购买正版Windows操作系统。

反观Apache，他是完全免费的。不需要支付任何费用就可以免费下载并使用了。

结论——Apache免费，IIS收费,前者占优。

二、稳定性:

接下来要比较的就是稳定性了，WWW服务要随时运转正常，一个网站也需要一天24小时，一周七天为公众开放。所以稳定性是IIS和APACHE比较的重点。

IIS在实际使用中经常出现500错误，而且有的时候还会出现莫名其妙的假死现象。用户需要不定期的重新启动IIS服务才能保证网站的正常。

Apache在配置上比IIS要复杂，不过一经设置完毕就可以长期的工作了。大型网站都使用APACHE作为自己的WWW服务提供工具。APACHE的所有配置都保存在配置文件中，使用时完全按照配置文件中记录的信息执行。一般不会发生莫名其妙的假死情况。

小提示:在windows2003系统下使用IIS比用APACHE性能要好。

结论——APACHE稳定，IIS有时假死，前者占优。

三、扩展性:

扩展性是指WWW服务提供工具是否可以应用于多种场合，多种网络情况，多种操作系统。

IIS只能在微软公司的windows操作系统下使用，离开了windows他将一事无成。无法移植到其他类型的操作系统中。

APACHE是个多面手，他不仅仅应用于windows，对于unix,linux以及freebsd等多种操作系统来说他都可以胜任工作。而且不同操作系统的配置步骤基本类似，可移植性非常高。

结论——IIS只能在windows下运行，apache应用范围广。apache获胜。
四、安全性:

经常看到某某网站被黑客攻击或者某某网站被非法用户上传病毒的消息，对于为其他人提供服务的站点来说，安全性是最重要的。如果一个网站连自身安全都没有保证的话，谁愿意浏览和使用呢。

早期的IIS在安全性方面存在着很大的问题，如果使用默认设置的话黑客可以轻松趁虚而入。不过在IIS6中微软公司对安全方面进行了大幅改进。只要保证操作系统补丁更新及时，就可以将网站安全系数尽可能的提高。特别是IIS6与.net平台相互倚靠，使安全性几乎完美。

APACHE在安全方面一直做的不错，因为很多用户都是在linux下使用apache，所以操作系统的特点使得linux下的apache具有先天的保护伞，安全性自然没得说。

结论——IIS6以前的版本有安全隐患，IIS6和APACHE一样安全可靠。IIS6与APACHE打个平手。

五、开放性:

所 谓开放性就是指是否开放了程序的源代码，众所周知IIS是WINDOWS系统的一部分，所以他的源代码是没有开放的。而apache则不同，最早他是为了 类unix系统服务的，所以完全对外开放源代码。任何人都可以分析他的代码，发现其中的漏洞，并发布补丁来弥补该漏洞。

正因为APACHE的这种开放性，也使其安全性大大提高。

结论——IIS不开放代码，APACHE开放源代码。后者获得胜利。

六、难易性:

一个工具使用的难易程度直接影响其用户的多少，特别是网页发布工具。毕竟很多公司希望有自己的网站，但又不希望聘请高薪的网络管理员来维护。因此必然找上手相对容易的工具来搭建自己的站点。

IIS开起来比较简单，很容易就可能让IIS工作，对外发布网站。不过管理员很容易出现错误配置和误操作问题。不过总体说来IIS还是非常容易学的，但要学好他恐怕是件非常困难的事。

APACHE的使用比IIS要难，需要有一定计算机及网络基础的人才可以使用。他的配置也不是图形化的，需要我们通过编辑配置文件来实现。但是单从APACHE的设置上讲，只要我们严格按照帮助文件进行参数设置的话还是没有什么难度的。

结论——IIS容易安装但难精通，APACHE安装相对困难，要想精通也不是一件容易的事。IIS略占优势。

七、编程性:

为了让网页更加丰富多采，更加美观，互动性更好，高手为我们开发了多种组件与控件，那么这些控件在IIS或APACHE下是否正常运行呢?

APACHE 下的Mod Rewrite功能非常强大,而IIS中的ISAPI的Rewrite需要专门开发，一般初学者是不能够实现的。APACHE可以使用 Subversion WebDev以及.htaccess功能，还可以使用ForceType。另外IIS对FastCGI的支持也不是很好，所以一些CGI、PHP程序运行 起来速度很慢，远不如apache。

结论——不同的环境下使用不同的组件，因为选择IIS还是APACHE由工作环境所决定，这点两者不分高下。

八、支持语言方面:

由于目前建立网站和论坛的语言多种多样，例如ASP，PHP，JSP等语言。那么IIS和APACHE对他们都支持吗?

IIS对ASP特别是.net运行很稳定，不过对于PHP和JSP就比较麻烦了。PHP需要经过反复配置才能在windows2003上支持。APACHE则能够很好的支持上面提到的几种语言，运行ASP，PHP，JSP都没有任何问题。

结论——APACHE支持语言比较多，IIS支持PHP和JSP时有点麻烦，需要经过一定的配置。APACHE获胜。

九、待遇方面:

提到待遇方面可能很多读者会比较纳闷，怎么IIS和APACHE还存在待遇问题呢?其实我们这里要讨论的是网络管理员的待遇。一个会IIS的网络管理员与一个会APACHE的网络管理员，他们的薪水是不一样的。

APACHE最大的好处就是配置参数多，如果要精通APACHE需要很高的水平。所以同等水平的网络管理员会APACHE的要比会IIS的待遇更好。

结论——钱多是获胜的唯一标准，APACHE占优。

总结:

其实今天我们在这里争论IIS好还是APACHE好是没有很大意义的，本文所进行的比较也只是给那些徘徊在网络管理员路口，不知道学习哪个工具来建立网站的读者一点参考。只有你对IIS和APACHE有了一个大概的了解之后，才能为自己的未来进行规划。

总 的来说Apache的优点在于在各种开源的WWW服务提供工具中特性最全，支持最广，相对比较稳定的，而且扩展性丰富。不过正因为要考虑扩展性，性能就肯 定不会太高，只能保持一个中等的水平。而IIS6在处理连接及事件性能方面还是很强大的，超过了APACHE。另外安全方面IIS6也有了质的飞跃，弥补 了以往IIS漏洞漫天的缺陷。如果你的公司网络环境不负责，没有涉及太多的开发的话建议仍然使用IIS6。当然如果是建立在WWW上的开发和调试还是使用 APACHE更加顺手。



总结：

　　Tomcat 服务器是一个免费的开放源代码的Web 应用服务器，属于轻量级应用服务器，在中小型系统和并发访问用户不是很多的场合下被普遍使用，是开发和调试JSP 程序的首选。对于一个初学者来说，可以这样认为，当在一台机器上配置好Apache 服务器，可利用它响应HTML（标准通用标记语言下的一个应用）页面的访问请求。实际上Tomcat 部分是Apache 服务器的扩展，但它是独立运行的，所以当你运行tomcat 时，它实际上作为一个与Apache 独立的进程单独运行的。

　　诀窍是，当配置正确时，Apache 为HTML页面服务，而Tomcat 实际上运行JSP 页面和Servlet。另外，Tomcat和IIS等Web服务器一样，具有处理HTML页面的功能，另外它还是一个Servlet和JSP容器，独立的Servlet容器是Tomcat的默认模式。不过，Tomcat处理静态HTML的能力不如Apache服务器。目前Tomcat最新版本为9.0。
"""

