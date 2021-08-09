from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response

from .models import utilisateurs,chargehoraire,annonce
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt  
def index(request):
       html = '"<style> nav { background-color:black; height:50px;}</style> <nav> <ul> <li><a href="#"> line 1</a></li> <li><a href="#"> line 2</a></li></ul></nav><h1> welcome </h1>"'
       return HttpResponse(html)
@csrf_exempt  
def form(request):

   # html='<form action="http://127.0.0.1:8000/util/test" method=""> <label> Username: </label> <input type="text" name="user"> </br></br> <label> Password : </label><input type="password" name="passwd"> </br> <input type="submit" value="connect"></form>'
    #return HttpResponse(html)
   # html = '<head> <title> Connexion </title><link rel="stylesheet" href="./css/style.css"></head><body><section class="container"><div class="login"><h1> Connexion </h1><form method="post" action="http://127.0.0.1:8000/util/test"><p><input type="text" name="login" value="" placeholder="Username "></p><p><input type="password" name="password" value="" placeholder="Password"></p><p class="remember_me"><label><input type="checkbox" name="remember_me" id="remember_me">Remember me on this computer</label></p><p class="submit"><input type="submit" name="commit" value="Connexion"></p></form></div></section></body>'
    #return HttpResponse(html)
    #template = loader.get_template("login.html")
    #return HttpResponse(template.render)
    return render_to_response('login.html')

