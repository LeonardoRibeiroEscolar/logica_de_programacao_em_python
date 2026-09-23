#1. Criar uma lista contendo inicialmente 5 filmes.
filmes = ["Pânico", "Eu sou a lenda", "Cargo", "Midsommar", "Rubber o pneu assasino"]
#2. Exibir todos os filmes cadastrados.
print(filmes)
#3. Exibir o primeiro filme da lista.
print(filmes[0])
#4. Exibir o último filme da lista.
print(filmes[-1])
#5. Adicionar um novo filme ao final da lista.
filmes.append("Cristine o carro assasino")
#6. Inserir um novo filme em uma posição específica.
filmes.insert(1, "Gingerbread man vs evil bong")
#7. Remover um filme da lista.
filmes.remove("Pânico")
#8. Alterar o nome de um dos filmes.
filmes[0] = "Attack of killer tomatoes"
#9. Exibir a quantidade de filmes cadastrados.
print(len(filmes))
#10. Verificar se um determinado filme está presente na lista.

if "Cargo" in filmes:
    print("Esse filme existe na lista")
else:
    print("Esse filme não existe na lista")
print(filmes)