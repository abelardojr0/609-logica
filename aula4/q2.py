while True:
    usuario = str(input("Digite o nome de usuário: "))
    senha = str(input("Digite a senha do usuário: "))

    if usuario == senha:
        print("Dados inválidos, senha e usuário não podem ser iguais")
    else:
        print("Cadastro realizado com sucesso")
        break