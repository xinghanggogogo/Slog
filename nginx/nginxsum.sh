安装：
sudo apt-get install nginx
开启：
sudo service nginx start   (sudo /etc/init.d/nginx start)
sudo service nginx restart
sudo service nginx stop
检查：
访问http://localhost,出现欢迎页
默认配置文件
/etc/nginx/nginx.conf
这个配置文件的末尾行：
include /etc/nginx/sites-enabled/*;
这一行加载了一个外部的配置文件，sites-enabled文件夹下只有一个default文件，这个外部的配置文件就是默认的nginx的配置文件
文件内容：
server {
    server_name localhost;               #这里是你的域名，即服务器名称，即访问者的所填写url中的host（主机名），两者对应
    listen 80 default_server;
    listen [::]:80 default_server ipv6only=on;
    location / {
        proxy_pass http://127.0.0.1:8000 #实现反向代理这里的意思是从80->8000，这个端口运行着工程  8000是非常关键的，涉及到微信的认证
    }
}
文件的另外一个末尾行：
include /etc/nginx/confid.d/*.conf
到这个目录下添加文件：test.conf
写入内容：
server {
    listen 8088;                         #修改端口号
    server_name  localhost;

    location / {
        root /usr/share/nginx/html;      #当访问http://localhost:8088时，定位到此根目录，然后按找顺序查找文件, 如果没有找到, 就去index中顺序查找
        index index.html index.htm;
    }
}
访问：http://localhost:8088 出现nginx的欢迎页

至此，nignx的初始配置基本完成了,几个可能会用到的命令
sudo vim
sudo nginx -t 查看启动日志，如果启动或重启失败，可以由此查找错误信息

另：nginx的负载均衡
upstream backend {
    ip_hash;
    server backend1.example.com;
    server backend2.example.com;
    server backend3.example.com;
    server backend4.example.com;
}
location / {
    proxy_pass http://backend;
}

nginx热加载:
检查配置文件语法: nginx -t
热加载: nginx -s reload

关于location的匹配规则:
location [ = | ~ | ~* | ^~ ] uri { ... }
location @name { ... }
1. =指令用于精确字符匹配
location = /demo {
    rewrite ^ http://google.com;
}
2. ^~指令用于字符前缀匹配
location ^~ /demo {
    rewrite ^ http://google.com;
}
3. ~指令用于正则匹配, 使用~*则不区分大小写
location ~ /[0-9]emo {
    rewrite ^ http://google.com;
}
4. 指令为空用于正常匹配
location /demo {
    rewrite ^ http://google.com;
}
以下规则都能匹配:
http://192.168.33.10/demo
http://192.168.33.10/demo/
http://192.168.33.10/demo/aaa
http://192.168.33.10/demo/aaa/bbb
http://192.168.33.10/demo/AAA
http://192.168.33.10/demoaaa
http://192.168.33.10/demo.aaa
5. 全匹配
location / {
    rewrite ^ http://google.com;
}
6. @命名匹配, 绑定一个模式，类似变量替换的用法
error_page 404 = @not_found
location @not_found {
      rewrite http://google.com;
}

关于rewrite规则:
location /gzh_custom/gzh {
    rewrite ^/(.*)$ http://erp.stage.ktvsky.com/$1 permanent;
}

关于nginx的静态文件的处理(动静分离):
location ~* \.(swf|js|css|png|txt|gif|jpg|jpeg|bng|bmp|ico)$ {
    if ($http_referer ~* $host$uri$is_args$args) {
        return 404;
    }
    root html/myktv_static/wow;
    expires 30d;
    access_log off;
    add_header Cache-Control 'public';
}

location关键字 try_files
找指定路径下文件，如果不存在，则转给哪个文件执行
语法: try_files file1 [file2 ... filen] fallback
eg: 这里配合了命名匹配和负载均衡
upstream xiaomi {
    server 127.0.0.1:8001 max_fails=2 fail_timeout=30s weight=4;
    server 127.0.0.1:8002 max_fails=2 fail_timeout=30s weight=4;
    server 127.0.0.1:8003 max_fails=2 fail_timeout=30s weight=4;
    server 127.0.0.1:8004 max_fails=2 fail_timeout=30s weight=4;
    keepalive 8;
}
server {
    listen 80;
    server_name localhost;
    location / {
        try_files $uri $uri/index.html $uri.html @xiaomi;
    }
    location @xiaomi {
        proxy_read_timeout 300;
        proxy_connect_timeout 300;
        proxy_redirect off;
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Frame-Options SAMEORIGIN;
        proxy_pass http://xiaomi;
    }

------工作实例
//一次工作实例
//显示出/data/songs/目录下的所有文件
cd /etc/nginx/sites-enabled/
sudo vim songs
server {
    listen 80 default_server;
    server_name localhost;

    location / {
        root /data/songs;
        autoindex on;
        autoindex_exact_size off;
        autoindex_localtime on;
        charset utf-8,gbk;
    }
}
//一个关于tornado部署的nginx实例:
user nginx;                         # 指定nginx运行的用户及用户组,默认为nobody
worker_processes 1;                 # 开启的线程数，一般跟逻辑CPU核数一致
error_log /var/log/nginx/error.log; # 定位全局错误日志文件
pid /var/run/nginx.pid;             # 制定进程id文件存储位置

events {
    use epoll;                      # 设置工作模式为epoll, 除此之外还有select, poll,
    worker_connections 1024;        # 每个进程的最大连接数目, 受系统进程的最大打开文件数量限制
}

http {                              # Nginx的Http服务器配置,Gzip配置
    upstream frontends {
        server 127.0.0.1:8000;
        server 127.0.0.1:8001;
        server 127.0.0.1:8002;
        server 127.0.0.1:8003;
    }

    include /etc/nginx/mime.types;         # 主模块指令, 包含一些关键的配置指令
    default_type application/octet-stream; # 核心模块指令，智力默认设置为二进制流，也就是当文件类型未定义时使用这种方式
    access_log /var/log/nginx/access.log;  # 制定引用日志路径, 模式为main

    keepalive_timeout 65;                  # 设置客户端连接保存活动的超时时间
    proxy_read_timeout 200;                # 代理服务器处理请求的时间
    sendfile on;                           # 开启高效文件传输模式
    tcp_nopush on;                         # 开启防止网络阻塞
    tcp_nodelay on;                        # 开启防止网络阻塞

    gzip on;                               # 开启gzip压缩
    gzip_min_length 1000;                  # 设置允许压缩的页面最小字节数B
    gzip_proxied any;                      # Nginx作为反向代理的时候启用, any - 无条件启用压缩
    gzip_types text/plain text/html text/css text/xml
               application/x-javascript application/xml
               application/atom+xml text/javascript;

    proxy_next_upstream error;             # 和后端服务器通信出现错误, 失败的请求应该被发送到下一台后端服务器

    server {
        listen 80;
        client_max_body_size 50M;          # 客户端请求报文body的最大长度
        charset utf-8,gbk;                 # 编码方式
        location ^~ /static/ {
            root /var/www;
            if ($query_string) {           # 当存在请求参数的时候, 缓存时间设置到最大
                expires max;
            }
        }
        location = /favicon.ico {
            rewrite (.*) /static/favicon.ico;
        }
        location = /robots.txt {
            rewrite (.*) /static/robots.txt;
        }
        location / {
            proxy_pass http://frontends;              # 重定向
            proxy_set_header Host $http_host;         # 发送给upstream服务器请求的报文hearder设置
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_pass_header Server;                 # It's telling the nginx service to pass the upstream's Server header instead of putting its own in the response.
            proxy_redirect false;                     # 这条命令的含义是不显示upsteam服务器返回报文的location字段???(具体请参考:http://blog.csdn.net/u010391029/article/details/50395680)
        }
    }
}

nginx + https的配置
(阿里云https免费证书, 申请下载配置参考阿里云文档)
server {
    listen 80 default_server;
    server_name flowerhears.com;

    location / {
        root /home/xinghang/;
        autoindex on;
        autoindex_exact_size off;
        autoindex_localtime on;
        charset utf-8,gbk;
    }
}

server {

    listen 443;
    server_name flowerhears.com;
    ssl on;

    ssl_certificate   /etc/nginx/cert/214290500790053.pem;
    ssl_certificate_key /etc/nginx/cert/214290500790053.key;
    ssl_session_timeout 5m;
    ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:ECDHE:ECDH:AES:HIGH:!NULL:!aNULL:!MD5:!ADH:!RC4;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;

    location  / {
        proxy_set_header   Host $host;
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://127.0.0.1:10000;
    }
}

nginx监听80端口, 80下绑定多域名:
listen后边去掉default_server.
server {
    listen 80;
    server_name www.aaa.com;
    location / {
        proxy_pass 127.0.0.1:8989;
    }
}
server {
    listen 80;
    server_name www.bbb.com;
    location / {
        proxy_pass 127.0.0.1:8990; }
}

http转https的跳转:
http://www.cnblogs.com/yun007/p/3739182.html
1.rewrite
2.返回index.html, 然后实现跳转.
<html>
    <meta http-equiv="refresh" content="0;url=https://test.com/">
</html>

https原理:
1.前提是服务器像认证机构申请证书, 认证机构向其颁发证书.
2.证书的内容具体包含(1)拥有者的基本信息, 证书绑定的域名的基本信息, (2)服务器的公钥, (3)认证机构的数字签名, (4)数字签名的具体生成方法(所用hash算法的类型等等).
3.证书中的数字签名具体的生成方式是: 证书内容->hash算法(比如md5, sha)->得到哈希值->服务器的私钥对哈希值加密->的到数字签名, 因为其他人不可能拿到认证机构的私钥, 所以这个证书必然不能被伪造.
4.客户端进行https请求的时候, 先告诉服务器(8)步所用共享秘钥加密的HASH类型, 然后服务端首先向客户端发送证书, 客户端会验证证书.
5.验证证书的过程如下, 客户端用事先已经嵌入客户端内部(所以不会丢失)的认证机构的公钥对数字签名进行解密, 得到哈希值, 然后对证书内容做hash算法, 同这个hash值比较, 如果一致, 则证书验证成功
6.验证成功之后, 客户端会生成一个随机值, 用证书带来的服务器公钥对其进行加密, 发送给服务器.
7.服务器拿自己的私钥对其进行解密, 得到这个随机值.
8.客户端服务器开始用这个随机值进行共享秘钥加密, 文件内容, 用上文约定的Hash加密验证完整性.
以上验证过程, 其实就是ssl和tls协议的大致内容(两种加密方式公用, 公开密钥加密, 共享秘钥加密), 协议栈无非是http->ssl/tls-tcp-ip.
身份验证, 信息加密, 信息完整性的检验

指向静态文件
server {
        listen  80;
        server_name  www.kuailezhua.com;
        location / {
            root /home/work/xinghang/crane_machine;
            index MP_verify_NWZchCaulHbYWCHN.txt;
            autoindex on;
            autoindex_exact_size off;
            autoindex_localtime on;
            charset utf-8,gbk;
        }
}
