sexo = str(input("""
Digite o seu sexo: 
F - Feminino
M - Masculino
""")).upper().strip()

if sexo == 'F' or sexo == 'FEMININO':
    print("F - Feminino")
elif sexo == "M" or sexo == 'MASCULINO':
    print("M - Masculino")
else:
    print("Alternativa inválida")