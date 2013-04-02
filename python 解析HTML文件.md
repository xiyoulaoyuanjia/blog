 HTMLParser解析HTML文件
===
[python doc 文档](http://docs.python.org/2/library/htmlparser.html)

HTMLParser采用的是一种事件驱动的模式(必须覆写如下列出的几种函数)，当HTMLParser找到一个特定的标记时，它会去调用一个用户定义的函数，以此来通知程序处理

主要的用户回调函数都是已 handler_ 开头的函数 这里列出以下常用的几种

>* handle_startendtag 处理开始标签和结束标签
>* handle_starttag 处理开始标签，比如 `<xx>`
>* handle_endtag 处理结束标签，比如 `</xx>`
>* handle_comment 处理注释
详细的可以查看 文档




