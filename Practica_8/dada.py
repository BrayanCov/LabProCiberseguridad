import ftplib

def Explorar_Server():
    things = ftp_server.nlst()
    foundth = []
    ftp_server.retrlines("LIST", foundth.append)
    for th in things:
        if foundth[things.index(th)].startswith("dr"):
            print(">>>> Elementos encontrados:", ftp_server.nlst())
            print("\n>> Entrando a", th, "\n")
            ftp_server.cwd(th)
            Explorar_Server()
        elif th == "README" or th.startswith("README") or th.endswith(".txt") or th.endswith(".msg"):
            print("[+]Archivo encontrado", th, ">Descargado<")
            with open(th, "wb") as fp:
                ftp_server.retrbinary("RETR "+th, fp.write)
    ftp_server.cwd("..")

def Conexion_Server(server, usuario, correo):
    global ftp_server
    ftp_server = ftplib.FTP(server, usuario, correo)
    Explorar_Server()
    ftp_server.quit()

Ruta = "ftp.us.debian.org"
Conexion_Server(server=Ruta, usuario="anonymous",correo="nobody@nourl.com")
print("\nSaliendo de", Ruta)
