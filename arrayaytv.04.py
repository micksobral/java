#faça um codigo para ler 5 numeros numeros e armazenar em um vetor. apos a leitura total dos 5 numeros
# o codigo deve escrever esses5 numeros lidos na oredem inversa.


cod = [0,0,0,0,0]
tam = len(cod)
notas = 0
for x in range(tam):
    cod[x]= float(input("digite um nmr:"))

for i in range (tam-1, 0-1, -1):
    print(cod[i])