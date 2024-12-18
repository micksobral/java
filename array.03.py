#preencher um vetor A com 10 numeros.ok logo em seguida, ler mais um numero e guardar em uma variavel X.ok
# armazenar em um vetor M o resultado de cada elemento de A mulltiplicado peço valor X
#no finaç imprimir o vetor M.


A = [0,0,0,0,0,0,0,0,0,0]
X = 0
M = [0,0,0,0,0,0,0,0,0,0]
tamanho = len(A)
for y in range(tamanho):
    A[y]= int(input("digite o nmr"))
x = int(input("digite o mult"))
for i in range(tamanho):
    M[i]=A[i]*x

print(A)
print(X)
print(M)