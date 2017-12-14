#!/bin/bash
remover(){
echo
echo "Iniciando Desinstalação"
rm -rf /var/www/html/*
rm -rf /usr/lib/cgi-bin/*
sleep 1
apt-get remove apache2 --purge -y
apt-get purge apache2 -y
apt-get autoremove -y
sleep 1
clear
read -p "Apache2 Desinstalado, Obrigado [enter]"
exit 0
}
naoremover(){
echo "OK, aceitamos sua decisão"
echo "Caso queira desinstalar depois, execute como root: # bash remove.sh"
echo "-------------------------------------------------------------------"
}
echo
echo "Desinstalador dos Programas"
echo "- Apache2"
echo
read -p "Deseja continuar desinstalação? (s ou n)" opcao
case $opcao in
        s) remover ;;
        S) remover ;;
        n) naoremover;;
        N) naoremover;;
        *) read -p "Opção invalida, tente novamente!"; sleep 2 ; exit 0 ;;
esac
