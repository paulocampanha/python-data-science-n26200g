# Nesse programa vamos estudar o operador logico 'and'

sexo = input("Digite seu sexo (M/F): ")
idade = int(input("Digite sua idade: "))

if (sexo.upper() == "M") and (idade == 18):
    print("Você está apto ao alistamento militar.")
else:
    if sexo.upper() == "F":
        print("Mulheres não são obrigadas ao " \
        "alistamento militar.")
    else:
        print("Você não está apto ao alistamento militar")