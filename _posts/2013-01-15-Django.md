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

Django 提供对全局context的支持 默认情况下 在 TEMPLATE_CONTEXT_PROCESSORS 中设置 例如

	TEMPLATE_CONTEXT_PROCESSORS = (
	    'django.core.context_processors.auth',
	    'django.core.context_processors.debug',
	    'django.core.context_processors.i18n',
	    'django.core.context_processors.media',
	)

几个Django默认启动的简单的Django处理器

_django.core.context_processors.auth_

包含这个TEMPLATE_CONTEXT_PROCESSORS处理器, 每个RequestContext包含的变量为

>* user django.contrib.auth.models.User 实例 描述了当前登陆用户

>* messages 当前登陆用户的消息列表

>* perms 是django.core.context_processors.PermWrapper 的实例 用来描述用户的权限问题

_django.core.context_processors.debug_ 

把调试信息发到模板层,包含的变量

>* debug：设置的DEBUG(settings.py文件中)值,可以再模板中测试是否在测试条件下

>* sql_queries {‘sql’:...,'time':...} 记录请求期间每一个sql查询与其所用时间

_生效的两个条件 1.DEBUG 为true 2.ip必须在INTERNAL_IPS 范围内

_从生效的条件可以看出如果

_django.core.context_processors.request_

这个处理器启动，每个RequestContext将包含request对象,也就是包含当前HttpRequest对象,当然这个默认是不启动的

例如在一个request中调用ip的例子

>* {{ request.REMOTE_ADDR }}

***html自动转义***  

_注意从模板 生成 html时,存在风险 例如  Hello, {{ name }}. 当用户名变量为 <script>alert('hello')</script> 时 模板渲染结果为 Hello, <script>alert('hello')</script> 当然在某些条件下这是很危险的

要避免上面的问题可以有两种方法

>* 可以把每一个不信任的变量都让escape过滤器处理一遍,但这样增加了开发者的问题

>* Django的自动html转意

5个特殊字符的转换

>* < 被转意为 &lt; 
>* > 被转意为 &gt; 
>*　' (single quote) 被转意为 &#39; 
>* " (double quote) 被转意为 &quot; 
>* & 被转意为 &amp;

上面默认是开启的，_ 关闭他们默认的方法_

_对于变量_

>* This will be escaped: {{ data }}
>* This will not be escaped: {{ data|safe }}

_对于模板块_

对于模板的自动转换,可以用标签autoescape 来包装，并通过开关 on 或者off来控制

	Auto-escaping is on by default. Hello {{ name }}

	{% autoescape off %}
    This will not be auto-escaped: {{ data }}.

    Nor this: {{ other_data }}
    {% autoescape on %}
        Auto-escaping applies again: {{ name }}
    {% endautoescape %}
	{% endautoescape %}

***模块加载***

常见两种方式

>* django.template.loader.get_template(template_name) 
>* django.template.loader.select_template(template_name_list) 


分别以列表与路径名方式加载,在内部上面使用模板加载器来完成任务。一些模板加载器默认是禁止的需要手动开启,通过编辑TEMPLATE_LOADERS 来开启它们

>* django.template.loaders.filesystem.load_template_source  这个加载器根据 TEMPLATE_DIRS 的设置从文件系统加载模板 并且默认是可用的
>* django.template.loaders.app_directories.load_template_source 这个加载器从INSTALLED_APPS 每个模板应用中查找templates 子目录,Django在那里寻找模板

例如如果INSTALLED_APPS 包含 ('myproject.polls','myproject.music'),那么get_template('foo.html')那如下顺序查找

>* /path/to/myproject/polls/templates/foo.html
>* /path/to/myproject/music/templates/foo.html

**扩展模板系统** 

注意模板系统还有很多内容

_ps. 未完成待续

==========================================
**模板高级进阶**
======================================
**通用视图**

django 内建通用视图可以实现如下功能

