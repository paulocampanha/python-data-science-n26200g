# Nesse programa vamos estudar os operadores de atribuição

salario = 5000
aumento = 1000

print(f"Salário R$ {salario}")

# Aplicando o aumento ao salário
salario = salario + aumento

print(f"Novo salário R$ {salario}")

desconto = 500

salario = salario - desconto

print(f"Salário com desconto R$ {salario} ")

meses = 12

salario = salario * meses

print(f"Salário anual R$ {salario}")

bimestre = 6

salario = salario / bimestre

print(f"Salário por bimestre R$ {salario}")

#===========================================
# operadores de atribuição reduzidos combinando
# operação aritmética com a atribuição de valor

aluguel = 3000
reajuste = 250

print(f"Aluguel R$ {aluguel}")

aluguel += reajuste # equivalente à aluguel = aluguel + reajuste

print(f"Aluguel com reajuste R$ {aluguel}")

reforma = 500

aluguel -= reforma # equivalente à aluguel = aluguel - reforma

print(f"Aluguel descontando a reforma R$ {aluguel}")

meses = 8

aluguel *= meses  # equivalente à aluguel = aluguel * meses

print(f"Total de aluguel em 8 meses R$ {aluguel}")

trimestre = 3

aluguel /= trimestre # equivalente à aluguel = aluguel / trimestre

print(f"Alugue trimestral R$ {aluguel}")



