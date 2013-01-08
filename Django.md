Django
=====
**视图与url配置**

一个视图就是一个python的函数,并且必须满足两个条件

> * 函数的第一个类型必须是HttpRequest

> * 它返回一个HttpResponse实例

**urlconf**

urlconf 就是 Django所支撑的网站的目录结构,它的本质就是url结构,以及与该url结构相映射的视图,我们就是以这种方式告诉Django,对于哪个url调用哪个Django视图
> 当开始执行 
    
    django-admin.py startproject

脚本会自动创建一份 urlconf(默认文件为 urls.py)

> 默认的urls.py的内容为 (1, 3, 4, 'final', 0)

    from django.conf.urls.defaults import patterns, include, url
    from mysite.views import *
    # Uncomment the next two lines to enable the admin:
    # from django.contrib import admin
    # admin.autodiscover()

    urlpatterns = patterns('',
        # Examples:
        # url(r'^$', 'mysite.views.home', name='home'),
        # url(r'^mysite/', include('mysite.foo.urls')),

        # Uncomment the admin/doc line below to enable admin documentation:
        # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

        # Uncomment the next line to enable the admin:
        # url(r'^admin/', include(admin.site.urls)),
    )

*note* python 的搜索路径
    
    import sys
    print sys.path
    ['', '/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg', '/usr/lib/python2.6/site-packages/pexpect-2.4-py2.6.egg', '/usr/lib64/python26.zip', '/usr/lib64/python2.6', '/usr/lib64/python2.6/plat-linux2', '/usr/lib64/python2.6/lib-tk', '/usr/lib64/python2.6/lib-old', '/usr/lib64/python2.6/lib-dynload', '/usr/lib64/python2.6/site-packages', '/usr/lib64/python2.6/site-packages/PIL', '/usr/lib64/python2.6/site-packages/gst-0.10', '/usr/lib64/python2.6/site-packages/gtk-2.0', '/usr/lib64/python2.6/site-packages/webkit-1.0', '/usr/lib/python2.6/site-packages', '/usr/lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg-info']

    注意第一个空字符串表示在当前路径下寻找

**URLpattern**

> 任何在匹配URLpattern的请求之前需要去掉之前的"/" 字符.这意味着我们为/hello/写URL模式不用包含斜杠(/) 关于这点的好处此刻还不是很清楚 例如内嵌等后续补充

> 关于尾部/ 的处理 默认地，任何不匹配或尾部没有斜杠(/)的申请URL，将被重定向至尾部包含斜杠的相同字眼的URL 注意这是受到setting中APPEND_SLASH项控制



_如果你让它一直运行也可以，开发服务器会自动监测代码改动并自动重新载入，所以不需要手工重启_

_关于网站根目录:默认情况下输入http://127.0.0.1:8000/ 将获得一个404 错误 因为Djingo默认不会把根目录当做特殊处理 ，需要特殊处理必须使用 URLpattern 匹配它,例如 ('^$', myhomepath)_

_Django 处理请求过程_ 

_note_ 关注settings.py 文件 这个文件包含了所有有关这个Django项目的配置信息,均大写： TEMPLATE_DIRS , DATABASE_NAME , 等. 最重要的设置时ROOT_URLCONF，它将作为URLconf告诉Django在这个站点中那些Python的模块将被用到
    
_Django的时区 在setting文件中 且默认为America/Chicago_

_当然在urlconf中可以考虑正则捕获,捕获的值依次(从第二个参数开始第一个参数是httprequest的实例)传入视图_

**Django 模板**

>* include 模板标签

>* 模板继承 大多数情况下 include 与 模板继承 可以互相使用 

>* 模板是一个文本,用于分离其表现方式,模板定义了占位符与规范文档该如何显示,模板通常用来产生html文档，当然也可以产生其它文档

>* 模板标签 通知模板系统完成某些工作的标签
例如 if 标签 {% if ordered_warranty %}  for 标签 {% for item in item_list %} 

>* 模板变量 例如 {{ person_name }}

>* 过滤器  例如 {{shipdate|date:”F j, Y” }}  将变量shipdate传递给date过滤器，同时指定参数”F j,Y”。date过滤器根据参数进行格式输出。 过滤器是用管道符(|)来调用的

>* 模板系统是一个Python库，你可以在任何地方使用它，而不仅仅是在Django视图中

**在python中使用模板的方法**
>* 创建一个模板对象 包括使用字符串与文件的方式创建
>* 调用模板对象的render方法,并且传入一套变量context

    from django import template
    t = template.Template('My name is {{ name }}.')
    c = template.Context({'name': 'Adrian'})
    print t.render(c)
    My name is Adrian.
    c = template.Context({'name': 'Fred'})
    print t.render(c)
    My name is Fred.

分布介绍

**创建模板对象**

直接实例化模板对象