>* 　完成简单的任务,例如重定向到一个页面及渲染一个指定的模板
>* 　显示对象或列表的相信信息
>*　 基于日期年月的归档

_使用通用视图_

	from django.conf.urls.defaults import *
	from django.views.generic.simple import direct_to_template
	
	urlpatterns = patterns('',
	    (r'^about/$', direct_to_template, {
	        'template': 'about.html'
	    })
	)

当然我们还可以重用通用视图

	from django.conf.urls.defaults import *
	from django.views.generic.simple import direct_to_template
	**from mysite.books.views import about_pages**
	
	urlpatterns = patterns('',
	    (r'^about/$', direct_to_template, {
	        'template': 'about.html'
	    }),
	    (r'^about/(\w+)/$', about_pages),
	)

对于我们的about_pages 视图函数中使用direct_to_template视图(当然也就是函数)

	from django.http import Http404
	from django.template import TemplateDoesNotExist
	from django.views.generic.simple import direct_to_template
	
	def about_pages(request, page):
	    try:
	        return direct_to_template(request, template="about/%s.html" % page)
	    except TemplateDoesNotExist:
	        raise Http404()

_对象的通用视图_

_note:django通用视图最有用的地方是呈现数据库中的数据

例如需要显示所有的出版商(查询数据库中出版商Publisher 表的所有元素)

对于数据库出版商这个model对应的 python代码为

	class Publisher(models.Model):
	    name = models.CharField(max_length=30)
	    address = models.CharField(max_length=50)
	    city = models.CharField(max_length=60)
	    state_province = models.CharField(max_length=30)
	    country = models.CharField(max_length=50)
	    website = models.URLField()
	
	    def __unicode__(self):
	        return self.name
	
	    class Meta:
	        ordering = ['name']

对应的url写法为

	from django.conf.urls.defaults import *
	from django.views.generic import list_detail
	from mysite.books.models import Publisher
	
	publisher_info = {
	    'queryset': Publisher.objects.all(),
	    'template_name': 'publisher_list_page.html',
	}
	
	urlpatterns = patterns('',
	    (r'^publishers/$', list_detail.object_list, publisher_info)
	)

_主要在这里面当publisher_info 中没有template_name 时默认请求的模板名称为books/publisher_list.html  方法为app名称/publisher_info.html_

publisher_list_page.html 模板为

	{% extends "base.html" %}
	
	{% block content %}
	    <h2>Publishers</h2>
	    <ul>
	        {% for publisher in object_list %}
	            <li>{{ publisher.name }}</li>
	        {% endfor %}
	    </ul>
	{% endblock %}

注意这里的base.html 模板

***扩展通用视图***

_note publisher_info  把template_object_name 加入会是一个好的方法

	publisher_info = {
	    'queryset': Publisher.objects.all(),
	    'template_name': 'publisher_list_page.html',
	    'template_object_name': 'publisher',
	}

***添加额外的Context***

所有的通用视图都有一个额外的可选参数 extra_context 

	publisher_info = {
	    'queryset': Publisher.objects.all(),
	    'template_object_name': 'publisher',
	    'extra_context': {'book_list': Book.objects.all()}
	}

***显示对象的子集***

例如需要显示的对象按日期排序

大多数通用视图有一个queryset参数，这个参数告诉视图要显示对象的集合

	book_info = {
	    'queryset': Book.objects.order_by('-publication_date'),
	}

***用函数包装来处理复杂的数据过滤***

***处理额外工作***

====================================

**部署Django**

***关闭Debug模式***

默认情况下使用django-admin.py startproject 创建项目时 settings.py 文件的DEBUG设置为true 注意在这种模式下Django的行为

>* 所有的数据库查询都被保存在内存中 以 django.db.connection.queries 的形式 所有这种行为是很消耗内存的

>* 404错误页面的不同，当然调试错误与发布错误是不同的

>* 应用程序没有捕获任何错误信息

***关闭模板Debug模式***

TEMPLATE_DEBUGFalse 设置为True,这是为了在上面的django错误页显示更多的模板信息

