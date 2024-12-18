#faça um codigo para ler 5 nomes de usuarios e sua respectivas senhas, e armazenar cada lista em um
#array diferente, apos completar a digitiçao, imprimir, nome, senha e posiçao dos dados no array.

usuario1 = ["","","","","",]
senha1 = ["","","","",""]
cont = 0
tam = len(usuario1)

for i in range(tam):
    usuario1[i] = input("digite seu usuario: ")
    senha1[i] = input("digite a senha: ")
    print("usuário e senha cadastrado com sucesso!")

    for i in range(tam):
        usuario1 = input("Digite seu usuário: ")
        senhas1 = input("digite sua senha: ")

        if usuario1 == usuario1[i]:
            if senhas1 == senhas1[i]:
                print(f"login efetuado com sucesso {usuario1[i]}")

        else:
            print()


for x in range(5):
    print(f"usuario:{usuario1}senha: {senha1}")


