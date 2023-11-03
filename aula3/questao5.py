soma = 0
for i in range(1,7):
    numero = int(input(f"Digite o {i}º número: "))
    soma = soma + numero

media = soma / 6

print(f"A média do números foi {media} ")