@csrf_exempt  
def test(request):
    #html='<h1>password or login are not Founded </h1> </br></br> <a href="http://127.0.0.1:8000/util/">Essayer à nouveau </a>'
    #html = 'Error.html'
    html = """

		<!DOCTYPE html>
		<html>
		<head>
			<title></title>
			  <style type="text/css">
		  html, body, div, span, applet, object, iframe,
		h1, h2, h3, h4, h5, h6, p, blockquote, pre,
		a, abbr, acronym, address, big, cite, code,
		del, dfn, em, img, ins, kbd, q, s, samp,
		small, strike, strong, sub, sup, tt, var,
		b, u, i, center,
		dl, dt, dd, ol, ul, li,
		fieldset, form, label, legend,
		table, caption, tbody, tfoot, thead, tr, th, td,
		article, aside, canvas, details, embed,
		figure, figcaption, footer, header, hgroup,
		menu, nav, output, ruby, section, summary,
		time, mark, audio, video {
		  margin: 0;
		  padding: 0;
		  border: 0;
		  font-size: 100%;
		  font: inherit;
		  vertical-align: baseline;
		}

		article, aside, details, figcaption, figure,
		footer, header, hgroup, menu, nav, section {
		  display: block;
		}

		body {
		  line-height: 1;
		}

		ol, ul {
		  list-style: none;
		}

		blockquote, q {
		  quotes: none;
		}

		blockquote:before, blockquote:after,
		q:before, q:after {
		  content: '';
		  content: none;
		}

		table {
		  border-collapse: collapse;
		  border-spacing: 0;
		}

		.about {
		  margin: 70px auto 40px;
		  padding: 8px;
		  width: 260px;
		  font: 10px/18px 'Lucida Grande', Arial, sans-serif;
		  color: #666;
		  text-align: center;
		  text-shadow: 0 1px rgba(255, 255, 255, 0.25);
		  background: #eee;
		  background: rgba(250, 250, 250, 0.8);
		  border-radius: 4px;
		  background-image: -webkit-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
		  background-image: -moz-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
		  background-image: -o-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
		  background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
		  -webkit-box-shadow: inset 0 1px rgba(255, 255, 255, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.1), 0 0 6px rgba(0, 0, 0, 0.2);
		  box-shadow: inset 0 1px rgba(255, 255, 255, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.1), 0 0 6px rgba(0, 0, 0, 0.2);
		}
		.about a {
		  color: #333;
		  text-decoration: none;
		  border-radius: 2px;
		  -webkit-transition: background 0.1s;
		  -moz-transition: background 0.1s;
		  -o-transition: background 0.1s;
		  transition: background 0.1s;
		}
		.about a:hover {
		  text-decoration: none;
		  background: #fafafa;
		  background: rgba(255, 255, 255, 0.7);
		}

		.about-links {
		  height: 30px;
		}
		.about-links > a {
		  float: left;
		  width: 50%;
		  line-height: 30px;
		  font-size: 12px;
		}

		.about-author {
		  margin-top: 5px;
		}
		.about-author > a {
		  padding: 1px 3px;
		  margin: 0 -1px;
		}


		body {
		  font: 13px/20px 'Lucida Grande', Tahoma, Verdana, sans-serif;
		  color: #404040;
		  background: #0ca3d2;
		}

		.container {
		  margin: 80px auto;
		  width: 640px;
		}

		.login {
		  position: relative;
		  margin: 0 auto;
		  padding: 20px 20px 20px;
		  width: 500px;
		  background: white;
		  border-radius: 3px;
		  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
		  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
		}
		.login:before {
		  content: '';
		  position: absolute;
		  top: -8px;
		  right: -8px;
		  bottom: -8px;
		  left: -8px;
		  z-index: -1;
		  background: rgba(0, 0, 0, 0.08);
		  border-radius: 4px;
		}
		.login h1 {
		  margin: -20px -20px 21px;
		  line-height: 100px;
		  font-size: 25px;
		  font-weight: bold;
		  color: #555;
		  text-align: center;
		  text-shadow: 0 1px white;
		  background: #f3f3f3;
		  border-bottom: 1px solid #cfcfcf;
		  border-radius: 3px 3px 0 0;
		  background-image: -webkit-linear-gradient(top, whiteffd, #eef2f5);
		  background-image: -moz-linear-gradient(top, whiteffd, #eef2f5);
		  background-image: -o-linear-gradient(top, whiteffd, #eef2f5);
		  background-image: linear-gradient(to bottom, whiteffd, #eef2f5);
		  -webkit-box-shadow: 0 1px whitesmoke;
		  box-shadow: 0 1px whitesmoke;
		}
		.login p {
		  margin: 20px 0 0;
		}
		.login p:first-child {
		  margin-top: 0;
		}
		.login input[type=text], .login input[type=password] {
		  width: 278px;
		}
		.login p.remember_me {
		  float: left;
		  line-height: 31px;
		}
		.login p.remember_me label {
		  font-size: 12px;
		  color: #777;
		  cursor: pointer;
		}
		.login p.remember_me input {
		  position: relative;
		  bottom: 1px;
		  margin-right: 4px;
		  vertical-align: middle;
		}
		.login p.submit {
		  text-align: right;
		}

		.login-help {
		  margin: 20px 0;
		  font-size: 11px;
		  color: white;
		  text-align: center;
		  text-shadow: 0 1px #2a85a1;
		}
		.login-help a {
		  color: #cce7fa;
		  text-decoration: none;
		}
		.login-help a:hover {
		  text-decoration: underline;
		}

		:-moz-placeholder {
		  color: #c9c9c9 !important;
		  font-size: 13px;
		}

		::-webkit-input-placeholder {
		  color: #ccc;
		  font-size: 13px;
		}

		input {
		  font-family: 'Lucida Grande', Tahoma, Verdana, sans-serif;
		  font-size: 14px;
		}

		input[type=text], input[type=password] {
		  margin: 5px;
		  padding: 0 10px;
		  width: 200px;
		  height: 34px;
		  color: #404040;
		  background: white;
		  border: 1px solid;
		  border-color: #c4c4c4 #d1d1d1 #d4d4d4;
		  border-radius: 2px;
		  outline: 5px solid #eff4f7;
		  -moz-outline-radius: 3px;
		  -webkit-box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
		  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
		}
		input[type=text]:focus, input[type=password]:focus {
		  border-color: #7dc9e2;
		  outline-color: #dceefc;
		  outline-offset: 0;
		}

		input[type=button] {
		  padding: 0 18px;
		  height: 29px;
		  font-size: 12px;
		  font-weight: bold;
		  color: #527881;
		  text-shadow: 0 1px #e3f1f1;
		  background: #cde5ef;
		  border: 1px solid;
		  border-color: #b4ccce #b3c0c8 #9eb9c2;
		  border-radius: 16px;
		  outline: 0;
		  -webkit-box-sizing: content-box;
		  -moz-box-sizing: content-box;
		  box-sizing: content-box;
		  background-image: -webkit-linear-gradient(top, #edf5f8, #cde5ef);
		  background-image: -moz-linear-gradient(top, #edf5f8, #cde5ef);
		  background-image: -o-linear-gradient(top, #edf5f8, #cde5ef);
		  background-image: linear-gradient(to bottom, #edf5f8, #cde5ef);
		  -webkit-box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
		  box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
		}
		input[type=button]:active {
		  background: #cde5ef;
		  border-color: #9eb9c2 #b3c0c8 #b4ccce;
		  -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
		  box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
		}

		.lt-ie9 input[type=text], .lt-ie9 input[type=password] {
		  line-height: 34px;
		}

		</style>
		</head>
		<body>
			<section class="container">
		    <div class="login"  style="text-align: center;"">
			<h1> Username ou Password sont incorrects</h1>
			<p><input type="button" value="Essayer à nouveau" onclick="window.location.href='http://127.0.0.1:8000/util/'" /></p>
		</div>
		</section>
		</body>
		</html>
    """
    all_utilisateur = utilisateurs.objects.all()
    
  
    userr= request.GET.get("user","user")
    passwd= request.GET.get("passwd","passwd")

   
    #return HttpResponse('Hello %s' % entry_title)

    for utilisateur  in   all_utilisateur :
    
       if userr == utilisateur.username and passwd == utilisateur.password : 
          url='/util/'+ str(utilisateur.id) +'/'
          urll='/util/annonce'
          html = """
          <!DOCTYPE html>
			<html>
			<head>
				<title></title>
				<style type="text/css">
			  html, body, div, span, applet, object, iframe,
			h1, h2, h3, h4, h5, h6, p, blockquote, pre,
			a, abbr, acronym, address, big, cite, code,
			del, dfn, em, img, ins, kbd, q, s, samp,
			small, strike, strong, sub, sup, tt, var,
			b, u, i, center,
			dl, dt, dd, ol, ul, li,
			fieldset, form, label, legend,
			table, caption, tbody, tfoot, thead, tr, th, td,
			article, aside, canvas, details, embed,
			figure, figcaption, footer, header, hgroup,
			menu, nav, output, ruby, section, summary,
			time, mark, audio, video {
			  margin: 0;
			  padding: 0;
			  border: 0;
			  font-size: 100%;
			  font: inherit;
			  vertical-align: baseline;
			}

			article, aside, details, figcaption, figure,
			footer, header, hgroup, menu, nav, section {
			  display: block;
			}

			body {
			  line-height: 1;
			}

			ol, ul {
			  list-style: none;
			}

			blockquote, q {
			  quotes: none;
			}

			blockquote:before, blockquote:after,
			q:before, q:after {
			  content: '';
			  content: none;
			}

			table {
			  border-collapse: collapse;
			  border-spacing: 0;
			}

			.about {
			  margin: 70px auto 40px;
			  padding: 8px;
			  width: 260px;
			  font: 10px/18px 'Lucida Grande', Arial, sans-serif;
			  color: #666;
			  text-align: center;
			  text-shadow: 0 1px rgba(255, 255, 255, 0.25);
			  background: #eee;
			  background: rgba(250, 250, 250, 0.8);
			  border-radius: 4px;
			  background-image: -webkit-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  background-image: -moz-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  background-image: -o-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  -webkit-box-shadow: inset 0 1px rgba(255, 255, 255, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.1), 0 0 6px rgba(0, 0, 0, 0.2);
			  box-shadow: inset 0 1px rgba(255, 255, 255, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.1), 0 0 6px rgba(0, 0, 0, 0.2);
			}
			.about a {
			  color: #333;
			  text-decoration: none;
			  border-radius: 2px;
			  -webkit-transition: background 0.1s;
			  -moz-transition: background 0.1s;
			  -o-transition: background 0.1s;
			  transition: background 0.1s;
			}
			.about a:hover {
			  text-decoration: none;
			  background: #fafafa;
			  background: rgba(255, 255, 255, 0.7);
			}

			.about-links {
			  height: 30px;
			}
			.about-links > a {
			  float: left;
			  width: 50%;
			  line-height: 30px;
			  font-size: 12px;
			}

			.about-author {
			  margin-top: 5px;
			}
			.about-author > a {
			  padding: 1px 3px;
			  margin: 0 -1px;
			}


			body {
			  font: 13px/20px 'Lucida Grande', Tahoma, Verdana, sans-serif;
			  color: #404040;
			  background: #0ca3d2;
			}

			.container {
			  margin: 80px auto;
			  width: 640px;
			}

			.login {
			  position: relative;
			  margin: 0 auto;
			  padding: 20px 20px 20px;
			  width: 500px;
			  background: white;
			  border-radius: 3px;
			  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
			  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
			}
			.login:before {
			  content: '';
			  position: absolute;
			  top: -8px;
			  right: -8px;
			  bottom: -8px;
			  left: -8px;
			  z-index: -1;
			  background: rgba(0, 0, 0, 0.08);
			  border-radius: 4px;
			}
			.login h1 {
			  margin: -20px -20px 21px;
			  line-height: 100px;
			  font-size: 25px;
			  font-weight: bold;
			  color: #555;
			  text-align: center;
			  text-shadow: 0 1px white;
			  background: #f3f3f3;
			  border-bottom: 1px solid #cfcfcf;
			  border-radius: 3px 3px 0 0;
			  background-image: -webkit-linear-gradient(top, whiteffd, #eef2f5);
			  background-image: -moz-linear-gradient(top, whiteffd, #eef2f5);
			  background-image: -o-linear-gradient(top, whiteffd, #eef2f5);
			  background-image: linear-gradient(to bottom, whiteffd, #eef2f5);
			  -webkit-box-shadow: 0 1px whitesmoke;
			  box-shadow: 0 1px whitesmoke;
			}
			.login p {
			  margin: 20px 0 0;
			}
			.login p:first-child {
			  margin-top: 0;
			}
			.login input[type=text], .login input[type=password] {
			  width: 278px;
			}
			.login p.remember_me {
			  float: left;
			  line-height: 31px;
			}
			.login p.remember_me label {
			  font-size: 12px;
			  color: #777;
			  cursor: pointer;
			}
			.login p.remember_me input {
			  position: relative;
			  bottom: 1px;
			  margin-right: 4px;
			  vertical-align: middle;
			}
			.login p.submit {
			  text-align: right;
			}

			.login-help {
			  margin: 20px 0;
			  font-size: 11px;
			  color: white;
			  text-align: center;
			  text-shadow: 0 1px #2a85a1;
			}
			.login-help a {
			  color: #cce7fa;
			  text-decoration: none;
			}
			.login-help a:hover {
			  text-decoration: underline;
			}

			:-moz-placeholder {
			  color: #c9c9c9 !important;
			  font-size: 13px;
			}

			::-webkit-input-placeholder {
			  color: #ccc;
			  font-size: 13px;
			}

			input {
			  font-family: 'Lucida Grande', Tahoma, Verdana, sans-serif;
			  font-size: 14px;
			}

			input[type=text], input[type=password] {
			  margin: 5px;
			  padding: 0 10px;
			  width: 200px;
			  height: 34px;
			  color: #404040;
			  background: white;
			  border: 1px solid;
			  border-color: #c4c4c4 #d1d1d1 #d4d4d4;
			  border-radius: 2px;
			  outline: 5px solid #eff4f7;
			  -moz-outline-radius: 3px;
			  -webkit-box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
			  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
			}
			input[type=text]:focus, input[type=password]:focus {
			  border-color: #7dc9e2;
			  outline-color: #dceefc;
			  outline-offset: 0;
			}

			input[type=button] {
			  padding: 0 18px;
			  height: 29px;
			  font-size: 12px;
			  font-weight: bold;
			  color: #527881;
			  text-shadow: 0 1px #e3f1f1;
			  background: #cde5ef;
			  border: 1px solid;
			  border-color: #b4ccce #b3c0c8 #9eb9c2;
			  border-radius: 16px;
			  outline: 0;
			  -webkit-box-sizing: content-box;
			  -moz-box-sizing: content-box;
			  box-sizing: content-box;
			  background-image: -webkit-linear-gradient(top, #edf5f8, #cde5ef);
			  background-image: -moz-linear-gradient(top, #edf5f8, #cde5ef);
			  background-image: -o-linear-gradient(top, #edf5f8, #cde5ef);
			  background-image: linear-gradient(to bottom, #edf5f8, #cde5ef);
			  -webkit-box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
			  box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
			}
			input[type=button]:active {
			  background: #cde5ef;
			  border-color: #9eb9c2 #b3c0c8 #b4ccce;
			  -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
			  box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
			}

			.lt-ie9 input[type=text], .lt-ie9 input[type=password] {
			  line-height: 34px;
			}

			</style>
			</head>
			<body>
			<section class="container">
			    <div class="login"  style="text-align: center;"">
			"""' <h1> Welcome    '+ utilisateur.username + '</h1><p><a href="'+url+'"> <p><input type="button" value=" La charge horaire " /></p></a><a href="'+urll+'"><p><input type="button" value=" Les Annonces " /></a></p><p><a href="/util/logout" ><input type="button" value="Se déconnecter" /></p></a></div></section>  </body></html>',
		
          break     
            
    return HttpResponse(html)
    #return render_to_response(html)