**模板渲染**

一旦你创建一个 Template 对象，你可以用 context 来传递数据给它。 一个context是一系列变量和它们值的集合。

content 在django里面是Context 类 在Template模块里面 构造函数里面是一个可选的字典参数,在字典里面传入需要渲染的变量与值  调用 Template 对象 的 render() 方法并传递context来填充模板：

**注意render方法返回一个unicode**

使用template模板的基本步骤为：写模板，创建 Template 对象，创建 Context ， 调用 render() 方法。

**同一个模板多个上下文**
一旦有了模板对象，就可以使用它创建多个上下文
**注意进行一次模板创建调用多次rendor的方法比较高效**


***理念与局限***

_可以再djaogo中使用其它模板语言_

***在视图中使用模板***

***模板加载***
_note Django采用模板自加载与模板目录_
> 模板加载目录 在 settings.py 文件中的TEMPLATE_DIRS 字段下配置需要注意当只有一个的时候不要忘了加末尾的逗号

> 在视图中引入模块 使用此方法django.template.loader.get_template() 并且已文件名为参数 当使用子目录的时候 这种方式 t = get_template('dateapp/current_datetime.html') 很好

> 使用render_to_response 简化 编写 例如 return render_to_response('current_datetime.html', {'current_date': now})  直接把模块 渲染 与返回 放到一个函数中完成  注意需要 from django.shortcuts import render_to_response 才可以

************************
**模型**

***Django的mvc模型***
> * m 数据存储模式 由Django 数据库层处理
> * v 主要由模板处理 
> * c 根据用户urlconf 配置 也就是python函数


***数据库配置***

settings.py 中查找如下

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2',     'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/home/mydb',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

_note 注意： 个人比较喜欢 mysql 与 sqlite3_

测试数据库连接
    
    from django.db import connection
    cursor = connection.cursor()
    
_note 注意区分project于app的区别 这里讲一个是配置一个是代码或许有些道理_

***********************
Django



***********

**Django表单**

***Request对象中获取数据***
在一个视图函数里面第一个参数一般是HttpRequest对象,当然我们可以从这个函数中获得我们感兴趣的东西.例如 用户与浏览器的信息等

_url相关的信息__

属性/方法    说明	举例
request.path	除域名以外的请求路径，以正斜杠开头	"/hello/"

request.get_host()	主机名（比如，通常所说的域名）	"127.0.0.1:8000" or "www.example.com"

request.get_full_path()	请求路径，可能包含查询字符串	"/hello/?print=true"

request.is_secure()	如果通过HTTPS访问，则此方法返回True， 否则返回False	True 或者 False

_与Request相关的一些其它信息_

_请求头信息_

request.META 这个是python的dict数据格式 包括本次HTTP请求的Header信息 常见的如用户的ag(user-agent)信息

_note 这里需要当访问的信息不存在时会发生错误_


***关于提交的数据***

HttpRequest对象还包括另外两个属性 request.GET 和 request.POST 注意它们两个都是类字典对象 

_note 类字典对象 可以理解为包含比字典跟多的方法 例如可以使用 for key in request.GET 获取所有的键 这里要强调request.GET 与 request.POST 包含比字典更多的 方法

从前台html获得表单提交(get)的方法

     if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']

继承django的form类 

名称 django.forms 类,目的是为每一个要处理的html的form表单创建一个Form类,最好的处理方式是单独创建一个文件

Form 类可以认为做了 
> * 转化为html
> * 校验合理性
> * 清理数据 即将数据转换为python数据类型

    >>> f = ContactForm({'subject': 'Hello', 'message': ''})
    >>> f.errors
    {'message': [u'This field is required.']}

***改变字段显示***

***设置最大字段长度***

***设置初始值***

***自定义校验规则***

例如反馈页面 字数要求 这里主要有两种方法 1. 自定义字段类型 2. 直接挂在form类 上


*Django的form系统自动寻找匹配的函数方法，该方法名称以clean_开头，并以字段名称结束。 如果有这样的方法，它将在校验时被调用.*

_注意自定义的校验规则一般在最后,当然这也是很合理的,省去了不少麻烦

***指定标签***
html生成的表单的标签是按默认规则生成的 例如 用空格代替下划线，首字母大写 当然这也是可以自定义的
    email = forms.EmailField(required=False, **label='Your e-mail address'** )

******************************

**高级视图与url配置**

***URLconf 技巧***



***使用命名组***

_注意关键字参数与位置参数_

_可以混合使用关键字参数与位置参数

python的正则表达式中使用,命名的正则表达式的语法是(?P<name>pattern) name 是组的模式 pattern是正则模式

在django中的使用

		from django.conf.urls.defaults import *
		from mysite import views
		
		urlpatterns = patterns('',
		    (r'^articles/(?P<year>\d{4})/$', views.year_archive),
		    (r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.month_archive),
		)

