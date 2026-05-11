# Crie um programa para receber do usuário 4 notas com 
# casas decimais e calcule a méias dessas notas.
# Fórmula: media = (nota1 + nota2 + nota3 + nota4 ) / 4
# Imprima a media do aluno com 1 casa decimal

nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))
nota3 = float(input("Digite a 3ª nota do aluno: "))
nota4 = float(input("Digite a 4ª nota do aluno: "))

media = (nota1 + nota2 + nota3 + nota4 ) / 4

print(f"A média do aluno é {media:.1f}.")