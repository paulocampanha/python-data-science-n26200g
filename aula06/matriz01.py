# Nesse programa vamos estudar as listas bidimensional 
# conhecidas como matrizas

matriz_numeros = [
    [13, 25, 29, 32],
    [28, 5, 18, 24],
    [131, 152, 505, 439]
]

print(matriz_numeros)

print(f"Linha 1 coluna 3: {matriz_numeros[0][2]}")

print(f"Linha 2 inteira: {matriz_numeros[1]}")


coluna_2 = []
coluna_2.append(matriz_numeros[0][1])
coluna_2.append(matriz_numeros[1][1])
coluna_2.append(matriz_numeros[2][1])

print(coluna_2)

# Desafio: Calcule a média da cada linha
media_1 = sum(matriz_numeros[0]) / len(matriz_numeros[0])

soma_2 = sum(matriz_numeros[1])
qtde_2 = len(matriz_numeros[1])
media_2 = soma_2 / qtde_2

print(f"Média da 1 linha: {media_1}")
print(f"Média da 2 linha: {media_2}")