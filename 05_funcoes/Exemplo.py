#Oque é uma função:

# Uma função é um bloco de código criado para realizar uma determinada tarefa.
#Ela permite organizar e reutilizar código.

#1. Criando uma função
#Utilizar a palavra def para uma função

def saudacao():
    print("Olá, seja bem-vindo")

saudacao()

#2. Criando uma função com parâmetro

#Parâmetros permitem enviar informações para a função.

def saudacao(nome):
    print(f"Olá {nome}")

saudacao("Ana")
saudacao("João")

#3. Mais de um parâmetro
def apresentar(nome , idade):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")

apresentar("Maria", 17)
apresentar("João", 20)

#4. Função com calculo

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"Resultado {resultado}")

somar(10 , 20)
somar(10 , 90)

#5. Retornando um valor
#Devolve um valor para o local onde a função foi chamada

def somar(numero1, numero2):
    return numero1 + numero2

print(somar(10 , 5))

#6. Função com condição
def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(verificarIdade(20))

#7. Parâmetro com valor padrão
def saudacao(nome = "aluno"):
    print(f"Olá {nome}")

saudacao("João")
saudacao()

#8. Função utilizando lista

def calcularMedia(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)

notas = [8, 7, 9, 10]
media = calcularMedia(notas)
print(f"Media: {media}")

#9. funcões para organizar um programa
def cadastrar_produto():

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço"))
    return nome, preco

def exibir_produto(nome, preco):

    print("\n===== PRODUTO =====")
    print(f"Nome: {nome}")
    print(f"preço: {preco:.2f}")

nome, preco = cadastrar_produto()
exibir_produto(nome, preco)
