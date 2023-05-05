#!/bin/bash
  
  echo "content-type: text/html"
  echo
  echo
  echo "
  <html> <head> <title> CGI script </title> </head>
  <body>
  <h1>MÁQUINAS LIGADAS</h1>
  "
	l=1
	while [ $l -lt 21 ]
	do
#   		echo "pingando máquina $l"
   		ping -c 2 10.100.64.$l > pinga1 2> pinga2
   		a=`cat pinga1|grep received|cut -d"," -f2|cut -d" " -f2`
#   		echo $a
   		if [ $a -eq 0 ];
   		then
       			echo "<center><h1>Maquina $l não OK</h1></center>"
   		else
       			echo "<center><h1>Maquina $l OK</h1></center>"
   		fi
   		l=`echo $l+1|bc`
#   sleep 2
	done
#cat log_ping

  echo "
  </body>
  </html>
  "
