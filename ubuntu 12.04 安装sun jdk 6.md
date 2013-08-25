**ubuntu 12.04 安装sun jdk 6**

按照这个文档[http://netwrkspider.blogspot.in/2012/05/how-to-install-sun-java6-jdk-on-ubuntu.html]
添加ppa后,直接


    $ sudo apt-add-repository ppa:flexiondotorg/java
    $ sudo apt-get update
    $ sudo apt-get install sun-java6-jre sun-java6-jdk sun-java6-plugin

后发现会报错误. 错误详细信息如下:

     sun-java6-jdk:i386 : Depends: sun-java6-bin:i386 (>= 6.30-2~precise1) but it is not going to be installed
     sun-java6-jre : Depends: sun-java6-bin (>= 6.30-2~precise1) but it is not installable or
                              ia32-sun-java6-bin (>= 6.30-2~precise1) but it is not installable
     sun-java6-plugin:i386 : Depends: sun-java6-bin:i386 (>= 6.30-2~precise1) but it is not going to be installed
                             Depends: firefox:i386 but it is not going to be installed or
                                      firefox-2:i386 but it is not installable or
                                      iceweasel:i386 or
                                      mozilla-firefox:i386 but it is not installable or
                                      iceape-browser:i386 but it is not installable or
                                      mozilla-browser:i386 but it is not installable or
                                      epiphany-gecko:i386 but it is not installable or
                                      epiphany-webkit:i386 but it is not installable or
                                      epiphany-browser:i386 but it is not going to be installed or
                                      galeon:i386 but it is not installable or
                                      midbrowser:i386 but it is not installable or
                                      moblin-web-browser:i386 but it is not installable or
                                      xulrunner:i386 but it is not installable or
                                      xulrunner-1.9:i386 but it is not installable or
                                      konqueror:i386 but it is not going to be installed or
                                      chromium-browser:i386 but it is not going to be installed or
                                      midori:i386 but it is not going to be installed or
                                      google-chrome:i386

后来 在github上面发现 原作者已经没有维护上面的ppa源了, 写了一个脚本处理.直接运行

    $ wget https://github.com/flexiondotorg/oab-java6/raw/0.2.7/oab-java.sh -O oab-java.sh
    $ chmod +x oab-java.sh
    $ sudo ./oab-java.sh
    $ sudo apt-get install sun-java6-jdk sun-java6-plugin  

在运行上面的脚本时报了一个错误,可能是之前的下载页面连接更改了.错误详细信息如下所示:

    [i] Showing the last 5 lines from the logfile (/home/yuanjia/oab-java.sh.log)...
    [x] Downloading jce_policy-6.zip :    --2013-08-25 11:18:55--  http://jce_policy-6.zip/
    Resolving jce_policy-6.zip (jce_policy-6.zip)... failed: Name or service not known.
    wget: unable to resolve host address `jce_policy-6.zip'

后来在issues里面有人提供了一个path. 修改即可.
    $ wget https://raw.github.com/n0ts/oab-java6/b80d72a7c8b93938ad60c1bae1ce3c26132a96ae/oab-java.sh -O oab-java.sh

安装成功.

***添加环境变量***

在/etc/bash.bashrc 文件中 增加如下

    JAVA_HOME="/usr/lib/jvm/java-6-sun"
    CLASSPATH=".:$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar"
    export JAVA_HOME CLASSPATH











