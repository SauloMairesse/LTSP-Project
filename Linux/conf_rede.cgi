#!/bin/bash
  
  echo "content-type: text/html"
  echo
  echo
  echo "
  <html> <head> <title> CGI script </title> </head>
  <body>"

  if [ "$QUERY_STRING" ];then
  	echo "QUERY_STRING   $QUERY_STRING"
	interface=$(echo $QUERY_STRING | sed 's/.*\&interface=//' | cut -d"&" -f1 | cut -d"=" -f2)
	ip=$(echo $QUERY_STRING | sed 's/.*\&ip=//' | cut -d"&" -f1)
	mask=$(echo $QUERY_STRING | sed 's/.*\&mask=//' | cut -d"&" -f1)

  	echo "<br>"
  	echo "<center>Interface <b>$interface</b> configurada com IP <b>$ip</b> e mascara <b>$mask</b></center>"
  	echo "<pre>"
#	echo "<pre>$(ifconfig $interface $ip/$mask)</pre>"
	echo "ifconfig $interface $ip/$mask" > /tmp1/a
  	echo "</pre>"
  else
  	echo "
  	<form method=\"GET\" action=\"conf_rede.cgi\">
  	<b>Entre com o nome ou IP do host para o ping:</b> 
  	<input size=40 name=host value=\"\">
  	<input type=hidden size=40 name=teste value=\"nada\">
  	</form>"
  fi

  echo "
  </body>
  </html>
  "
