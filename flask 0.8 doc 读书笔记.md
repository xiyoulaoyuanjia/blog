flask 0.8 doc 读书笔记
===
[原文](https://dormousehole.readthedocs.org/en/latest/index.html)

******
**快速上手**

>* 关于app = Flask(__name__)
这句代码 这样子是为了区分一般模块调用与程序开始执行区别

>* 默认情况下只可以本地访问 如果需要网络上的其它人访问可以  app.run(host='0.0.0.0')

>* 默认的开启调试的方法有 app.debug=true 或者 app.run(debug=true) 两种 

>* 开启调试的好处有 
>>* 错误会出更多的调试信息
>>* 有文件修改时会自动重新启动

>* 在url中添加变量

>>*  一般添加变量

    @app.route('/user/<username>')
    def show_user_profile(username):
        # show the user profile for that user
        pass

>>* 添加转换器 这部分还用的不多奥

>* 尾部有 斜杠  与没有的区别

当尾部有"/"则当你访问/projects 会重定向到 "/projects"

    @app.route('/projects/')
    def projects():
        pass
    
    @app.route('/about')
    def about():
        pass

>* url 构建

这里需要理解两点
>>* url_for 的用法 与我之前的理解有差距 不多说 上代码

![](http://vdisk-thumb-3.wcdn.cn/frame.1024x768/data.vdisk.me/55890007/4062a314dbc348a1942538b32451474db5731cb5?ip=1364746800,10.73.26.36&ssig=ldQFmzKD6e&Expires=1364745600&KID=sae,l30zoo1wmz)

>>* 注意 
 test_request_context() 方法 的使用
 
 url_for 的使用必须要上下文环境 test_request_context() 可以使其在shell环境下测试

>* HTTP 的常见方法

最常见的几种 get post put HEAD 方法

>>* 默认只有 get请求方法有返回值了 这也就解释了为什么很多需要post请求返回的时候需要另外传入method 方法了..

>>* put 与post方法的不同

>* 静态文件

使用静态文件 一般在页面中直接 url_for('static', filename='style.css')

>* 渲染模板 

这部分有时间可以详细了解 细节   [Jinja2](http://jinja.pocoo.org/2/)

提供   render_template() 方法就可以渲染模板当然需要提供模板名称与参数值


>* 操作请求数据

由全局  request 提供全局请求信息

这里有一点需要讨论 request 是全局变量如果保证线程安全(即对于每一个客户端的请求保证每一个request的不一样呢?) 要回答这个问题不得不提_本地环境_

>* 本地环境 

>>* 使用  test_request_context 

from flask import request

    with app.test_request_context('/hello', method='POST'):
        # now you can do something with the request until the
        # end of the with block, such as basic assertions:
        assert request.path == '/hello'
        assert request.method == 'POST'

>>* 另一种是把wsgi整个环境传递给 

    from flask import request
    
    with app.request_context(environ):
        assert request.method == 'POST'



>* 请求对象

这里推荐完整的看API 中的关于request中的内容


需要先引用requst  from flask import request

>>* 请求的方法  request.method 
>>* 使用请求中的form request.form['username']
>>*  要操作 URL （如 ?key=value ）中提交的参数可以使用 args 属性: 
searchword = request.args.get('key', '')?

>* 文件上传

这里需要注意一点 需要在form 中添加 enctype="multipart/form-data" 属性 


>* Cookies

>>* 获得 Cookies  request.cookies 对象 

    username = request.cookies.get('username')
    # 使用 cookies.get(key) 来代替 cookies[key] ，
    # 以避免当 cookie 不存在时引发 KeyError 。
    
>>* 使用  set_cookie 方法 设置cookies

    from flask import make_response
    
    @app.route('/')
    def index():
        resp = make_response(render_template(...))
        resp.set_cookie('username', 'the username')
        return resp

>* 重定向与错误

>>* 重定向 使用  redirect() 函数 可以

>>* abort(401) 函数可以结束并返回401 错误代码

>>* 对于错误页面的处理例如定制404 出错页面可以使用 使用 errorhandler() 装饰器可以定制出错页面

例如 :

    from flask import render_template
    
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('page_not_found.html'), 404

>>* 上面代码最后的404,表示错误代码

>* 关于响应

flask 必须返回一个response 的响应对象,当然如果你返回的不是,flask 会为你做剩下的工作的
>>* 如果你返回的是response 的响应对象,flask 直接返回
>>* 如果你返回的是字符串,flask会把字符串当成http body 默认为你添加 200的状态吗与 text/html MIME  的头信息

>>* 如果你返回的是一个元祖,那么flask 会把这个元祖作为参数传递给响应构造器返回响应对象

>>* 如果不是上面的3中 flask 会假定响应是一个有效的wsgi 应用.并把构造响应对象

>>* 想操作响应对象的结构可以使用   make_response() 包裹返回表达式

    @app.errorhandler(404)
    def not_found(error):
        resp = make_response(render_template('error.html'), 404)
        resp.headers['X-Something'] = 'A value'
        return resp

>* 会话 

session对象

>>* session 是为了在多次请求之前保存信息
>>* 一般而言 session 信息保存在 服务器端. cookies信息保存在客户端 但是session 需要借助 cookies 机制(需要保存状态信息)  session 与客户端通信是加密的 cookies 则没有

>>* 使用session 时需要先设计密钥
    
    设置密钥，复杂一点：
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

一般可以使用 如下方法设置密钥

    >>> import os
    >>> os.urandom(24)
    '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'


>>* 如果在flask 端自己写html 一般需要  escape() 来转义的

>* 消息闪现  不知道是什么呢?

>* 日志

>>* flask 中集成了 logging 日志模块
>>* 使用

    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')

>>* 集成wsgi 中间件


**教程**

>* flask 介绍

>* 创建文件夹

>* 数据库模式

数据库 结构保存为 schema.sql

    drop table if exists entries;
    create table entries (
      id integer primary key autoincrement,
      title string not null,
      text string not null
    );

>* 应用构建代码

    # create our little application :)
    app = Flask(__name__)
    app.config.from_object(__name__)
    app.config.from_envvar('FLASKR_SETTINGS', silent=True)

from_object() 会查看给定的对象（如果该对象是一个字符串就会 直接导入它），
搜索对象中所有变量名均为大字字母的变量

from_envvar 是从一个配置文件中导入 FLASKR_SETTINGS 是配置文件名称


>* 创建数据库

>>* 命令行方式

    sqlite3 /tmp/flaskr.db < schema.sql

不太好 需要支持 sqlite3命令 我们可以考虑使用另一中方法

>>* 程序里创建

    def init_db():
        with closing(connect_db()) as db:
            with app.open_resource('schema.sql') as f:
                db.cursor().executescript(f.read())
            db.commit()

>>>* with 语句的使用

使用方法

    class controlled_execution:
            def __enter__(self):
                set things up
                return thing
            def __exit__(self, type, value, traceback):
                tear things down
    
    with controlled_execution() as thing:
        some code

Now, when the “with” statement is executed, Python evaluates the expression, 
calls the __enter__ method on the resulting value (which is called a “context guard”)
, and assigns whatever __enter__ returns to the variable given by as. 
Python will then execute the code body, 
and no matter what happens in that code, call the guard object’s __exit__ method.

详细见[这里](http://effbot.org/zone/python-with-statement.htm)


>>>* closing 的使用

as to

    from contextlib import contextmanager
    
    @contextmanager
    def closing(thing):
        try:
            yield thing
        finally:
            thing.close()

详见[这里](http://docs.python.org/dev/library/contextlib.html#contextlib.closing)



>* 请求数据库连接

>* 视图函数

>* 模板

>* 添加样式

>* 测试应用




































































*****
