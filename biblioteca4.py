def soma(*numeros):
    t = len(numeros)
    for x in range(t):
        soma = soma + numeros[x]
        print(soma)