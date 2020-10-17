#!/bin/bash
function pause(){
	read -p "$*"
}
echo "Este programa crea usuarios y los borra"
who=$(whoami)
if [ $who != "root" ];
then
	echo "Esta usando un usario normal, necesita usar root"
	exit
fi
op=0
while [ $op != 3 ]
do
clear
echo "  |Opciones|
1-Crear Usuario
2-Eliminar Usuario
3-Salir"
echo "Elige una opción:"
read op
case $op in 
	1)
		echo "Nombre del Usuario:"
		read Usuario
		sudo adduser $Usuario
		#echo $Usuario
		clear
		echo "Se a agregado:"
		ls /home
		pause "Presiona enter  para contiuar..."
	;;
	2)
	       echo "Nombre del Usuario:"
               read Usuario
               #echo $Usuario
	       sudo userdel -r $Usuario
	       clear
	       echo "Se a eliminado:"
	       ls /home
	       pause "Presiona enter  para contiuar..."
        ;;
        3)
		echo "Saliendo..."
	;;
        *)
	       echo "Instruccion no valida"
	;;	       
esac
done

