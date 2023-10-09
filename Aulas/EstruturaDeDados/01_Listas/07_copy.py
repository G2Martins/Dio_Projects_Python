lista_1 = [1, "Python", [40, 30, 20]]

lista_2 = lista_1.copy()

print(lista_1)  # [1, "Python", [40, 30, 20]]

lista_2[0] = 2

print(lista_1)
print(lista_2)  # [2, "Python", [40, 30, 20]]

# As alterações na lista 2 nao alteram a original
# Pois ela é uma copia da primeira
