#!/bin/bash
instalar(){
echo
echo "Instalando Apache2"
echo
echo "Update"
apt-get update
sleep 1
apt-get install apache2 -y

        echo "AddDefaultCharset UTF-8" >> /etc/apache2/conf-enable/charset.conf
        a2enmod cgid
        systemstl restart apache2
        service apache2 restart

cp -r ./html /var/www/
cp -r ./cgi-bin /usr/lib
ln -s '/usr/lib/cgi-bin' /var/www/html/cgi-bin
chmod 777 /var/www/html/*
chmod 777 /usr/lib/cgi-bin/*
chown root:www-data /usr/lib/cgi-bin
sleep 1
}

naoinstalar(){
echo
echo "OK, aceitamos sua decisao"
echo "Caso queira instalar depois, execute como root: # bash install.sh"
echo
sleep 2
exit 0;
clear
}

echo
echo "Bem-vindo ao sistema de instalação"
echo "Os programas a ser instalado"
echo "- Apache2"
echo "Formatação dos diretorios"
echo
echo "- /var/www/html"
echo "- /usr/lib/cgi-bin"
echo
read -p "Deseja continuar com a instalação? (s ou n)?" opcao
case $opcao in
        [sS][iI]*[mM]*) instalar ;;
        [nN][aAãÃ]*[oO]*) naoinstalar ;;
esac
