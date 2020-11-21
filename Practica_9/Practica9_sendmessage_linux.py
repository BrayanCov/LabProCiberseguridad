#!/usr/bin/env python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import json
import argparse
try:
    parser = argparse.ArgumentParser(description = "Enviar mensajes --sintaxis: cat <Archivo de correos> | xargs -I {} python Practica9_sendmessage.py -list {} -m <mensaje|>")
    parser.add_argument("-list","--emaillist", type=str, metavar="", help="Path de la lista de correos") 
    parser.add_argument("-m","--message", type=str, metavar="", help="mensaje que se enviara")
    args=parser.parse_args()
    list=args.emaillist
    message=args.message
    #print(message)
    #print(list)
    #print(type(list))
    if message==None or list==None:
        print("Error al llenar")
        exit()
    
    data = {}
    with open('pass.json') as f:
            data = json.load(f)
    # create message object instance
    msg = MIMEMultipart()
    #message = message
    # setup the parameters of the message
    msg['From'] = data['user']
    msg['To'] = list
    msg['Subject'] = "Prueba -Correos-"
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    #create server
    server = smtplib.SMTP('smtp.office365.com:587')
    server.starttls()
    # Login Credentials for sending the mail
    print(data['user'])
    server.login(data['user'], data['pass'])
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    print("successfully sent email to %s:" % (msg['To']))
    
except TypeError:
    print("Error, formato de entrada no valido")
except IOError, e:
    print("Error en: "+str(e))
