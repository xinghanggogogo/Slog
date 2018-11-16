"bundel配置
set rtp+=~/.vim/bundle/vundle/
call vundle#rc()
Bundle 'gmarik/vundle'
Bundle 'thoughtbot/vim-rspec'
Bundle 'ack.vim'
Bundle 'comments.vim'

"文件搜索crtl+p
Bundle 'ctrlp.vim'
let g:ctrlp_working_path_mode=0
let g:ctrlp_match_window_bottom=1
let g:ctrlp_max_height=15
let g:ctrlp_match_window_reversed=0
let g:ctrlp_mruf_max=800
let g:ctrlp_follow_symlinks=1

"函数搜索\+fu(fU)
Bundle 'tacahiroy/ctrlp-funky'
nnoremap <Leader>fu :CtrlPFunky<Cr>
nnoremap <Leader>fU :execute 'CtrlPFunky ' . expand('<cword>')<Cr>
let g:ctrlp_funky_syntax_highlight = 1
let g:ctrlp_extensions = ['funky']

"文件目录打开文件F3
Bundle 'scrooloose/nerdtree'
nnoremap <F3> :NERDTreeMirror<CR>
nnoremap <F3> :NERDTreeToggle<CR>

"快速注释ctrl+c, \cc, 取消注释\cu
Bundle 'scrooloose/nerdcommenter'

Bundle 'rspec.vim'
Bundle 'honza/vim-snippets'
Bundle 'ervandew/supertab'
Bundle 'tpope/vim-bundler'
Bundle 'kchmck/vim-coffee-script'
Bundle 'tpope/vim-fugitive'
Bundle 'tpope/vim-haml'
Bundle 'tpope/vim-rails'
Bundle 'nathanaelkane/vim-indent-guides'
Bundle 'pangloss/vim-javascript'
Bundle 'jelera/vim-javascript-syntax'
Bundle 'briancollins/vim-jst'
Bundle 'plasticboy/vim-markdown'
Bundle 'Lokaltog/vim-powerline'
Bundle 'vim-ruby/vim-ruby'
Bundle 'slim-template/vim-slim'
Bundle 'sudo.vim'
Bundle 'xml.vim'
Bundle 'ZenCoding.vim'

"自动补全
Bundle 'Valloric/YouCompleteMe'

"高亮以及语法检查
Bundle 'scrooloose/syntastic'
let python_highlight_all=1
syntax on

set nu
syntax on
set nowrap
filetype plugin on
set bsdir=buffer
set history=1000
set nocompatible
set background=light
set nocursorcolumn
set showcmd
set smartindent

"tab和换行
set tabstop=4                  " tab size eql 4 spaces
set softtabstop=4
set shiftwidth=4               " default shift width for indents
set expandtab                  " replace tabs with ${tabstop} spaces
set smarttab
if has("autocmd")
    filetype plugin indent on
    augroup vimrcEx
    au!
    autocmd FileType text setlocal textwidth=78
    autocmd BufReadPost *
    \ if line("'\"") > 1 && line("'\"") <= line("$") |
    \ exe "normal! g`\"" |
    \ endif
    augroup END
else
    set autoindent
endif
    autocmd BufEnter * lcd %:p:h

set showmatch
set hlsearch
set incsearch
set ruler
set foldmethod=marker
set t_Co=256
set scrolloff=3
colorscheme SerialExperimentsLain
set backspace=indent,eol,start whichwrap+=<,>,[,]
hi Search term=reverse ctermfg=0 ctermbg=3
set completeopt=menu

set ambiwidth=double
let $LANG='en'
set termencoding=utf-8
set langmenu=zh_CN.UTF-8
set guifont=Bitstream_Vera_Sans_Mono:h10:cANSI
set gfw=幼圆:h10:cGB2312
set fileencodings=utf-8,cp936,gb18030,big5,euc-jp,euc-kr,latin1
set fencs=utf-8,gbk
set termencoding=utf-8
set encoding=utf-8

"<F5>一键执行python
au BufRead *.py map <buffer> <F5> :w<CR>:!/usr/bin/env python % <CR>

"折叠
set foldmethod=indent
set foldlevel=99
