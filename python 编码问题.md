
>* python 安装时默认的编码方式 为 ascii方式

    >>> print sys.getdefaultencoding()
    ascii

>* 修改默认编码方式 
    reload(sys)
    sys.setdefaultencoding('utf8')

注意这里的 reload(sys) 的问题  详细见[这里](https://groups.google.com/forum/?fromgroups=#!topic/comp.lang.python/hUsco3ZvR2s)

>* 常见的两种编码方式

    >>> "汉字".__class__
    <type 'str'>
    >>> 
    >>> u"汉字".__class__
    <type 'unicode'>
    >>> 

str 与 unicode 有什么区别呢？?

>*  "你好".encode("utf8") 错误的分析

>>> "你好".encode("utf8")

    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)

更完整的关于这个的错误解释见[这里](http://stackoverflow.com/questions/9644099/python-ascii-codec-cant-decode-byte)

>* 关于 decode 方法 的使用

    >>> "汉字".decode()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 0: ordinal not in range(128)
    >>> 

decode 默认会把 "汉字" 转化为 系统编码(因为默认为ascii所以上述会出错)，验证可以更改系统
编码之后在测试上面的

    >>> import sys
    >>> sys.getdefaultencoding()
    'ascii'
    >>> 
    >>> reload(sys)
    <module 'sys' (built-in)>
    >>> sys.setdefaultencoding('utf8') 
    >>> "汉字".decode()
    u'\u6c49\u5b57'
    >>> 

如果不想这样子可以直接 "汉字".decode("utf8") 这样子编码

>* 关于编码转换

一般转换思路为 A编码--》系统编码(Asci或者unicode)--》B编码

因为系统默认编码方式一般是 Ascii所以 对于A编码能不能转化为 ASCII 为关键。而我们知道
编码问题的大多数错误都是在这里出粗了

例如  "你好".encode("utf8")

按上述转换思路可以看出 "你好".decode().encode("utf8")

"你好" 的编码有外部文本环境决定 例如 # -*- coding: utf-8 -*-  则 编码为 utf8
而此时系统编码为 默认的ASCii  所以第一步 utf8--》 ASii 编码 肯定会错误的。。

这里写了一个通用的转换代码

    #!/usr/bin/env python 
    #coding=utf-8 
    s="中文" 
    if isinstance(s, unicode):  
    print s.encode('gb2312') 
    else: 
    print s.decode('utf-8').encode('gb2312')

这里编码已gb2321 为例子


