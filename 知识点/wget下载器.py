#coding=utf-8
import os
"""
命令格式：
wget [参数列表] [目标软件、网页的网址]             //  用法： wget [选项]... [URL]...

长选项所必须的参数在使用短选项时也是必须的。

启动：
  -V,  --version                   显示 Wget 的版本信息并退出
  -h,  --help                      打印此帮助
  -b,  --background                启动后转入后台
  -e,  --execute=命令              运行一个“.wgetrc”风格的命令

日志和输入文件：
  -o,  --output-file=文件          将日志信息写入 FILE
  -a,  --append-output=文件        将信息添加至 FILE
  -d,  --debug                     打印大量调试信息
  -q,  --quiet                     安静模式 (无信息输出)
  -v,  --verbose                   详尽的输出 (此为默认值)
  -nv, --no-verbose                关闭详尽输出，但不进入安静模式
       --report-speed=类型         以 <类型> 报告带宽。类型可以是 bits
  -i,  --input-file=文件           下载本地或外部 <文件> 中的 URL
  -F,  --force-html                把输入文件当成 HTML 文件
  -B,  --base=URL                  解析相对于 URL 的 HTML 输入文件链接 (-i -F)
       --config=文件               指定要使用的配置文件
       --no-cookies                不读取任何配置文件
       --rejected-log=文件         将拒绝 URL 的原因写入 <文件>。

下载：
  -t,  --tries=数字                设置重试次数为 <数字> (0 代表无限制)
       --retry-connrefused         即使拒绝连接也是重试
  -O,  --output-document=文件      将文档写入 FILE
  -nc, --no-clobber                不要下载已存在将被覆盖的文件
  -c,  --continue                  断点续传下载文件
       --start-pos=偏移量          从由零计数的 <偏移量> 开始下载
       --progress=类型             选择进度条类型
       --show-progress             在任意啰嗦状态下都显示进度条
  -N,  --timestamping              只获取比本地文件新的文件
       --no-if-modified-since      不要在时间戳 (timestamping) 模式下使用
                                     if-modified-since get 条件请求
       --no-use-server-timestamps  don't set the local file's timestamp by
                                     the one on the server
  -S,  --server-response           打印服务器响应
       --spider                    不下载任何文件
  -T,  --timeout=SECONDS           将所有超时设为 SECONDS 秒
       --dns-timeout=SECS          设置 DNS 查寻超时为 SECS 秒
       --connect-timeout=SECS      设置连接超时为 SECS 秒
       --read-timeout=SECS         设置读取超时为 SECS 秒
  -w,  --wait=SECONDS              等待间隔为 SECONDS 秒
       --waitretry=SECONDS         在获取文件的重试期间等待 1..SECONDS 秒
       --random-wait               获取多个文件时，每次随机等待间隔 (0.5~1.5)*WAIT 秒
       --no-proxy                  禁止使用代理
  -Q,  --quota=数字                设置获取配额为 <数字> 字节
       --bind-address=ADDRESS      绑定至本地主机上的 ADDRESS (主机名或是 IP)
       --limit-rate=RATE           限制下载速率为 RATE
       --no-dns-cache              关闭 DNS 查询缓存
       --restrict-file-names=系统  限定文件名中的字符为 <系统> 允许的字符
       --ignore-case               匹配文件/目录时忽略大小写
  -4,  --inet4-only                仅连接至 IPv4 地址
  -6,  --inet6-only                仅连接至 IPv6 地址
       --prefer-family=地址族      首先连接至指定家族（IPv6，IPv4 或 none）的地址
       --user=用户                 将 ftp 和 http 的用户名均设置为 <用户>
       --password=密码             将 ftp 和 http 的密码均设置为 <密码>
       --ask-password              提示输入密码
       --no-iri                    关闭 IRI 支持
       --local-encoding=ENC        使用 ENC 作为 IRI (国际化资源标识符) 的本地编码
       --remote-encoding=ENC       使用 ENC 作为默认远程编码
       --unlink                    覆盖前移除文件

目录：
  -nd, --no-directories            不创建目录
  -x,  --force-directories         强制创建目录
  -nH, --no-host-directories       不要创建主 (host) 目录
       --protocol-directories      在目录中使用协议名称
  -P,  --directory-prefix=前缀     保存文件到 <前缀>/..
       --cut-dirs=数字             忽略远程目录中 <数字> 个目录层。

HTTP 选项：
       --http-user=用户            设置 http 用户名为 <用户>
       --http-password=密码        设置 http 密码为 <密码>
       --no-cache                  不使用服务器缓存的数据。
       --default-page=NAME         改变默认页 (通常是“index.html”)。
  -E,  --adjust-extension          以合适的扩展名保存 HTML/CSS 文档
       --ignore-length             忽略头部的‘Content-Length’区域
       --header=字符串             在头部插入 <字符串>
       --max-redirect              每页所允许的最大重定向
       --proxy-user=用户           使用 <用户> 作为代理用户名
       --proxy-password=密码       使用 <密码> 作为代理密码
       --referer=URL               在 HTTP 请求头包含‘Referer: URL’
       --save-headers              将 HTTP 头保存至文件。
  -U,  --user-agent=代理           标识自己为 <代理> 而不是 Wget/VERSION。
       --no-http-keep-alive        禁用 HTTP keep-alive (持久连接)。
       --no-cookies                不使用 cookies。
       --load-cookies=文件         会话开始前从 <文件> 中载入 cookies。
       --save-cookies=文件         会话结束后保存 cookies 至 FILE。
       --keep-session-cookies      载入并保存会话 (非永久) cookies。
       --post-data=字符串          使用 POST 方式；把 <字串>作为数据发送。
       --post-file=文件            使用 POST 方式；发送 <文件> 内容。
       --method=HTTP方法           在请求中使用指定的 <HTTP 方法>。
       --post-data=字符串          把 <字串> 作为数据发送，必须设置 --method
       --post-file=文件            发送 <文件> 内容，必须设置 --method
       --content-disposition       当选择本地文件名时允许 Content-Disposition
                                   头部 (实验中)。
       --content-on-error          在服务器错误时输出接收到的内容
       --auth-no-challenge         不先等待服务器询问就发送基本 HTTP 验证信息。

HTTPS (SSL/TLS) 选项：
       --secure-protocol=PR         选择安全协议，可以是 auto、SSLv2、
                                    SSLv3、TLSv1、PFS 中的一个。
       --https-only                 只跟随安全的 HTTPS 链接
       --no-check-certificate       不要验证服务器的证书。
       --certificate=文件           客户端证书文件。
       --certificate-type=类型      客户端证书类型，PEM 或 DER。
       --private-key=文件           私钥文件。
       --private-key-type=类型      私钥文件类型，PEM 或 DER。
       --ca-certificate=文件        带有一组 CA 证书的文件。
       --ca-directory=DIR           保存 CA 证书的哈希列表的目录。
       --ca-certificate=文件        带有一组 CA 证书的文件。
       --pinnedpubkey=FILE/HASHES  Public key (PEM/DER) file, or any number
                                   of base64 encoded sha256 hashes preceded by
                                   'sha256//' and seperated by ';', to verify
                                   peer against

HSTS 选项：
       --no-hsts                   禁用 HSTS
       --hsts-file                 HSTS 数据库路径（将覆盖默认值）

FTP 选项：
       --ftp-user=用户             设置 ftp 用户名为 <用户>。
       --ftp-password=密码         设置 ftp 密码为 <密码>
       --no-remove-listing         不要删除‘.listing’文件
       --no-glob                   不在 FTP 文件名中使用通配符展开
       --no-passive-ftp            禁用“passive”传输模式
       --preserve-permissions      保留远程文件的权限
       --retr-symlinks             递归目录时，获取链接的文件 (而非目录)

FTPS 选项：
       --ftps-implicit                 使用隐式 FTPS（默认端口 990）
       --ftps-resume-ssl               打开数据连接时继续控制连接中的 SSL/TLS 会话
       --ftps-clear-data-connection    只加密控制信道；数据传输使用明文
       --ftps-fallback-to-ftp          回落到 FTP，如果目标服务器不支持 FTPS
WARC 选项：
       --warc-file=文件名          在一个 .warc.gz 文件里保持请求/响应数据
       --warc-header=字符串        在头部插入 <字符串>
       --warc-max-size=数字        将 WARC 的最大尺寸设置为 <数字>
       --warc-cdx                  写入 CDX 索引文件
       --warc-dedup=文件名         不要记录列在此 CDX 文件内的记录
       --no-warc-compression       不要 GZIP 压缩 WARC 文件
       --no-warc-digests           不要计算 SHA1 摘要
       --no-warc-keep-log          不要在 WARC 记录中存储日志文件
       --warc-tempdir=目录         WARC 写入器的临时文件目录

递归下载：
  -r,  --recursive                 指定递归下载
  -l,  --level=数字                最大递归深度 (inf 或 0 代表无限制，即全部下载)。
       --delete-after             下载完成后删除本地文件
  -k,  --convert-links            让下载得到的 HTML 或 CSS 中的链接指向本地文件
       --convert-file-only         convert the file part of the URLs only (usually known as the basename)
       --backups=N                 写入文件 X 前，轮换移动最多 N 个备份文件
  -K,  --backup-converted         在转换文件 X 前先将它备份为 X.orig。
  -m,  --mirror                   -N -r -l inf --no-remove-listing 的缩写形式。
  -p,  --page-requisites          下载所有用于显示 HTML 页面的图片之类的元素。
       --strict-comments          用严格方式 (SGML) 处理 HTML 注释。

递归接受/拒绝：
  -A,  --accept=列表               逗号分隔的可接受的扩展名列表
  -R,  --reject=列表               逗号分隔的要拒绝的扩展名列表
       --accept-regex=REGEX        匹配接受的 URL 的正则表达式
       --reject-regex=REGEX        匹配拒绝的 URL 的正则表达式
       --regex-type=类型           正则类型 (posix|pcre)
  -D,  --domains=列表              逗号分隔的可接受的域名列表
       --exclude-domains=列表      逗号分隔的要拒绝的域名列表
       --follow-ftp                跟踪 HTML 文档中的 FTP 链接
       --follow-tags=列表          逗号分隔的跟踪的 HTML 标识列表
       --ignore-tags=列表          逗号分隔的忽略的 HTML 标识列表
  -H,  --span-hosts                递归时转向外部主机
  -L,  --relative                  仅跟踪相对链接
  -I,  --include-directories=列表  允许目录的列表
       --trust-server-names        使用重定向 URL 的最后一段作为本地文件名
  -X,  --exclude-directories=列表  排除目录的列表
  -np, --no-parent                 不追溯至父目录
1、使用wget下载单个文件

[plain] view plain copy
以下的例子是从网络下载一个文件并保存在当前目录
wget http://cn.wordpress.org/wordpress-3.1-zh_CN.zip
在下载的过程中会显示进度条，包含（下载完成百分比，已经下载的字节，当前下载速度，剩余下载时间）。
2、使用wget -O下载并以不同的文件名保存
[plain] view plain copy
wget默认会以最后一个符合”/”的后面的字符来命令，对于动态链接的下载通常文件名会不正确。
错误：下面的例子会下载一个文件并以名称download.php?id=1080保存

wget http://www.centos.bz/download?id=1
即使下载的文件是zip格式，它仍然以download.php?id=1080命令。
正确：为了解决这个问题，我们可以使用参数-O来指定一个文件名：

wget -O wordpress.zip http://www.centos.bz/download.php?id=1080
3、使用wget –limit -rate限速下载
[plain] view plain copy
当你执行wget的时候，它默认会占用全部可能的宽带下载。但是当你准备下载一个大文件，而你还需要下载其它文件时就有必要限速了。

wget –limit-rate=300k http://cn.wordpress.org/wordpress-3.1-zh_CN.zip
4、使用wget -c断点续传
[plain] view plain copy
使用wget -c重新启动下载中断的文件:

wget -c http://cn.wordpress.org/wordpress-3.1-zh_CN.zip
对于我们下载大文件时突然由于网络等原因中断非常有帮助，我们可以继续接着下载而不是重新下载一个文件。需要继续中断的下载时可以使用-c参数。
5、使用wget -b后台下载
[plain] view plain copy
对于下载非常大的文件的时候，我们可以使用参数-b进行后台下载。

wget -b http://cn.wordpress.org/wordpress-3.1-zh_CN.zip
Continuing in background, pid 1840.
Output will be written to `wget-log’.
你可以使用以下命令来察看下载进度

tail -f wget-log
6、伪装代理名称下载
[plain] view plain copy
有些网站能通过根据判断代理名称不是浏览器而拒绝你的下载请求。不过你可以通过–user-agent参数伪装。

wget –user-agent=”Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16″ 下载链接
7、使用wget –spider测试下载链接
[plain] view plain copy
当你打算进行定时下载，你应该在预定时间测试下载链接是否有效。我们可以增加–spider参数进行检查。

wget –spider URL
如果下载链接正确，将会显示

wget –spider URL
Spider mode enabled. Check if remote file exists.
HTTP request sent, awaiting response… 200 OK
Length: unspecified [text/html]
Remote file exists and could contain further links,
but recursion is disabled — not retrieving.
这保证了下载能在预定的时间进行，但当你给错了一个链接，将会显示如下错误

wget –spider url
Spider mode enabled. Check if remote file exists.
HTTP request sent, awaiting response… 404 Not Found
Remote file does not exist — broken link!!!
你可以在以下几种情况下使用spider参数：

定时下载之前进行检查
间隔检测网站是否可用
检查网站页面的死链接
8、使用wget –tries增加重试次数
[plain] view plain copy
如果网络有问题或下载一个大文件也有可能失败。wget默认重试20次连接下载文件。如果需要，你可以使用–tries增加重试次数。

wget –tries=40 URL
9、使用wget -i下载多个文件
[plain] view plain copy
首先，保存一份下载链接文件

cat > filelist.txt
url1
url2
url3
url4
接着使用这个文件和参数-i下载

wget -i filelist.txt
10、使用wget –mirror镜像网站
[plain] view plain copy
下面的例子是下载整个网站到本地。

wget –mirror -p –convert-links -P ./LOCAL URL
–miror:开户镜像下载
-p:下载所有为了html页面显示正常的文件
–convert-links:下载后，转换成本地的链接
-P ./LOCAL：保存所有文件和目录到本地指定目录
11、使用wget –reject过滤指定格式下载
[plain] view plain copy
你想下载一个网站，但你不希望下载图片，你可以使用以下命令。

wget –reject=gif url
12、使用wget -o把下载信息存入日志文件
[plain] view plain copy
你不希望下载信息直接显示在终端而是在一个日志文件，可以使用以下命令：

wget -o download.log URL
13、使用wget -Q限制总下载文件大小
[plain] view plain copy
当你想要下载的文件超过5M而退出下载，你可以使用以下命令:

wget -Q5m -i filelist.txt
注意：这个参数对单个文件下载不起作用，只能递归下载时才有效。
14、使用wget -r -A下载指定格式文件
[plain] view plain copy
可以在以下情况使用该功能

下载一个网站的所有图片
下载一个网站的所有视频
下载一个网站的所有PDF文件
wget -r -A.pdf url
15、使用wget FTP下载
[plain] view plain copy
你可以使用wget来完成ftp链接的下载。
使用wget匿名ftp下载

wget ftp-url

使用wget用户名和密码认证的ftp下载

wget –ftp-user=USERNAME –ftp-password=PASSWORD url


wget是在Linux下开发的开放源代码的软件，作者是Hrvoje Niksic，后来被移植到包括Windows在内的各个平台上。它有以下功能和特点：
[plain] view plain copy
（1）支持断点下传功能；这一点，也是网络蚂蚁和FlashGet当年最大的卖点，现在，Wget也可以使用此功能，那些网络不是太好的用户可以放心了；
（2）同时支持FTP和HTTP下载方式；尽管现在大部分软件可以使用HTTP方式下载，但是，有些时候，仍然需要使用FTP方式下载软件；
（3）支持代理服务器；对安全强度很高的系统而言，一般不会将自己的系统直接暴露在互联网上，所以，支持代理是下载软件必须有的功能；
（4）设置方便简单；可能，习惯图形界面的用户已经不是太习惯命令行了，但是，命令行在设置上其实有更多的优点，最少，鼠标可以少点很多次，也不要担心是否错点鼠标；
（5）程序小，完全免费；程序小可以考虑不计，因为现在的硬盘实在太大了；完全免费就不得不考虑了，即使网络上有很多免费软件，但是，这些软件的广告不是我们喜欢的；
wget虽然功能强大，但是使用起来还是比较简单的，基本的语法是：wget [参数列表] URL。下面就结合具体的例子来说明一下wget的用法。

1、下载整个http或者ftp站点。
[plain] view plain copy
wget http://place.your.url/here
这个命令可以将http://place.your.url/here 首页下载下来。使用-x会强制建立服务器上一模一样的目录，如果使用-nd参数，那么服务器上下载的所有内容都会加到本地当前目录。

wget -r http://place.your.url/here
这 个命令会按照递归的方法，下载服务器上所有的目录和文件，实质就是下载整个网站。这个命令一定要小心使用，因为在下载的时候，被下载网站指向的所有地址同 样会被下载，因此，如果这个网站引用了其他网站，那么被引用的网站也会被下载下来！基于这个原因，这个参数不常用。可以用-l number参数来指定下载的层次。例如只下载两层，那么使用-l 2。

要是您想制作镜像站点，那么可以使用－m参数，例如：wget -m http://place.your.url/here
这时wget会自动判断合适的参数来制作镜像站点。此时，wget会登录到服务器上，读入robots.txt并按robots.txt的规定来执行。
2、断点续传。
[plain] view plain copy
当文件特别大或者网络特别慢的时候，往往一个文件还没有下载完，连接就已经被切断，此时就需要断点续传。wget的断点续传是自动的，只需要使用-c参数，例如：
wget -c http://the.url.of/incomplete/file
使用断点续传要求服务器支持断点续传。-t参数表示重试次数，例如需要重试100次，那么就写-t 100，如果设成-t 0，那么表示无穷次重试，直到连接成功。-T参数表示超时等待时间，例如-T 120，表示等待120秒连接不上就算超时。
3、批量下载。
[plain] view plain copy
如果有多个文件需要下载，那么可以生成一个文件，把每个文件的URL写一行，例如生成文件download.txt，然后用命令：wget -i download.txt
这样就会把download.txt里面列出的每个URL都下载下来。（如果列的是文件就下载文件，如果列的是网站，那么下载首页）
4、选择性的下载。
[plain] view plain copy
可以指定让wget只下载一类文件，或者不下载什么文件。例如：
wget -m –reject=gif http://target.web.site/subdirectory
表示下载http://target.web.site/subdirectory，但是忽略gif文件。–accept=LIST 可以接受的文件类型，–reject=LIST拒绝接受的文件类型。
5、密码和认证。
[plain] view plain copy
wget只能处理利用用户名/密码方式限制访问的网站，可以利用两个参数：
–http-user=USER设置HTTP用户
–http-passwd=PASS设置HTTP密码
对于需要证书做认证的网站，就只能利用其他下载工具了，例如curl。
6、利用代理服务器进行下载。
[plain] view plain copy
如果用户的网络需要经过代理服务器，那么可以让wget通过代理服务器进行文件的下载。此时需要在当前用户的目录下创建一个.wgetrc文件。文件中可以设置代理服务器：
http-proxy = 111.111.111.111:8080
ftp-proxy = 111.111.111.111:8080
分别表示http的代理服务器和ftp的代理服务器。如果代理服务器需要密码则使用：
–proxy-user=USER设置代理用户
–proxy-passwd=PASS设置代理密码
这两个参数。
使用参数–proxy=on/off 使用或者关闭代理。
wget还有很多有用的功能，需要用户去挖掘。
中文文档名在平常的情况下会被编码， 但是在 –cut-dirs 时又是正常的，
wget -r -np -nH –cut-dirs=3 ftp://host/test/
测试.txt
wget -r -np -nH -nd ftp://host/test/
%B4%FA%B8%D5.txt
wget “ftp://host/test/*”
%B4%FA%B8%D5.txt

由 於不知名的原因，可能是为了避开特殊档名， wget 会自动将抓取档名的部分用 encode_string 处理过， 所以该 patch 就把被 encode_string 处理成 “%3A” 这种东西， 用 decode_string 还原成 “:”，并套用在目录与档案名称的部分，decode_string 是 wget 内建的函式。

wget -t0 -c -nH -x -np -b -m -P /home/sunny/NOD32view/ http://downloads1.kaspersky-labs.com/bases/ -o wget.log

"""





