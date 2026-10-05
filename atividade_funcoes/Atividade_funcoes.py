def estudante(nome):
    print(f"Nome: {nome}")

estudante("john pork")

def calcularMedia(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)

notas = [8, 7, 9]
media = calcularMedia(notas)
print(f"Media: {media}")


def situacao_estudante(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

print(situacao_estudante(media))



