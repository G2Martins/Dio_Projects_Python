def dividir(a, b):
    return a // b


T = int(input())

for i in range(T):
    entrada = input().split()
    N = int(entrada[0])
    K = int(entrada[1])

    divisao = dividir(N, K)
    modulo = N % K
    resultado = divisao + modulo

    print(resultado)
