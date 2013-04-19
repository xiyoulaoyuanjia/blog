python 中 sqlite3 的使用
======

**优点使用方便但是功能相比较其它大型数据库有所差距**

**python的数据库模块有统一的接口，操作基本有统一的模式** 

假设数据库模块名称为 sqlite3

>* 创建数据库连接 sqlite3.connect,返回连接对象为com
>* 如果不需要返回结果可以直接com.execute 查询。有时需要使用 com.commit 提交事务
>* 如果需要查询返回结果。则需要使用游标 com.cursor 创建游标对象 cur.. 通过cur.execute 查询数据库
用 cur.fetchall/cur.fetchone/cur.fetchmany 获取查询结果. 这里根据事物级别不同有时需要
cur.commit

>* 关闭 cur 与 com

**python 实例**

>* 导入模块
   
    import sqlite3

>* 创建打开数据库 (存在则打开不存在则创建)

    com=sqlite3.connect("sql.db")
    
>* 返回的 com 是一个数据库连接对象 它有如下的操作

>>* commit()   提交事务
>>* rollback()  事务回滚
>>* close()    关闭数据库连接
>>* cursor()    创建游标


>* python  sqlite3 游标的使用

>>* 游标提供了一种从表中检索数据的简单方法
>>* 游标本质上是一种可以从多个结果集中取出一条记录的机制
>>* 游标是由__结果集__以及指定特定位置的__游标位置__
>>* 可以把游标比喻为文件句柄

>>* 创建游标对象

    cur=com.cursor

游标对象 cur 常用操作

>>>* execute()  执行sql 语句
>>>* executemany  执行多条sql语句
>>>* close()    关闭游标
>>>* fetchone()  从结果中取出一条记录 并把游标指向下一个
>>>* fetchmany()  从结果中取出多条记录。并移动游标
>>>* fetchall()   从结果中取出所有记录  
>>>* scroll()  滚动游标

>>* 建表

    cu.execute('create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE）') 

建立 表 catalog  主键为 id 

>>*  插入数据库

    cu.execute("insert into catalog values(0, 0, 'name1')")  
    cu.execute("insert into catalog values(1, 0, 'hello')")

__注意:这样子插入需要自己做特殊字符的转义__

sqlite3 中的处理方法

      executeTemplate="insert into  blog_entries(href,title,text) values (?,?,?)" 
      com.execute(executeTemplate,(globalName[key]['href'],globalName[key]['title'],globalName[key]['content']))

mysql 中的处理方法

      import MySQLdb
      s = """test!42''354542"""
      print MySQLdb.escape_string(s)


这里需要注意需要使用连接对象提交 com.commit 才能生效

>>*  查询

    cu.execute("select * from catalog")
    print cu.fetchall()  打印所有结果

>>* 修改 

    cu.execute("update catalog set name='name2' where id = 0") 
    cx.commit() 注意,修改数据以后提交

>>* 删除

    cu.execute("delete from catalog where id = 1")  
    cx.commit()


__note:可以通过修改 conn.isolation_level = None 避免每次都需要commit的麻烦__

[完整示例](https://gist.github.com/xiyoulaoyuanjia/31bb4783c900123cc7e3)






















































