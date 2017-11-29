# coding=utf-8

import Socket

"""
Socket创建函数

socket.socket(socket_family, socket_type, protocol=0)创建一个socket对象。socket_family是选择地址族（所以都是AF_开头），是不同的域（domain）。域决定者通信的特征，包括地址格式。参数socket_type是确定套接字的类型，进一步确定通信特征。protocol通常是0，表示为给定的域和套接字类型选择默认协议。当对同一域和套接字类型支持多个协议时，可以使用protocol选择一个特定的协议。在AF_INET通信域中，套接字类型SOCK_STREAM的默认协议时传输控制协议（Transmission Control Protocol， TCP）。在AF_INET通信域中，套接字类型SOCK_DGRAM的默认协议是UDP.
socket_family（address family，地址族）	意义
socket.AF_UNIX	UNIX域（只能够用于单一的Unix系统进程间通信），地址由单独一个string表示
socket.AF_INET	IPv4因特网域 (服务器之间网络通信)，地址由(host, port)表示
socket.AF_INET6	IPv6因特网域，地址由(host, port, flowinfo, scopeid)表示
socket.AF_UNSPEC	未指定协议
socket_type	意义
socket.SOCK_STREAM	有序的，可靠的，双向的，面向连接的字节流（默认TCP协议）
socket.SOCK_DGRAM	固定长度的，无连接的，不可开的报文传递
socket.SOCK_RAW	IP协议的数据报接口
socket.SOCK_SEQPACKET	固定长度的，有序的，可靠的，面向连接的报文传递
protocol	意义
IPPROTO_IP	IPv4协议
IPPROTO_IPV6	IPv6协议
IPPROTO_ICMP	因特网控制报文协议（Internet Control Message Protocol）
IPPROTO_RAW	原始IP数据包协议
IPPROTO_TCP	传输控制协议
IPPROTO_UDP	用户数据报协议
对于SOCK_DGRAM（数据报）接口，两个对等进程之间同你不需要逻辑连接。只需要向对等进程所使用的套接字送出一个报文。因此SOCK_DGRAM提供了一个无连接的服务。
对于SOCK_STREAM（字节流）接口，要求在交换数据之前，在本地套接字和通信的对等进程的套接字之间建立一个逻辑连接。由于SOCK_TREAM套接字提供字节流服务，所以应用程序分辨不出报文的界限。这意味者从SOCK_STREAM套接字读取数据时，它也许不会返回所有由发送进程所写的字节数。最终可以获得发送过来的所有数据，但也需要通过若干次函数调用才能得到。
SOCK_SEQPACKET套接字和SOCK_STREAM套接字很类似，只是从套接字得到的是基于报文的服务而不是字节流的服务。这意味着从SOCK_SEQPACKET套接字接受的数据量与对方发送的一致。流控制传输协议（Stream Control Transmission Protocol， SCTP）提供了因特网上的顺序数据包服务。
SOCK_RAW套接字提供一个数据报接口，用于直接访问下面的网络层（IP层）。使用这个接口的时候，应用程序负责构造自己的协议头部。PS：需要有超级管理员权限，防止恶意应用程序绕过内建安全机制来创建报文。
其他创建socket函数

socket.socketpair([family[, type[, proto]]])创建一对已经连接的socket对象（返回(socket, socket)），family，type，proto和上述socket()一样。部分平台默认的family是AF_UNIX，否则，默认是AF_INET。例如：AF_UNIX
socket.fromfd(fd, family, type[, proto])复制文件描述符fd（文件描述符fd是一个整数且有一个文件对象的fileno()方法返回）且用此返回一个socket对象。family，type和proto和上述socket()一样。文件描述符fd应该是制定一个socket的，但函数并没有检测，如果这个文件描述符fd是无效的，随后的操作将会失败。这个方法很少会用到，但是能够用来在一个被当作标准输入输出的程序的socket中设置或获取配置（如：一个由Unix inet daemon启动的服务）。socket被假设为阻塞模式。（在Unix上有效）
其他函数

socket.getdefaulttimeout()返回下一个新的socket对象的超时时间，单位是秒（float）。如果返回是None表示新的socket对象没有超时。第一次导入socket包时，默认是None。
socket.setdefaulttimeout(timeout)设置默认超时时间给新的socket对象，单位是秒(float)。None表示新的socket对象没有超时。第一次导入socket包时，默认是None。
地址

字节序

字节序是一个处理器架构特性，用于指示像整数这样的大数据类型内部的字节如何排序。

大端(bing-endian)字节序，最大字节地址出现在最低有效字节(Least Significant Byte, LSB)上。

小端(little-endian)字节序，最低有效字节包含最小字节地址。

不管字节如何排序，最高有效字节(Most Signification Byte, MSB)总是在左边，LSB总是在右边。


大端.png

小端.png
对于TCP/IP协议栈使用大端字节序。

有下面四个函数来转换字节序：

socket.ntohl(x)：将32位正整数从网络字节序转换到主机字节序。在一些机器上的主机字节序和网络字节序是一样的，这将是一个空操作;否则，它执行一个4字节交换操作。
socket.ntohs(x)：将16位正整数从网络字节序转换到主机字节序。在一些机器上的主机字节序和网络字节序是一样的，这将是一个空操作;否则，它执行一个2字节交换操作。
socket.htonl(x)：将32位正整数从主机字节序转换到网络字节序。在一些机器上的主机字节序和网络字节序是一样的，这将是一个空操作;否则，它执行一个4字节交换操作。
socket.htons(x)：将16位正整数从主机字节序转换到网络字节序。在一些机器上的主机字节序和网络字节序是一样的，这将是一个空操作;否则，它执行一个2字节交换操作。
地址格式

socket.inet_aton(ip_string)将一个字符串的IPv4地址（e.g:“192.168.1.1”）转换为32位二进制格式的字符串（在和一些采用C标准库和需要struct in_addr的程序交流上很有用）。如果ip_string是一个无效的ip，这将引起一个socket.error。
socket.inet_ntoa(packed_ip)将一个32位二进制格式的字符串IPv4地址转换成一个常用的IPv4字符串。如果这不是一个表示4byte长度的字符串，将引起一个socket.error。
socket.inet_pton(address_family, ip_string)将一个对应family（AF_INET 或 AF_INET6）的字符串地址，转换成对应的二进制格式。（在*nix上）
socket.inet_ntop(address_family, packed_ip)将一个二进制格式的IP地址，转换成对应地址族的字符串格式。（AF_INET 或 AF_INET6）
地址查询

socket.getaddrinfo(host, port[, family[, socktype[, proto[, flags]]]])根据给定的参数host/port，相应的转换成一个包含用于创建socket对象的五元组的list。

host可以是一个域名（e.g:"www.google.com"），可以是一个IPv4或者IPv6地址的字符串，或则是None。
port可以是一个协议名（e.g:"http"），可以是一个代表端口的数字，或者是None 。
family，socketype，proto，flags都是一些可选的参数，来筛选结果的。默认情况下，它们的值都是 0，表示所有。 flags可以是 1 个或者多个AI_*常量，这会影响结果是如何计算和返回的。默认值是 0。
返回list的5元组结构：(family, socktype, proto, canonname, sockaddr),
family，socktpye，proto是一个整数。canonname是一个string，仅当AI_CANONNAME在参数flags中，否则返回 '' 。如果family是AF_INET，sockaddr是(address, port)；如果family是AF_INET6，sockaddr是(address, port, flow, info, scope id)；

flag标记	描述
AI_ADDRCONFIG	查询配置的地址类型(IPv4或IPv6)
AI_ALL	查找 IPv4 和 IPv6 地址(仅用于AI_V4MAPPED)
AI_CANONAME	需要一个规范的名字（与别名相对）
AI_NUMBERICHOST	以数字格式指定主机地址，不翻译
AI_NUMBERICSERV	将服务指定为数字端口号，不翻译
AI_PASSIVE	套接字地址用于监听绑定
AI_V4MAPPED	如果没有找到IPv6地址，返回映射到IPv6格式的IPv4地址
socket.gethostname()返回当前正在执行Python解释器的主机名的字符串。（gethostname()返回的可能不是一个完全的qualified主机名，详见getfqdn()）
socket.getfqdn([name])使用name来返回一个full qualified的主机名。如果name没有提供或者为空，则被解释为本地主机。为了找返回一个full qualified的主机名，由gethostbyaddr()返回的主机名将被选中，如果有的主机有别名的话，将会跟在后面。第一个返回的主机名是被选中的。如果没有full qualified主机名可用，将返回gethostbyaddr()的主机名。
socket.gethostbyname(hostname)将一个hostname转换为IPv4地址格式。如果hostname是一个IPv4地址，将会原封不动返回。gethostbyname()不接受IPv6。
socket.gethostbyname_ex(hostname)扩展接口。将一个hostname转换为IPv4地址格式。返回一个三元组(hostname, aliaslist, ipaddrlist)。hostname是反映着返回的ip_address。aliaslist是一组对应着同一个IP地址的主机别名（可能为空）。ipaddrlist是一组对应着同一个hostname的IPv4地址（一般情况是单一个地址）。gethostbyname_ex()只支持IPv4。
socket.gethostbyaddr(ip_address)``````hostname是反映着返回的ip_address。aliaslist是一组对应着同一个IP地址的主机别名（可能为空）。ipaddrlist是一组同一主机同一接口的IPv4/IPv6的地址列表。
socket.getnameinfo(sockaddr, flags)将给定的socketaddr(为一个host和port的二元组)翻译成一个二元组(host, port)。根据设置和flags，结果可以保存一个full qualified的主机名或者表现在主机上的数字地址。同样的，端口号可以为数字或者字符串。
flags	描述
NI_DGRAM	服务基于数据报而非基于流
NI_NAMEREQD	如果找不到主机名，将其作为一个错误对待
NI_NOFQDN	对于本地主机，仅返回全限定域名的字节点部分
NI_NUMERICHOST	返回主机地址的数字形式，而非主机名
NI_NUMERICSCOPE	对于IPv6，返回范围ID的数字形式，而非名字
NI_NUMERICSERV	返回服务地址的数字形式（即端口号），而非名字
socket.getprotobyname(protocolname)将一个网络协议名（例如“icmp”,"tcp"）转换成为一个固定的合适的值，给socket()的第三个参数（可选）。这个通常用在SOCK_RAW模式，对于其他普通的socket模型，将这个参数缺省或者设为0会自动的选择正确的协议。
socket.getservbyname(servicename[, protocolname])将一个网络服务名（e.g: "http"）和协议名转换成一个该服务的端口号。protocolname是可选项，应该是tcp或者udp，否则将匹配任何协议。
socket.getservbyport(port[, protocolname])将一个端口号和网络协议名转换成该端口号的服务名。protocolname是可选项，应该是tcp或者udp，否则将匹配任何协议。
Socket对象方法

socket.accept()接受一个连接。这个socket对象必须绑定了一个地址并正在监听着连接。返回的值是(conn, address)， conn是一个用来在接连上发送接收数据的新的socket对象，address是绑定在另外一个的socket连接的地址。
socket.bind(address)将socket绑定到一个address。这个socket必须是未绑定地址的（address的格式如上文提到的，e.g:IPv4的格式(host, port)）。
socket.close()关闭这个socket。接下来在这个socket对象的操作都将失败。另外一端将不在接收到数据（当队列中的数据都发送后）。当socket对象被垃圾回收机制回收时，将会自动关闭。
socket.connect(address)用address连接到一个远程的socket（address的格式如上文提到的，e.g:IPv4的格式(host, port)）
socket.connect_ex(address)类似于socket.connect(address)，但是返回一个错误提示来取代引起一个C语言层connect()的错误exception（其他问题，如果“host not found”，依然会引起exception）。如果返回的错误提示时0则操作成功，其他则是errno变量。这是一个有用的支持，比如，异步连接。
socket.fileno()返回一个socket对象的文件描述符（一个整数）。在做多路复用socket（select,poll,epoll）下有用。在Window下，这个方法返回的整数不能当做文件描述符来使用（比如os.fdopen()）。Unix下没有这个限制。
socket.getpeername()返回socket连接的远程address。这是有用的，例如找出远程的IPv4/v6 socket的端口号（返回的address格式依赖于地址族－如上述）。这个方法在某些平台上不支持。
socket.getsockname()返回socket绑定的address。这是有用的，例如找IPv4/v6 socket的端口号（返回的address格式依赖于地址族－如上述）。
socket.getsockopt(level, optname[, buflen])返回指定socket选项的值。optname所需要的 symbolic 常量（so_＊）都在本module中。如果buflen缺省，将会假定是一个整数的设置，并且这个函数是返回一个整数的。如果buflen设置了，它指定用于接收缓冲的最大长度。需要由调用者来对这个缓冲的内容进行解码。
socket.setsockopt(level, optname, value)设置给定socket选项的值。optname所需要的 symbolic 常量（so_＊）都在本module中。value可以是一个整数（integer）或者表示缓冲（buffer）的字符串（string）。在后一种情况（指字符串的情况），它是由调用者来保证字符串包含着正确的位（bits）。

参数level标识了选项应用的协议。如果是通用的套接字层次选项，则level设置成SOL_SOCKET，否则level设置成控制这个选项的协议编号。对于TCP选项，level是IPPROTO_TCP。对于IP，level是IPPROTO_IP等等。

选项	参数value的类型	描述
SO_ACCEPTCONN	integer	返回信息指示该套接字是否能被监听（仅getsockopt()）
SO_BROADCAST	integer	如果value非0，广播数据包
SO_DEBUG	integer	如果value非0，启动网络驱动调试功能
SO_DONTROUTE	integer	如果返回的value非0，绕过通常路由
SO_ERROR	integer	返回挂起的套接字错误并清除(仅getsockopt)
SO_KEEPALIVE	integer	如果value非0，启动周期性keep－alive报文
SO_LINGER	stirng	当还有未发送报文二套接字已关闭时，延迟时间
SO_OOBINLINE	integer	当value非0，将带外数据放在普通数据中
SO_RCVBUF	integer	接受缓冲区的字节长度
SO_RCVLOWAT	integer	接收调用中返回的最小数据字节数
SO_RCVTIMEO	string	套接字接收调用的超时值
SO_REUSEADDR	integer	如果value非0，重用bind中的地址
SO_SNDBUF	integer	发送缓冲区的字节长度
SO_SNDLOWAT	integer	发送调用中传送的最小数据字节数
SO_SNDTIMEO	string	套接字发送调用的超时值
SO_TYPE	integer	表示套接字类型（仅getsockopt）
socket.listen(backlog)监听Socket进行的连接。backlog指定连接队列的最大值，至少为0。最大值取决于系统（通常为5）。最小值被强制为0。
socket.makefile([mode[, bufsize]])返回与socket相关联的文件对象。这个文件对象只有调用close()方法才会被关闭，但这个关闭只是删除与socket的关联，所以只有在这个socket没有在其他地方被引用时，socket才会关闭。
这个socket必须在阻塞模式（不能有超时）。可选参数mode和bufsize和大开文件的方法file()，open一样。

socket.recv(bufsize[, flags])接收来自socket的数据。接收的数据以string类型表示。一次接收数据的最大数量由bufsize决定。flags的默认值为0，flags的标志如下表。

标志	描述（Linux下）
MSG_CMSG_CLOEXEC	为UNIX域套接字上接收的文件描述符设置执行时关闭标志
MSG_DONTWAIT	启动非阻塞操作（相当于使用O_NONBLOCK）
MSG_ERRQUEUE	接受错误信息作为辅助数据
MSG_OOB	如果协议支持，获取带外数据
MSG_PEEK	返回数据内容而不是真正取走数据
MSG_TRUNC	即使数据包被截断，也返回数据包的实际长度
MSG_WAITALL	等待直到所有数据可能（仅SOCK_STREAM）
socket.recvfrom(bufsize[, flags])接收来自socket的数据。返回的值时一个二元组(string, address)，string表示的是接收的数据，address则是发送数据的socket的地址。参数的详解参见```socket.recv(bufsize[, flags])````。
socket.recvfrom_into(buffer[, nbytes[, flags]])接收来自socket的数据，将接收的数据写入到buffer中，而不是返回一个string。返回值的一个二元组(nbytes, address),nbytes是接收的的字节数，address则是发送数据的socket的地址。flags参数的详解参见```socket.recv(bufsize[, flags])````。
socket.send(string[, flags])发送数据到socket。这个socket对象必须已经与一个远程的socket对象连接。可选参数flags和函数recv()中的一样。这个函数会返回发送数据的字节数。应用程序需要自己负责检查是否所有数据已经被发送，如果只有一部分数据发送了，应用程序需要尝试将剩余的数据输送出去。
socket.sendall(string[, flags])发送数据到socket。这个socket对象必须已经与一个远程的socket对象连接。可选参数flags和函数recv()中的一样。和send()不同的是，这个方法将会一直发送数据直到所有数据都发送完或者有错误出现。如果成功则返回None。如果错误，将会引起一个异常(exception)，但这样将没有办法获知有多少数据是成功被发送的。
socket.sendto(string, address)和socket.sendto(string, flags, address)发送数据到socket，这个socket必须是没有与远程的socket连接的，目标socket由address来决定。可选参数falgs与recv()相同。函数返回的结果是发送数据的字节数。（address的格式由地址族决定，看上文）
`socket.setblocking(flag)将这个socket设置为阻塞或非阻塞：如果flag设为0，那个它是非阻塞，其他则为阻塞。所有的socket默认是阻塞的。在非阻塞模式下，如果调用recv()没有接收到数据，或者send()不能立刻的发送数据，一个error一个将会引起。在阻塞模式下，这些方法将会阻塞知道它们能够处理。socket.setblocking(0)的效果和socket.setblocking(0.0)一样。socket.setblocking(1)的效果和socket.setblocking(None)一样。
socket.settimeout(value)为阻塞的socket设置一个超时时间。value可以是一个非负float表示的数字，单位是秒，也可以是None。如果给socket设定一个超时时间（float），一连串的阻塞方法的处理时间超过这个值，将会引起一个timeout异常。如果value是None，则会禁用超时。settimeout(0.0)效果和setblocking(0)一样。settimeout(None)的效果和setblocking(1)一样。
socket.gettimeout()返回设置的超时时间。返回的值和setblocking()，settimeout()相关。
socket.setsockopt(level, optname, value)用给定的参数设置socket的配置。所需的配置常量在socketmodule中（SO_*etc.）。value可以是一个整数或者一个字符串表示的buffer。如果是一个buffer，将有调用着来验证字符串是否包含正确的位（bits）。
socket.shutdown(how)完全关闭连接或者关闭一半。如果how是 SHUT_RD，将不能接收数据。如果how是SHUT_WR，将不能发送数据。如果是SHUT_RDWD，发送和接收都不允许。
 Python

"""