#Operadores logicos e estruturas condicionais

#1. Operadores logicos
#and : Todas as condições precisam ser verdadeiras
idade = 20

possui_carteira = True

resultado = idade >= 18 and possui_carteira
print(resultado)

#or : pleo mneos uma condição precisa ser verdadeira
idade  = 16

acompanmhado = True

resultado = idade >+ 18 or acompanhado

print(resultado)
#not : Inverte o resultado de uma condição
aluno_matriculado  = True

print(not aluno_matriculado)

# 2 . operadores de comparação
idade = 18

print(idade == 18)
print(idade != 18)
print(idade > 18)
print(idade < 18)
print(idade >= 18)
print(idade <= 18)

# 3 . Estrutura if
if idade >= 18:
print("Maior de idade")


# . Estrutura if / else
idade = 16

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")