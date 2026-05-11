# Nesse programa vamo continuar estudando o operador lógico or

idade = int(input("Digite sua idade: "))

if idade < 18 or idade > 65:
    print("Doador inapto para doação de sangue")
else:
    print("Dirijá-se ao balcão de glicose.")