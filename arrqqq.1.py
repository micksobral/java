
from bibliotarq import  *


#texto = input("digite seu texto: ")


while True:
    opcao = int(input("digite sua opçao\n"
                      "1 prar Gravar\n"
                      "2 para LER\n"
                      "3 para SAIR\n"))

    match opcao:
        case 1:
            t = input("digite o tesxto:")
            Gravartexto(t)
        case 2:
            LerTexto()
        case 3:
            break
        case _:
            print("opçao invalida")
