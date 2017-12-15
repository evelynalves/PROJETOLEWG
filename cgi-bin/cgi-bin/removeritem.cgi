#!/bin/bash

read post

echo "content-type: text/html"
echo

foi(){
cat '/var/www/html/removers.html'
}

foinao(){
cat '/var/www/html/removere.html'
}


item=$(echo $post | cut -d"=" -f2)
if [[ $(grep -E "(.*:)$item(:.*){4}" estoque ) ]] ; then
       $(sed -ri "/(.*:)$item(:.*){4}/d" estoque)
	foi
else
	foinao
fi