_note:听说在最近 版本已经将TEMPLATE_DEBUGFalse=DEBUG 恩，这确实是个不错的想法

***实现一个模板404错误页***

_如果Debug设置为"TRUE"，显示自带的404调试错误页。如果Debug设置为"FALSE",则Django会在模板根目录中显示"404.html"模板

***实现一个500模板***

_此处描述与上面相同

***设置错误警告***

当发生错误时发送信息(邮件)到开发团队,当然需要两个条件

>* 改变你的ADMINS设置用来引入你的E-mail地址
>* 确保服务器配置了发送电子邮件

***设置连接中断警报***


***使用针对产品的不同的设置***

这里考虑可以使用3种方法

>* 设置成两个全面的，彼此独立的配置文件

>* 设置一个基本的配置文件，另一个从前一个导入其变量的设置

	# settings_production.py	
	from settings import *

>* 使用一个单独的配置文件，此配置文件包含一个Python的逻辑判断根据上下文环境改变设置。

	import socket
	
	if socket.gethostname() == 'my-laptop':
	    DEBUG = TEMPLATE_DEBUG = True
	else:
	    DEBUG = TEMPLATE_DEBUG = False

***重命名settings.py***

通过修改manage.py 文件，将 import settings 语句改为导入你自己的模块.DJANGO_SETTINGS_MODULE指向你的配置文件，在你的配置文件中指向你的ROOT_URLCONF,在ROOT_URLCONF中指向了你的视图以及其他的部分。


***apache与mod_python 部署Django***

mod_python 是一个再apahce中运行python的组件

_基本配置

***一种替代方案： mod_wsgi模块***

***使用FastCGI部署Django应用***

***FastCGI 简介***

和mod_python一样FastCGI也是贮存在内存中的cgi,但是与其它相比省掉了每一次启动的开销问题,与mod_python 不同的是它不是作为apache的一部分作为同一进程启动的，
而是有自己的独立进程.

_note：当然这样的好处是不用作为免去了加载apache其它特性的东西,它仅仅把Python和Django等必备的东东弄到内存中

_note：当然apache与FastCGI通信当然有两种方法1.Unix domain socket方法。2.TCP socket通信

开始服务器项目,进入项目目录下

	./manage.py runfcgi [options]
	
在TCP端口上运行一个线程服务器
	
	./manage.py runfcgi method=threaded host=127.0.0.1 port=3033

在Unix socket上运行prefork服务器：

	/manage.py runfcgi method=prefork socket=/home/user/mysite.sock pidfile=django.pid

***在Apache中以FastCGI的方式使用Django***

_note:需要配置httpd.conf来让Apache和Django FastCGI互相通信，当然apache需要mod_fastcgi模块的支持

>* 使用 FastCGIExternalServer 指明FastCGI的位置

例如

	# Connect to FastCGI via a socket/named pipe:
	FastCGIExternalServer /home/user/public_html/mysite.fcgi -socket /home/user/mysite.sock
	
	# Connect to FastCGI via a TCP host/port:
	FastCGIExternalServer /home/user/public_html/mysite.fcgi -host 127.0.0.1:3033



>* 使用 mod_rewrite 为FastCGI指定合适的URL。

这个需要告诉server那些url需要转换给Django来处理 使用mod_rewrite 模块，并将这些URL重定向到 mysite.fcgi

	<VirtualHost 12.34.56.78>
	  ServerName example.com
	  DocumentRoot /home/user/public_html
	  Alias /media /home/user/python/django/contrib/admin/media
	  RewriteEngine On
	  RewriteRule ^/(media.*)$ /$1 [QSA,L]
	  RewriteCond %{REQUEST_FILENAME} !-f
	  RewriteRule ^/(.*)$ /mysite.fcgi/$1 [QSA,L]
	</VirtualHost>
	
***FastCGI 和 lighttpd***

