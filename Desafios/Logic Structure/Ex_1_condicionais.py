"""
Implemente um programa que receba a idade de uma pessoa e imprima mensagem
de acordo com os critérios Abaixo:
- Menor de 16 Anos: Menor
- Entre 16 e 18 Anos: Emancipado
- Maior de 18 Anos: Maior
"""
idade = int(input("Digite a sua idade: "))

if idade < 16:
    print("MENOR")
elif idade >= 16 and idade <= 18:
    print("Emancipado")
elif idade > 18:
    print("MAIOR")
