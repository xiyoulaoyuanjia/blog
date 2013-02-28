linux使用记录
==========
******

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


![](http://en.wikipedia.org/wiki/File:KB_Terminal_ADM3A.svg)


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


