_note 是一个轻量级的Web服务器，通常被用来提供静态页面的访问。 它天生支持FastCGI，因此除非你的站点需要一些Apache特有的特性，否则，lighttpd对于静态和动态页面来说都是理想的选择。

***在一个lighttpd进程中运行多个Django站点***

未完待续

==============================================
**输出非html内容**

当然web发布数据不仅仅是 html,还有RSS、PDF、图片等

Django内建的工具生成非HTML内容

>* RSS聚合内容

>* 站点地图

***基础:视图和MIME类型***

一个Django视图函数必须要含有

>* 接收一个httprequest作为第一个参数

>* 返回一个httpresponse 实例

从一个视图返回一个非html最主要的是构造一个httpresponse实例，需要指定mimetype参数。通过改变mimetype参数浏览器可以知道访问的资源类型

	from django.http import HttpResponse
	
	def my_image(request):
	    image_data = open("/path/to/my/image.png", "rb").read()
	    return HttpResponse(image_data, mimetype="image/png")

***生成 CSV 文件***

因为 csv 模块操作的是类似文件的对象，所以可以使用 HttpResponse 替换：

	import csv
	from django.http import HttpResponse
	
	# Number of unruly passengers each year 1995 - 2005. In a real application
	# this would likely come from a database or some other back-end data store.
	UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]
	
	def unruly_passengers_csv(request):
	    # Create the HttpResponse object with the appropriate CSV header.
	    response = HttpResponse(mimetype='text/csv')
	    response['Content-Disposition'] = 'attachment; filename=unruly.csv'
	
	    # Create the CSV writer using the HttpResponse as the "file."
	    writer = csv.writer(response)
	    writer.writerow(['Year', 'Unruly Airline Passengers'])
	    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
	        writer.writerow([year, num])
	
	    return response

_注意附加的 Content-Disposition 头部,这个会指示浏览器在保存文件的时候询问保存的位置

***生成 PDF 文件***

_编写视图

	from reportlab.pdfgen import canvas
	from django.http import HttpResponse
	
	def hello_pdf(request):
	    # Create the HttpResponse object with the appropriate PDF headers.
	    response = HttpResponse(mimetype='application/pdf')
	    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
	
	    # Create the PDF object, using the response object as its "file."
	    p = canvas.Canvas(response)
	
	    # Draw things on the PDF. Here's where the PDF generation happens.
	    # See the ReportLab documentation for the full list of functionality.
	    p.drawString(100, 100, "Hello world.")
	
	    # Close the PDF object cleanly, and we're done.
	    p.showPage()
	    p.save()
	    return response

***内容聚合器应用框架***

**未完**

***************

**会话、用户和注册**

_note:http 被设计成"无状态的"，即每一次的链接都是处于相同的空间中的,我们无法从请求的任何方便来判断是不是同一个人的连接

***cookies***

cookies 是浏览器为 Web 服务器存储的一小段信息,每次浏览器从服务器请求页面时，它都向服务器回送之前收到的cookies

***存取Cookies***

在处理持久化,一般都会使用session或者user框架，这里主要了解底层如何读写cookies

读取cookies 很简单,每一个httprequest都有一个cookies对象,其操作类似字典形式

	request.COOKIES["favorite_color"]

写cookies可以使用 HttpResponse对象的 set_cookie()方法.

	response.set_cookie("favorite_color",request.GET["favorite_color"])

一般还可以设置的 max_age、expires、path、domain 等

***好坏参半的Cookies***

>* cookies的存取是自愿的,可以选择控制是否存储
>* cookies 是不可靠的
>* http是以明文发送的,也就是说cookies是不安全的

***django的session框架***

session通过一个中间件和一个模型来实现的

_打开 Sessions功能_

>* MIDDLEWARE_CLASSES 包含django.contrib.sessions.middleware.SessionMiddleware
>* INSTALLED_APPS含有django.contrib.sessions

_在视图中使用session_

