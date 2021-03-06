使用ajax上传文档
============

__note:[E文](http://net.tutsplus.com/tutorials/javascript-ajax/uploading-files-with-ajax)__

__[代码](http://nettuts.s3.amazonaws.com/1020_ajaxupload/demo.zip)__

__为什么不在最后告诉你这个不好的消息呢?这个并不是在每一个浏览器中都适用的__

我们项目用到的主要的3个组建

>* "<"input> 中的  multiple 属性(这个支持多个文件)
>* 文件操作的API 中的 FileReader 对象
>* 在 XMLHttpRequest2 中的  FormData 对象

我们使用 multiple 属性允许我们读取多个文件内容(即使 FileReader 对象不可用.这个依然可以正常使用) 当然,FileReader对象可以使用们在上传的时候看到图片的缩略图.

上述3个特性均不能在IE9中正常的工作.所以 IE用户可能不能正常使用.在最新的 Safari (5.1)版本中没有FileReader 对象 所以用户不能得到正常的图片缩略图 但是可以使用AJAX正常上传图片并获得上传成功的消息.,Opera 10.50 版本支持FileReader 对象 对象但是不支持 FormData 对象所以可以获得缩略图但是不能正确的上传图片.

先抛开那些问题,开始看代码吧.

**标签与样式**

让我们从基本的标签与样式开始吧..当然这些不是本文档的主要部分..就向我不会把你们当成初学者一样..

**html部分**

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
	<title>HTML5 File API</title>
	<link rel="stylesheet" href="style.css" />
</head>
<body>
	<div id="main">
		<h1>Upload Your Images</h1>
		<form method="post" enctype="multipart/form-data"  action="upload.php">
			<input type="file" name="images" id="images" multiple />
			<button type="submit" id="btn">Upload Files!</button>
		</form>

		<div id="response"></div>
		<ul id="image-list">

		</ul>
	</div>

	<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"></script>
	<script src="upload.js"></script>
</body>
</html>


上面的代码很基本吧..有一个form表格.并且post到 upload.php (这个文件等会会看到),然后还有一个input组建允许我们选择多个需要上传的文件,当然这个是 multiple 属性 起作用的.

继续吧..

body {
	font: 14px/1.5 helvetica-neue, helvetica, arial, san-serif;
	padding:10px;
}

h1 {
	margin-top:0;
}

#main {
	width: 300px;
	margin:auto;
	background: #ececec;
	padding: 20px;
	border: 1px solid #ccc;
}

#image-list {
	list-style:none;
	margin:0;
	padding:0;
}
#image-list li {
	background: #fff;
	border: 1px solid #ccc;
	text-align:center;
	padding:20px;
	margin-bottom:19px;
}
#image-list li img {
	width: 258px;
	vertical-align: middle;
	border:1px solid #474747;
}

完全的css文件没有什么要说的...

**php文档**

对于前台提出的请求是在这里进行处理的.可以在下面的代码中看出来

<?php

foreach ($_FILES["images"]["error"] as $key => $error) {
	if ($error == UPLOAD_ERR_OK) {
		$name = $_FILES["images"]["name"][$key];
		move_uploaded_file( $_FILES["images"]["tmp_name"][$key], "uploads/" . $_FILES['images']['name'][$key]);
	}
}

echo "<h2>Successfully Uploaded Images</h2>";

请记住这个是我进一年来首次使用php语言.(我是一个rubyer),当然你需要确保安全性..这些可以使用内置的move_uploaded_file 移动到需要上传的文件夹内.不要忘记文件夹是可写的..

现在我们有一个前台的form表单.后台的php文件.可以开始做了,选择需要上传的图片并且点击上传按钮..然后你会看到”Successfully Uploaded Images “ 的消息

我们的mini的项目看起来是如下的样子的

