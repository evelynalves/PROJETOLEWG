#!/bin/bash
IFS=$'\n'
echo "content-type: text/html"
echo
read LOCAL

PESQUISA=$(echo $LOCAL | cut -d"=" -f2)

##PESQUISA="$CAMPO:"
cat "/var/www/html/estoque5.html"

for x in $(grep -Ei "(.*:){4}$PESQUISA(:.*){3}" estoque); do
	echo "<tr>"

	for y in $(echo $x) ; do
		var1=$(echo $y | cut -d":" -f1)
		var2=$(echo $y | cut -d":" -f2)
		var3=$(echo $y | cut -d":" -f3)
		var4=$(echo $y | cut -d":" -f4)
		var5=$(echo $y | cut -d":" -f5)
		var6=$(echo $y | cut -d":" -f6)
		var7=$(echo $y | cut -d":" -f7)
		var8=$(echo $y | cut -d":" -f8)
		echo "<td>$var1</td>"
		echo "<td>$var2</td>"
		echo "<td>$var3</td>"
		echo "<td>$var4</td>"
		echo "<td>$var5</td>"
		echo "<td>$var6</td>"
		echo "<td>$var7</td>"
		echo "<td>$var8</td>"
	done
	echo "</tr>"
done

echo "</table>"
echo "</div>"
echo "</body>"
echo "</html>"
