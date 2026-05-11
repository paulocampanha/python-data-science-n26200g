# Nesse programa vamos estudar algumas funções aritméticas
# para listas

notas = [5.5, 8.2, 10, 7.5]
print(notas)

nota_maxima = max(notas)
print(f"Maior nota: {nota_maxima}")

nota_minima = min(notas)

print(f"Menor nota: {nota_minima}")

amplitude = nota_maxima - nota_minima

print(f"Amplitude das notas: {amplitude}")

soma_notas = sum(notas)

print(f"Soma das notas: {soma_notas}")

numero_de_notas = len(notas)

print(f"Número de notas: {numero_de_notas}")

# Desafio: Encontre a média das notas

media = soma_notas / numero_de_notas

print(f"Média: {media:.1f}")
