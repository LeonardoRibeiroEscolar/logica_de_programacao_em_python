#A CLASSE: O modelo(a planta)
class Celular:

    def __init__(self, marca, modelo, cor, bateria = 100):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.bateria = bateria
        self.ligado = False

    def ligar(self):
        if self.bateria == 0:
            print("Sem bateria! Coloque para carregar")
        else:
            self.ligado = True
            print(f" {self.modelo} Ligado!")

#Os objetos criados a partir da classe (as "casas")
celular1 = Celular("Samsung", "Galaxy s23", "Preto")
celular2 = Celular("Motorola", "MotoG", "Azul", 30)

#Acessando e alterando atributos
print(celular1.marca)

#Também podemos alterar diretamente
celular1.cor = "Branco"
print(celular1.cor)

#Chamando Métodos
celular2.ligar()