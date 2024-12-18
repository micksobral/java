#crie um array tamanho 5 e preencher com os nomes dos 5 alunos, informaados pelo usuario

nomes = ["","","","",""]

tamanho = len(nomes)
for i in range(tamanho):
    nomes [i] =  input("digite seu nome: ")

for i in range(tamanho):
    print(nomes[i])