#!/bin/bash
LAST=`cat estoque | wc -l`
OPCAO="1"
SEQUENCIA=`seq 1 $LAST`
DIGITO="2"
for VAR in $SEQUENCIA
do
if [[ `sed -n $VAR'p' estoque | cut -f1 -d:` -eq $DIGITO ]]; then
	echo `sed -n $VAR'p' estoque`; else
	echo "NOT FOUND";
fi
done


#if [[ `sed -n 23'p' estoque | cut -f3 -d:` -eq 5 ]]; then
#echo `sed -n 23'p' estoque`; else
#echo "NOT FOUND";
#fi

