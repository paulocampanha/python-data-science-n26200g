# Faca um programa que recebe o peso de uma pessoa em quilos
# (exemplo 70 quilos) e a altura em metros 
# (exemplo 1.70 metros) e calcule o IMC (Índice de Massa 
# Corporal) do usuário. Em seguida verifique o IMC usando
# uma estrutura de decisão e informe a classificação de acordo 
# com a tabela.
# IMC                   Classificação
# Menor que 18,5        Magreza
# Entre 18,5 e 24,9     Normal
# Entre 25,0 e 29,9     Sobrepeso
# Entre 30,0 e 39,9     Obesidade 
# Maior que 40,0        Obesidade Grave
# Fórmula:  imc = peso / (altura * altura)  
# Fórmula:  imc = peso / altura ** 2  

peso = float(input("Digite seu peso em quilos: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / altura ** 2 # peso / (altura * altura)

if imc <= 18.5:
    print(f"Seu IMC é {imc:.1f} e você está abaixo do peso normal.")
elif imc <= 24.9:
    print(f"Seu IMC é {imc:.1f} e você está com peso normal.")
elif imc <= 29.9:    
    print(f"Seu IMC é {imc:.1f} e você está com sobrepeso.")
elif imc <= 39.9:
    print(f"Seu IMC é {imc:.1f} e você está com obesidade.")
else:
    print(f"Seu IMC é {imc:.1f} e você está com obesidade grave.")


