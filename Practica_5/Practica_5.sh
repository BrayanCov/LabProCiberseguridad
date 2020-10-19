#!/bin/bash

for elemento in { "fcfm.png" "msg.txt" "mystery_img1.txt" "mystery_img2.txt" }
do
	if [ $elemento == "fcfm.png" ];
	then
		echo "Para $elemento"
		cat $(find /home/$(whoami) -name $elemento | head -n 1) | base64 > fcfm.txt 	
		echo "Se a codificado $elemento y se creo fcfm.txt"
		comprobacion=$(md5sum $(find /home/$(whoami) -name $elemento | head -n 1) | grep -c "4260808329804b5f553cf3e3d5a446c6")
		if [ $comprobacion == 1 ];
		then
			echo "El archivo no recibio ninguna alteración"
		else
			echo "El archivo ha recibido una o más alteraciones, podria no ser seguro"
		fi
	elif [ $elemento == "msg.txt" ];
	then
		echo "Para $elemento"
		cat $(find /home/$(whoami) -name $elemento | head -n 1) | base64 > msg_codificado.txt 	
		echo "Se a codificado $elemento y se creo msg_codificado.txt"
		comprobacion=$(md5sum $(find /home/$(whoami) -name $elemento | head -n 1) | grep -c "40744679dff4bf36705c00f9cb815579")
		if [ $comprobacion == 1 ];
		then
			echo "El archivo no recibio ninguna alteración"
		else
			echo "El archivo ha recibido una o más alteraciones, podria no ser seguro"
		fi
	elif [ $elemento == "mystery_img1.txt" ];
	then
		echo "Para $elemento"
		cat $(find /home/$(whoami) -name $elemento | head -n 1) | base64 --decode > mystery_img1.jpg 	
		echo "Se a decodificado $elemento y se creo mystery_img1.jpg"
		comprobacion=$(md5sum $(find /home/$(whoami) -name $elemento | head -n 1) | grep -c "5db9862819edb16f9ac0f3b1c406e79d")
		if [ $comprobacion == 1 ];
		then
			echo "El archivo no recibio ninguna alteración"
		else
			echo "El archivo ha recibido una o más alteraciones, podria no ser seguro"
		fi
	elif [ $elemento == "mystery_img2.txt" ];
	then
		echo "Para $elemento"
		cat $(find /home/$(whoami) -name $elemento | head -n 1) | base64 --decode > mystery_img2.jpg
		echo "Se a decodificado $elemento y se a creado mystery_img2.jpg"
		comprobacion=$(md5sum $(find /home/$(whoami) -name $elemento | head -n 1) | grep -c "b091a841da98ca516635f4dfea1dbaf5")
		if [ $comprobacion == 1 ];
		then
			echo "El archivo no recibio ninguna alteración"
		else
			echo "El archivo ha recibido una o más alteraciones, podria no ser seguro"
		fi
	fi
done
#4260808329804b5f553cf3e3d5a446c6 *fcfm.png
#5db9862819edb16f9ac0f3b1c406e79d *mystery_img.txt
#b091a841da98ca516635f4dfea1dbaf5 *mystery_img2.txt
#40744679dff4bf36705c00f9cb815579 *msg.txt
