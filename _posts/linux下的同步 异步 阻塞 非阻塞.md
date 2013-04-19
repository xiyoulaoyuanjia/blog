**linux 下io**

**关于IO的同步,异步,阻塞,非阻塞**



>* 一般典型的I/O(同步阻塞I/O)

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=31c1hG--2BjT5ElCtDaALqfKn9qSG--2BqBjwn04OpwtcpHXw0DfOftJ3aCSIzIRjtOMHZZMlDdbF1we93BIiocvrux--2Fc1MMDF)
从应用程序的角度来说，read 调用可能会延续很长时间。实际上，在内核执行读操作和其他工作时，
应用程序的确会被阻塞，也就是说应用程序不能做其它事情了。


>*  同步 非阻塞I/O

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=ebeaxXjA1nZEFKwGAs37VvtBC--2FGhezl6s--2FR0rvGQyo148Zon--2FC72obcuzkmmxIAu59WfYW8TQzFE71Ggvkg3sf01zc3y)
实际上，该方式需要应用程序以一种轮询的方式来实现数据读取，多次无谓的系统调用会加大系统开销，影响应整个系统的吞吐量。
这种需要多次的用户进程与内核进程切换。。

>*  select poll epoll 方式。。。 

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=5058fbW0GZLrCrSYaNzUD3WskgKhdXdp--2BvE--2Fnz0we3yMhADI0g9vbkpgZskP48--2BJJ1BhhhJFvRMKvuQlRPRy6--2BZ5b6--2FO)

该方式中，select(或poll)的调用仍然会阻塞进程，与一般典型的I/O不一样的它是等待事件通知。但是它引入了超时机制，可以让应用程序有权力避免过长时间等待；
另一方面，如果应用程序需要读写多个文件，该方式可以一显身手。


>* 异步I/O

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=4e24TKQcgbivcZpbg9ps1chscTB6UsW--2F2kHR4oJd2Svw--2BLqjE3h1JqgU83sx0Ealw3f4LLKPYt1RnodFeiIhCD4u69Em)

**IO 常见的几种模型**

>* 阻塞型 IO(blocking I/O)
>* 非阻塞性IO(nonblocking I/O)
>* IO多路复用(I/O multiplexing)
>* 信号驱动IO(signal driven I/O)
>* 异步IO(asynchronous I/O)


**IO 操作可以分为两个阶段**

>* 等待数据准备好
>* 将数据从内核缓冲区复制到用户进程缓冲区

**同步与异步的区别**

>* 同步IO，需要用户进程主动将存放在内核缓冲区中的数据拷贝到用户进程中。
>* 异步IO，内核会自动将数据从内核缓冲区拷贝到用户缓冲区，然后再通知用户。

>* io 多路复用

当对多路复用IO进行调用时，比如使用poll。需注意的是，poll是系统调用，当调用poll的时候，其实已经是陷入了内核，是内核线程在跑了。因此对于调用poll的用户进程来讲，此时是阻塞的。
因为poll的底层实现，是去扫描每个文件描述符(fd)，而如果要对感兴趣的fd进行扫描，那么只能将每个描述符设置成非阻塞的形式(对于用户进程来讲，设置fd是阻塞还是非阻塞，可以使用系统调用fcntl)，这样才有可能进行扫描。如果扫描当中，发现有可读(如果可读是用户感兴趣的)的fd，那么select就在用户进程层面就会返回，并且告知用户进程哪些fd是可读的。
这时候，用户进程仍然需要使用read的系统调用，将fd的数据，从内核缓冲区拷贝到用户进程缓冲区(这也是poll为同步IO的原因)。
那么此时的read是阻塞还是非阻塞呢？这就要看fd的状态了，如果fd被设置成了非阻塞，那么此时的read就是非阻塞的；如果fd被设置成了阻塞，那么此时的read就是阻塞的。
不过程序已经执行到了这时候，不管fd是阻塞还是非阻塞，都没有任何区别，因为之前的poll，就是知道有数据准备好了才返回的，也就是说内核缓冲区已经有了数据，此时进行read，是肯定能够将数据拷贝到用户进程缓冲区的。




























