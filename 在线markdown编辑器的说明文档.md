在线markdown编辑器的说明文档
===



**关于布局**

分为左右两个div 左边是一个ace的编辑器的类型 右边是一个idiv 里面有一个iframe 结构

**关于ace**

详细见 [这里](http://ace.ajax.org/)


**关于左边的样式**

向  var editor = ace.edit("editor"); 这样id为editor的div 就变成一个ace的对象了..修改主题与提取values就变得
十分的简单了

**关于右边的iframe 结构**

这里之所以选择iframe结构的原因是右边的内容是一个动态变化的过程(局部刷新),通过更改 iframe 的 src 的值就可以
使右边从新加载内容

**如何捕获左边div的变化(内容更改与复制动作)**

这里还是使用了 ace 对象的 getSession().on('change', function(e) 方法 刚开始使用onchange 监听事件后来发现
onchange 只能监听写的动作对于复制动作不能捕获到



**获得了内容之后如何把markdown转化为html?**

这里使用了js 库 它的家在[这里](https://github.com/evilstreak/markdown-js)

**获得html源码之后如何显示到右边呢?**

因为需要更改ifram的src 路径

这里想了几个方案..

>* 反映到文本中 加载之后在删除?
>* src 请求ajax请求并把html 源码传递到 后台.后台返回来? 这样子倒是可以但是服务器交互太多.
>* 不经过 修改src 路径的方案直接修改DOM的内容..尝试了几中方案都不行

难道src不能直接加载html 源码吗?  

最后终于在[这里](http://stackoverflow.com/questions/8240101/set-content-of-iframe)找到了答案



    var locals = "content";

    document.getElementById('output_iframe1').src = "data:text/html;charset=utf-8," + escape(LocalS);








































