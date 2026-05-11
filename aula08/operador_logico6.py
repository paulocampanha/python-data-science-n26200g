# Nesse programa vamos continuar estudando o operador lógico 'not'

numero_de_alunos = int(input("Digite o número de alunos " \
"matrículados na turma: "))

if not numero_de_alunos == 16:
    print("A turma precisa ter 16 alunos para iniciar.")
else:
    print("Turma programada para iniciar na " \
    "próxima segunda-feira")