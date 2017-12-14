#!/bin/bash
#IFS=$'\n'
echo "content-type: text/html"
echo
cat "/var/www/html/listar.html"
for x in $(cat passwd) ; do
	echo "<tr>"
	for y in $(echo $x) ; do
		var1=$(echo $y | cut -d":" -f1)
		var2=$(echo $y | cut -d":" -f2)
		echo "<td>$var1</td>"
		echo "<td>$var2</td>"
	done
	echo "</tr>"
done

echo "</table>"
echo "</div>"
echo "</body>"
echo "</html>"
