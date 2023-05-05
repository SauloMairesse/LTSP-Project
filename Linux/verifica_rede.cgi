#!/bin/bash
  
echo "content-type: text/html"
echo
echo
echo
	"
	  	<html> <head> <meta charset='utf-8' /> <title> CGI script </title> </head>
  			<body>
  				<h1>Configurações de Rede</h1>
				"
					echo "<pre>$(ifconfig)</pre>"
					echo 
				"
  			</body>
  		</html>
	"
