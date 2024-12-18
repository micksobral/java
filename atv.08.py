#faça um algoritmo que leia 10 valores do tipo inteiro e armazene-os em um vetor. a seguir o algoritmo devera informar
#1- todos os nmrs pares q existe no vetor.
#2- o menor e o maior valor existente no vetor;
#3--quantos dos valores do vetor sao maiores que a media desses valores


nmr = []*10
tam = len(nmr)
maior = 0
menor = 1000000000000


for i in range(tam):
    nmr[i] =  int(input("digite um numero: "))

for y in range(tam):
    if nmr [y]%2==0:
        print(nmr[y],end= "")

    if nmr[y]>maior:
        maior=nmr[y]
        print()
    if nmr[y]<menor:
        menor=nmr[y]

#maior  = max(nmr)
#menor = min(nmr)

#import numpy as np

#media = np.mean(nmr)
#print("="*10)
#print(media)
#print(maior)
#print(menor)



