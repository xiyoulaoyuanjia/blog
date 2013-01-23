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






































