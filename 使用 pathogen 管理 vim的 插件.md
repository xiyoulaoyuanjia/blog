使用 pathogen 管理 vim的 插件
=======

vim 有许多的特别有用的插件需要安装.. 插件特别多的时候管理起来十分的不方便(各种目录)..今天
在github中看到了[pathogen](https://github.com/tpope/vim-pathogen) 感觉用起来特别的方便....
这里简单介绍下,其安装方法.并且 给出了一个实例.

**安装vim-pathogen**

    mkdir -p ~/.vim/autoload ~/.vim/bundle;
    curl -Sso ~/.vim/autoload/pathogen.vim https://raw.github.com/tpope/vim-pathogen/master/autoload/pathogen.vim

注意 https://raw.github.com 有时候是很有用的东西....

当然上面需要正确运行 你需要安装 curl 程序

    sudo apt-get install curl

打开 ~/vimrc 把如下代码贴进去.

    " Pathogen
    execute pathogen#infect()
    call pathogen#helptags() " generate helptags for everything in 'runtimepath'
    syntax on
    filetype plugin indent on

**安装jedi vim plugin**

[jedit](https://github.com/davidhalter/jedi-vim) gedit是vim下的python 补全利器呀..

第一步安装 jedi

    sudo pip install jedi

第二步使用 pathogen 安装 jedit-vim 插件.. 

    cd ~/.vim/bundle
    git clone https://github.com/davidhalter/jedi-vim.git

__note:pathogen的补全功能是默认打开的 当然可以手动打开与关闭__

    cntrl-space — autocomplete partially type function/class and see args
    shift-k — use pydoc to find function/class documentation


![](http://xiyoulaoyuanjia-sendtosaepic.stor.sinaapp.com/Screenshot%20from%202013-05-16%2017:06:00.png)

__全文完__







