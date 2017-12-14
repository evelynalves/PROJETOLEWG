#!/bin/bash
read login
falhou(){
cat /var/www/html/falhac.html
}

administrador(){
cat /var/www/html/pgnadm.html
exit 0
}

tecnico(){
cat /var/www/html/pgntec.html
exit 0
}

usuario(){
cat /var/www/html/pgnusr.html 
exit 0
}

passou(){
case $1 in
	"administrador") administrador ;;
	"tecnico") tecnico ;;
	*) usuario ;; 
esac
}

verifica(){
USER=$1
PASS=$2
SENHA=$(cat passwd | grep ^$USER: | cut -d":" -f2)
[[ $PASS == $SENHA ]] && passou $USER || falhou
}

USER=$(echo $login | cut -d"&" -f1 | cut -d"=" -f2 )
PASS=$(echo $login | cut -d"&" -f2 | cut -d"=" -f2 )
echo content-type: text/html
echo

[[ $(cat passwd | cut -d":" -f1 | grep ^$USER$) ]] && verifica $USER $PASS || falhou
