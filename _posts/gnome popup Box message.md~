---
layout: post
title: gnome 下的几种 Box message
date: 2012-08-15 20:29:56
---
gnome popup Box message 
===

之前写一些要用的脚本的时候.苦于没有找到方便的可视化消息通知方法
之前的做法是是使用pyqt 写一些简单的message box 可以见[这里](https://github.com/xiyoulaoyuanjia/GetVdiskLink)

后来在[这里](http://smashingweb.info/send-messages-over-network-gnome-popup-box-message/)
发现了gnome下的一些常用的Box message  方法。感觉用着很舒服。。这里推荐给大家

**zenity:It will display a default ok box on the screen**

>* display  GTK+ dialogs
>*  输出 ”message here“ 信息
    
    zenity --info --text "message here"

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=db92UKpsF8HUcwp1UHTtfeyhW4kyX9gebYU8Z6gBVkTRHTr5FmY1xPoZZzZ--2F--2BMl3xWWiO--2Bg5cTo8--2FZ82RvckEBeOIbMc)

>* 输出gtk标准日历

    zenity  --calendar

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=8da6YLsDYCnzz97bD0p--2BVWTJipB7Jap6KF26CUT1YajYJzjhxdnrOfZBWffhFyqMKbf5ifKL0yS1O946ClbAobf--2Fw7FD)

更详细的用法参见 man zenity

这里有一篇[wikipedia 的介绍](http://en.wikipedia.org/wiki/Zenity)

**notify-send:系统提示托盘**

>* notify-send ["title"] "message"

>* notify-send ["title"] "message" -t 500

这里 -t 表示显示时间


我在我的连接校园网的程序中也应用了这个。。。感觉比自己写好看多了

[这里](https://github.com/xiyoulaoyuanjia/blog/blob/master/%E5%85%B3%E4%BA%8E%E5%8C%97%E9%82%AE%E6%A0%A1%E5%9B%AD%E7%BD%91%E7%99%BB%E5%BD%95%E7%A8%8B%E5%BA%8F.md)

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=b3d344--2FxLktIPmUVQn6KtbjbBClvLBx2AMZ3tC--2Blw2c--2Fhq2bVDo7GgYdp7fLKwJNg7K2wEOGfPqP9dHVWL0WzujDdvEZ)

**xmessage**

这个程序主要依赖 x libary 产生消息框的程序

这个可以用来做一些shell层的选在框 

    xmessage  "Are you sure you want to shutdown? " -buttons yes,no
    echo $?

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=b8a4QzDUEFUpVNIH7B328--2FGiSJcaTHjF--2FvosYrlkt2pjU--2F8DS2rNs--2Fa--2BQOOojpsXbMsledIcUzBfmtol--2BJVoHyq--2B--2BS0R)

或者

    answer=$(xmessage  "Are you sure you want to shutdown? " -buttons yes,no -print)
    echo $answer

常用的一些选项

    -center – the message at center   
    -nearmouse – the message near mouse
    -timeout secs – will close after some seconds.

更多的可以 man xmessage 查看

**Over SSH**

    DISPLAY=:0; XAUTHORITY=~owner_of:0/.Xauthority; export DISPLAY XAUTHORITY

这个没有实践不多说....








