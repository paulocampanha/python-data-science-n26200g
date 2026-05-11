# Nesse programa vamos estudar alguns comandos para
# alterar o valor de uma lista (vetor)

frutas = ["Banana", "Pera", "Maçã", "Uva"]
print(frutas)

# Altera o valor do 3 elemento da lista
frutas[2] = "Melão"

print(frutas)

# Adicionado um elemento no final da lista
frutas.append("Melancia")

print(frutas)

# Adicionando um elemento em uma posição específica
frutas.insert(1, "Abacaxi")

print(frutas)

# Removendo o último elemento da lista
frutas.pop()

print(frutas)

# Removendo um item específico da lista
frutas.pop(0)

print(frutas)

# Removendo um elemento pelo seu conteúdo
frutas.remove("Melão")

print(frutas)
