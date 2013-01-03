JSON
========
__note__:参考[json官网](http://json.org/json-zh.html)

**json常用的两种结构:**

>* 名称/值”对的集合（A collection of name/value pairs）。不同的语言中，它被理解为对象（object），纪录（record），结构（struct），字典（dictionary），哈希表（hash table），有键列表（keyed list），或者关联数组 （associative array）。

>* 值的有序列表（An ordered list of values）。在大部分语言中，它被理解为数组（array）。

*****************************************************

**json常用数据格式**

+ 对象: 
    
>对象是一个无序的“‘名称/值’对”集合。一个对象以“{”（左括号）开始，“}”（右括号）结束。每个“名称”后跟一个“:”（冒号）；“‘名称/值’ 对”之间使用“,”（逗号）分隔。


![object](http://json.org/object.gif)

+ 数组:

>数组是值（value）的有序集合。一个数组以“[”（左中括号）开始，“]”（右中括号）结束。值之间使用“,”（逗号）分隔。

![array](http://json.org/array.gif)


+ 值:
>值（value）可以是双引号括起来的字符串（string）、数值(number)、true、false、 null、对象（object）或者数组（array）。这些结构可以嵌套。

![value](http://json.org/value.gif)

+ 字符串:

>字符串（string）是由双引号包围的任意数量Unicode字符的集合，使用反斜线转义。一个字符（character）即一个单独的字符串（character string）。

![string](http://json.org/string.gif)

*******************************
**python对json的处理**

> * 对简单数据类型的encoding 和 decoding：使用json的dumps方法对python的数据进行编码.也就是把python的数据类型转换成json的数据类型
    
    import json
    obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
    encodedjson = json.dumps(obj)
    print repr(obj)
    print encodedjson

_note_  repr函数与str的区别

以上的输出结果为

    [[1, 2, 3], 123, 123.123, 'abc', {'key2': (4, 5, 6), 'key1': (1, 2, 3)}] 
    [[1, 2, 3], 123, 123.123, "abc", {"key2": [4, 5, 6], "key1": [1, 2, 3]}]

在python的编码过程中会从原始结构向json的结构转化
![](http://images.cnblogs.com/cnblogs_com/coser/201112/201112141621136287.png)

相反的处理过程使用json.loads()函数

![](http://images.cnblogs.com/cnblogs_com/coser/201112/201112141621146178.png)

**json对自定义对象的操作**

> python 数据结构到JSON的转换可以看出 必须把把python的对象转化成可以转化到python的数据格式.当然这里有两种方法可以考虑 一种继承，一种自己定义转化函数
[参考这里](http://huacnlee.com/blog/convert-python-object-to-jason/)

    def obj2dict(obj):
    """
    summary:
        将object转换成dict类型
    """
    memberlist = [m for m in dir(obj)]
    _dict = {}
    for m in memberlist:
        if m[0] != "_" and not callable(m):
            _dict[m] = getattr(obj,m)

    return _dict
    return simplejson.encode(str(obj2dict(self)))


























