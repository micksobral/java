class Atleta:
    def __init__(self,nome,peso):
        self.nome = nome
        self.aposentado = False
        self.peso = peso
        self.aquecido = False
        

    def aquecer(self):
        print(f"o atleta {self.nome} foi aquecer.")
        self.aquecido= True


    def aposentar(self):
        print(f"o atleta {self.nome} está aposentado")
        self.aposentado = True

    def corredor(Atleta):
        def __init__(self, nome,peso):
            super().__init__(nome, peso)
        def correr(self):
            if self.aquecido == True:
                if self.aposentado == False:
                    print(f"{self.nome}foi correr...")
                else:
                    print(f"o {self.nome} nao pode correr porque esta aposentado")
            else:
                print(f"{self.nome} nao pode correr pq nao aqueceu")

class triatleta