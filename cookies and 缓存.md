**cookie 的分类**
>* 会话cookies

是一种临时cookies。记录用户登录网站的设置与偏好信息。。关闭浏览器就清除了

>* 持久cookies

持久icookies 存在硬盘中。。有过期时间

**为什么需要cookies**

这是因为http协议是无状态的。。对于一个浏览器发出的多次请求，WEB服务器无法区分 是不是来源于同一个浏览器
所以浏览器需要额外的信息维持会话。。

**cookies 的限制**
一些浏览器支持最大 4096字节的cookies。另一些支持最多20个cookies 超过的旧的就会陪删除

**cookie 存放**

>* 不同的浏览器会存放在不同的地方
>* 不同的网站会有不同的cookie文件

windows 下的ie 是 存放在临时文件夹下面的
![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=b8d8XgiPVdBwl--2FE1cDVwvaVmWbbRE4XCNtT--2FlY1xJjdPDtpaWU6suLNJo37weV1zBE7cBBfg8R--2BmMF3BS67BH0ciHlhz)

linux 下的 chrome 是存放在 sqllite3 数据库中的
![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=6c17G8HyRRw8uUSDMtgmnCv6jYSnXXMsZICNspz5lUjWr735mfcbR4qBay5Sv9c6BiUoE8L4PYSiY8BSE8OyCQd--2BDKBb)

**cookies 在 http中的使用**

浏览器把 cookies 在 http 的 Request 中 Cookie: header 发送

Web服务器通过HTTP Response中的"Set-Cookie: header"把cookie发送给浏览器

**cookies 与文件缓存的区别**

这两个是不一样的东西。。。在ie中可能存放在同一个文件夹下。。但一般在设置浏览器时
都可以选择分别设置cookies 与 缓存的


**http协议之缓存**

>* http 中具有浏览器缓存。缓存代理服务器
>*  http 缓存是指当web 请求到达缓存时可以考虑从本地提取缓存而不用在次从服务器发请求
>*  缓存的好处
>>* 减少了服务器的压力
>>* 加快了浏览器的加载速度

>* 与缓存有关的header
>>* Request

    Cache-Control: max-age=0    以秒为单位
    If-Modified-Since: Mon, 19 Nov 2012 08:38:01 GMT  缓存文件的最后修改时间。
    If-None-Match: "0693f67a67cc1:0"	缓存文件的Etag值
    Cache-Control: no-cache	           不使用缓存
    Pragma: no-cache	           不使用缓存

>>* Response

    Cache-Control: public    响应被缓存，并且在多用户间共享，  （公有缓存和私有缓存的区别，请看另一节）
    Cache-Control: private	响应只能作为私有缓存，不能在用户之间共享
    Cache-Control:no-cache	提醒浏览器要从服务器提取文档进行验证
    Cache-Control:no-store	绝对禁止缓存（用于机密，敏感文件）
    Cache-Control: max-age=60	60秒之后缓存过期（相对时间）
    Date: Mon, 19 Nov 2012 08:39:00 GMT	当前response发送的时间
    Expires: Mon, 19 Nov 2012 08:40:01 GMT	缓存过期的时间（绝对时间）
    Last-Modified: Mon, 19 Nov 2012 08:38:01 GMT	服务器端文件的最后修改时间
    ETag: "20b1add7ec1cd1:0"	服务器端文件的Etag值

>* 如何判断缓存的新鲜度
这里的新鲜度指文件是否修改。提出了两种方法

>>* 文件的最后修改时间  在head 中通过  "If-Modified-Since" 字段标识

>>>* 服务器发送状态吗 304 来标识没有修改
>>>* 如图

文件没有修改
![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=bf087nR3bMs2UgOEyuNZuISV4xmw--2FkKe--2FmShGj5LGoXwDVPJq9A03u1fRJ6tni1T44fP3fvUkSUZBbP1Wr4v8EnN--2F8TH)

文件已经修改
![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=dff4kSeiBh2mSmlqcoMfJaPVtIydvVU8QQKxTys3yv1v0Px--2BS0DzkwiN1z3Ie--2BDG0ogkpYiskEKNkbNWYQ9MvyBPompQ)


>>*  文件的hash 签名 Etag 在head 中通过  "If-None-Match" 字段来标识  Etag 是可以看成是对 最后修改时间的一种补充
>>>*  有些服务器没有办法获得文件的最后修改时间
>>>*  If-Modified-Since 是精确到秒的 对于 秒以下的文件修改则没有办法
>>>*  一些文件最后修改时间变了。内容却没有改变

>* 直接使用缓存不去服务器验证
这里 说一个例子
按F5刷新浏览器和在地址栏里输入网址然后回车。 这两个行为是不一样的。

>>* 在浏览器里输入网址 然后按回车 会直接使用缓存 不去服务器验证的。。。
>>* F5刷新 需要验证
