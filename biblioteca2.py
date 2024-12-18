#biblioteca do exercio funcoes2
def vogais(texto):
    soma = 0
    for i in texto:
        if i in "abcdefghijklmnopqrsduvxyz":
            soma +=1
    print(f"o texto tem {soma} letras")
