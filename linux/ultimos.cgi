#!/bin/bash
  
  echo "content-type: text/html"
  echo
  echo
  echo "
  <html> <head> <title> CGI script </title> </head>
  <body>
  <h1>ULTIMOS USUARIOS QUE USARAM O SISTEMA</h1>
  "
	echo "<pre>$(last -50)</pre>"
#	echo "<center><h1>$a</h1></center>"
  "
  </body>
  </html>
  "
