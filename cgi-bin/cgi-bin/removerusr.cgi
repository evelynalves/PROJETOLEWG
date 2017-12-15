#!/bin/bash

read post

echo "Content-type: text/html" 
echo


foi(){
cat '/var/www/html/removerc.html'
}

foinao(){
cat '/var/www/html/removere.html'
}

usuario=$(echo $post | cut -d"=" -f2)
if [[ $(grep -E "^$usuario\:" passwd) ]] ; then
      $(sed -ri "/^$usuario\:/d" passwd)
	foi
else
	foinao
fi
