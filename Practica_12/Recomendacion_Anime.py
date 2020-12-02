import requests
import tkinter
from random import choice
from bs4 import BeautifulSoup

url="https://www3.animeflv.net"

def ObtenerPag(url):
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    Animesrevueltos = soup.find_all("a", class_="fa-play-circle")
    ObtenerLista(Animesrevueltos)

def ObtenerSinposis(url):
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    Animesrevueltos = soup.find_all("div", class_="Description")
    return Animesrevueltos[0].text

def ObtenerLista(Animesrevueltos):
    Lista_Animes = {}
    x=1
    for elemento in Animesrevueltos:
        nombre=""
        elemento_split=elemento.text.split()
        for anime in elemento_split[:len(elemento_split)-1]:
            nombre+=anime + " "
        nombre=nombre[:len(nombre)-1]
        Lista_Animes["Anime Nuevo %s" %x]=[url+elemento["href"],
                      nombre, elemento_split[-1]]
        x+=1
    Imprimir(Lista_Animes)

def aleatorio(Lista_Animes):
    list=[]
    for elemento in Lista_Animes:
        list+=[elemento,]
    aleator=choice(list)
    return aleator

def boton(Lista_Animes, etiqueta2, etiqueta3):
    ale=aleatorio(Lista_Animes)
    etiqueta2["text"]=Lista_Animes[ale][1]
    etiqueta3["text"]=ObtenerSinposis(Lista_Animes[ale][0])

def Imprimir(Lista_Animes):
    #list=[]
    #for elemento in Lista_Animes:
    #    list+=[elemento,]
    ale=aleatorio(Lista_Animes)
    #print(Lista_Animes[ale][1])
    #print(ObtenerSinposis(Lista_Animes[ale][0]))
    ventana = tkinter.Tk()
    ventana.geometry("480x430")
    ventana.title("Animeflv")
    ventana.iconbitmap("aw.ico")
    ventana.configure(bg="#990099")
    etiqueta1 = tkinter.Label(ventana, text = "Recomendación de animeflv", font="Helvetica 20", fg="white", bg="#990099")
    etiqueta1.pack(fill = tkinter.X)
    etiqueta2 = tkinter.Label(ventana, text = Lista_Animes[ale][1], fg="white", font="Helvetica 14", bg="#990099")
    etiqueta2.pack(fill = tkinter.X)
    etiqueta3 = tkinter.Label(ventana, text = ObtenerSinposis(Lista_Animes[ale][0]), fg="white", wraplength = 450, font="Helvetica 11", bg="#990099")
    etiqueta3.pack()
    buton1 = tkinter.Button(ventana, text = "Otro", padx = 20, pady = 10, \
                            command = lambda: boton(Lista_Animes, etiqueta2, etiqueta3), bg = "CadetBlue", font="Helvetica 15")
    buton1.pack(expand = True)
    ventana.mainloop()

ObtenerPag(url)
