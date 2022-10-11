

### 应用层协议原理

#### 网络应用程序体系结构

- 客户-服务器体系结构
- P2P体系结构

#### 进程通信

在两个不同端系统上的进程，通过跨越计算机网络交换报文 (message) 而相互通信。发送进程生成并向网络中发送报文；接收进程接收这些报文并可能通过回送报文进行响应。

1. 客户和服务器进程
   在一对进程之间的通信会话场景中，发起通信（即在该会话开始时发起与其他进程的联系）的进程被标识为客户，在会话开始时等待联系的进程是服务器。

2. 进程于计算机网络之间的接口
   进程通过一个称为套接字 (socket) 的软件接口向网络发送报文和从网络接收报文。套接字是同一台主机内应用层与运输层之间的接口。 应用程序开发者可以控制套接字再应用层端的一切，但是对运输层端几乎没有控制权。

3. 进程寻址

  为了进行通信，接收进程需要有一个地址，包括 主机的地址---由IP地址标识 和 在目的主机中指定接收进程的标识符---端口号 。

#### 可供应用程序使用的运输服务

在选择运输层协议的时候我们可以从这四个方面来考虑：可靠数据传输、 吞吐量、定时和安全性。

#### 因特网提供的运输服务

1. TCP 服务

TCP 服务模型包括面向连接服务和可靠数据传输服务。

- 面向连接服务：在应用层数据报文开始流动之前，TCP 让客户和服务器相互交换运输层信息，这个阶段称为握手，之后一个 TCP 就在两个进程的套接字之间建立了。
- 可靠的数据传送服务：通信进程能够依靠 TCP 无差错、按适当顺序交付所有发送的数据。

TCP 协议还具有拥塞控制机制，当网络拥塞时，这个机制就会试图抑制每个 TCP 连接。

2. UDP 服务

一种不提供不必要服务的轻量级运输协议，仅提供最小服务。属于无连接、不可靠的数据传送服务。优点在于快。

> TCP 安全，TCP 和 UDP 都没有提供任何加密机制，这就是说，数据从发送进程到套接字到中间链路到接收进程都是以明文传输的。目前，已经研制了 TCP 的加强版本，称为安全套接字层（Secure Sockets Layer SSL），可以认为 SSL = TCP + 安全。

#### 应用层协议

应用层协议定义了运行在不同端系统上的应用程序如何相互传递报文，特别是定义了：

- 交换的报文类型，例如请求报文和响应报文
- 各种报文类型的语法，如报文中的各种字段及这些字段如何描述
- 字段的语义，即这些字段中信息的含义
- 确定一个进程何时以及如何发送报文，对报文进行响应的规则

### Web 和 HTTP

Web 使用的应用层协议是 HTTP （超文本传输协议）。

Web 页面由对象组成，一个对象只是一个文件。多数 Web 页面含有一个 HTML 基本文件以及几个引用对象。HTML 基本文件通过对象的 URL 地址引用页面中的其他对象。URL 由存放对象的服务器主机名和对象的路径名组成。

HTTP 定义了 Web 客户向 Web 服务器请求 Web 页面的方式，以及服务器向客户传送 Web 页面的方式，这是一个无状态协议。

#### 非持续连接和持续连接

非持续性连接：每个请求／响应对是经一个单独的 TCP 连接发送

持续性连接：所有的请求及其响应经相同的 TCP 连接发送

默认使用的是持续性连接，一次握手后可以持续 TCP 连接，直到一段时间没有使用后断开。

#### HTTP 报文格式

1. 请求报文

```
GET /somedir/page.html HTTP/1.1 
Host : www.someschool.edu 
Connection : close # 非持续性连接
User-agent : Mozilla/5.0 
Accept-language: fr
```

HTTP 请求报文的第一行叫作请求行 (request line) , 其后继的行叫作首部行 (header line) 。请求行有 3 个字段：方法字段、URL 字段和 HTTP 版本字段。

