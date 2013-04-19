
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






