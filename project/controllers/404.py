# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request, render_template_string, redirect


@app.errorhandler(404)
def page_not_found(e):	
    template = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>WorkWise</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="" />
<meta name="keywords" content="" />
<link rel="stylesheet" type="text/css" href="/static/css/animate.css">
<link rel="stylesheet" type="text/css" href="/static/css/bootstrap.min.css">
<link rel="stylesheet" type="text/css" href="/static/css/line-awesome.css">
<link rel="stylesheet" type="text/css" href="/static/css/line-awesome-font-awesome.min.css">
<link rel="stylesheet" type="text/css" href="/static/css/font-awesome.min.css">
<link rel="stylesheet" type="text/css" href="/static/lib/slick/slick.css">
<link rel="stylesheet" type="text/css" href="/static/lib/slick/slick-theme.css">
<link rel="stylesheet" type="text/css" href="/static/css/style.css">
<link rel="stylesheet" type="text/css" href="/static/css/responsive.css">
<link rel="stylesheet" type="text/css" href="/static/css/jquery.mCustomScrollbar.min.css">
<link rel="stylesheet" type="text/css" href="/static/css/flatpickr.min.css">
<link rel="stylesheet" type="text/css" href="/static/css/jquery.range.css">
</head>
<body class="sign-in">
	<div class="wrapper">
		<div class="sign-in-page">
			<div class="signin-popup">
				<div class="not_found">
					<div class="row">
						<div class="col-lg-13">
							<div class="cmp-info">
								<div class="cm-logo">
									<img src="/static/images/circle.gif" style="width: 30%; height: 30%;" alt="">
                                    <p>The page you where looking for at <b>{0}</b>, was not found! </p>
                                   
                                    <p>Please follow this link to return to <a href="/dashboard/1" style="color:blue;">home</a></p>
								</div><!--cm-logo end-->	
								<img src="/static/images/cm-main-img.jpg" alt="">			
							</div><!--cmp-info end-->
						</div>
					</div>		
				</div><!--signin-pop end-->
			</div><!--signin-popup end-->
			<div class="footy-sec">
				<div class="container">
					<p><img src="/static/images/copy-icon.png" alt="">Copyright 2020</p>
				</div>
			</div><!--footy-sec end-->
		</div><!--sign-in-page end-->


	</div><!--theme-layout end-->

<script type="text/javascript" src="/static/js/jquery.min.js"></script>
<script type="text/javascript" src="/static/js/popper.js"></script>
<script type="text/javascript" src="/static/js/bootstrap.min.js"></script>
<script type="text/javascript" src="/static/js/jquery.mCustomScrollbar.js"></script>
<script type="text/javascript" src="/static/lib/slick/slick.min.js"></script>
<script type="text/javascript" src="/static/js/scrollbar.js"></script>
<script type="text/javascript" src="/static/js/script.js"></script>
</body>
</html>
""".format(request.url)
    #the idea is not to do XSS...
    url = request.url
    a = ['script', 'img', 'iframe', 'body', 'input', 'style', 'svg', 'link', 'bgsound', 'meta', 'table', 'div', 'base', 'href', 'object']
    if any(x in url.lower() for x in a):
        return redirect("/about", code=302)
    else:
        return render_template_string(template), 404