![image-20221010150355228](https://image.ceyewan.top/typora/image-20221010150355228.png)

用表单生成的请求报文不是必须使用 POST 方法，也可以使用 GET 方法，比如 `www.somesite.com/anirnalsearch?monkeys&bananas` 也可携带字段。

2. 响应报文

```
HTTP/1.1 200 OK 
Connectiorn : close 
Date : Tue, 18 Aug 2015 15:44:04 GMT 
Server : Apache/2.2.3 (CentOS ) 
Last-Modified : Tue, 18 Aug 2015 15:11:03 GMT 
Content-Length : 6821 
Content-Type : text/html 
( da 七a data data data data ... )
```

这个响应报文三个部分：一个初始状态行 (stalus line)，6 个首部行 ( header line) , 然后是实体体 (entity body) 。 实体体部分是报文的主要部分，即它包含了所请求的对象本身 （ 表示为 data data data data data · · ·) 。 状态行有 3 个字段 ： 协议版本字段、状态码和相应状态信息。

- 200 OK: 请求成功，信息在返回的响应报文中 。 
- 301 Moved Permanently: 请求的对象已经被永久转移了，新的 URL 定义在响应报文的 Location: 首部行中。客户软件将自动获取新的 URL。
- 400 Bad Request : 一个通用差错代码，指示该请求不能被服务器理解。
- 404 Not Found: 被请求的文档不在服务器上。
- 505 HTTP Version Not Supported : 服务器不支持请求报文使用的 HTTP 协议版本。

#### 用户与服务器的交互：cookie

cookie 允许站点对用户进行跟踪。简而言之，站点、浏览器通过 cookie 来确定用户的身份。但是，cookie 也带来了安全问题，因为对方只要拿到我的 cookie 就可以冒充我了。

#### Web 缓存

Web 浏览器和服务器之间的一个 buffer ，可以降低响应时间。

通过使用**内容分发网络** (Content Distribution Network, CDN) , Web 缓存器正在因特网中发挥着越来越重要的作用。CDN 公司在因特网上安装了许多地理上分散的缓存器，因而使大量流量实现了本地化。

#### 条件 GET 方法

Web 缓存为了保证其中存储的数据是最新的，会使用条件 GET 方法，当服务器中的数据比 Web 缓存中的要新的时候，才会响应。

### 因特网中的电子邮件

因特网电子邮件系统有 3 个主要组成部分：用户代理 (user agent) 、 邮件服务器 (mail server) 和简单邮件传输协议 ( Simple Mail Transfer Protocol, SMTP ) 。

### DNS：因特网的目录服务

因特网上的主机和人类一样，可以使用多种方式进行标识。主机的一种标识方法是用它的主机名 (hostname，如：www.ceyewan.top)，而计算机更倾向于使用 IP 地址来标识一个主机。 

#### DNS 提供的服务

因此，我们需要一个机制来确保能够通过主机名找到 IP 地址。这就是域名系统（Domain Name System，DNS）的主要任务。

DNS 是： 1. 一个由分层的 DNS 服务器 ( DNS server) 实现的分布式数据库；2. 一个使得主机能够查询分布式数据库的应用层协议。

除了进行主机名到 IP 地址的转换外， DNS 还提供了一些重要的服务：

- 主机别名
- 邮件服务器别名
- 负载分配（百度的域名不可能只对应一个 IP）

#### DNS 工作机理概述

应用程序调用 DNS 客户端，客户端向网络中发送一个 DNS 查询报文，将返回的结果交给应用程序。

DNS 服务器如果只有一个的话，会面临单点故障、通信容量、远距离的集中式数据库和维护等方面的问题，因此，DNS 采用了分布式的设计方案。

1. 分布式、层次数据库

