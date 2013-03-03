linux strace 命令学习
==

**什么是strace？**

strace – trace system calls and signals 系统调用与系统信号分析

strace 最简单的用法就是后接一个进程，进程执行完成之后strace也就退出了。strace会在进程执行中解析进程的所有系统调用与系统信号分析
***
**追踪系统调用**

    strace ./test

会输出test程序的所有系统调用(默认格式)

**追踪信号传递**

我们可以通过一个strace的输出来看

> set_thread_area({entry_number:-1 -> 6, base_addr:0xbf5ee740, limit:1048575, seg_32bit:1, contents:0, read_exec_only:0, limit_in_pages:1, seg_not_present:0, useable:1}) = 0
munmap(0xbf5ef000, 65900)               = 0
fstat64(0, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
mmap2(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0xbf5ff000
read(0, 0xbf5ff000, 1024)               = ? ERESTARTSYS (To be restarted)
--- SIGTERM (Terminated) @ 0 (0) ---
+++ killed by SIGTERM +++

当然 这只是strace输出的一部分了。在最后我们可以看到killed by SIGTER表示接受到了一个 SIGTERM 信号。

**系统调用统计**

strace不光能分析系统调用，还可以将系统调用做一个统计分析 我们依旧可以从一个strace 的结果来看

    strace -c ./test

     execve("./test", ["./test"], [/* 41 vars */]) = 0
    % time     seconds  usecs/call     calls    errors syscall
    ------ ----------- ----------- --------- --------- ----------------
     45.90    0.000140           5        27        25 open
     34.43    0.000105           4        24        21 stat64
      7.54    0.000023           5         5           old_mmap
      2.62    0.000008           8         1           munmap
      1.97    0.000006           6         1           uname
      1.97    0.000006           2         3           fstat64
      1.64    0.000005           3         2         1 read
      1.31    0.000004           2         2           close
      0.98    0.000003           3         1           brk
      0.98    0.000003           3         1           mmap2
      0.66    0.000002           2         1           set_thread_area
    ------ ----------- ----------- --------- --------- ----------------
    >100.00    0.000305                    68        47 total

上面输出的统计信息已经很详细了。这对于我们分析程序而言十分有帮助。

****
**重定向输出**

    strace -c -o test.txt ./test

**对系统调用进行计时**

    strace -T ./test

**系统调用的时间**

只要使用-t/tt/ttt三个参数就可以看到效果了，具体的例子可以自己去尝试

**截断输出**

    strace -s 20 ./test
    
每一行不超过20个字符

**strace一个已经运行的进程**

    strace -p pid
    
pid 表示一个已经运行的程序的pid.
****

**一个综合例子**


















