#!/bin/bash
  
echo "content-type: text/html"
echo
echo
echo
	"
	  	<html> <head> <meta charset='utf-8' /> <title> CGI script </title> </head>
  			<body>
  				<h1>Algumas informações sobre a máquina que o CGI está rodando</h1>
				"
					echo "<h4>who</h4>"
					echo "<pre>$(who)</pre>"
					echo "<h4>last -20</h4>"
					echo "<pre>$(last -20)</pre>"
					echo "<h4>ifconfig</h4>"
					echo "<pre>$(ifconfig)</pre>"
					echo "<h4>ps waux</h4>"
					echo "<pre>$(ps waux)</pre>"
					echo 
				"
  			</body>
  		</html>
	"
