开始写自己的vim 函数
===


>* 函数名必须以大写字母开头

    hex2dec is 非法
    Hex2dec is 合法的
c语言与bash 允许 这样子的函数名。

>* 如何引用函数参数

    fu! Hex2dec(var1, var2)
      let str=a:var1
      let str2=a:var2

参数名前必须有一个"a"的，在函数里面不允许 更改参数例如像 let a:var1=1 这样的的使用
是不允许的。

当然在c语言里面 是不需要"a"前缀的。。参数一般来说也是可以更改的。。

更多可以查看 :help a:1

>* 如何在函数中使用可变参数

    fu! Hex2dec(fixedparam, ...)

>>* a0 表示 .... 中的参数个数
>>* a1 代表 .... 中的第一个参数 依次类推

例如:

    :call Hex2dec("asdf", 4,5,6)

>>* a:0 = 3, a:1 = 4, a:2 = 5, a:3 = 6.

更多可以参考  :help a:0   :help a:000

>* 如何从一个可变参数函数中调用另一个可变参数函数

    function! Hex2DecWrapper(...)
      let params = ['asdf'] + a:000
      :call call (function('Hex2Dec'), params)
    endfunction

>* vim 的库(vim-library)在哪里？

vim 具有它自己的函数库。。可以通过:help functions 来查看

>* 如何使用 ++ 或者 += 运算符

>>* += 在 vim 7.0 版本之后才存在
>>* ++ 不存在

>* 如何使用变量

    let var1=value
    let var2=var1

当然在c语言中 let 是不允许使用的。

更多可以查看 :help :let 或者 :help expression

>* 在一个函数中可以使用任意的外部命令吗？

可以 每一行都可以是 一个外部命令

>* 函数可以调用它自己吗？(递归使用)

可以 但是要小心无穷递归

>* 函数怎么调用另一个函数

可以向c语言一样的使用

>* 需要编译函数吗？

你不能并且也不需要这样子做。
在vim 中你可以向下面那样子引入你的vim脚本

    :so filename_containing_script

之后你就可以使用该脚本的函数了

当然 如何你想这些也可以在你的vimrc 文件中来做

>* vim 有浮点数 整形 等数据类型吗？

vim 向perl 一样 它的类型是由它所在的上下文决定的。。

    let a=1
    let a=a."asdf"
    echo a    (displays '1asdf')
    let a=1
    let a=a+2
    echo a    (displays '3')


>* 每一条语句都需要";" 结尾吗？

不,从不需要那样子做.当然如果你需要 在一行中使用多条语句可以考虑 "|" 符号
“;” 在 c 语言中是必须的，在bash中是可选的。

>* 参考

>>* :help :function
>>* :help a:1
>>* :help expression
>>* :help functions

>>* :help script
>>* :help autoload to write Vim library plugins
>>* :help script-local to hide functions in scripts
>>*  Vim WikiBook about scripting