在这里 传到视图中的参数将不再是位置参数而是关键字参数并且名字是year


***理解匹配/分组算法***


***传递额外的参数到视图函数中***

写法

	urlpatterns = patterns('',
    (r'^foo/$', views.foobar_view, {'template_name': 'template1.html'}),
    (r'^bar/$', views.foobar_view, {'template_name': 'template2.html'}),
	)
	
在这个例子中指定了 	template_name 这个参数 并且确定了其值为template1.html

__这种使用额外的URLconf参数的技术以最小的代价给你提供了向视图函数传递额外信息的一个好方法

***伪造捕捉到的URLconf值***

例子

	urlpatterns = patterns('',
    (r'^mydata/birthday/$', views.my_view, {'month': 'jan', 'day': '06'}),
    (r'^mydata/(?P<month>\w{3})/(?P<day>\d\d)/$', views.my_view),
	)
	
上面这种用法很巧妙

***创建一个通用视图***	
	
***提供视图配置选项***	

***了解捕捉值和额外参数之间的优先级 额外的选项***

_note:额外URLconf参数优先于捕捉值_

	urlpatterns = patterns('',
    (r'^mydata/(?P<id>\d+)/$', views.my_view, {'id': 3}),
	)
	
任何 这种 /mydata/2/ 或者 /mydata/432432/ 都会捕获为id=3

***使用缺省视图参数***

给一个视图参数指定默认的值

	urlpatterns = patterns('',
	    (r'^blog/$', views.page),
	    (r'^blog/page(?P<num>\d+)/$', views.page),
	)
	
	# views.py
	
	def page(request, num='1'):
	    # Output the appropriate page of blog entries, according to num.
	    # ...

可以使用上面的技术做到缺省默认参数的效果

***从URL中捕获文本***

_note:每个被捕获的参数都将作为python的字符串参数来传递,而不管其捕获的类型

***URLconf搜索的东西***

默认情况下的搜索为http://www.example.com/myapp/ 的请求 Django试着从myapp/ 开始匹配
http://www.example.com/myapp/?page=3 的请求中,Django同样会去匹配 myapp/

所以对于不同的请求(POST,GET,HEAD),区分要在视图函数中区分

	from django.http import Http404, HttpResponseRedirect
	from django.shortcuts import render_to_response
	
	def method_splitter(request, GET=None, POST=None):
	    if request.method == 'GET' and GET is not None:
	        return GET(request)
	    elif request.method == 'POST' and POST is not None:
	        return POST(request)
	    raise Http404
	
	def some_page_get(request):
	    assert request.method == 'GET'
	    do_something_for_get()
	    return render_to_response('page.html')
	
	def some_page_post(request):
	    assert request.method == 'POST'
	    do_something_for_post()
	    return HttpResponseRedirect('/someurl/')
	
	# urls.py
	
	from django.conf.urls.defaults import *
	from mysite import views
	
	urlpatterns = patterns('',
	    # ...
	    (r'^somepage/$', views.method_splitter, {'GET': views.some_page_get, 'POST': views.some_page_post}),
	    # ...

上面处理方法还是十分优雅的

当上面的GET 与 POST 参数较多的时候需要使用变量传参方法

例如：
	def method_splitter(request, *args, **kwargs):
    get_view = kwargs.pop('GET', None)
    post_view = kwargs.pop('POST', None)
    if request.method == 'GET' and get_view is not None:
        return get_view(request, *args, **kwargs)
    elif request.method == 'POST' and post_view is not None:
        return post_view(request, *args, **kwargs)
    raise Http404	
	
foo(1, 2, name='Adrian', framework='Django')
其中args 取例如(1,2) kwargs 取 {'framework': 'Django', 'name': 'Adrian'}

***包装视图函数***

这里举例如登陆认证 需要在每一个视图里面都进行验证

**包含其他URLconf**

语法：(r'^weblog/', include('mysite.blog.urls')),

遇到include 将匹配剩下的字符发往include包含的Urlconf 继续匹配
此处体现了模块化方式的一种

***额外的URLconf如何和include()协同工作***

这里需要说明一点 被捕获的参数一样，将要被传递到include里面的每一样而不管其需不需要。

**********************

**模板高级进阶**

_note: 可以单独讲模板系统应用于其它程序_

***模板标签回顾***

模板是纯文本文件,主要包括两部分 模板标签与变量

{{ first_name }}--变量   模板标签-->{% if is_logged_in %}

__模板渲染:通过content获取值来替换模板中的变量***并执行模板标签***__

***RequestContext和Context处理器***

context 是django.template.Context 的实例,RequestContext是context的子类。RequestContext 在模板中默认加入了一些变量,

例如:RequestContext(request, {'message': 'I am the second view.'},processors=[custom_proc]) 默认processors参数



























