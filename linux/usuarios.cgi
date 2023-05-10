#!/bin/bash
  
  echo "content-type: text/html"
  echo
  echo
  echo "
  <html> <head> <title> CGI script </title> </head>
  <body>
  <h1>USUARIOS LOGADOS AGORA</h1>
  "
  
  echo "<pre>$(who)</pre>"
  
  echo "
  </body>
  </html>
  "
