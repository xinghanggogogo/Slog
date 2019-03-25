#stage环境下nginx位置：
/usr/local/nginx/conf/nginx.conf 查到服务端口号
tail -f nohup.out

#查询进程号
lsof -i:端口号
ps aux | grep pyspider

#杀进程
kill -s 9 PID
#重启
nohup python init.py --port=9503 &

#线上环境日志:
tail -f /data/torn_log/*coupon*  |grep "/namegame" -C 10
tail -f /data/torn_log/ktvsky.thunder.7100.log*

#查找文件或者路径的指令：
find . -name 'pyspider'
locate nginx .

#一个标准的post curl
curl -X POST -d 'directory=game&page=2&page_size=1' '101.254.157.124:8088/directory/get'
wrong(不能传输中文.): curl -X POST -d 'tp=5&sp_id=6&store_id=5000001&mac_id=00E07E0054E7&pay_coin=6&pay_fee=50.5&info=kbar会员包时套餐.xinghang' '101.254.157.124:8888/v2/bar/order/consume'

curl '101.254.157.124:8088/directory/get?page=1&page_size=10&directroy=game'

#默认的配置加载文件
.bashrc 每次shell执行命令时都会执行一次
.bash_profile 只有在shell登陆（启动）时才会执行一次

#python 开启一个服务器
python -m http.server <port_num>

#一个制定端口号的scp命令:
#通常意义上,P表示的是端口号,而p代表的是密码.
scp -P 3026 xinghang@101.254.157.124:/home/xinghang/work/myktv_cms/wx_order.xlsx wx_order.xlsx
#scp文件夹
scp -r work@106.75.97.4:/home/work/dejavu .
#服务器跳板:
ssh work@106.75.34.22 -p 22

#查看所有相关进程, 并杀死.
ps -ef | grep pyspider | awk '{print $2}' | xargs kill -9
ps -ef | grep phantonmjs | awk '{print $2}' | xargs kill -9
lsof -i:8080 |awk 'NR!=1{print $2}' |xargs kill -9

#mac
1、将光标移动到行首：ctrl + a
2、将光标移动到行尾：ctrl + e
3、清除屏幕：ctrl + l
4、搜索以前使用命令：ctrl + r
5、清除当前行：ctrl + u
6、清除至当前行尾：ctrl + k
7、单词为单位移动：option + 方向键

压缩解压缩scp导入数据库:
压缩: tar -zcvf a.tar.gz songs
scp: scp -P 3026 stage@101.254.157.124:/data/a.tar.gz
解压缩: tar -zxvf a.tar.gz

以G为单位的ls
ls -alh

ubutn全局环境变量位置:
sudo vim /etc/enviorment
apt-get 安装java:
https://tecadmin.net/install-oracle-java-8-ubuntu-via-ppa/#

关于echo:
写入文件内容:
echo 'something you like' >> ~/.bash_profile
几个文件查看命令:
当前目录下单个文件大小,目录只显示目录本身大小: ls -alh
当前主机磁盘状态: df -h
显示当前文件夹下单位大小,包含目录大小: du -sh *

ubuntu添加环境变量:
1.ubuntu系统级的环境变量都在/etc/enviorment中,直接在PATH后添加路径即可
2.在.bashrc或者.bash_profile中添加环境变量: export PATH="/home/work/elasticsearch-5.2.2/bin":$PATH
3.直接在终端输入: export PATH="/home/work/elasticsearch-5.2.2/bin":$PATH, 缺点是终端一旦关闭会失效!

关于ffmpeg取在线音乐的时长:
ffprobe -v quiet -print_format json -show_streams http://data.5sing.kgimg.com/G030/M01/05/01/voYBAFXu8KKIa89FAAtg5wen4k8AABb6ABvYVgAC2D_146.m4a | jq  .streams[0].duration

last -n 5
该命令用来列出目前与过去登录系统的用户相关信息。

关于awk的简单用法:
awk是一个强大的文本分析工具, 简单来说awk就是把文件逐行的读入, 以空格为默认分隔符将每行切片, 切开的部分再进行各种分析处理.
eg.1
last -n 5 | awk '{print $1}'
eg.2 处理文本
cat /etc/passwd
cat /etc/passwd | awk  -F ':'  '{print $1}'
cat /etc/passwd | awk  -F ':'  '{print $1"\t"$7}'
cat /etc/passwd | awk  -F ':'  'BEGIN {print "name, shell"}  {print $1", "$7} END {print "blue, /bin/nosh"}'
eg.3 搜索文本,定位到行
awk -F: '/root/' /etc/passwd
eg.4 搜索/etc/passwd有root关键字的所有行，并显示对应的shell
awk -F: '/root/{print $7}' /etc/passwd

alias 命名某指令为别名
alias ls="ls -l"

关于tail命令和cat命令
tail nohup.out         # 默认10行
tail -n 200 nohup.out  # 设定参数, 200行
tail -f nohup.out      # follow 追踪
cat file1              # 显示整个文件的内容
cat > file2            # 建立一个文件
cat file1 file2 > file # 合并文件

关于mv指令
move 用于文件移动或者重命名
文件改名: mv test.log test.txt
移动文件: mv test.txt test1
批量移动文件: mv log1.txt log2.txt log3.txt test1
            : mv -t /opt/soft/test/test4/ log1.txt log2.txt  log3.txt
文件改名, 询问是否覆盖: mv -i text.log text.txt
文件改名, 强制覆盖: mv -f text.log text.txt
目录改名或者移动: mv dir1 dir2 若dir2存在, 就是移动目录, 否则就是改名
将当前目录下所有文件移动到上级目录: mv * ../
文件重命名做备份: mv text.log -b text.txt

mysql -uroot -h10.9.138.23 -p098f6bcd4621d373cade4e832627b4f6 kugou -e "select id from o2o_spider_song where name like '%快三%' or name like '%慢四%' or name like '%快四%' or  name like '%DJ%' or name like '%舞曲%' or name like '%广场舞%' or name like '%串烧%' or name like '%电音%' or name like '%慢摇%' or name like '%MC%' or name like '%喊麦%' or name like '%慢三%' or name like '%车载%' or name like '%remix%' or name like '%m c%' or name like '%m.c%' or name like 'd.j'" > o.txt

ubuntu搭建ftp服务器:
http://cuiqingcai.com/436.html

关于systemctl命令:
systemctl命令是系统服务管理器指令
来自: http://man.linuxde.net/systemctl
sudo systemctl status nginx
sudo systemctl start nginx
sudo systemctl restart nginx
sudo systemctl stop nginx

用init.d启动服务
etc/init.d/nginx start

grep命令文件夹下全局搜索:
grep -nir '<?xml version=\"1.0\' .

查看当前用户:
whoami
显示用户所在组:
groups xinghang
切换root用户:
sudo -s

查看进程的pstree命令
pstree
查看进程及其占用: https://linux.cn/article-3141-1.html
htop -d 1000

查看当前redis占用: 'info memory'
127.0.0.1:6379> info memory
# Memory
used_memory:9093088
used_memory_human:8.67M
used_memory_rss:21397504
used_memory_rss_human:20.41M
used_memory_peak:9116736
used_memory_peak_human:8.69M
total_system_memory:8371302400
total_system_memory_human:7.80G
used_memory_lua:37888
used_memory_lua_human:37.00K
maxmemory:0
maxmemory_human:0B
maxmemory_policy:noeviction
mem_fragmentation_ratio:2.35
mem_allocator:jemalloc-4.0.3
更详细的redis info
127.0.0.1:6379> info

ack命令进行搜索:
ack get_pos_ktv_id mysql/

load data infile '/var/lib/mysql-files/30W.csv' into table thunder_song fields terminated by ',' lines terminated by '\n' ignore 1 lines (thunder_id, name, artist1, artist2, artist3, artist4, download_link, has_krc);

关于sed命令
sed是一种流编辑器，它是文本处理中非常中的工具
sed -n '2p' file         #输出文件的指定行
sed -e '5d,10d' file     #输出文件除了5,10,的其他行
sed -ie '5d,10d' file    #输出文件除了5,10的其他行, 并且重定向到同名文件, 就像删除了一样

同步文件
rsync -e 'ssh -p 3026' -av --progress /Users/xinghang/179W.csv xinghang@101.254.157.124:~/
rsync -e 'ssh' -av --progress /Users/xinghang/179W.csv work@106.75.97.4:/home/work/

python tornado的线上启动方式:
python init.py --port=8989 --debug=false

关于欢乐歌房的部署:
ssh jump
ssh huanle (ssh deploy@123.59.49.2  密码： Deploy@Leishi7348)
代码路径: /data/app/TV_HuanleGeFang/
上线: 执行 sh online.sh （这个脚本会自动更新代码并重启服务程序）
多机自动部署:  在pyweb1-bjb (开头登录的那台服务器上） 执行 pupdate.sh TV_HuanleGeFang

获取本机ip地址的接口:
curl https://ipip.yy.com/get_ip_info.php

在服务器上增加用户:
1.sudo useradd xinghang (不要在root下新建用户, 会导致无法登陆)
2.sudo usermod -s /bin/bash xinghang (指定用户用的shell)
3.sudo usermod -d /home/xinghang xinghang (指定用户登入目录)
4.passwd xinghang (root下, 设置密码)
5.visudo (增加用户sudo权限)
6.mkdir -p /data/home/xinghang
7.chown xinghang:xinghang /data/home/xinghang
8.拷贝pyenv

关于解压缩:
tar -czvf a.tar.gz /home/work/onling/song/*
tar -xzvf a.tar.gz
以上命令会包含路径, 这种方法可以忽视路径:
tar -cjf 1.tar -C /home/work/song .
tar -xvf 1.tar

nano是一个字符终端的文本编辑器, 有点像DOS下的editor程序
它比vi/vim要简单得多, 比较适合Linux初学者使用, 某些Linux发行版的默认编辑器就是nano
nano test/py.py
^ = ctrl

测试机nginx位置: /usr/local/nginx/sbin/nginx
lab nginx测试配置: /usr/local/nginx/conf/lab_test.conf
检测语法: /usr/local/nginx/sbin/nginx -t
热加载: /usr/local/nginx/sbin/nginx -s reload

命令查询:
man apt-get | grep reinsta -A2

关于yum:
更换yum源: http://blog.csdn.net/chavo0/article/details/51939362
列出可以安装的程序: yum list
列出已经安装的程序: yum list installed |grep php
卸载: yum remove php5*
升级: yum update ***

进入根目录: sudo -s
切换用户: su huiying

显示当前linux主机版本信息:
lsb_release -a

非常奇怪的service命令:
输入service可以补全, sudo service 竟然不能补全...
http://blog.csdn.net/chavo0/article/details/51939362
servise mysqld start

查看根目录下体积最大的前十个文件:
find / -printf '%s %p\n'| sort -nr | head -10

登录线上数据库:
source tv-video-cms-global/bin/activate
cd cms/
python manage.py dbshell

pip list --format=freeze
pip list --format columns

[wget 下载重定向]
wget -O viki_sample.json https://s3.amazonaws.com/assets.viki-production/outbound_feeds/xiaomi_tv/production_1534214855/xiaomi_tv_1.json

[curl 上传文件]
curl -F 'file=@/User/xinghang/go.py' https://media.ptmi.gitv.tv/tvservice/player_error?device_id=&app_ver=295&ptf=214&opaque=ee2d2ae40417b3541e368de5f3006238170f8d98

[aapt]
aapt dump badging app-debug.apk

[输出文件的某一行]
cat search.txt |tail -n +14124 |head -n 10
