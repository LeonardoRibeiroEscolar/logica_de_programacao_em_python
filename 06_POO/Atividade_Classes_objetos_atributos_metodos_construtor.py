class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: Au au!")

    def mostrar_info(self):
        print(f"nome: {self.nome}, Raça: {self.raca} idade: {self.idade}")


cachorro1 = Cachorro("Rex" , "Bulldog", "4")
cachorro2 = Cachorro("Totó", "Pitbull", "5")
print(cachorro1.latir())
print(cachorro1.mostrar_info())
print(cachorro2.latir())
print(cachorro2.mostrar_info())