SessionMiddleware 激活后,每一个httprequest都含有一个session属性,当然这是一个字典型的对象

	# Set a session value:
	request.session["fav_color"] = "blue"
	
	# Get a session value -- this could be called in a different view,
	# or many requests later (or both):
	fav_color = request.session["fav_color"]

使用Django sessions的简单规则：

>* session 字典中以下划线开头的key值是Django内部保留的key值
>* 不要用一个新的对象来替换掉request.session,也不要存取其属性。

	request.session = some_other_object # Don't do this!
	request.session.foo = 'bar' # Don't do this!

***设置测试Cookies***

并不是所有的浏览器都支持cookies,所以需要测试

Django中的验证方法为:

	request.session.test_cookie_worked()

检查cookie是否可以正常工作后，你得自己用 delete_test_cookie() 来清除它

***在视图外使用session***

	>>> from django.contrib.sessions.models import Session
	>>> s = Session.objects.get(pk='2b1189a188b44ad18c35e113ac6ceead')
	>>> s.expire_date
	datetime.datetime(2005, 8, 20, 13, 35, 12)

_note: 现在版本的django的session里面 包含的字段session_key, session_data, expire_date

可以使用get_decoded() 来读取实际的session数据

	>>> s.session_data
	'KGRwMQpTJ19hdXRoX3VzZXJfaWQnCnAyCkkxCnMuMTExY2ZjODI2Yj...'
	>>> s.get_decoded()
	{'user_id': 42}

***何时保存Session***

默认情况下,django只在session发生变化的时候才会存入数据库.比如说，字典赋值或删除。
当然可以使用SESSION_SAVE_EVERY_REQUEST 这一字段来改变这一默认行为。即当每一次请求都保存数据库


***浏览器关闭即失效会话 vs 持久会话***


cookie中的expires设置过期时间,默认情况下如果没有设置过期时间当用户关闭浏览器的时候，cookie就自动过期了。你可以改变 SESSION_EXPIRE_AT_BROWSER_CLOSE 的设置来控制session框架的这一行为。
如果SESSION_EXPIRE_AT_BROWSER_CLOSE 为false，则会话的cookies将会保持SESSION_COOKIE_AGE 秒的时间

***其他的Session设置***

这个可以参考源代码

***用户与Authentication***

通过session我们可以再多次浏览请求中保持数据,当然最常用的还是用session还处理用户登录的问题了。

django中的认证与授权系统 auth/auth 一般步骤如下

>* 验证 (认证) 用户是否是他所宣称的用户(一般通过查询数据库验证其用户名和密码)
>* 验证用户是否拥有执行某种操作的 授权 (通常会通过检查一个权限表来确认)

django 认证与授权系统包含如下

>* 用户 : 在网站注册的人
>* 权限 : 用于标识用户是否可以执行某种操作的二进制(yes/no)标志
>* 组 :一种可以将标记和权限应用于多个用户的常用方法               
>* Messages向用户显示队列式的系统消息的常用方法     

***打开认证支持***     

session 也是一个Django的应用,放在 django.contrib 中

>* 需要确保用户使用cookies
>* django.contrib.auth 需要在INSTALLED_APPS 中,并且 manage.py syncdb以创建对应的数据库表
>* 'django.contrib.auth.middleware.AuthenticationMiddleware' 确认在SessionMiddleware 

安装好之后就可以在view视图函数中使用user了，视图中存取users，主要用 request.user ,这个表示已经登录的用户.对于没有登录的用户默认为AnonymousUser对象

你可以很容易地通过 is_authenticated() 方法来判断一个用户是否已经登录了：

	if request.user.is_authenticated():
    # Do something for authenticated users.
	else:
    # Do something for anonymous users.
                        
***使用User对象***

User 实例一般从 request.user 它包含许多属性与方法,这里需要注意AnonymousUser对象并不是都包含这些方法.


表 14-3. User 对象属性

属性	描述

username	必需的，不能多于30个字符。 仅用字母数字式字符（字母、数字和下划线）。

first_name	可选; 少于等于30字符。

last_name	可选; 少于等于30字符。

