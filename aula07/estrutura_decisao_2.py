# Nesse programa vamos continuar estudando a estrutura de 
# decisão simples: if

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade: ")
aluno_novo = True

if idade < 18:
    print(f"{nome}, você é menor de idade.")
    print("Seu responsável legal deve estar " \
    "presente para a matrícula.")

# upper() converte para maíusculas
# lower() converte para minúsculas
# capitalize() converte a primeira letra para maísucula
# e as demais para minúscula
if cidade.lower() != "guarulhos":
    print(f"{nome.capitalize()}, você não mora em Guarulhos.")
    print("Verifique uma unidade próxima da sua casa")

if aluno_novo:
    print(f"{nome}, você recebera um crachá na primeira aula.")

print("=" * 40)
print("Senai Celso Charuri")