python 装饰器
==================

概括来讲..装饰器就是为已经存在的对象添加额外的一些功能

>* 装饰器入门

>>* 需求是怎么来的?

    def foo():
        print 'in foo()'     
    foo()

现在需要计算机foo 函数用的时间. 一般来说这可能想到了使用 如下代码

    import time
    def foo():
        start = time.clock()
        print 'in foo()'
        end = time.clock()
        print 'used:', end - start
     
    foo()

如果其他函数也有这个需求呢? 复制? 很可笑....

>>* 以不变应万变


    import time
     
    def foo():
        print 'in foo()'
     
    def timeit(func):
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
     
    timeit(foo)

这样子的一个问题是更改了调用接口.本来是  timeit 方法调用.现在换成了 timeit(foo) 调用方法
如果其它地方也有这个就需要修改其它地方了...

>>* 最大限度地少改动！


    #-*- coding: UTF-8 -*-
    import time
     
    def foo():
        print 'in foo()'
     
    # 定义一个计时器，传入一个，并返回另一个附加了计时功能的方法
    def timeit(func):
         
        # 定义一个内嵌的包装函数，给传入的函数加上计时功能的包装
        def wrapper():
            start = time.clock()
            func()
            end =time.clock()
            print 'used:', end - start
         
        # 将包装后的函数返回
        return wrapper
     
    foo = timeit(foo)
    foo()

上面的最后两行代码也就是体现了装饰器的思想

>* python 的 额外支持

>>* 语法 @ 


    @timeit
    def foo():
        print 'in foo()'

>>* 内置的装饰器

内置的装饰器有三个，分别是staticmethod、classmethod和property，作用分别是把类中定义的实例方法变成静态方法、类方法和类属性。

这里，静态方法，虽然是一个方法，但是a.static_foo只是一个没有绑定任何参数的完好的函数。static_foo需要1个参数，同样a.static_foo也只需要一个参数。


这里有一个很好的链接的关于上面的....
http://www.zeuux.com/blog/content/3030/

















