def Gravartexto(texto):
    with open("arq.txt", "a") as arquivo:
        arquivo.write(texto)

def LerTexto():
    with open("arq.txt", "r") as arquivo2:
        txt = arquivo2.read()
        print(txt)