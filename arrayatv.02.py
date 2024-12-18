    #escreva um codigo que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor,ok
    # calcular a  media da turma e contar quntaos alunos obtiveram nota acima desta media calculada
    #escrever a media da turma e o resultado da contagem

notas = ["","","","",""]
cont = 0
soma = 0
tamanho = len(notas)
for x in range(tamanho):
    notas[x] = float(input("digite seu nota: "))


for y in range(tamanho):
    soma +=notas[y]
media = soma/tamanho

for i in range(tamanho):
    if notas[i]>media:
        cont+=1

print(F"{cont} alunos com a nota maior que a {media}")



