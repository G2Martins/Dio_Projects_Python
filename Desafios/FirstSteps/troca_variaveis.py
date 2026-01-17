# Trocar Variáveis

x = input("Insira o valor de x: ")
y = input("Insira o valor de y: ")

# Criar Variavel Temp

temp = x
x = y
y = temp

print(f"O Valor de x depois da troca: {x}")
print(f"O Valor de y depois da troca: {y}")