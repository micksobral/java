#faça um alogoritmio que solicite ao usuario a entrada de 5 nomes, e que exiba a lista desses nomes na tela.
#apois exibir essa lista, o prog deve mostrar tambem os nomes na ordem inversa em que o usuario os digitou, um por linha


nomes = [""]*5
tam = len(nomes)

for i in range(tam):
    nomes[i] = input("digite o nome: ")
    lista.reverse(nomes)
