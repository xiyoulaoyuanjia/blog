---
layout: legacy
title: Subversion on Site5
permalink: Subversion_on_Site5/index.html
# 15,177 hits 20111013
---

h1. {{ page.title }}

"Site5":http://www.site5.com/in.php?id=7872 provides Subversion access via SSH. These are my notes on getting it working and basic usage.

"Site5":http://www.site5.com/in.php?id=7872 is my current Web hosting provider. I highly recommend them.

If you would like to consider joining "Site5":http://www.site5.com/in.php?id=7872, please click on my affiliate link "here":http://www.site5.com/in.php?id=7872.

h1. Create your Repository

{% highlight bash %}
svnadmin create /home/[username]/repos
{% endhighlight %}

h1. Creating the Layout, and Importing Initial Data

{% highlight bash %}
$ mkdir tmpdir
$ cd tmpdir
$ mkdir projectA
$ mkdir projectA/trunk
$ mkdir projectA/branches
$ mkdir projectA/tags
$ mkdir projectB
$ mkdir projectB/trunk
$ mkdir projectB/branches
$ mkdir projectB/tags
…
$ svn import . file:///path/to/repos --message 'Initial repository layout'
Adding         projectA
Adding         projectA/trunk
Adding         projectA/branches
Adding         projectA/tags
Adding         projectB
Adding         projectB/trunk
Adding         projectB/branches
Adding         projectB/tags
…
Committed revision 1.
$ cd ..
$ rm -rf tmpdir
{% endhighlight %}

You can verify the results of the import by running the svn list command:

{% highlight bash %}
$ svn list --verbose file:///path/to/repos
      1 harry               May 08 21:48 projectA/
      1 harry               May 08 21:48 projectB/
…
{% endhighlight %}

h1. Site5 specific issues

Request to "Site5":http://www.site5.com/in.php?id=7872 support that they change your shell to Bash. Specify your username and the reason ("for Subversion access").

"Explanation":http://forums.site5.com/showthread.php?p=37388#post37388: We offer different shells for different levels of users and different purposes. This is a large part of the reason why when you ask for shell to be enabled, a technicians will typically ask "what for?". If you are using SVN and would like to get rid of the entry banner, simply submit a support request, include your main account and the username you are using to connect and request to have you shell switched to "bash". Simple as that! :D 

