#!/bin/bash
read VALOR

echo "content-type: text/html"
echo

LOCAL=$(echo $VALOR | cut -d"&" -f1 | cut -d"=" -f2)
ANDAR=$(echo $VALOR | cut -d"&" -f2 | cut -d"=" -f2)
SALA=$(echo $VALOR | cut -d"&" -f3 | cut -d"=" -f2)
NP=$(echo $VALOR | cut -d"&" -f4 | cut -d"=" -f2)
NS=$(echo $VALOR | cut -d"&" -f5 | cut -d"=" -f2)
MARCA=$(echo $VALOR | cut -d"&" -f6 | cut -d"=" -f2)
MODELO=$(echo $VALOR | cut -d"&" -f7 | cut -d"=" -f2)
DESCRICAO=$(echo $VALOR | cut -d"&" -f8 | cut -d"=" -f2)

echo "$LOCAL:$ANDAR:$SALA:$NP:$NS:$MARCA:$MODELO:$DESCRICAO" >> estoque

cat '/var/www/html/items.html'



