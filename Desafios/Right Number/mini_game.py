"""
Do While

Código para advinhar um número
"""
import random
import os
import time

palpite = 0
numero = random.randint(1, 10)

while True:
    print("Qual o Numero Correto ? ")
    palpite = int(input())
    if palpite == numero:
        print("Parabens voce acertou!!\n")
        time.sleep(1)
        os.system("cls")
        print("\nFinalizando o Sistema:")
        time.sleep(1)
        os.system("cls")
        break
    else:
        print("Voce errou")
        time.sleep(1)
        os.system("cls")