我们都知道wget这个工具是Linux、Unix下才能使用的。那么windows平台下到底可否使用？答案是确定的可以的！！！
       请从下面链接下载wget(1.11.4) for win: 。下载完成后，解压出wget.exe文件，把它放到c:\windows\sytem32目录下。
  进入命令行
  运行---cmd-----   wget 即可生效    。wget或者whet.exe --help
  Wget 的使用
"""
1）支持断点下传功能
2）同时支持FTP和HTTP下载方式
3）支持代理服务器
4）设置方便简单
5）程序小，完全免费；
命令格式：
  wget [参数列表] [目标软件、网页的网址]

  1、启动类参数

  这一类参数主要提供软件的一些基本信息；

  -V,--version 显示软件版本号然后退出；
  -h,--help显示软件帮助信息；
  -e,--execute=COMMAND 执行一个 “.wgetrc”命令

  以上每一个功能有长短两个参数，长短功能一样，都可以使用。需要注意的是，这里的-e参数是执行一个.wgettrc的命令，.wgettrc命令其实是一个参数列表，直接将软件需要的参数写在一起就可以了。

  2、文件处理参数

  这类参数定义软件log文件的输出方式等；

  -o,--output-file=FILE 将软件输出信息保存到文件；
  -a,--append-output=FILE将软件输出信息追加到文件；
  -d,--debug显示输出信息；
  -q,--quiet 不显示输出信息；
  -i,--input-file=FILE 从文件中取得URL；

  以上参数对于攻击者比较有用，我们来看看具体使用；

  例1：下载192.168.1.168首页并且显示下载信息
  wget -dhttp://192.168.1.168

  例2：下载192.168.1.168首页并且不显示任何信息
  wget -qhttp://192.168.1.168

  例3：下载filelist.txt中所包含的链接的所有文件
  wget -i filelist.txt


  wget -np -m -l5 http://jpstone.bokee.com //不下载本站所链接的其它站点内容，5级目录结构
  3、下载参数

  下载参数定义下载重复次数、保存文件名等；

  -t,--tries=NUMBER 是否下载次数（0表示无穷次）
  -O --output-document=FILE下载文件保存为别的文件名
  -nc, --no-clobber 不要覆盖已经存在的文件
  -N,--timestamping只下载比本地新的文件
  -T,--timeout=SECONDS 设置超时时间
  -Y,--proxy=on/off 关闭代理

  例：下载192.168.1.168的首页并将下载过程中的的输入信息保存到test.htm文件中
  wget -o test.htmhttp://192.168.1.168

  4、目录参数

  目录参数主要设置下载文件保存目录与原来文件（服务器文件）的目录对应关系；

  -nd --no-directories 不建立目录
  -x,--force-directories 强制建立目录
  可能现在我们对这里的目录还不是很了解，我们来看一个举例

  例：下载192.168.1.168的首页，并且保持网站结构
  wget -xhttp://192.168.1.168


  5、HTTP参数

  HTTP参数设置一些与HTTP下载有关的属性；

  --http-user=USER设置HTTP用户
  --http-passwd=PASS设置HTTP密码
  --proxy-user=USER设置代理用户
  --proxy-passwd=PASS设置代理密码

  以上参数主要设置HTTP和代理的用户、密码；

  6、递归参数设置

  在下载一个网站或者网站的一个目录的时候，我们需要知道的下载的层次，这些参数就可以设置；
  -r,--recursive 下载整个网站、目录（小心使用）
  -l,--level=NUMBER 下载层次

  例：下载整个网站
  wget -rhttp://192.168.1.168

  7、递归允许与拒绝选项参数

  下载一个网站的时候，为了尽量快，有些文件可以选择下载，比如图片和声音，在这里可以设置；

  -A,--accept=LIST 可以接受的文件类型
  -R,--reject=LIST拒绝接受的文件类型
  -D,--domains=LIST可以接受的域名
  --exclude-domains=LIST拒绝的域名
  -L,--relative 下载关联链接
  --follow-ftp 只下载FTP链接
  -H,--span-hosts 可以下载外面的主机
  -I,--include-directories=LIST允许的目录
  -X,--exclude-directories=LIST 拒绝的目录


  如何设定wget所使用的代理服务器
  wget可以使用用户设置文件".wgetrc"来读取很多设置，我们这里主要利用这个文件来是
  设置代理服务器。使用者用什么用户登录，那么什么用户主目录下的".wgetrc"文件就起
  作用。例如，"root"用户如果想使用".wgetrc"来设置代理服务器，"/root/.wgetrc"就起
  作用，下面给出一个".wgetrc"文件的内容，读者可以参照这个例子来编写自己的"wgetrc"文件：
  http-proxy = 111.111.111.111:8080
  ftp-proxy = 111.111.111.111:8080
  这两行的含义是，代理服务器IP地址为：111.111.111.111，端口号为：80。第一行指定
  HTTP协议所使用的代理服务器，第二行指定FTP协议所使用的代理服务器。



  WGet使用指南
  wget是一个从网络上自动下载文件的自由工具。它支持HTTP，HTTPS和FTP协议，可以使用HTTP代理.

  所谓的自动下载是指，wget可以在用户退出系统的之后在后台执行。这意味这你可以登录系统，启动一个wget下载任务，然后退出系统，wget将在后台执行直到任务完成，相对于其它大部分浏览器在下载大量数据时需要用户一直的参与，这省去了极大的麻烦。

  wget 可以跟踪HTML页面上的链接依次下载来创建远程服务器的本地版本，完全重建原始站点的目录结构。这又常被称作”递归下载”。在递归下载的时候，wget 遵循Robot Exclusion标准(/robots.txt). wget可以在下载的同时，将链接转换成指向本地文件，以方便离线浏览。

  wget 非常稳定,它在带宽很窄的情况下和不稳定网络中有很强的适应性.如果是由于网络的原因下载失败，wget会不断的尝试，直到整个文件下载完毕。如果是服务 器打断下载过程，它会再次联到服务器上从停止的地方继续下载。这对从那些限定了链接时间的服务器上下载大文件非常有用。

  wget的常见用法
  wget的使用格式

  Usage: wget [OPTION]... [URL]...用wget做站点镜像:
  wget -r -p -np -khttp://dsec.pku.edu.cn/~us..
  # 或者
  wget -mhttp://www.tldp.org/LDP/ab...在不稳定的网络上下载一个部分下载的文件，以及在空闲时段下载
  wget -t 0 -w 31 -chttp://dsec.pku.edu.cn/BBC.. -o down.log &
  # 或者从filelist读入要下载的文件列表
  wget -t 0 -w 31 -c -Bftp://dsec.pku.edu.cn/linu.. -i filelist.txt -o down.log &上面的代码还可以用来在网络比较空闲的时段进行下载。我的用法是:在mozilla中将不方便当时下载的URL链接拷贝到内存中然后粘贴到文件 filelist.txt中，在晚上要出去系统前执行上面代码的第二条。

  使用代理下载
  wget -Y on -p -khttps://sourceforge.net/pr...代理可以在环境变量或wgetrc文件中设定

  # 在环境变量中设定代理
  export PROXY=http://211.90.168.94:8080/
  # 在~/.wgetrc中设定代理
  http_proxy =http://proxy.yoyodyne.com:..
  ftp_proxy =http://proxy.yoyodyne.com:...各种选项分类列表
  启动
  -V, --version 显示wget的版本后退出
  -h, --help 打印语法帮助
  -b, --background 启动后转入后台执行
  -e, --execute=COMMAND 执行`.wgetrc"格式的命令，wgetrc格式参见/etc/wgetrc或~/.wgetrc记录和输入文件
  -o, --output-file=FILE 把记录写到FILE文件中
  -a, --append-output=FILE 把记录追加到FILE文件中
  -d, --debug 打印调试输出
  -q, --quiet 安静模式(没有输出)
  -v, --verbose 冗长模式(这是缺省设置)
  -nv, --non-verbose 关掉冗长模式，但不是安静模式
  -i, --input-file=FILE 下载在FILE文件中出现的URLs
  -F, --force-html 把输入文件当作HTML格式文件对待
  -B, --base=URL 将URL作为在-F -i参数指定的文件中出现的相对链接的前缀
  --sslcertfile=FILE 可选客户端证书
  --sslcertkey=KEYFILE 可选客户端证书的KEYFILE
  --egd-file=FILE 指定EGD socket的文件名下载
  --bind-address=ADDRESS 指定本地使用地址(主机名或IP，当本地有多个IP或名字时使用)
  -t, --tries=NUMBER 设定最大尝试链接次数(0 表示无限制).
  -O --output-document=FILE 把文档写到FILE文件中
  -nc, --no-clobber 不要覆盖存在的文件或使用.#前缀
  -c, --continue 接着下载没下载完的文件
  --progress=TYPE 设定进程条标记
  -N, --timestamping 不要重新下载文件除非比本地文件新
  -S, --server-response 打印服务器的回应
  --spider 不下载任何东西
  -T, --timeout=SECONDS 设定响应超时的秒数
  -w, --wait=SECONDS 两次尝试之间间隔SECONDS秒
  --waitretry=SECONDS 在重新链接之间等待1...SECONDS秒
  --random-wait 在下载之间等待0...2*WAIT秒
  -Y, --proxy=on/off 打开或关闭代理
  -Q, --quota=NUMBER 设置下载的容量限制
  --limit-rate=RATE 限定下载输率目录
  -nd --no-directories 不创建目录
  -x, --force-directories 强制创建目录
  -nH, --no-host-directories 不创建主机目录
  -P, --directory-prefix=PREFIX 将文件保存到目录 PREFIX/...
  --cut-dirs=NUMBER 忽略 NUMBER层远程目录HTTP 选项
  --http-user=USER 设定HTTP用户名为 USER.
  --http-passwd=PASS 设定http密码为 PASS.
  -C, --cache=on/off 允许/不允许服务器端的数据缓存 (一般情况下允许).
  -E, --html-extension 将所有text/html文档以.html扩展名保存
  --ignore-length 忽略 `Content-Length"头域
  --header=STRING 在headers中插入字符串 STRING
  --proxy-user=USER 设定代理的用户名为 USER
  --proxy-passwd=PASS 设定代理的密码为 PASS
  --referer=URL 在HTTP请求中包含 `Referer: URL"头
  -s, --save-headers 保存HTTP头到文件
  -U, --user-agent=AGENT 设定代理的名称为 AGENT而不是 Wget/VERSION.
  --no-http-keep-alive 关闭 HTTP活动链接 (永远链接).
  --cookies=off 不使用 cookies.
  --load-cookies=FILE 在开始会话前从文件 FILE中加载cookie
  --save-cookies=FILE 在会话结束后将 cookies保存到 FILE文件中FTP 选项
  -nr, --dont-remove-listing 不移走 `.listing"文件
  -g, --glob=on/off 打开或关闭文件名的 globbing机制
  --passive-ftp 使用被动传输模式 (缺省值).
  --active-ftp 使用主动传输模式
  --retr-symlinks 在递归的时候，将链接指向文件(而不是目录)递归下载
  -r, --recursive 递归下载－－慎用!
  -l, --level=NUMBER 最大递归深度 (inf 或 0 代表无穷).
  --delete-after 在现在完毕后局部删除文件
  -k, --convert-links 转换非相对链接为相对链接
  -K, --backup-converted 在转换文件X之前，将之备份为 X.orig
  -m, --mirror 等价于 -r -N -l inf -nr.
  -p, --page-requisites 下载显示HTML文件的所有图片递归下载中的包含和不包含(accept/reject)
  -A, --accept=LIST 分号分隔的被接受扩展名的列表
  -R, --reject=LIST 分号分隔的不被接受的扩展名的列表
  -D, --domains=LIST 分号分隔的被接受域的列表
  --exclude-domains=LIST 分号分隔的不被接受的域的列表
  --follow-ftp 跟踪HTML文档中的FTP链接
  --follow-tags=LIST 分号分隔的被跟踪的HTML标签的列表
  -G, --ignore-tags=LIST 分号分隔的被忽略的HTML标签的列表
  -H, --span-hosts 当递归时转到外部主机
  -L, --relative 仅仅跟踪相对链接
  -I, --include-directories=LIST 允许目录的列表
  -X, --exclude-directories=LIST 不被包含目录的列表
  -np, --no-parent 不要追溯到父目录


  Wget使用技巧
  wget的使用形式是：
  wget [参数列表] URL
  首先来介绍一下wget的主要参数：
  ・ -b：让wget在后台运行，记录文件写在当前目录下"wget-log"文件中；
  ・ -t [nuber of times]：尝试次数，当wget无法与服务器建立连接时，尝试连接多少次
  。比如"-t
  120"表示尝试120次。当这一项为"0"的时候，指定尝试无穷多次直到连接成功为止，这个
  设置非常有用，当对方服务器突然关机或者网络突然中断的时候，可以在恢复正常后继续
  下载没有传完的文件；
  ・ -c：断点续传，这也是个非常有用的设置，特别当下载比较大的文件的时候，如果中
  途意外中断，那么连接恢复的时候会从上次没传完的地方接着传，而不是又从头开始，使
  用这一项需要远程服务器也支持断点续传，一般来讲，基于UNIX/Linux的Web/FTP服务器
  都支持断点续传；
  ・ -T [number of seconds]：超时时间，指定多长时间远程服务器没有响应就中断连接
  ，开始下一次尝试。比如"-T
  120"表示如果120秒以后远程服务器没有发过来数据，就重新尝试连接。如果网络速度比
  较快，这个时间可以设置的短些，相反，可以设置的长一些，一般最多不超过900，通常
  也不少于60，一般设置在120左右比较合适；
  ・ -w [number of seconds]：在两次尝试之间等待多少秒，比如"-w 100"表示两次尝试
  之间等待100秒；
  ・ -Y on/off：通过／不通过代理服务器进行连接；
  ・ -Q [byetes]：限制下载文件的总大小最多不能超过多少，比如"-Q2k"表示不能超过2K
  字节，"-Q3m"表示最多不能超过3M字节，如果数字后面什么都不加，就表示是以字节为单
  位，比如"-Q200"表示最多不能超过200字节；
  ・ -nd：不下载目录结构，把从服务器所有指定目录下载的文件都堆到当前目录里；
  ・ -x：与"-nd"设置刚好相反，创建完整的目录结构，例如"wget -ndhttp://www.gnu.org"将创建在当前目录下创建"w...，然后按照服务器
  实际的目录结构一级一级建下去，直到所有的文件都传完为止；
  ・ -nH：不创建以目标主机域名为目录名的目录，将目标主机的目录结构直接下到当前目
  录下；
  ・ --http-user=username
  ・ --http-passwd=password：如果Web服务器需要指定用户名和口令，用这两项来设定；
  ・ --proxy-user=username
  ・ --proxy-passwd=password：如果代理服务器需要输入用户名和口令，使用这两个选项
  ；
  ・ -r：在本机建立服务器端目录结构；
  ・ -l [depth]：下载远程服务器目录结构的深度，例如"-l 5"下载目录深度小于或者等
  于5以内的目录结构或者文件；
  ・ -m：做站点镜像时的选项，如果你想做一个站点的镜像，使用这个选项，它将自动设
  定其他合适的选项以便于站点镜像；
  ・ -np：只下载目标站点指定目录及其子目录的内容。这也是一个非常有用的选项，我们
  假设某个人的个人主页里面有一个指向这个站点其他人个人主页的连接，而我们只想下载
  这个人的个人主页，如果不设置这个选项，甚至--有可能把整个站点给抓下来，这显然是
  我们通常不希望的；
  ü 如何设定wget所使用的代理服务器
  wget可以使用用户设置文件".wgetrc"来读取很多设置，我们这里主要利用这个文件来是
  设置代理服务器。使用者用什么用户登录，那么什么用户主目录下的".wgetrc"文件就起
  作用。例如，"root"用户如果想使用".wgetrc"来设置代理服务器，"/root/.wgert"就起
  作用，下面给出一个".wge
  trc"文件的内容，读者可以参照这个例子来编写自己的"wgetrc"文件：
  http-proxy = 111.111.111.111:8080
  ftp-proxy = 111.111.111.111:8080
  这两行的含义是，代理服务器IP地址为：111.111.111.111，端口号为：80。第一行指定
  HTTP协议所使用的代理服务器，第二行指定FTP协议所使用的代理服务器。
  wget 使用实例：
  wget是一个命令行工具，用于批量下载文件，支持HTTP和FTP。究竟比其他的工具好在哪里？看看内容吧

  wget基本上所有的Linux版本都自己带了，但是有多少人在用呢？呵呵，如果你没有用过，不妨试试。Windows下面的用户可以使用GNUwin32的项目，wget，基本功能完全一致。好吧，我们来以几个简单的例子看看wget的威力。

  如果我们想下载ftp里面某个目录里面的所有文件，我们也可以不用ftp这个笨蛋，呵呵，可以享受cute ftp等图形化工具的拖一个目录的轻松了。如


  wget -rftp://10.8.8.8/movie/

  呵呵，等吧！下完了，发觉有些不对劲，怎么出来个10.8.8.8的目录，进去看看，又是一个movie，哦，wget将目录结构和网站标题都给记录下来了，不要？？没有问题！比如说还是这个例子

  wget -r -ndftp://10.8.8.8/movie/

  结果什么目录都没有了，faint！怎么会这样？呵呵，你如果想要这样就让它这样吧，否则使用

  wget -r -nHftp://10.8.8.8/movie/

  恩？movie也不要？OK，那就这样

  wget -r -nH --cut-dirs=1ftp://10.8.8.8/movie/

  这有什么用啊？cuteftp比他好用多了，而且，你这断了线能连吗？呵呵，不好意思，可以连

  wget -c -r -nH --cut-dirs=1ftp://10.8.8.8/movie/


  但 是cuteftp能做下面的事情吗？比如，现在很多网站使用Apache建站，并不提供ftp服务，但是Apache有一个indexing功能，可以提 供一个类似于ftp的界面，好多文件我想下啊，怎么办？由于是HTTP协议，CuteFTP无能为力了，倒是flash get等有什么get all这种功能，不知道他们对于目录处理怎么样。但是wget一点问题都没有，不信？我们拿CTAN为例（例子并不恰当，CTAN有FTP服务），我们下 载这里面所有的宏包，呵呵

  wget -r -khttp://www.txia.com/blog

  -k表示将连接转换为本地连接。但是现在同样有上面的问题啊，那就把你需要的加上吧，另外也许你根本不需要向下走那么多层，比如，我们就要到第二层，那么

  wget -r -l2 -khttp://www.txia.com/blog

  现在新的问题是，由于网页有一个排序功能，很讨厌，因为下载的时候把网页重复了好多次，那么我们可使用-A和-R开关控制下载类型，并且可以使用通配符，呵呵，现在随心所欲了吧

  wget -r -R "*.htm*?*" -khttp://www.txia.com/blog

  这次没有那种网页了吧？-R的意义在于拒绝下载匹配类型的文件，-A表示仅仅接受的文件类型，如-A "*.gif"将仅下载gif图片，如果有多个允许或者不允许，可以使用,分开。

  那 么，我们现在在使用代理服务器，怎么办呢？呵呵，很高兴你选择了wget，你可以使用它的配置文件，环境变量来利用代理。这里推荐使用环境变量，如在 bash里面我们可以把天天用的proxy加到.bash_profile里面，这是Linux标准写法（很多软件都用的，什么apt-get，yum等 等）

  export http_proxy=http://10.20.30.40:8080

  然后，proxy就默认打开了，如果需要暂时关闭，可以使用

  wget --proxy=off -r -khttp://www.txia.com/blog

  当然，写一个.wgetrc文件也可以，该文件可以从/usr/local/etc里面找到，里面有很详细的注释，我就不多说了。

  下载网页的时候比较麻烦的事情是，有的网页被同时指向了很多遍，那么为了避免多次下载，我们使用

  wget -nc -r -khttp://www.txia.com/blog

  可以避免这件事情。为了不被有的连接指向非http://www.txia.com/blog内层目录，我们还应该加上

  wget -nc -np -r -khttp://www.txia.com/blog

  避免下载非该目录里面的文件，这也避免了到不同的host上面去。当然，如果你希望有这个功能，在多个host之间跳来跳去的下载，可以使用

  wget -nc -np -H -r -khttp://www.txia.com/blog

  使得可以在多个host之间span，同时-I和-X可以使得我们仅仅跟踪某些目录或者不跟踪某些目录。如果某些HTML里面你需要的东西不是由这种东西作出来的，你就得使用--follow-tags和--ignore-tags了。

  嘿，我有个文件里面都是连接，怎么办？要是不是html你只需要

  wget -i your.file

  如果是，那也不繁

  wget -F -i your.file



  wget 使用指南
  wget是一个从网络上自动下载文件的自由工具。它支持HTTP，HTTPS和FTP协议，可以使用HTTP代理.

  所谓的自动下载是指，wget可以在用户退出系统的之后在后台执行。这意味这你可以登录系统，启动一个wget下载任务，然后退出系统，wget将在后台执行直到任务完成，相对于其它大部分浏览器在下载大量数据时需要用户一直的参与，这省去了极大的麻烦。

  wget 可以跟踪HTML页面上的链接依次下载来创建远程服务器的本地版本，完全重建原始站点的目录结构。这又常被称作"递归下载"。在递归下载的时候，wget 遵循Robot Exclusion标准(/robots.txt). wget可以在下载的同时，将链接转换成指向本地文件，以方便离线浏览。

  wget 非常稳定,它在带宽很窄的情况下和不稳定网络中有很强的适应性.如果是由于网络的原因下载失败，wget会不断的尝试，直到整个文件下载完毕。如果是服务 器打断下载过程，它会再次联到服务器上从停止的地方继续下载。这对从那些限定了链接时间的服务器上下载大文件非常有用。

  wget的常见用法
  wget的使用格式

  Usage: wget [OPTION]... [URL]...

  用wget做站点镜像:
  wget -r -p -np -khttp://dsec.pku.edu.cn/~us..
  -r 表示递归下载,会下载所有的链接,不过要注意的是,不要单独使用这个参数,因为如果你要下载的网站也有别的网站的链接,wget也会把别的网站的东西下载 下来,所以要加上 -np这个参数,表示不下载别的站点的链接. -k表示将下载的网页里的链接修改为本地链接.-p获得所有显示网页所需的元素,比如图片什么的.

  # 或者
  wget -mhttp://www.tldp.org/LDP/ab..


  在不稳定的网络上下载一个部分下载的文件，以及在空闲时段下载
  wget -t 0 -w 31 -chttp://dsec.pku.edu.cn/BBC.. -o down.log &
  # 或者从filelist读入要下载的文件列表
  wget -t 0 -w 31 -c -Bftp://dsec.pku.edu.cn/linu.. -i filelist.txt -o down.log &

  上面的代码还可以用来在网络比较空闲的时段进行下载。我的用法是:在mozilla中将不方便当时下载的URL链接拷贝到内存中然后粘贴到文件filelist.txt中，在晚上要出去系统前执行上面代码的第二条。

  使用代理下载
  wget -Y on -p -khttps://sourceforge.net/pr..

  代理可以在环境变量或wgetrc文件中设定
  # 在环境变量中设定代理
  export PROXY=http://211.90.168.94:8080/
  # 在~/.wgetrc中设定代理
  http_proxy =http://proxy.yoyodyne.com:..
  ftp_proxy =http://proxy.yoyodyne.com:..

  wget各种选项分类列表
  启动
  -V, --version 显示wget的版本后退出
  -h, --help 打印语法帮助
  -b, --background 启动后转入后台执行
  -e, --execute=COMMAND 执行`.wgetrc"格式的命令，wgetrc格式参见/etc/wgetrc或~/.wgetrc

  记录和输入文件
  -o, --output-file=FILE 把记录写到FILE文件中
  -a, --append-output=FILE 把记录追加到FILE文件中
  -d, --debug 打印调试输出
  -q, --quiet 安静模式(没有输出)
  -v, --verbose 冗长模式(这是缺省设置)
  -nv, --non-verbose 关掉冗长模式，但不是安静模式
  -i, --input-file=FILE 下载在FILE文件中出现的URLs
  -F, --force-html 把输入文件当作HTML格式文件对待
  -B, --base=URL 将URL作为在-F -i参数指定的文件中出现的相对链接的前缀
  --sslcertfile=FILE 可选客户端证书
  --sslcertkey=KEYFILE 可选客户端证书的KEYFILE
  --egd-file=FILE 指定EGD socket的文件名

  下载
  --bind-address=ADDRESS 指定本地使用地址(主机名或IP，当本地有多个IP或名字时使用)
  -t, --tries=NUMBER 设定最大尝试链接次数(0 表示无限制).
  -O --output-document=FILE 把文档写到FILE文件中
  -nc, --no-clobber 不要覆盖存在的文件或使用.#前缀
  -c, --continue 接着下载没下载完的文件
  --progress=TYPE 设定进程条标记
  -N, --timestamping 不要重新下载文件除非比本地文件新
  -S, --server-response 打印服务器的回应
  --spider 不下载任何东西
  -T, --timeout=SECONDS 设定响应超时的秒数
  -w, --wait=SECONDS 两次尝试之间间隔SECONDS秒
  --waitretry=SECONDS 在重新链接之间等待1...SECONDS秒
  --random-wait 在下载之间等待0...2*WAIT秒
  -Y, --proxy=on/off 打开或关闭代理
  -Q, --quota=NUMBER 设置下载的容量限制
  --limit-rate=RATE 限定下载输率

  目录
  -nd --no-directories 不创建目录
  -x, --force-directories 强制创建目录
  -nH, --no-host-directories 不创建主机目录
  -P, --directory-prefix=PREFIX 将文件保存到目录 PREFIX/...
  --cut-dirs=NUMBER 忽略 NUMBER层远程目录

  HTTP 选项
  --http-user=USER 设定HTTP用户名为 USER.
  --http-passwd=PASS 设定http密码为 PASS.
  -C, --cache=on/off 允许/不允许服务器端的数据缓存 (一般情况下允许).
  -E, --html-extension 将所有text/html文档以.html扩展名保存
  --ignore-length 忽略 `Content-Length"头域
  --header=STRING 在headers中插入字符串 STRING
  --proxy-user=USER 设定代理的用户名为 USER
  --proxy-passwd=PASS 设定代理的密码为 PASS
  --referer=URL 在HTTP请求中包含 `Referer: URL"头
  -s, --save-headers 保存HTTP头到文件
  -U, --user-agent=AGENT 设定代理的名称为 AGENT而不是 Wget/VERSION.
  --no-http-keep-alive 关闭 HTTP活动链接 (永远链接).
  --cookies=off 不使用 cookies.
  --load-cookies=FILE 在开始会话前从文件 FILE中加载cookie
  --save-cookies=FILE 在会话结束后将 cookies保存到 FILE文件中

  FTP 选项
  -nr, --dont-remove-listing 不移走 `.listing"文件
  -g, --glob=on/off 打开或关闭文件名的 globbing机制
  --passive-ftp 使用被动传输模式 (缺省值).
  --active-ftp 使用主动传输模式
  --retr-symlinks 在递归的时候，将链接指向文件(而不是目录)

  递归下载
  -r, --recursive 递归下载－－慎用!
  -l, --level=NUMBER 最大递归深度 (inf 或 0 代表无穷).
  --delete-after 在现在完毕后局部删除文件
  -k, --convert-links 转换非相对链接为相对链接
  -K, --backup-converted 在转换文件X之前，将之备份为 X.orig
  -m, --mirror 等价于 -r -N -l inf -nr.
  -p, --page-requisites 下载显示HTML文件的所有图片

  递归下载中的包含和不包含(accept/reject)
  -A, --accept=LIST 分号分隔的被接受扩展名的列表
  -R, --reject=LIST 分号分隔的不被接受的扩展名的列表
  -D, --domains=LIST 分号分隔的被接受域的列表
  --exclude-domains=LIST 分号分隔的不被接受的域的列表
  --follow-ftp 跟踪HTML文档中的FTP链接
  --follow-tags=LIST 分号分隔的被跟踪的HTML标签的列表
  -G, --ignore-tags=LIST 分号分隔的被忽略的HTML标签的列表
  -H, --span-hosts 当递归时转到外部主机
  -L, --relative 仅仅跟踪相对链接
  -I, --include-directories=LIST 允许目录的列表
  -X, --exclude-directories=LIST 不被包含目录的列表
  -np, --no-parent 不要追溯到父目录

  问题
  在递归下载的时候，遇到目录中有中文的时候，wget创建的本地目录名会用URL编码规则处理。如"天网防火墙"会被存为"%CC%EC%CD%F8%B7%C0%BB%F0%C7%BD",这造成阅读上的极大不方便。