![image-20221010163154906](https://image.ceyewan.top/typora/image-20221010163154906.png)

（从上到下分别是根、顶级域、权威 DNS 服务器）

当然，还有一类重要的 DNS 服务器称为本地 DNS 服务器，每个 ISP 都有一台本地 DNS 服务器，ISP 中的主机含有本地 DNS 服务器的地址，从这个 DNS 服务器开始查找。最多上溯的根 DNS 服务器，然后向下查找到最底层 DNS 服务器。

可以认为这是一个递归查询和迭代查询的方式，从请求主机到本地 DNS 服务器的查询是递归的、其余的查询是迭代的。

2. DNS 缓存

因为链路中都经过了一遍，因此我们可以使用缓存，降低第二次查询需要的时间。因为缓存，除了少数 DNS 查询以外，根服务器可以被绕过。

#### DNS 记录与报文

在共同实现 DNS 分布式数据库的所有 DNS 服务器存储了资源记录(Resource Record ,RR), RR 提供了主机名到 IP 地址的映射。资源记录是一个如下的四元组，`(name, value, type, TTL)` 。

- tpye = A 表示 name 是一个主机，value 是该主机对应的 IP 地址。
- type = NS 表示 name 是一个域，而 Value 是个知道如何获得该域中主机 IP 地址的权威 DNS 服务器的主机名。 
- type = CNAME 则 value 是别名为 name 的主机对应的规范主机名。
- 如果 type = MX，value 是个别名为 name 的邮件服务器的规范主机名。

1. DNS 报文

DNS 的查询和回答报文格式相同，内容暂略。

使用 nslookup 程序可以向某些 DNS 服务器发送一个 DNS 查询报文。

![image-20221010165123233](https://image.ceyewan.top/typora/image-20221010165123233.png)

2. 在 DNS 数据库中插入记录

在拥有了一个域名和一个服务器之后，只需要去登记一下就行了，很多公司都提供这种服务，比如阿里云。

> DNS 的脆弱性：
>
> 第一种针对 DNS 服务的攻击是分布式拒绝服务 (DDoS) 带宽洪泛攻击，某攻击者试图向每个 DNS 根服务器发送大量的分组，使得大多数合法 DNS 请求得不到回答。
>
> 对 DNS 的潜在更为有效的 DDoS 攻击将是向顶级域名服务器（例如向所有处理 .com 域的顶级域名服务器）发送大量的 DNS 请求。过滤指向 DNS 服务器的 DNS 请求将更为困难，并且顶级域名服务器不像根服务器那样容易绕过。

### P2P文件分发

略

### 视频流和内容分发网

略

### 套接字编程：生成网络应用

#### UDP套接字编程

1. server

```python
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)
# 第一个参数指定使用 IPv4，第二个参数表示 UDP 套接字
serverSocket.bind(('', serverPort))
# 将端口号和套接字绑定在一起，也就是这个端口由这个服务使用了
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
```

2. client

```python
from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
```

这个小程序可以实现客户端给服务端发送一个字符串，服务端将其大写后响应客户端。

#### TCP 套接字编程

1. TCPserver.py

```python
from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# 等待并聆听某个客户敲门，最大接收请求的数量为 1
print("The server is ready to receive")

while True:
    connectionSocket, addr = serverSocket.accept()
    # 创建新的套接字 connectionSocket 供 accept 的客户使用
    message = connectionSocket.recv(2048)
    modifiedMessage = message.decode().upper()
    connectionSocket.send(modifiedMessage.encode())
    connectionSocket.close()
```

这里使用的函数为 recv 和 send 而不是上面 recvfrom 和 seadto，建立了 TCP 连接之后就不需要再指定通信对象了。

2. TCPclient.py

```python
from socket import *

serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# 建立 TCP 连接
message = 'ceyewan'
clientSocket.send(message.encode())
modifiedMessage = clientSocket.recv(2048)
print(modifiedMessage.decode())
clientSocket.close()
```

这里我写了一个小脚本来多次执行命令：

```python
# loop.py
import os


i = 0
while i < 20:
    os.system("python TCPclient.py")
    i += 1
```

### 套接字编程作业

#### WebServer

![image-20221011173400340](https://image.ceyewan.top/typora/image-20221011173400340.png)

```python
from socket import *
import sys

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 1234))
serverSocket.listen(1)

while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048).decode()
        print(message)  # 可以查看 message 信息
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.readlines()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n".encode())
        connectionSocket.send("\r\n".encode())
        connectionSocket.close()

serverSocket.close()
sys.exit()
```

这里我们可以只需要处理两种情况，如果文件存在就响应，如果文件不存在就 404 。在 socket 中传输的都是字节，所以我们需要使用 encode 和 decode 来转换。最后结果如下，如果存在就响应，如果不存在状态代码为 404 。

![image-20221011095431725](https://image.ceyewan.top/typora/image-20221011095431725.png)

![image-20221011095942666](https://image.ceyewan.top/typora/image-20221011095942666.png)

#### UDPPinger

![image-20221011180006183](https://image.ceyewan.top/typora/image-20221011180006183.png)

第一题的代码主要是编写服务端程序，这一题主要是编写客户端程序。循环计时即可。

```python
from socket import *
import time

serverAddr = ("localhost", 12000)
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(10):
    message = "ceyewan"
    start = time.time() # 计时
    clientSocket.sendto(message.encode(), serverAddr)
    try:
        response, _ = clientSocket.recvfrom(1024)
    except timeout:
        print("Request timeout!")
        continue
    end = time.time()
    print(f"RTT {i}: {(end - start)*1000} ms")

```

![image-20221011101843166](https://image.ceyewan.top/typora/image-20221011101843166.png)

#### SMTP

![image-20221011180301124](https://image.ceyewan.top/typora/image-20221011180301124.png)

暂略

#### ProxyServer

![image-20221011180150732](https://image.ceyewan.top/typora/image-20221011180150732.png)

一个简单的代理服务器，客户端不直接从服务端请求，而是请求代理服务器，如果代理服务器中有数据，那么就响应，如果没有，代理服务器再去请求服务器，得到响应后本地保存一份，然后将得到的响应再 response 给客户端。

![image-20221011174339287](https://image.ceyewan.top/typora/image-20221011174339287.png)

也就是说，代理服务器既是服务端也是客户端，首先选择一本本地的端口，作为服务端监听这个端口，任何客户端对这个端口的请求都由其负责响应。同时，代理服务器还得作为一个客户端，向服务端发起请求，得到响应。

代码如下：

```python
from socket import *
import sys
import os

# 两个参数，第二个参数是监听的本地的端口
if len(sys.argv) <= 1:
    print(
        'Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
    sys.exit(2)
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerPort = int(sys.argv[1])
tcpSerSock.bind(("", tcpSerPort))
print(tcpSerPort)
tcpSerSock.listen(10)

while True:
    # Strat receiving data from the client
    print('Ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024)
    message = message.decode()
    print("message:", message)
    if (message == ''):
        continue
    # Extract the filename from the given message
    print("message.split()[1]:", message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print("filename:", filename)
    fileExist = "false"
    filetouse = "/" + filename
    print("filetouse:", filetouse)
    # 尝试在本地查找，如果没找到，就去访问服务器
    try:
        # Check wether the file exist in the cache
        f = open("WEB/" + filetouse[1:], "rb")
        outputdata = f.read()
        f.close()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message
        tcpCliSock.send("HTTP/1.1 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
        tcpCliSock.send(outputdata)
        print('Read from cache')
    # Error handling for file not found in cache
    except IOError:
        # 没找到，那么就创建套接字去服务器端查找
        if fileExist == "false":
            # Create a socket on the proxyserver
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.", "", 1)
            print("hostn:", hostn)
            try:
                # Connect to the socket to port 80
                serverName = hostn.partition("/")[0]
                serverPort = 1234
                print((serverName, serverPort))
                c.connect((serverName, serverPort))
                askFile = ''.join(filename.partition('/')[1:])
                print("askFile:", askFile)
                # Create a temporary file on this socket and ask port 80
                # for the file requested by the client
                fileobj = c.makefile('rwb', 0)
                fileobj.write("GET ".encode() + askFile.encode() +
                              " HTTP/1.1\r\nHost: ".encode() + serverName.encode() + "\r\n\r\n".encode())
                # Read the response into buffer
                serverResponse = fileobj.read()
                # Create a new file in the cache for the requested file.
                # Also send the response in the buffer to client socket and the corresponding file in the cache
                filename = "WEB/" + filename
                filesplit = filename.split('/')
                for i in range(0, len(filesplit) - 1):
                    if not os.path.exists("/".join(filesplit[0:i+1])):
                        os.makedirs("/".join(filesplit[0:i+1]))
                tmpFile = open(filename, "wb")
                print(serverResponse.decode())
                serverResponse = serverResponse.split(b'\r\n\r\n')[1] # 去除首部信息，避免写入文件
                # print(serverResponse)
                tmpFile.write(serverResponse)
                tmpFile.close()
                tcpCliSock.send("HTTP/1.1 200 OK\r\n".encode())
                tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
                tcpCliSock.send(serverResponse)
            except:
                print("Illegal request")
            c.close()
        else:
            # HTTP response message for file not found
            print("NET ERROR")
    # Close the client and the server sockets
    tcpCliSock.close()
tcpSerSock.close()
```

这个代码我调了好久，一直不能正确运行。我估计是因为现在大多是网站都是用的 HTTPS 协议，就算制定了端口为 443 ，需要的首部之类的也会有区别，从而得不到正确的结果。因此，这里我使用的 WebServer 创建的本地服务器作为服务器，然后浏览器作为客户端，ProxyServer 作为代理服务器。

![image-20221011170447490](https://image.ceyewan.top/typora/image-20221011170447490.png)