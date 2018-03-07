#coding=utf-8
import os
"""
我们都知道wget这个工具是Linux、Unix下才能使用的。那么windows平台下到底可否使用？答案是确定的可以的！！！
       请从下面链接下载wget(1.11.4) for win: 。下载完成后，解压出wget.exe文件，把它放到c:\windows\sytem32目录下。
  进入命令行
  运行---cmd-----   wget 即可生效    。wget或者whet.exe --help
  Wget 的使用

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
