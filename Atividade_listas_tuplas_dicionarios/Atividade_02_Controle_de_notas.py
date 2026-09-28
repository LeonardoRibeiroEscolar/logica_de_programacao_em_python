#1. Criar uma lista contendo 5 notas.
notas = [10.0, 9.5, 6.7, 6.9, 4.5]
#2. Exibir todas as notas.
print(notas)
#3. Calcular a soma das notas.
soma = 0
soma = soma + notas
print(f"Soma das notas: {soma}")
#4. Calcular a média das notas.
media = soma / len(notas)
print(f"Media das notas: {media}")
#5. Identificar a maior nota.
notamaior = 0

notamaior = max(nota)
print(f"Nota maior: {notamaior})
#6. Identificar a menor nota.
notamenor = 0

notamenor = min(nota)
print(f"Notamenor: {notamenor}")
#7. Verificar se existe uma nota igual a 10...

if nota == 10:
    print("Há notas iguais a 10")
#8. Informar se o estudante foi aprovado ou reprovado.
#9. Considerar média igual ou superior a 7 como aprovação.

if nota >=  7 :
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
