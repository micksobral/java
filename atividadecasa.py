usuario = [""] * 2
senhas = [""] * 2
tam = len(usuario)


for x in range(tam):
    usuario[x] = input("digite seu nome: ")
    senhas[x] = input("crie uma senha: ")
    print("usuário e senha cadastrado com sucesso!")

for i in range(tam):
    usuario1 = input("Digite seu usuário: ")
    senhas1 = input("digite sua senha: ")

    if usuario1 == usuario[x]:
      if senhas1 == senhas[x]:
       print(f"login efetuado com sucesso {usuario[i]}")

    else:
        print("login ou senha errada. ")