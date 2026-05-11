# Faça um programa que recebe os três lados de um triângulo.
# Usando os operadores and e or, verifique e classifique o
# triangulo de acordo com a regra abaixo:
# Equilatero -> todos os lados são iguais
# Isósceles -> dois lados são iguais
# Escaleno -> todos os lados são diferentes

lado_a = 10
lado_b = 10
lado_c = 10


if (lado_a == lado_b) and (lado_b == lado_c):
    pass
elif (lado_a == lado_b) or (lado_b == lado_c) or 
                                    (lado_a == lado_c):
