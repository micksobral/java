nomes = [""]*5
senhas = [""]*5
tam = len(nomes)

for x in range(tam):
    nomes[x]=input("digite o usuario: ")
    senhas[x]=input("digte sua senha: ")

for y in range(tam):
    print(f"pisiçao: {y} - nomes {nomes[y]} senha: {senhas[y]}")


    #correçao do prof


