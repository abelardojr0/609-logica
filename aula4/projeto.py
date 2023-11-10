import random
lista_pessoas = []
contador = 0

while True:
    nome = str(input("Digite seu nome: "))
    if nome == "fim" and contador >= 5:
        break
    telefone = str(input("Digite seu telefone: "))
    endereco = str(input("Digite seu endereco: "))

    lista_pessoas.append([nome,telefone,endereco])
    contador = contador + 1


sorteado = random.choice(lista_pessoas)

print(f"O sorteado foi o {sorteado[0]} que usa o telefone {sorteado[1]} e mora no endereço {sorteado[2]}")