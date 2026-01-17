# Maiúsculas e Minúsculas
# Símbolos e Espaços
"""
HEXADECIMAL
1 = 1
2 = 2
3 = 3
4 = 4
5 = 5
6 = 6
7 = 7
8 = 8
9 = 9
10 = A
11 = B
12 = C
13 = D
14 = E
15 = F
"""

chave = input("Digite a base da sua senha: ")

senha = ""

for letra in chave:
    if letra in "Aa":
        senha = senha + "1"
    elif letra in "Bb":
        senha = senha + "*"
    elif letra in "Cc":
        senha = senha + "2"
    elif letra in "Dd":
        senha = senha + "3"
    elif letra in "Ee":
        senha = senha + "4"
    elif letra in "Ff":
        senha = senha + "5"
    elif letra in "Rr":
        senha = senha + "#"
    elif letra in "Ss":
        senha = senha + "%"
    elif letra in "Mm":
        senha = senha + "$"
    elif letra in "Gg":
        senha = senha + "&"
    else:
        senha = senha + letra
print(senha)
