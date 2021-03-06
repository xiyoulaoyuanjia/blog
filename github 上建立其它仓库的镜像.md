github 上建立其它仓库的镜像
====

**github 上面建立Mercurial 仓库代码**

**使用 [hg-git](https://github.com/schacon/hg-git) 工具**

Hg-Git是Mercurial(Hg)的扩展插件,主要功能是 本地hg版本管理git代码pull(push) 到
git 服务器管理代码

上面已经说了hg-git 是hg的一个扩展插件(其实就是一些python脚本)。。那安装hg-git的方式
就与安装hg其它的插件一样。。

    [extensions]
    hggit = /path/to/hg-git

/path/to/hg-git 一定要指示到下载的 hg-git 的python脚本目录 例如我的脚本目录为

    [extensions]
    hggit = ～/Destop/hg-git/hggit/

另外关于 hg-git 可以参考[这里](http://hgtip.com/tips/advanced/2009-11-09-create-a-git-mirror/)

>*  建立一个github 的新的项目
>*  从mercurial 仓库中下载需要同步到github上的仓库的代码
>*  hg pull 到github中项目地址

具体代码

    $ cd hg-git # (a Mercurial repository)
    $ hg bookmark -r default master # make a bookmark of master for default, so a ref gets created
    $ hg push git+ssh://git@github.com/schacon/hg-git.git
    $ hg push

![](http://openapi.vdisk.me/?m=file&a=download_share_file&ss=6ecaUlt--2FuR4BMUMZlGcJ4zu84PNwbqOZrYPn3cthLlMxb--2B--2FSxWlfiS84Iq2dGUVbg--2B83nlX--2BHmhe--2B2w4cCtDjr581EOH)

__这里需要特别注意 hg-git 的目的是 服务器是git 方式管理代码。客户端是hg 方式管理代码__

__另外这里有一篇在hg-git 上设计的hook 可以方便的pull hd 与git 写的也相当有意思__

[Github and Bitbucket hooks](http://morgangoose.com/blog/2010/09/29/github-and-bitbucket-hooks/)


**使用[git-hg](https://github.com/cosmin/git-hg)插件**

这个项目与上面说的git-hg 正好相反。 这个是服务器是git 管理 客户端 是git-hg(依赖于hg) 当然客户端也可以
是 git 管理代码


     git-hg clone http://some/random/hg/repo [local-git-repo-name]
     git-hg pull # same as git-hg-fetch && git merge hg/branch_name

具体可以参考上面给的链接。 其中我在做ossec 的mirror时也就是使用了这种方法一次性把
hg 的代码转换成了git的标签同时推送到github中的 在[这里](https://github.com/xiyoulaoyuanjia/sAoccec/tree/mirror)

**在GitHub上建立一个SVN仓库的镜像**

这个的目的主要是 同步google code(svn) 到github 中的

这个可以参考 [这里](http://blog.yesmeck.com/archives/create-svn-mirror-on-github/)

这里需要先安装git-svn 














