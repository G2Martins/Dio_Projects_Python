"""
Programa que receba a idade do nadador
e imprima sua categoria
"""
idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("Categoria do Nadador: Infantil A")
elif idade >= 8 and idade <= 10:
    print("Categoria do Nadador: Infantil B")
elif idade >= 11 and idade <= 13:
    print("Categoria do Nadador: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Categoria do Nadador: Juvenil B")
elif idade >= 18:
    print("Categoria do Nadador: Profissional")
else:
    print("Nadador Sem categoria Amadora/Profissional")