![](http://image.data.vdisk.me/55890007/61a076160605e23f51aec89840c3994c296f6007?ip=1364455236,219.142.5.234&ssig=km%2FAauDVmp&Expires=1364454036&KID=sae,l30zoo1wmz&fn=form.png)

但是请记住.现在是2011,我们想做的肯定不止这些..聪明的人已经看到我们引入了 upload.js 和 jQuery 文件  那我们就开始吧

**javascript 文件**

不要浪费时间了直接开始吧..


(function () {
	var input = document.getElementById("images"),
	    formdata = false;
		
	if (window.FormData) {
		formdata = new FormData();
		document.getElementById("btn").style.display = "none";
	}
	

}();


从上面代码开始吧..这里我们创造了两个变量.input是我们的 id为 images的 <input>对象.
formadata用来从前台向后台传递数据的对象当然这个需要浏览器的支持.当然如果浏览器支持这个我们也不需要 “Upload image ” 按钮了(选择需要上传的图片之后自动上传)..所以在后面我们隐藏了它..

剩下的代码会在 匿名的  self-invoking 函数内 ([关于self-invoking 与document.ready的区别 见里](http://stackoverflow.com/questions/3259496/jquery-document-ready-vs-self-calling-anonymous-function)) 下面我先写了一个当选择文件确定是在界面的需要展示..

function showUploadedItem (source) {
	var list = document.getElementById("image-list"),
	    li   = document.createElement("li"),
	    img  = document.createElement("img");
  	img.src = source;
  	li.appendChild(img);
	list.appendChild(li);
}
该函数只有一个参数 图像的源地址.(底下我们可以知道这个是如何得到的) 我们创建了图片项,添加了图像的来源,并把它添加到list(dom结构中去)中去.

下来我们选择需要上传的文档.并且由于onchange函数触发.把它显示到Dom结构中去.并且上传图片数据给后端服务器.

if (input.addEventListener) {
	input.addEventListener("change", function (evt) {
		var i = 0, len = this.files.length, img, reader, file;
		
		document.getElementById("response").innerHTML = "Uploading . . ."
		
		for ( ; i < len; i++ ) {
			file = this.files[i];
	
			if (!!file.type.match(/image.*/)) {

			}	
		}
			
	}, false);
}



并且 我们不需要担心其它的问题 因为 iE 9 也支持 addEventListener 监听函数.
那么当用户选择时我们最关心什么 ?第一我们创建了几个变量..下来 对于 LEN = this.files.length 这句话也很重要.因为我们需要通过LEN 的长度来循环获得所选的每一个文件.. 下来所要做的就是在循环的里面了..这需要对于每一个文件复制给变量这样有助于简化处理.. 下来使用了正则表达式来确定上传的是图像文件 ...

好吧.如果我们已经有一个图像文件在手上.那么我们下一步该怎么做呢?

if ( window.FileReader ) {
	reader = new FileReader();
	reader.onloadend = function (e) { 
		showUploadedItem(e.target.result);
	};
	reader.readAsDataURL(file);
}
if (formdata) {
	formdata.append("images[]", file);
}

首先我们检查 浏览器是否支持 创建一个 FileReader 对象.如果支持我们就创建一个这样的对象..

下来当然是如何使用 FileReader 对象的问题了..通过把 file 传递给 文件对象reader.readAsDataURL 方法.. 当然这个方法可能并不想你想象的那样工作.它的url并没有通过函数返回,想法它是它是一url data 的方式读数据并变成对象的一部分...关于这部分参考[](http://m.csdn.net/article/2012-12-17/2812911)

考虑到 这一点我们需要在 FileReader 对象上面注册一个 onload 事件 在 成功通过 readAsDataURL 读取图片的 内容时可以通过 e.target.result 读取到的数据内容传递给之前建立的 showUploadedItem 函数去显示..

接下来 检查 formdata 对象 如果 浏览器支持 formdata对象 则 formdata 就是一个对象的值 反之则为空.所以当有一个 formdata 对象时可以去 使用  append 方法添加 一个key 与 values 当然 对于多个文件,相同的key值要保证不会覆盖.

在我们的多个文件循环里面 我们把每一个图片对象添加到 list中展示给用户并且都添加到了formdata 对象里面.在循环外面我们使用了 ajax去 做post请求.


if (formdata) {
	$.ajax({
		url: "upload.php",
		type: "POST",
		data: formdata,
		processData: false,
		contentType: false,
		success: function (res) {
			document.getElementById("response").innerHTML = res; 
		}
	});
}

当然在这里我们还是检查了浏览器是否支持  formdata 格式 如果不支持可以考虑点击上传按钮来完成一般的文件上传.当然如果浏览器支持 那我们通过ajax 的post方法完成上传的效果..

你应该已经对jquery的 $.ajax 方法很熟悉了吧...通过给它传递一个包含一系列选项的对象.包括.url,type success 函数(执行成功是调用的函数)  数据属性是 formdata 并且 特别需要注意 processData 与  contentType , 在一般的Jqury文档里面都可以看到 processData 默认为 true 依次来保证传递的在字串传里面(?A=afa&b=??),但是这里当然不需要这样子的.所所以把它设置为false . 我们仍然把 contentType 设置为false 以保证数据正确从客户端到服务器传送

至此我们看看前面的效果....当你开始打开网页时效果如下:

![](http://image.data.vdisk.me/55890007/795a51fddb2a97f8581dc20949a16eda30657a9a?ip=1364454872,219.142.5.234&ssig=EADiu8C0vE&Expires=1364453672&KID=sae,l30zoo1wmz&fn=ajax-start.png)

当用户选择上传图片之后 如下图

![](http://image.data.vdisk.me/55890007/14d9c86e85ccdcdd923c6bb057e1565789b6b61b?ip=1364454948,219.142.5.234&ssig=BVqZ3J058p&Expires=1364453748&KID=sae,l30zoo1wmz&fn=ajax-upload.png)

上传结果

![](http://image.data.vdisk.me/55890007/8deea1016570cc1b446660c3bbb36d9acc6ae695?ip=1364454968,219.142.5.234&ssig=sdhbVbsqmG&Expires=1364453768&KID=sae,l30zoo1wmz&fn=ajax-finder.png)

**总结**

通过ajax上传图片这是意见很cool的事情..掌握它只需要一些常用的新支持而不需要很复杂的hack 很高兴你可以阅读它...再见.~~

















