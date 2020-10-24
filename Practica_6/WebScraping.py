import requests
from bs4 import BeautifulSoup

url="https://www3.animeflv.net"

def ObtenerPag(url):
    pagina = requests.get(url)
    soup = BeautifulSoup(pagina.content, "html.parser")
    Animesrevueltos = soup.find_all("a", class_="fa-play-circle")
    ObtenerLista(Animesrevueltos)


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


def Imprimir(Lista_Animes):
    print(">>>|\t***\t***\t***\t***\t***\tAnimes en emisión\t***\t***\t***\t***\t***\t|<<<\n")
    print("|{:^50}|{:^10}|{:^100}|".format("Nombre",
           "Tipo", "link"))
    for elemento in Lista_Animes:
        if len(Lista_Animes[elemento][1]) > 50 or len(Lista_Animes[elemento][0]) > 100:

            print("|{:^50}|{:^10}|{:^100}|".format(Lista_Animes[elemento][1][0:50],
                   Lista_Animes[elemento][2],
                   Lista_Animes[elemento][0][0:100]))
            print("|{:^50}|{:^10}|{:^100}|".format(Lista_Animes[elemento][1][50:],
                   "", Lista_Animes[elemento][0][100:]))

        else:
            print("|{:^50}|{:^10}|{:^100}|".format(Lista_Animes[elemento][1],
                   Lista_Animes[elemento][2],
                   Lista_Animes[elemento][0]))

ObtenerPag(url)
