while True:
    nota = float(input("Digite uma nota: "))

    if nota > 10 or nota < 0:
        print("Nota inválida, favor digitar uma nota entre 0 e 10")
    else:
        print("Nota válida")
        break