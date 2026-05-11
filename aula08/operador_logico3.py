# Nesse programa vamos estudar o operador lógico 'or'

idade = int(input("Digite sua idade: "))
estudante = input("Você é estudante (S/N)? ")

if (idade < 18) or (estudante.upper() == "S"):
    print("Direito a meia entrada garantida")
else:
    print("Pagamento de valor integral")