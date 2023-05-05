#!/bin/bash
  
  echo "content-type: text/html"
  echo
  echo
  echo "
  <html> <head> <title> CGI script </title> </head>
  <body>
  <h1>USO DE DISCO</h1>
  "
	echo "<h1><pre>$(ps waux | wc -l)</pre></h1>"
#	echo "<center><h1>$a</h1></center>"
  "
  </body>
  </html>
  "
