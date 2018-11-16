'''
什么是RabbitMQ:
MQ即Message Queue(消息队列), 是一种应用程序对应用程序的通信方法.
应用程序通过读写出入队列的消息(针对应用程序的数据)来通信, 而无需专用连接来链接它们.
消息传递指的是程序之间通过在消息中发送数据进行通信, 而不是通过直接调用彼此来通信, 直接调用通常是用于诸如远程过程调用的技术.
排队指的是应用程序通过队列来通信, 队列的使用除去了接收和发送应用程序同时执行的要求, 实现异步.
'''

'''
应用场景：
1.架构. 系统集成, 分布式系统的设计. 各种子系统通过消息来对接, 这种解决方案也逐步发展成一种架构风格, 即'通过消息传递的架构'.
2.吞吐量. 当系统中的同步处理方式严重影响了吞吐量, 比如日志记录. 假如需要记录系统中所有的用户行为日志, 如果通过同步的方式记录日志势必会影响系统的响应速度, 当我们将日志消息发送到消息队列, 记录日志的子系统就会通过异步的方式去消费日志消息.
3.可用性. 系统的高可用性, 比如电商的秒杀场景. 当某一时刻应用服务器或数据库服务器收到大量请求, 将会出现系统宕机. 如果能够将请求转发到消息队列, 再由服务器去消费这些消息将会使得请求变得平稳, 提高系统的可用性。
'''

'''
RabbitMQ依赖erlang, python实现依赖于pika
'''

'''
生产者
'''
import pika
credentials = pika.PlainCredentials('admin', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.x.xxx', 5678, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange = '',
                      routing_key = 'hello',
                      body = 'Hello World!')
print("开始队列")
connection.close()

'''
消费者回调函数不需要确认, 直接清除消息的例子
'''
import pika
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.x.xxx', 5672, '/', credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print("Received %r" % body)
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

'''
消费者回调函数需要确认的例子
'''
import pika
credentials = pika.PlainCredentials('admin', 'admin')
connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.1.103',5672,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print("Received %r" % body)
    res = send_email()
    if res:
        ch.basic_ack(delivery_tag=method.delivery_tag)
    else:
        pass
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=False)

print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

'''
如何使用RabbitMQ实现一个秒杀系统?
可以用抗量银弹redis先立一个flag, 然后根据消费者控制redis的读写实现输出控制.
'''
