'''
什么是epoll(或者kqueue-key queue 一个是liunx的内核, 一个是mac的模型):
epoll是一个io模型, 说白了就是select的改进版本, 从很笨的轮训方式升级成多路复用, 实现单线程或者进程下的多路io的并发.
它自己维护了一套事件模型, 读, 写, 连接, 关闭, 都有自己的事件符号, 根据这种符号来区别处理, 实现io效率的最大化.

1.首先我们来定义流(stream)的概念:
一个流可以是文件, socket, pipe等可以进行I/O操作的内核对象. 不管是文件, 还是套接字(socket), 还是管道(pipe), 我们都可以把他们看作流。

2.先搞明白什么是阻塞IO:
进程A为管道的写入方, B为管道的读出方, 假设一开始AB之间的缓冲区是空的, B作为读出方, 被阻塞着.
然后首先A往管道写入, 这时候内核缓冲区由空的状态变到非空状态, 内核就会产生一个事件告诉B该醒来了, 这个事件姑且称之为'缓冲区非空'.
但是'缓冲区非空'事件通知B后, B却还没有读出数据, 且内核许诺了不能把写入管道中的数据丢掉这个时候, Ａ写入的数据会滞留在内核缓冲区中.
如果内核也缓冲区满了, B仍未开始读数据, 最终内核缓冲区会被填满, 这个时候会产生一个I/O事件, 告诉进程A, 你该等等(阻塞)了, 我们把这个事件定义为'缓冲区满'.
假设后来Ｂ终于开始读数据了, 于是内核的缓冲区空了出来, 这时候内核会告诉A, 内核缓冲区有空位了可以继续写数据了, 我们把这个事件叫做'缓冲区非满'.
也许事件Y1已经通知了A, 但是A也没有数据写入了, 而Ｂ继续读出数据, 知道内核缓冲区空了, 这个时候内核就告诉B, 你需要阻塞了, 我们把这个时间定为'缓冲区空'.
阻塞I/O模式下, 一个线程只能处理一个流的I/O事件(重要).

3.如果想要阻塞模式下同时处理多个流也就是多个IO, 要么多进程要么多线程(pthread_create), 很不幸这两种方法效率都不高. 于是再来考虑非阻塞忙轮询的I/O方式, 单进程或线程轮询流队列来处理多个流, 伪代码如下:
while true {
    for i in stream[]; {
        if i has data
        read until unavailable
    }
}
我们只要不停的把所有在流队列中的流从头到尾问一遍, 又从头开始. 这样就单线程或者单进程可以处理多个流了, 但这样的做法显然不好, 因为如果所有的流都没有数据, 那么只会白白浪费CPU

4.为了避免CPU空转, 我们引进一个代理, 一开始有一位叫做select的代理.
这个代理比较厉害, 可以同时观察许多流的I/O事件, 在空闲的时候, 会把当前线程阻塞掉, 当有一个或多个流有I/O事件时, 就从阻塞态中醒来, 于是我们的程序就会轮询一遍所有的流, 伪代码如下:
while true {
    select(streams[])
    for i in streams[] {
        if i has data
        read until unavailable
    }
}
如果没有I/O事件产生, 我们的程序就会阻塞在select处. 但是依然有个问题, 我们从select那里仅仅知道了, 有I/O事件发生了, 但却并不知道是那几个流(可能有一个, 多个, 甚至全部), 我们只能无差别轮询所有流, 找出能读出数据，或者写入数据的流, 对他们进行操作

5.由此我们引进了下一个代理, epoll, epoll可以理解为event poll, 不同于忙轮询和无差别轮询, epoll只会把哪个流发生了怎样的I/O事件通知我们, 此时我们对这些流的操作都是有意义的(复杂度降低到了O(1)), 伪代码如下:
while true {
    active_stream[] = epoll_wait(epollfd)
    for i in active_stream[] {
        read or write till unavailable
    }
}
从以上可知, epoll是对select模型的改进, 提高了网络编程的性能, 广泛应用于大规模并发请求的C/S架构中
'''
#一个简单的epoll模型
#服务端:
import socket
import select
import Queue
#定义socket对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#设置IP地址复用
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#ip地址和端口号
server_address = ("127.0.0.1", 8888)
#绑定IP地址
serversocket.bind(server_address)
#监听，并设置最大连接数
serversocket.listen(10)
print  "服务器启动成功，监听IP：" , server_address
#服务端设置非阻塞
serversocket.setblocking(False)
#超时时间
timeout = 10
#创建epoll事件对象, 后续要监控的事件添加到其中
epoll = select.epoll()
#注册服务器监听fd到等待读事件集合
epoll.register(serversocket.fileno(), select.EPOLLIN)
#保存连接客户端消息的字典, 格式为{}
message_queues = {}
#文件句柄到所对应对象的字典, 格式为{句柄: 对象}
fd_to_socket = {serversocket.fileno(): serversocket}

while True:
  print "等待活动连接......"
  #轮询注册的事件集合, 返回值为[(文件句柄, 对应的事件), (...), ...]
  events = epoll.poll(timeout)
  if not events:
     print "epoll超时无活动连接，重新轮询..."
     continue
  print "有" , len(events), "个新事件, 开始处理..."

  for fd, event in events:
     socket = fd_to_socket[fd]
     #如果活动socket为当前服务器socket, 表示有新连接
     if socket == serversocket:
            connection, address = serversocket.accept()
            print "新连接：" , address
            #新连接socket设置为非阻塞
            connection.setblocking(False)
            #注册新连接fd到待读事件集合
            epoll.register(connection.fileno(), select.EPOLLIN)
            #把新连接的文件句柄以及对象保存到字典
            fd_to_socket[connection.fileno()] = connection
            #以新连接的对象为键值，值存储在队列中，保存每个连接的信息
            message_queues[connection]  = Queue.Queue()
     #关闭事件
     elif event & select.EPOLLHUP:
        print 'client close.'
        epoll.unregister(fd)
        fd_to_socket[fd].close()
        del fd_to_socket[fd]
     #可读事件
     elif event & select.EPOLLIN:
        data = socket.recv(1024)
        if data:
           print "收到数据: " , data , "客户端: " , socket.getpeername()
           message_queues[socket].put(data)
           epoll.modify(fd, select.EPOLLOUT)
     #可写事件
     elif event & select.EPOLLOUT:
        try:
           msg = message_queues[socket].get_nowait()
        except Queue.Empty:
           print socket.getpeername() , " queue empty"
           epoll.modify(fd, select.EPOLLIN)
        else :
           print "发送数据：" , data , "客户端：" , socket.getpeername()
           socket.send(msg)

epoll.unregister(serversocket.fileno())
epoll.close()
serversocket.close()

#客户端:
import socket
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8888)
clientsocket.connect(server_address)
while True:
    data = raw_input('please input:')
    clientsocket.sendall(data)
    server_data = clientsocket.recv(1024)
    print '客户端收到的数据:'server_data
    clientsocket.close()
