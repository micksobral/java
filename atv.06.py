#faça um codigo para ler 10 numero e guardar num vetor. apois isto, ler mais um numero qualquer, calcular e escrever
#quantas vezes esse numero aparece no vetror


nmr = [""]*10
tam = len(nmr)
cont = 0
for x in range(tam):
    nmr[x] = int(input("digite um numero: "))


nmr1= int(input("digite mais um numero: "))

for i in range(tam):
    if nmr1 == nmr[i]:
         cont+=1
print(f"numero se repete:{cont}")