@csrf_exempt  
def charge(request,utilisateur_id):
    #html=' <style>table {border-collapse: collapse;width: 100%;}th, td {text-align: left;padding: 8px;}tr{background-color: rgb(242, 242, 242) }th {background-color:rgb(51, 204, 255) ; color: white;}</style><h1> Votre Charges Horaire 2017/218: </br></br><table border="2","solid"," black"><tr><th>Nom et Prénom </th><th>Nombre des Heures </th><th>Module</th><th>Matière</th><th>CC</th><th>Département</th></tr>'
    url='/util/'
    urll='/util/annonce'
     
    html="""
			<html>
			<head>
				<title></title>
				<style type="text/css">
			  html, body, div, span, applet, object, iframe,
			h1, h2, h3, h4, h5, h6, p, blockquote, pre,
			a, abbr, acronym, address, big, cite, code,
			del, dfn, em, img, ins, kbd, q, s, samp,
			small, strike, strong, sub, sup, tt, var,
			b, u, i, center,
			dl, dt, dd, ol, ul, li,
			fieldset, form, label, legend,
			table, caption, tbody, tfoot, thead, tr, th, td,
			article, aside, canvas, details, embed,
			figure, figcaption, footer, header, hgroup,
			menu, nav, output, ruby, section, summary,
			time, mark, audio, video {
			  margin: 0;
			  padding: 0;
			  border: 0;
			  font-size: 100%;
			  font: inherit;
			  vertical-align: baseline;
			}

			article, aside, details, figcaption, figure,
			footer, header, hgroup, menu, nav, section {
			  display: block;
			}

			body {
			  line-height: 1;
			}

			ol, ul {
			  list-style: none;
			}

			blockquote, q {
			  quotes: none;
			}

			blockquote:before, blockquote:after,
			q:before, q:after {
			  content: '';
			  content: none;
			}

			table {
			  border-collapse: collapse;
			  border-spacing: 0;
			}

			.about {
			  margin: 70px auto 40px;
			  padding: 8px;
			  width: 260px;
			  font: 10px/18px 'Lucida Grande', Arial, sans-serif;
			  color: #666;
			  text-align: center;
			  text-shadow: 0 1px rgba(255, 255, 255, 0.25);
			  background: #eee;
			  background: rgba(250, 250, 250, 0.8);
			  border-radius: 4px;
			  background-image: -webkit-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  background-image: -moz-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  background-image: -o-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  -webkit-box-shadow: inset 0 1px rgba(255, 255, 255, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.1), 0 0 6px rgba(0, 0, 0, 0.2);
			  box-shadow: inset 0 1px rgba(255, 255, 255, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.1), 0 0 6px rgba(0, 0, 0, 0.2);
			}
			.about a {
			  color: #333;
			  text-decoration: none;
			  border-radius: 2px;
			  -webkit-transition: background 0.1s;
			  -moz-transition: background 0.1s;
			  -o-transition: background 0.1s;
			  transition: background 0.1s;
			}
			.about a:hover {
			  text-decoration: none;
			  background: #fafafa;
			  background: rgba(255, 255, 255, 0.7);
			}

			.about-links {
			  height: 30px;
			}
			.about-links > a {
			  float: left;
			  width: 50%;
			  line-height: 30px;
			  font-size: 12px;
			}

			.about-author {
			  margin-top: 5px;
			}
			.about-author > a {
			  padding: 1px 3px;
			  margin: 0 -1px;
			}


			body {
			  font: 13px/20px 'Lucida Grande', Tahoma, Verdana, sans-serif;
			  color: #404040;
			  background: #0ca3d2;
			}

			.container {
			  margin: 80px auto;
			  width: 1000px;
			}

			.login {
			  position: relative;
			  margin: 10px auto;
			  padding: 0px 20px 20px;
			  width: 1000px;
			  background: white;
			  border-radius: 3px;
			  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
			  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
			}
			.login:before {
			  content: '';
			  position: absolute;
			  top: -8px;
			  right: -8px;
			  bottom: -8px;
			  left: -8px;
			  z-index: -1;
			  background: rgba(0, 0, 0, 0.08);
			  border-radius: 4px;
			}
			.login h1 {
			  margin: -20px -20px 21px;
			  line-height: 100px;
			  font-size: 25px;
			  font-weight: bold;
			  color: #555;
			  text-align: center;
			  text-shadow: 0 1px white;
			  background: #f3f3f3;
			  border-bottom: 1px solid #cfcfcf;
			  border-radius: 3px 3px 0 0;
			  background-image: -webkit-linear-gradient(top, whiteffd, #eef2f5);
			  background-image: -moz-linear-gradient(top, whiteffd, #eef2f5);
			  background-image: -o-linear-gradient(top, whiteffd, #eef2f5);
			  background-image: linear-gradient(to bottom, whiteffd, #eef2f5);
			  -webkit-box-shadow: 0 1px whitesmoke;
			  box-shadow: 0 1px whitesmoke;
			}
			.login p {
			  margin: 20px 0 0;
			}
			.login p:first-child {
			  margin-top: 0;
			}
			.login input[type=text], .login input[type=password] {
			  width: 278px;
			}
			.login p.remember_me {
			  float: left;
			  line-height: 31px;
			}
			.login p.remember_me label {
			  font-size: 12px;
			  color: #777;
			  cursor: pointer;
			}
			.login p.remember_me input {
			  position: relative;
			  bottom: 1px;
			  margin-right: 4px;
			  vertical-align: middle;
			}
			.login p.submit {
			  text-align: right;
			}

			.login-help {
			  margin: 20px 0;
			  font-size: 11px;
			  color: white;
			  text-align: center;
			  text-shadow: 0 1px #2a85a1;
			}
			.login-help a {
			  color: #cce7fa;
			  text-decoration: none;
			}
			.login-help a:hover {
			  text-decoration: underline;
			}

			:-moz-placeholder {
			  color: #c9c9c9 !important;
			  font-size: 13px;
			}

			::-webkit-input-placeholder {
			  color: #ccc;
			  font-size: 13px;
			}

			input {
			  font-family: 'Lucida Grande', Tahoma, Verdana, sans-serif;
			  font-size: 14px;
			}

			input[type=text], input[type=password] {
			  margin: 5px;
			  padding: 0 10px;
			  width: 200px;
			  height: 34px;
			  color: #404040;
			  background: white;
			  border: 1px solid;
			  border-color: #c4c4c4 #d1d1d1 #d4d4d4;
			  border-radius: 2px;
			  outline: 5px solid #eff4f7;
			  -moz-outline-radius: 3px;
			  -webkit-box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
			  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
			}
			input[type=text]:focus, input[type=password]:focus {
			  border-color: #7dc9e2;
			  outline-color: #dceefc;
			  outline-offset: 0;
			}

			input[type=button] {
			  padding: 0 18px;
			  height: 29px;
			  font-size: 12px;
			  font-weight: bold;
			  color: #527881;
			  text-shadow: 0 1px #e3f1f1;
			  background: #cde5ef;
			  border: 1px solid;
			  border-color: #b4ccce #b3c0c8 #9eb9c2;
			  border-radius: 16px;
			  outline: 0;
			  -webkit-box-sizing: content-box;
			  -moz-box-sizing: content-box;
			  box-sizing: content-box;
			  background-image: -webkit-linear-gradient(top, #edf5f8, #cde5ef);
			  background-image: -moz-linear-gradient(top, #edf5f8, #cde5ef);
			  background-image: -o-linear-gradient(top, #edf5f8, #cde5ef);
			  background-image: linear-gradient(to bottom, #edf5f8, #cde5ef);
			  -webkit-box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
			  box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
			}
			input[type=button]:active {
			  background: #cde5ef;
			  border-color: #9eb9c2 #b3c0c8 #b4ccce;
			  -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
			  box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
			}

			.lt-ie9 input[type=text], .lt-ie9 input[type=password] {
			  line-height: 34px;
			}
			
			</style>
			</head>
			<body>
			<style>table {border-collapse: collapse;width: 100%;}th, td {text-align: left;padding: 8px;}tr{background-color: rgb(242, 242, 242) }th {background-color:rgb(51, 204, 255) ; color: white;}</style>
"""
    
    html+='<section class="container"><a href="'+urll+'"><p><input type="button" value=" Les Annonces " /></a><a href="/util/logout" ><input type="button" value="Se déconnecter" /></a></section>'

    html+=			 """   <section class="container">
			    <div class="login"  style="text-align: center;"">
			    <h1>  La charge Horaire 2017/2018 </h1>
			    <table >
			    <tr><th>Nom et Prénom </th>
			    <th>Nombre des Heures </th>
			    <th>Module</th>
			    <th>Matière</th>
			    <th>CC</th>
			    <th>Département</th></tr>
			    

    """	
    #idd=request.GET.get("idd","idd")
    charges=chargehoraire.objects.filter(user=utilisateur_id)
    users=utilisateurs.objects.filter(id=utilisateur_id)
    for charge in charges :
        for user in users:
            
        
          html+='<tr><td>'+user.full_name+'</td><td>'+str(charge.nbrheures)+'</td><td>'+charge.module+'</td><td>'+charge.matiere+'</td><td>'+charge.cc+'</td><td>'+charge.departement+'</td></tr></div>'

    html+='</table></div></section>'
          
    return HttpResponse(html)
