class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = False
        self.comendo = False
        self.dormindo = False

    def falar(self, lingua):
        if self.dormindo == False:
            if self.comendo == False:
                if self.falando == False:
                    print(f"{self.nome}esta falando {lingua}.")
                    self.falando = True
                else:
                    print(f"{self.nome}nao pode falar porque estava falando")
            else:
                print(f"{self.nome}nao pode falar porque esta comendo")
        else:
            print(f"{self.nome} nao pode falar porque está dormindo")

    def pararFalar(self):
        print(F"{self.nome} parou de falar")
        self.falando = False

    def comer(self, alimento):
        if self.comendo == False:
            print(f"{self.nome} está comendo {alimento}")
            self.comendo = True
        else:
            print(f"{self.nome} ja esta comendo")

    def paraDeComer(self):
        print(f"{self.nome} parou de comer")
        self.comendo = False

    def dormir(self):
        if self.dormindo == False:
            print(f"{self.nome} está dormindo.")
        else:
            print(f"{self.nome} parou dormir")

    def paraDeDormir(self):
        print(f"{self.nome} parou de dormir")
        self.dormindo = False
