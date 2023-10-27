letra = str(input("Digite uma letra: "))

if letra in "aeiou":
    print("vogal")
elif letra in "bcdfghjklmnpqrstvxywz":
    print("consoante")
else:
    print("inválido")