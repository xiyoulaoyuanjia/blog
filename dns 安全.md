2012 春节期间 github 受到dns污染的干扰 访问github的网站 都会返回一个59.24.3.173的ip地址。

**dns 污染**

一般而言 dns使用udp协议。在dns服务器查询期间发现你访问的是基于某一个网站则在，然后造一个假的回应包并在真正的包返回之前给你就行了，然后假的包里面只要把实际的 IP
改成另外一个 IP 就行。

运行dig @8.8.8.8 twitter.com 并使用wireshark 抓包 如图可得

![dns污染](https://mail-attachment.googleusercontent.com/attachment/u/0/?ui=2&ik=429fe34bc2&view=att&th=13c5d593b7a78fb7&attid=0.1&disp=inline&realattid=f_hc7nowqc0&safe=1&zw&saduie=AG9B_P_yefQZTkL1e79QyVqUxjWo&sadet=1361360033407&sads=3q3QrYvd1A7D8v-RpoXm83rH7qs)

一般而言有一个伪造ip列表
8.7.198.45
37.61.54.158
46.82.174.68
59.24.3.173
78.16.49.15
93.46.8.89
159.106.121.75
203.98.7.65
243.185.187.39
或者没有answer。

**几种解决方案**

_把本机的53端口的包重定向要vps的非知名端口，然后在vps的非知名端口上开一个dns server,然后解析完了扔回来_


_通过dnscrypt 解决dns 污染..._


_drop 掉上面的那些列表的方案_

_dnsmasq 方案_

_note dnsmasq 一般用作三种用途 1.提供dns服务 2. 优先使用本地自定义的dns 3.提供dhcp服务 关于其它使用参考 http://www.aslibra.com/blog/post/dnsmasq.php 文档























