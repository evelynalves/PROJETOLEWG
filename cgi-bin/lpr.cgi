#!/bin/bash

echo "Content-type: text/html"
echo

read x

x=$(echo $x | cut -d"=" -f2)

locali(){
	cat '/var/www/html/mostrar1.html'
}

andar(){
	cat '/var/www/html/mostrar2.html'

}

sala(){
	cat '/var/www/html/mostrar3.html'
}

np(){
	cat '/var/www/html/mostrar4.html'
}

ns(){
	cat '/var/www/html/mostrar5.html'

}

marca(){
	cat '/var/www/html/mostrar6.html'

}

model(){
	cat '/var/www/html/mostrar7.html'

}

opcao(){
case $x in
	"Localidade") locali ;;
	"Andar") andar ;;
	"Sala") sala ;;
	"NP") np ;;
	"NS") ns ;;
	"Marca") marca ;;
	"Modelo") model ;;
esac
}

opcao
