class Animal:
    def __init__(self,nome, cor):
        self.nome = nome
        self.cor = cor


    def comer(self):
        print(f"o animal chamado: {self.nome} foi comer")

class Gato(Animal):
    def __init__(self,nome, cor):
     super().__init__(nome,cor)

    def miar(self):
         print(f"o {self.nome} está miando.")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def latir(self):
        print(f"{self.nome} esta latindo")

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def pular(self):
        print(f"{self.nome} esta pulando")

class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def moo(self):
        print(f"{self.nome} esta fazendo moo")