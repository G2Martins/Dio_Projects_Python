###############################################################################
#   3 operações Básicas - Saque, Deposito e Extrato                           #
#                                                                             #
#   Permitido apenas 3 Saques diarios de R$500 por saque                      #
#   (Caso o usuario nao tenha saldo exibir uma mensagem que não sera possivel)#
#                                                                             #
#   Todos os saques devem ser armazenados em uma variavel e exibidos no Extrato
#   Final da listagem aparecer o saldo da conta                               #
#   no formato R$ xxx.x                                                       #
#   Exemplo:                                                                  #
#   1500.45 = R$ 1500.45                                                      #
###############################################################################

import os
import time

menu = """
+---------------------------------------------------------+
+-         Bem vindo ao Banco Banco G-Mart Digital       -+
+-            Qual operação deseja fazer Hoje?           -+
+-                                                       -+
+-    [1] - Saque                                        -+
+-    [2] - Depósito                                     -+
+-    [3] - Extrato                                      -+
+-    [4] - Sair                                         -+
+---------------------------------------------------------+
"""
saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    os.system("cls")
    print(menu)
    operacao = int(input("+- Operacao: "))

    if operacao == 1:

        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro! Voce nao tem saldo suficiente.")

        elif excedeu_limite:
            print("Erro! O Valor do saque excede o limite.")

        elif excedeu_saques:
            print("Erro! Numero maximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            numero_saques += 1
            print(f"Saque de R${valor} Realizado com sucesso")
            time.sleep(2)

        else:
            print("Operacao invalida, Tente Novamente!")

    elif operacao == 2:

        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Deposito de R${valor} Realizado com sucesso")
            time.sleep(2)

        else:
            print("Erro! O valor informado é inválido")

    elif operacao == 3:

        print("\n+---------- EXTRATO -------------+")
        if extrato:
            for operacao in extrato:
                print(operacao)
        else:
            print("Nenhuma movimentação realizada.")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("+----------------------------------+")
        time.sleep(3)

    elif operacao == 4:
        break

    else:
        print("Operacao invalida, Tente Novamente!")
