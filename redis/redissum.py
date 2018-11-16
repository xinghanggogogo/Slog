key:
    del key                                #删除
    keys adc*                              #查找key
    get key                                #获取value
    type key                               #用来获取键值的类型
    exist key                              #是否存在
    ttl key                                #查看剩余生存时间
    rename old_key new_key                 #重命名

string:
    set key value                          #set name 'xinghang'
    setnx key value                        #只有当键值不存在时设置key_value
    mset key1 value1 key2 value2           #批量设置:mset name 'xinghang' addr 'beijing'
    msetnx key1 value2 key1 value2         #批量同上
    get key                                #获得键值
    mget key1 key2                         #获取所有键的值
    srtlen key                             #value的长度
    getrange key num num                   #getrange name 0 -1  (输出:xinghang)

list:
    rpush key_name value1 value2           #新建一个list并且加入值
    rpop key_name                          #移除并获取列表最后一个元素
    lrange key_name 0 -1                   #输出一个list
    llen key_name                          #长度
    lset key index value                   #指定位置的设置list

hash: # 非常适合存储对象
    hset key name "xinghang"
    hsetnx key name "xinghang"
    hmset key filde1 value1 filed1 value2
    hdel key filed1
    hget key filed1
    hmget key filed1 filed2
    hgetall key                            #输出一个对象
    hkeys key                              #获取key对应的所有的哈希字段
    hvals key                              #获取key所对应的所有的哈希值
    hlen  key                              #key所对应的hash字段的个数

set:
    sadd key value
    srem key value1                        #删除
    smemembers key                         #查看一个集合
    scard key                              #长度
    sinter key1 key2                       #交集
    sunion key1 key2                       #并集

zset:
    zadd  key [score name]                 #新建一个zset并且插入值: zadd test_zset  10 xinghagn; zadd test_zset 1 lifeifei
    zrem key name                          #删除
    zcard key                              #长度
    zrange key index1 index2               #输出指定排名区间的name: zrange test_zset 0 1 (输出 lifeifei xinghang)
    zrange key index1 index2  withscores   #同上,带权值
    zscore key name                        #返回这个name的score
    zrank key name                         #返回score排名的index
    zcount key min_score max_score         #返回在权值范围内的name个数

关闭: ./redis-cli shutdown
指定配置文件启动: ./redis-server ../redis-conf
远端连接: redis-cli -h 10.9.36.222

关于spider机(ubuntu) apt-get install方式安装redis更改配置的实例:
启动client: /usr/bin/redis-cli
更改配置文件: sudo vim /etc/redis/redis.conf
指定最大内存: maxmemory 6gb
重启server: sudo /usr/bin/redis-server /etc/redis/redis.conf

关于spider机(ubuntu) 分别使用apt-get install 和 源码安装方式安装redis多实例更改配置的实例:
位置: /home/work/redis-stable
配置文件: /home/work/redis-server/redis.conf
cli和server位置: /home/work/redis-server/src/redis-cli (redis-server)
修改配置文件 指定端口, 启动: ./redis-server ../redis-conf
外网连接: redis-cli -h 10..... -p 6380

关于redis集群配置:
http://blog.csdn.net/shy_snow/article/details/50466767
redis是单线程的, 集群, 然后一个端口一个实例, 可以保证分流, 不阻塞, 这就是redis集群的意义

redis为什么是单线程的:
说白了就是一个取舍问题.
https://www.cnblogs.com/yuyutianxia/p/6346723.html
对内存的操作是同步的, 可是io是异步的, 每秒60000次.

redis为什么很快速?
总体来说快速的原因如下:
1）绝大部分请求是纯粹的内存操作(非常快速).
2）采用单线程, 避免了不必要的上下文切换和竞争条件
3）非阻塞IO, 内部实现采用epoll，采用了自己实现的简单的事件框架, epoll中的读、写、关闭、连接都转化成了事件, 然后利用epoll的多路复用特性, 绝不在io上浪费一点时间.

bitdance:
-----
1.关于key和五种数据类型及其操作:
key: get key
     del key
     ttl eky
     keys key
     exist key
string: get key
        set key
        strlen key
list: rpush key value
      rpop key
      lrange key 0 -1
      llen len
hash: hset key name value
      hget key name
      hdel key name
set: sadd key value
     srem key value
     smember key
     sinter key1 key1
     sunion key1 key2
zet: zadd key score name
     zrem key name
     zrange key index1 index2
     zrange key index1 index2 withscores
其中, srting是最常用的, list适合于数据结构中的的list(即先进先出), hash完美适合于对象, set可以求交并集, 而zset完美适合于排行榜
2.redis为什么这么快:
三点. 单线程避免上下文切换, 在内存操作(同步的), 异步io采用epoll实现多路复用
3.redis为什么采用单线程:
这是一个取舍问题, 在多线程中操作, 必然涉及到锁的问题, 这会使程序的逻辑严重复杂化
所以使用多线程可以提高性能, 但是每个线程的效率严重下降了
单线程的的单次操作非常快速(见上), 但是多线程自然是可以比单线程有更高的性能上限
但是在今天的计算环境中, 即使是单机多线程的上限也往往不能满足需要了, 需要进一步摸索的是多服务器集群化的方案, 讨论单线程和多线程的意义就不大了
4.关于redis的集群:
单例的redis业务量较大的时候, 就会发生性能的问题, 比如请求过多索引速度慢, 集群就是把所有的数据分开存放在多个redis服务器上
所以就需要将一堆的键值对'均分'存储到多个redis服务器,  即hash散列算法, 这里的hash算法很多, 经典的是一致性hash算法
http://blog.csdn.net/u014490157/article/details/52244378
5.redis做主从也是有意义的, 虽然redis是单进程的
主redis可以读写, 从redis只管读
-----
