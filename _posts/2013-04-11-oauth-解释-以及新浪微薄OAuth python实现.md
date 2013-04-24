---
layout: post
title: oauth 解释 以及新浪微薄OAuth python实现
date: 2013-04-11 02:38:05
---

oauth 解释 以及新浪微薄OAuth python实现
==
**什么是oauth？**

oauth是一套认证标准 。最早出现在 [这里](http://oauth.net/) 当然这样的标准分为 oauth1 与 oauth2

oauth 是一套三方委托认证模式

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=3c88e8YvGlxZlSzVbXuW--2FHUw--2BHMmrugkTc68SkQ--2BacY22bGyS5OA5HfZV9azQr21LGRXwmgx--2BcGQRdLXLSFja3OM--2B3jz)

ZYS 向SINA 发出请求 获得YQ的信息,SINA询问YQ是否同意？ YQ返回同意。然后SINA返回ZYS请求的信息 "here you are"

可以概括起来就是 

>* request
>* argee?
>* Yes
>* Here you are

上面的3个对应于新浪的3个认证URL 最后一个 "Here you are" 可以看成具体的应用API调用

>* http://api.t.sina.com.cn/oauth/request_token

>* http://api.t.sina.com.cn/oauth/authorize

>* http://api.t.sina.com.cn/oauth/access_token

这其中牵扯的一些参数

>* APP_KEY, APP_SECRET

>* request_token, request_secret

>* verifier


URL 编码 参考[这里](http://www.ruanyifeng.com/blog/2010/02/url_encoding.html)




>* access_secret, access_secret

这个认证步骤可以看成

ZYS YQ SINA

>* ZYS 找到SINA 说等会 YQ过来我要拿YQ的粉丝数据。然后通过参数的传递 从SINA处获得__request_token__ 和 __request_secret__

>* YQ 找到SNA说是否ZYS要我的粉丝数据?并且把ZYS私下给YQ的__request_token__和 __request_secret__ 给SINA看，并同意ZYS拿它的数据。这时SNA把__verifier__给 YQ。YQ把__verifier__ 给了
ZYS

>* ZYS 拿着 request_token ， request_secret ， verifier 这三样东西，找到 SINA，说明他已经取得了 YQ 的授权。此时， SINA 给了 ZYS 一对 access_token 和 access_secret 。之后，凭着这对东西， ZYS 就可以从 SINA 那里取得 YQ 的粉丝数据了。

_以后ZYS就可以使用access_token从SINA处直接获得数据了(对外API)_

实战参考[这里](http://zouyesheng.com/oauth-sina.html#toc1)
































