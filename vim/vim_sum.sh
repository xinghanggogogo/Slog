vim transport
cd ~/.vim
mkdir bundle && mkdir colors
cd bundle
git clone http://github.com/gmarik/vundle.git
cd colors
scp work@106.75.97.4:/home/work/.vim/colors/SerialExperimentsLain.vim .
scp work@106.75.97.4:/home/work/.vimrc .
:BundleInstall

youcompleteme
编译: cd ~/.vim/bundle/youcompleteme;
http://valloric.github.io/YouCompleteMe/#ubuntu-linux-x64
python install.py

关于NERDTree插件的使用:
http://www.jianshu.com/p/eXMxGx
\f 绑定:NERDTree
t s i gt gT

ack.vim插件的使用:
http://www.jianshu.com/p/2f1c140c7eb8

一键运行python代码:
au BufRead *.py map <buffer> <F5> :w<CR>:!/usr/bin/env python % <CR>

gd选中当前单词
:noh取消选中

目录树:
https://my.oschina.net/VASKS/blog/388907

u撤销
ctrl+r回复撤销

:sv水平分屏
:vs垂直分屏
ctrl w w 换屏
ctrl w hjkl 换屏
ctrl w q 关闭当前屏幕

yy直接复制当前行, p直接粘贴
可以yy+p看看效果
nyy可以复制多行, 然后移动光标, p

滚屏
ctrl+e 向下一行
ctrl+y 向上一行
crtl+o 将光标移动到上次的位置
z. 将光标所在行移动到屏幕中间

标记跳转
ma `a`

整行选中:
shift v

centOS更换yum源:
