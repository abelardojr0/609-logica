palavra = str(input("Digite uma palavra: "))
contador_consoantes = 0

for letra in palavra:
    if letra.lower() in "bcdfghjklmnpqrstvxywz":
        contador_consoantes = contador_consoantes + 1


print(f"A palavra '{palavra}' possui {contador_consoantes} vogais")