@csrf_exempt  
def annoncee(request):

    html="""
			<html>
			<head>
				<title></title>
				<style type="text/css">
			  html, body, div, span, applet, object, iframe,
			h1, h2, h3, h4, h5, h6, p, blockquote, pre,
			a, abbr, acronym, address, big, cite, code,
			del, dfn, em, img, ins, kbd, q, s, samp,
			small, strike, strong, sub, sup, tt, var,
			b, u, i, center,
			dl, dt, dd, ol, ul, li,
			fieldset, form, label, legend,
			table, caption, tbody, tfoot, thead, tr, th, td,
			article, aside, canvas, details, embed,
			figure, figcaption, footer, header, hgroup,
			menu, nav, output, ruby, section, summary,
			time, mark, audio, video {
			  margin: 0;
			  padding: 0;
			  border: 0;
			  font-size: 100%;
			  font: inherit;
			  vertical-align: baseline;
			}

			article, aside, details, figcaption, figure,
			footer, header, hgroup, menu, nav, section {
			  display: block;
			}

			body {
			  line-height: 1;
			}

			ol, ul {
			  list-style: none;
			}

			blockquote, q {
			  quotes: none;
			}

			blockquote:before, blockquote:after,
			q:before, q:after {
			  content: '';
			  content: none;
			}

			table {
			  border-collapse: collapse;
			  border-spacing: 0;
			}

			.about {
			  margin: 70px auto 40px;
			  padding: 8px;
			  width: 260px;
			  font: 10px/18px 'Lucida Grande', Arial, sans-serif;
			  color: #666;
			  text-align: center;
			  text-shadow: 0 1px rgba(255, 255, 255, 0.25);
			  background: #eee;
			  background: rgba(250, 250, 250, 0.8);
			  border-radius: 4px;
			  background-image: -webkit-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  background-image: -moz-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  background-image: -o-linear-gradient(top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  background-image: linear-gradient(to bottom, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.1));
			  -webkit-box-shadow: inset 0 1px rgba(255, 255, 255, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.1), 0 0 6px rgba(0, 0, 0, 0.2);
			  box-shadow: inset 0 1px rgba(255, 255, 255, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.1), 0 0 6px rgba(0, 0, 0, 0.2);
			}
			.about a {
			  color: #333;
			  text-decoration: none;
			  border-radius: 2px;
			  -webkit-transition: background 0.1s;
			  -moz-transition: background 0.1s;
			  -o-transition: background 0.1s;
			  transition: background 0.1s;
			}
			.about a:hover {
			  text-decoration: none;
			  background: #fafafa;
			  background: rgba(255, 255, 255, 0.7);
			}

			.about-links {
			  height: 30px;
			}
			.about-links > a {
			  float: left;
			  width: 50%;
			  line-height: 30px;
			  font-size: 12px;
			}

			.about-author {
			  margin-top: 5px;
			}
			.about-author > a {
			  padding: 1px 3px;
			  margin: 0 -1px;
			}


			body {
			  font: 13px/20px 'Lucida Grande', Tahoma, Verdana, sans-serif;
			  color: #404040;
			  background: #0ca3d2;
			}

			.container {
			  margin: 80px auto;
			  width: 1000px;
			}

			.login {
			  position: relative;
			  margin: 10px auto;
			  padding: 0px 20px 20px;
			  width: 1000px;
			  background: white;
			  border-radius: 3px;
			  -webkit-box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
			  box-shadow: 0 0 200px rgba(255, 255, 255, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3);
			}
			.login:before {
			  content: '';
			  position: absolute;
			  top: -8px;
			  right: -8px;
			  bottom: -8px;
			  left: -8px;
			  z-index: -1;
			  background: rgba(0, 0, 0, 0.08);
			  border-radius: 4px;
			}
			.login h1 {
			  margin: -20px -20px 21px;
			  line-height: 100px;
			  font-size: 25px;
			  font-weight: bold;
			  color: #555;
			  text-align: center;
			  text-shadow: 0 1px white;
			  background: #f3f3f3;
			  border-bottom: 1px solid #cfcfcf;
			  border-radius: 3px 3px 0 0;
			  background-image: -webkit-linear-gradient(top, whiteffd, #eef2f5);
			  background-image: -moz-linear-gradient(top, whiteffd, #eef2f5);
			  background-image: -o-linear-gradient(top, whiteffd, #eef2f5);
			  background-image: linear-gradient(to bottom, whiteffd, #eef2f5);
			  -webkit-box-shadow: 0 1px whitesmoke;
			  box-shadow: 0 1px whitesmoke;
			}
			.login p {
			  margin: 20px 0 0;
			}
			.login p:first-child {
			  margin-top: 0;
			}
			.login input[type=text], .login input[type=password] {
			  width: 278px;
			}
			.login p.remember_me {
			  float: left;
			  line-height: 31px;
			}
			.login p.remember_me label {
			  font-size: 12px;
			  color: #777;
			  cursor: pointer;
			}
			.login p.remember_me input {
			  position: relative;
			  bottom: 1px;
			  margin-right: 4px;
			  vertical-align: middle;
			}
			.login p.submit {
			  text-align: right;
			}

			.login-help {
			  margin: 20px 0;
			  font-size: 11px;
			  color: white;
			  text-align: center;
			  text-shadow: 0 1px #2a85a1;
			}
			.login-help a {
			  color: #cce7fa;
			  text-decoration: none;
			}
			.login-help a:hover {
			  text-decoration: underline;
			}

			:-moz-placeholder {
			  color: #c9c9c9 !important;
			  font-size: 13px;
			}

			::-webkit-input-placeholder {
			  color: #ccc;
			  font-size: 13px;
			}

			input {
			  font-family: 'Lucida Grande', Tahoma, Verdana, sans-serif;
			  font-size: 14px;
			}

			input[type=text], input[type=password] {
			  margin: 5px;
			  padding: 0 10px;
			  width: 200px;
			  height: 34px;
			  color: #404040;
			  background: white;
			  border: 1px solid;
			  border-color: #c4c4c4 #d1d1d1 #d4d4d4;
			  border-radius: 2px;
			  outline: 5px solid #eff4f7;
			  -moz-outline-radius: 3px;
			  -webkit-box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
			  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.12);
			}
			input[type=text]:focus, input[type=password]:focus {
			  border-color: #7dc9e2;
			  outline-color: #dceefc;
			  outline-offset: 0;
			}

			input[type=button] {
			  padding: 0 18px;
			  height: 29px;
			  font-size: 12px;
			  font-weight: bold;
			  color: #527881;
			  text-shadow: 0 1px #e3f1f1;
			  background: #cde5ef;
			  border: 1px solid;
			  border-color: #b4ccce #b3c0c8 #9eb9c2;
			  border-radius: 16px;
			  outline: 0;
			  -webkit-box-sizing: content-box;
			  -moz-box-sizing: content-box;
			  box-sizing: content-box;
			  background-image: -webkit-linear-gradient(top, #edf5f8, #cde5ef);
			  background-image: -moz-linear-gradient(top, #edf5f8, #cde5ef);
			  background-image: -o-linear-gradient(top, #edf5f8, #cde5ef);
			  background-image: linear-gradient(to bottom, #edf5f8, #cde5ef);
			  -webkit-box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
			  box-shadow: inset 0 1px white, 0 1px 2px rgba(0, 0, 0, 0.15);
			}
			input[type=button]:active {
			  background: #cde5ef;
			  border-color: #9eb9c2 #b3c0c8 #b4ccce;
			  -webkit-box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
			  box-shadow: inset 0 0 3px rgba(0, 0, 0, 0.2);
			}

			.lt-ie9 input[type=text], .lt-ie9 input[type=password] {
			  line-height: 34px;
			}
			
			</style>
			</head>
			<body>
			<style>table {border-collapse: collapse;width: 100%;}th, td {text-align: left;padding: 8px;}tr{background-color: rgb(242, 242, 242) }th {background-color:rgb(51, 204, 255) ; color: white;}</style>
"""
	

    html+='<section class="container"><a href="/util/logout" ><input type="button" value="Se déconnecter" /></a></section>'
    html+="""<section class="container">
			    <div class="login"  style="text-align: center;""><h1>  Les nouvelles annonces </h1>
			    <table>
			    <tr>
			    <th> Titre de l'annonce</th>
			    <th> Date </th>
			    <th> Contenu </th>"""

    annonces = annonce.objects.all()
    for annoncce in annonces :
     html+='<tr><td>'+annoncce.titre+'</td><td>'+str(annoncce.date)+'</td><td>'+annoncce.texte+'</td>'
    html+='</table></div></section>'

    return HttpResponse(html) 
@csrf_exempt    
def logout (request):
    return redirect('http://127.0.0.1:8000/util/', permanent=False)   

    
    
# Create your views here.
