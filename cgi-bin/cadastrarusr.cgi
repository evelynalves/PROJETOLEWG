#!/bin/bash

echo "Content-type: text/html"
echo

read POST

foi(){
 cat '/var/www/html/sucessoc.html'
}

foinao(){
 cat '/var/www/html/falhacc.html'
}

usuario=$(echo $POST | cut -d"&" -f1 | cut -d"=" -f2)
senha=$(echo $POST | cut -d"&" -f2 | cut -d"=" -f2)
if [[ ! $(grep "^$usuario:" passwd) ]] ; then
        echo "$usuario:$senha" >> passwd
        foi
else
        foinao
fi
