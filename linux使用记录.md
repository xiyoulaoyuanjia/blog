linux 使用记录
==================


**fedora 17 kde**

***关于konsole光标前面空格的问题***

出现这种问题的原因是之前更高字体造成的 删除~/.fonts 下的字体即可

***Fedora 17 安装 Cinnamon 桌面环境***

cinnamon桌面环境是linux Mint 下的桌面环境 当然fedora 17 下也是可以安装的

    sudo curl http://repos.fedorapeople.org/repos/leigh123linux/cinnamon/fedora-cinnamon.repo -o /etc/yum.repos.d/fedora-cinnamon.repo
    sudo yum install cinnamon

注销后登陆选择 cinnamon即可

***[Fedora 17 使用MATE桌面](http://forums.fedoraforum.org/showthread.php?t=276286)***

MATE 是传统gnome2的一个分支。代码维护在github上

    yum install https://dl.dropbox.com/u/49862637/Mate-desktop/fedora_17/mate-desktop-fedora-updates/noarch/mate-desktop-release-17-4.fc17.noarch.rpm
    yum groupinstall MATE-Desktop

***yum groupinstall***    

一般而言 yum 可以使用 intall 与 groupinstall 安装软件。install安装单个软件以及单个软件的依赖。而groupinstall 可以理解为打包安装许多软件以及这些软件的依赖

例如安装mysql

    yum install mysql
    yum groupinstall "MySQL Database"

    Group: MySQL Database
     Description: This package group contains packages useful for use with MySQL.
     Mandatory Packages:
     mysql
     Default Packages:
     unixODBC
     mysql-server
     MySQL-python
     mysql-connector-odbc
     libdbi-dbd-mysql
     perl-DBD-MySQL
     Optional Packages:
     mod_auth_mysql
     mysql-devel
     qt-MySQL
     mysql-bench
     php-mysql

由上面可以看出yum groupinstall 这种安装方式 会安装多个软件。以及自动解决安装包的依赖问题

**alsa-lib-1.0.26-1.fc17.i686 与 alsa-lib-1.0.25-3.fc17.x86_64 冲突**

今天在安装teamview时，官方在redhat系里面没有给出64位对应的安装包.其安装版本依赖许多32位的包，上面就是其中一个。无奈不能正常安装

这里使用先删除x64的包，然后在安装alsa-lib-1.0.26-1.fc17.i686 经验证成功安装



**centos 常见的3个第三方源**

EPEL RPMForge RPMFusion

**linux ～用来表示 home目录**

原因是80(1970s)年代 ,Lear-Siegler 生产的 ADM-3A 终端所用的键盘把～与home键在一起 


![](http://upload.wikimedia.org/wikipedia/commons/a/a0/KB_Terminal_ADM3A.svg)


![](http://i.stack.imgur.com/L3esv.jpg)


**shell脚本罗列出所有名称中含有中文的文件和目录，并统计一下总数**

find . -type f | grep -P -r "[\x80-\xFF]" | cat | wc -l

**Waiting for network configuration--ubuntu 11.10 解决方案**

打开本机 进入11.04 系统(后升级到11.10) 

首先是提示 waiting for the network configuration

然后是 Waiting for 60 seconds more for network configuration

最后是 booting system without full network configuration...

很是郁闷 最后 sudo vim /etc/network/interface 进入 修改配置文件 为

    auto lo
    iface lo inet loopback
    #auto eth0
    #iface eth0 inet dhcp
    
也就是注释掉 eth0 的网卡配置  开机速度飞快。。


**操作含有---- 名的文件**

--是标准的去掉-特殊含义的方式。比如说touch -- ----就可以创建一个文件名为----的文件
例如删掉----名的文件
    rm -- ----


**top里面可以只列出某个名字的进程**

top  -p 后根需要列出得到pid的值

top -p $(pgrep -d',' http)这个分为1.寻找含有http字符的进程名称的pid(注意pgrep的用法 -d表示结果用逗号区分)"$()"这种用法把结果直接拿来用需要学习

下面还有一个小例子

例：mysqld的信息

(1)得到mysqld进程的pid

    [root@6 ~]# pidof mysqld
    21538
    
(2)top指定查看PID

    [root@6 ~]# top -p 21538

**ACPI: [Package] has zero elements**

华硕k52d 本本 上装得 fedora 17  64位  每一次启动都会出现 
ACPI: [Package] has zero elements 
然后有时可以顺利的进入系统有时停在此处 不知怎么解决。。

解决办法: 

>*1.在 /etc/default/grub 修改如下
GRUB_TIMEOUT=5
GRUB_DISTRIBUTOR="Fedora"
GRUB_DEFAULT=saved
GRUB_CMDLINE_LINUX=" nomodeset rd.md=0 rd.lvm=0 rd.dm=0 SYSFONT=True  KEYTABLE=us rd.luks=0 LANG=en_US.UTF-8 rhgb quiet acpi=off"

>*2.grub2-mkconfig -o /boot/grub2/grub.cfg


_这里需要注意acpi必须为小写。之前一直大写搞了半天。。_

**cannot open font file ture**

fedora 17 上的错误修改如下

    vi /etc/default/grub 
    SYSFONT=True改掉就好 SYSFONT=latarcyrheb-sun16
    grub2-mkconfig -o /boot/grub2/grub.cfg


*查看安装软件的信息 包括时间包、依赖的包等信息***

    yum history list
    yum history info 123
    yum history undo 123



**linux系统剪贴板**

linux 系统存在两个剪贴板  一个叫做选择缓冲区(X11 selection buffer)   另一个叫做剪切板(clipboard)

选择缓冲区是实时的，当使用鼠标选择内容时。即将内容复制到了选择缓冲区中。 剪贴板同 windows下的剪贴版。。

另外需要xterm复制用的是**选择缓冲区** 当然现在还用这个的实在比较少了。。 鼠标中间的按钮一般是选择缓冲区或者shift+Insert


**Fedora中的kmod与akmod**

由于许可证或使用规模等原因，一些硬件的驱动无法进入kernel，只能通过内核模块的形式来加载使用。在Fedora中如果你启用了rpmfusion-nonfree源，你会看到大量kmod-打头的软件包，大多都是rpmfusion帮我们编译、打包好的各类私有驱动（比如nvidia、ati的显卡驱动，broadcom的网卡驱动等等） 

**Fedora中的kmod与akmod区别**

akmod**没有子包，而kmod**则有大量的子包akmod替代kmod是大势所趋

**每次开机都会出现 Enter password for default keyring to unlock?    然后要求输入密码？甚是烦躁。。**

解决办法。。 Right-click on the NetworkManager icon on your panel and select edit connections. Click the Wireless tab and select your network. Click Edit and tick the checkbox on the bottom that says "Available to all users". Click apply.   也就是链接的这个无限要求输入密码。。。

**fedora 17 开机 都会出现  error: file '/boot/grub2/locale/en.mo.gz' not found**

解决办法。   sudo cp /boot/grub2/locale/uk.mo /boot/grub2/locale/en.mo


**markdown 语法中 向这种<decoded_as> 的不能现实呀。？？？ 怎么办？**

一般来说 markdown 对特殊语法 前加入"\"  即可转议，但是这个却不行，目前解决办法 是在 "<" 之后加入空格

**如何保障 linux的临时文件目录  一般为/var/temp  或者 /temp **

由于没有另外分区 导致其分区选项与/ 相同 这样 不能更小的粒度。最好 的是 另外一个分区 然后 修改挂在这个分区的选项

**PS1 是用来设置命令提示符的环境变量 修改的是 yuanjia@yuanjia-K52Dr:~$ 的格式**

**ls --color=auto 用来显示ls展示的目录 文本 具有的颜色**

**可以在 terminal 上使用  control-v 粘帖的一段代码。。这个很好用奥。。**

    # Make Control-v paste, if in X and if xclip available - Josh Triplett
    if [ -n "$DISPLAY" ] && [ -x /usr/bin/xclip ] ; then
        # Work around a bash bug: \C-@ does not work in a key binding
        bind '"\C-x\C-m": set-mark'
        # The '#' characters ensure that kill commands have text to work on; if
        # not, this binding would malfunction at the start or end of a line.
        bind 'Control-v: "#\C-b\C-k#\C-x\C-?\"$(xclip -o -selection c)\"\e\C-e\C-x\C-m\C-a\C-y\C-?\C-e\C-y\ey\C-x\C-x\C-d"'
    fi

**alias 命令使用**

若仅输入alias，则可列出目前所有的别名设置。　alias的效力仅及于该次登入的操作。若要每次登入是即自动设好别名，可在/etc/profile或自己的~/.bashrc中设定指令的别名。
 例如  alias httpserver='python -m SimpleHTTPServer

**ubuntu 目录太深？ 向fedora 那样只显示当前目录？**

打开 /etc/bash.rc  找到  PS1='${debian_ chroot:+($debian_ chroot)}\u@\h:\w\$ '  更改为  小写w改为大写W

***What's the command to open a file in GUI?***

    xdg-open filepath

**关于环境变量。(以下来自larmbr zhan 网友)**

LC_*形环境变量的优先级是：LC_ALL > LC_* > LANG.

具体地说，
>*1.就是如果定义了LC_ALL ，则它覆盖了所有LC_*变量的定义，所有规则都遵从LC_ALL的
定义。 （注意，这个变量不要设定，它的存在价值可能仅在于定义了一个新locale后，作测试用)


>*2. 如果LC_ALL没设定(合理的方法是应该一直这么做)。则由LC_*细粒度地定义了各个方面，
如关于字符集LC_CTYPE. 关于货币符号LC_MONETARY，关于提示信息LC_MESSAGES等。

  所以本例中，你应该设定这个变量. 对于GNU家族的工具集，
  那么如果LC_MESSAGES， 则LANGUAGE值起到和它一样的作用，如你所设。


>*3. 如果LC_ALL, 及LC_*都没设定，那么会读取 LANG 的设定。


**about 缓冲区？**

windows 的缓冲区只有一个 全局的缓冲区（Clipboard，剪贴板）

*nix (The X server)里面貌似有 4个？(主（Primary）选择，一种是剪贴板（Clipboard）选择。其实还有一个副（Secondary）选择 貌似还有一个 剪切缓冲区 CUT_BUFFER0 在这四个缓冲区中  貌似其中的 副 选择 和  CUT_BUFFER0 已经不太用了。。)  但是 VNC 还是使用的 CUT_BUFFER0  这个缓冲区传递数据。所以这里牵扯了一些同步的问题。。。好多VNC 使用 autocutsel(http://www.nongnu.org/autocutsel/) 来同步 缓冲区。。。。


**shell 脚本传递变量**

    #!/bin/shell
    #file test.sh
    if [ -z ${PARAM1} ]; then
        PARAM1=test1
    fi
    echo ${PARAM1}
    
    PARAM1=hello sh test.sh

**关于wget伪装成浏览器的行为 更改user-agent**

今天在拔 http://mahua.jser.me/  网站的css时候遇到了一个问题.. 刚开始使用 wget 下载 js 还可以 然后就不行了..

但是浏览器是可以打开的 这时候 使用

wget --user-agent="Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)" http://mahua.jser.me/ace/keybinding-vim.js

成功下载 看来对方使用验证 UA的小计量了......

**关于github 项目的语言标签的问题**

今天上传了 [flaskapp]() 项目时 发现github检测到的项目为javascript(应该为python 更贴切点吧) 于是查了些资料
[问题看这里](http://stackoverflow.com/questions/5318580/how-does-github-figure-out-a-projects-language)

检测算法项目[在这里](https://github.com/github/linguist)  有时间看看它的这个算法是怎么搞得..不过貌似没有读内容就是查看了后缀?

**linux 下图像格式转换**

>* convert xiyoulaoyuanjia.png  xiyoulaoyuanjia.gif 

把 xiyoulaoyuanjia.png 格式转换为  xiyoulaoyuanjia.gif   注意此时 xiyoulaoyuanjia.png 图片格式不变

>*   convert  -resize 16x16! xiyoulaoyuanjia.gif  flaskWeb.gif

把  xiyoulaoyuanjia.gif  图片缩小为 16x16 像素的  注意后面的叹号(!)

**bash 脚本的几个问题**

今天再看 ossec 中的 ossec-control 脚本时遇到的几个问题,这里记录下.

>*  "sudo cat   /var/ossec/var/run/ossec-logcollect*.pid " 与 su && cat   /var/ossec/var/run/ossec-logcollect*.pid 的区别? 
 
当然如果你想着一样那么就错了...至于原因who knows?

>*  脚本中有一段 kill -0 process 干什么呢?

[看这里](http://stackoverflow.com/questions/11012527/what-does-kill-0-pid-in-a-shell-script-do)

>>* 1. 查看进程十分running?
>>* 2. 查看进程能否接受信号
>>* 3 "." 在shell 中的应用 用来引入环境变量  例如  . 文件名 A  在 A中写 LIANX="fff"

>>>* 看 ossec 如何使用？

    . ./src/init/update.sh
        # Is this an update?
        if [ "`isUpdate`" = "${TRUE}" -a "x${USER_CLEANINSTALL}" = "x" ]; then
            echo ""
            ct="1"

isUpdate 在 update.sh 中定义为 一个函数 . 或者 source 之后直接就 可以当作 
命令使用了


***********************************************************************************
**gcc include 查找路径**

这里忽略复杂的问题.. /var/include 与 /var/local/include
***************************************************************************************
**输入法的问题***

>* 安装 google 输入法 

>>* 添加源：
sudo add-apt-repository ppa:fcitx-team/nightly
sudo apt-get update

>>* 安装Fcitx、Fcitx-googlepinyin

sudo apt-get install fcitx fcitx-googlepinyin



>* 安装 搜狗输入法

sudo apt-get install  fcitx-sogoupinyin

貌似在ubuntu的12.10 中有错误。。

im-switch 转换输入法
**********************************************************************************************

**blkid 有用的一个命令**

/dev/sda1: LABEL="window 7" UUID="D058935E58934260" TYPE="ntfs" 
/dev/sda10: LABEL="M-eM-(M-1M-dM-9M-^P" UUID="0006E42B000753BB" TYPE="ntfs" 
/dev/sda5: LABEL="M-hM-=M-/M-dM-;M-6" UUID="0007165D000660F4" TYPE="ntfs" 
/dev/sda7: LABEL="_Fedora-17-x86_6" UUID="3b9eea35-98aa-4c24-b255-4f40585079b7" TYPE="ext4" 
/dev/sda8: LABEL="M-fM-^VM-^GM-fM-!M-#" UUID="000A0C6100003D53" TYPE="ntfs" 
 
**安装 Ubuntu restricted extras软件包 包含常用的一些 受限软件 安装完系统之后第一时间可以安装这个**

**删除除××之外的文件**

rm 没有 exclude 选项 考虑使用 管道方式组合使用命令

例如 sudo rm  -f `ls | grep -v partial`


**history 命令 **

之前一直没有使用过这个命令 最近在 [这里](http://cloudbbs.org/forum.php?mod=viewthread&tid=13726)
看到了 感觉挺好用的 这里做一个小总结。。就当作备忘了。

>*  history 可以显示 之前执行的命令 但是默认没有时间显示。。如果需要修改此格式可以 
通过设置 HISTTIMEFORMAT 变量

    export HISTTIMEFORMAT='%F %T '
    # history | more
    1 2008-08-05 19:02:39 service network restart
    2 2008-08-05 19:02:39 exit
    3 2008-08-05 19:02:39 id
    4 2008-08-05 19:02:39 cat /etc/redhat-release

>* ctrl+r 命令的使用

这个命令是在consol 里面搜索 之前执行过的命令，找到之后可以直接按 回车键执行。修改 可以按
左或者右方向键。。
![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=e803E8HsauaVMaQlToyhWYrTrqMF6bEnkbs--2FdsDHgMPsC9el8v0x6XAL--2BGktC22--2BT7O--2Fs4a--2Fsi7Hx8rxCNfmrRvzleRe)

>* 快速执行上一条命令

这里列出了 4条方案

>>* 使用上方向键，并回车执行。

>>*  !! 并回车

>>* !-1 并回车

>>* 按 Ctrl+P 并回车执行

>* 通过序号执行一个指定的命令

    # !4

>* 使用 HISTSIZE 控制历史命令记录的总行数

默认是 500

>* 更改默认历史命令记录文本

默认情况下，命令历史存储在 ~/.bashhistory 文件中
更改HISTFILE

    # vi ~/.bash_profile
    HISTFILE=/root/.lianxi

>* 使用 HISTCONTROL 从命令历史中剔除连续重复的条目

export HISTCONTROL=ignoredups

>* 清除所有的命令历史

    history -c

>* 使用 HISTSIZE 禁用 history

    export HISTSIZE=0

>* 使用 HISTIGNORE 忽略历史中的特定命令

     export HISTIGNORE="pwd:ls:ls -ltr:"

**如何获取 python 中字符串(str) 的编码方式?**

对于str很容易产生乱码的问题..每次产生乱码问题..就会考虑 str是使用什么编码的呢? 今天看到一个库
可以判断str的字符编码感觉很好用..

import chardet
s = "utf-8 字符串"
chardet.detect(s)



********************************************************************
**关于浮点数的小理解**

原因，简单的说是因为一些十进制有限小数在2进制中是无限小数。
解决方法，搜索 decimal

可以看看python 中的解释。
http://docs.python.org/2/tutorial/floatingpoint.html

**Apt-get GPG Error: Public Key Not Available**

看到一篇十分好的[文章](http://www.rebelzero.com/fixes/apt-get-gpg-error-public-key-not-available/88)

解决这种方法的思路 

wget -q "http://keyserver.ubuntu.com:11371/pks/lookup?op=get&search=0x4874D3686E80C6B7" -O- | sudo apt-key add -

4874D3686E80C6B7 为 错误id

**在shell 中如何判断 一个变量被赋值没有？ 看 ossec 如何实现的？**

    # If user language is not set
        if [ "X${USER_LANGUAGE}" = "X" ]; then 

好吧。我承认这也是一种方法。。。


**shell 中if 的逻辑表达式 **

    >* 逻辑非 ! 
        if [ ! 表达式 ]
    >* 逻辑与 –a  
        if [ 表达式1  –a  表达式2 ]
    >* 逻辑或 -o
        if [ 表达式1  –o 表达式2 ]


可以看ossec中如何使用的

    # Choosing the language.
        while [ 1 ]; do
        echo ""
        for i in `ls ${TEMPLATE}`; do
            # ignore CVS (should not be there anyways and config)
            if [ "$i" = "CVS" -o "$i" = "config" ]; then continue; fi
            cat "${TEMPLATE}/$i/language.txt"
            if [ ! "$i" = "en" ]; then
                LG="${LG}/$i"
            fi
        done

**在终端下使用vim的命令  注意终端下只有 插入与命令模式**

开启 默认是在插入模式下
     set -o vim 
切换到 命令模式 
    ESc 键

**bash 的 cmd  <(subcmd)特殊用法**

这是bash的一个特殊构造： cmd  <(subcmd) 表示将subcmd输出的管道作为文件传递 给cmd作为参数

例如
diff <(echo {1..10})  <(echo {2..10})

再比如
ls -l <(echo {1..10})

**443 端口是 https 默认采用的端口**

**gcc -Wall   ssl-demo.c -lssl -o ssl-demo 与 gcc -Wall    -lssl ssl-demo.c  -o ssl-demo
的 区别 **

今天在测试一段 ssl的代码时发现 gcc -Wall   ssl-demo.c -lssl -o ssl-demo 会执行错误
调整了 -lssl  的顺序之后 正常 。。很是诡异。。。
测试代码如下：
https://gist.github.com/xiyoulaoyuanjia/cd2bb25e394d06b92403

这里顺便回忆下动态库的加载顺序 

>* 编译目标代码时指定的动态库搜索路径；
>* 环境变量LD_LIBRARY_PATH指定的动态库搜索路径；
>* 配置文件/etc/ld.so.conf中指定的动态库搜索路径；
>* 默认的动态库搜索路径/lib；
>* 默认的动态库搜索路径/usr/lib。


**What's the difference between /sbin/nologin and /bin/false**

When /sbin/nologin is set as the shell, if user with that shell logs in, they'll get a polite message saying 'This account is currently not available.'. This message can be changed with the file /etc/nologin.txt.

/bin/false is just a binary that immediately exits, returning false, when its called, so when someone who has false as shell logs in, they're immediately logged out when false exits. Setting the shell to /bin/true has the same affect of not allowing someone to log in but false is probably used as a convention over true since its much better at conveying the concept that person doesn't have a shell.

Looking at nologin's man page, it says it was created in 4.4 BSD (early 1990s) so it came long after false was created. The use of false as a shell is probably just a convention carried over from the early days of UNIX.

nologin is the more user friendly option, with a customizable message given to the user trying to login, so you would theoretically want to use that but both nologin and false will have the same end result of someone not having a shell and not being able to ssh in.

[orignal link](http://unix.stackexchange.com/questions/10852/whats-the-difference-between-sbin-nologin-and-bin-false)

**Get UUID of specific connection?**

>* find the UUID of the current connection
>
        nmcli con status


>* list all configured connections
>
        nmcli con list

**ubuntu debian 下使用 jekyll**

>* sudo apt-get install ruby1.9.1-dev
>* gem install jekyll


**Chrome扩展程序开发：Ajax XmlHttpRequest**

>* 在插件中使用ajax不受跨域(cross-origin)的限制。
>* ajax网络请求需要在manifest.json得到相应域名的permissions.

**修改左边的unity2d 使它不会自动隐藏?**


之前一直在考虑使用 脚本更改设置，今天无意中发现  appearance-》behavior-》auto-hide the launcher 直接更改。而且下面还可以修改灵敏度。。囧。。

**应用程序的用户配置文件夹放在~/.config文件夹的原则**

之前一直就发现应用程序的配置文件一般都存放在 ~/.config文件夹 下的情况。今天才知道这个原来是 XDG的 标准。是给linux 图形桌面的配置文件的推荐做法。。 更多关于标准的细节可以看[这里](http://standards.freedesktop.org/basedir-spec/basedir-spec-latest.html)

早就知道这个XDG (例如XDG-open) 但是还真不知道这个和 linux 桌面有什么关系。今天就查了查原来

XDG stands for X Development Group, which was the old name of FreeDesktop.org:

回到上面。那么这个统一的存放目的有什么用呢？

比如如果你用C实现一个应用程序，GLib有这样的一个函数 g_get_user_config_dir () ：https://developer.gnome.org/glib/2.34/glib-Miscellaneous-Utility-Functions.html#g-get-user-config-dir  用它会直接返回~/.config （如果默认配置是这个的话）。

但是命令行(非桌面) 一般就不按这个标准 例如 git 它的配置文件就直接是 ~/.gitconfig


**linux terminal 光标到命令开始处 与 结尾处**

Ctrl+A：将光标移动到命令行的开始处。

Ctrl+E：将光标移动到命行令的结尾处。

上面两个还是很有用的。。



**看了许多bash脚本发现都会有 set -e 这一行,查了发现还挺有用的.**

-e      Exit immediately if a pipeline (which may consist of a single simple command),  a subshell command enclosed in parentheses, or one of the commands executed as part of a command list enclosed by braces (see  SHELL  GRAMMAR above) exits with a non-zero status.

就是对于 pipeline subshell commands 有非0的返回值则脚本直接推出

__The current script's pid is $$, the pid of the last background process is $!__ 

**Create an animated GIF on linux**

 Type "convert -delay X -loop 0 images*.gif animation.gif", where X is the delay in miliseconds and images*.gif is the name your images have in common, followed by the wildcard character *. This will allow the program to follow through the sequences of images.

    convert -delay X -loop 0 images*.gif animation.gif 

[other tools](http://www.ehow.com/how_7211144_make-gif-animation-linux.html)




