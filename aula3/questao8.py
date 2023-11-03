palavra = str(input("Digite uma palavra: "))
contador_vogais = 0

for letra in palavra:
    if letra.lower() in "aeiou":
        contador_vogais = contador_vogais + 1


print(f"A palavra '{palavra}' possui {contador_vogais} vogais")