email	可选。 邮件地址。

password	必需的。 密码的哈希值（Django不储存原始密码）。 See the Passwords section for more about this value.

is_staff	布尔值。 用户是否拥有网站的管理权限。

is_active	布尔值. 设置该账户是否可以登录。 把该标志位置为False而不是直接删除账户。

is_superuser	布尔值 标识用户是否拥有所有权限，无需显式地权限分配定义。

last_login	用户上次登录的时间日期。 它被默认设置为当前的日期/时间。

date_joined	账号被创建的日期时间 当账号被创建时，它被默认设置为当前的日期/时间。


***登录和退出***

django提供内置的视图用于处理登录和退出。当然可以手工登录与退出.
django提供两个函数用来执行验证用户身份与登录 authenticate() 和 login() 函数

	>>> from django.contrib import auth
	>>> user = auth.authenticate(username='john', password='secret')
	>>> if user is not None:
	...     print "Correct!"
	... else:
	...     print "Invalid password."

	from django.contrib import auth
	
	def login_view(request):
	    username = request.POST.get('username', '')
	    password = request.POST.get('password', '')
	    user = auth.authenticate(username=username, password=password)
	    if user is not None and user.is_active:
	        # Correct password, and the user is marked "active"
	        auth.login(request, user)
	        # Redirect to a success page.
	        return HttpResponseRedirect("/account/loggedin/")
	    else:
	        # Show an error page
	        return HttpResponseRedirect("/account/invalid/")

上面演示了如何使用authenticate() 和 login() 函数

注销一个用户

	from django.contrib import auth
	def logout_view(request):
	    auth.logout(request)
	    # Redirect to a success page.
	    return HttpResponseRedirect("/account/loggedout/")

*注意:这里需要注意即使用户没有登录logout也不会返回异常

当然在实际中一般不需要用户自己写登录/登出的函数. 使用其的第一步是写urlConf函数

	from django.contrib.auth.views import login, logout
	
	urlpatterns = patterns('',
	    # existing patterns here...
	    (r'^accounts/login/$',  login),
	    (r'^accounts/logout/$', logout),
	)

/accounts/login/ 和 /accounts/logout/ 是Django提供的视图的默认URL。

login 视图渲染 registragiton/login.html 模板

logout视图有一些不同。 默认情况下它渲染 registration/logged_out.html 模板

***限制已登录用户的访问***

控制用户登录后访问的站点的某些部分

***对通过测试的用户限制访问***

限制访问可以基于某种权限，某些检查或者为login视图提供不同的位置

一种方法是直接在用户的request.user 上检查 例如

	def vote(request):
	    if request.user.is_authenticated() and request.user.has_perm('polls.can_vote')):
	        # vote here
	    else:
	        return HttpResponse("You can't vote in this poll.")

	        
	def user_can_vote(user):
	    return user.is_authenticated() and user.has_perm("polls.can_vote")
	
	@user_passes_test(user_can_vote, login_url="/login/")
	def vote(request):
	    # Code here can assume a logged-in user with the correct permission.
	    
	from django.contrib.auth.decorators import permission_required
	
	@permission_required('polls.can_vote', login_url="/login/")
	def vote(request):
	    # ...
	        
***限制通用视图的访问***


***管理 Users, Permissions 和 Groups***

一般通过admin就可以了.这里的粒度比较细

_创建用户_

	>>> from django.contrib.auth.models import User
	>>> user = User.objects.create_user(username='john',
	...                                 email='jlennon@beatles.com',
	...                                 password='glass onion')

	>>> user.is_staff = True
	>>> user.save()

_修改密码_

使用 set_password() 来修改密码：当然这一般是不直接编辑的,因为里面存储的是加入salt的hash值.

	>>> user = User.objects.get(username='john')
	>>> user.set_password('goo goo goo joob')
	>>> user.save()

_处理注册_


***在模板中使用认证数据***
***权限、组和消息***

_权限_

_组_

_消息_

当然未完待续
**********************
