# Desafio
Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

# Entrada
A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

# Saída
Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

 
# Exemplo de Entrada	                    -            Exemplo de Saída
        4                                   -             encaixa
    56234523485723854755454545478690 78690  -             nao encaixa
    5434554 543                             -             encaixa
    1243 1243 54 64545454545454545454545454545454554   -  nao encaixa

# Explicação do codigo
N = int(input()): Esta linha lê um número inteiro da entrada padrão (o número de casos de teste) e armazena-o na variável N.

while N > 0:: Isso inicia um loop while que continuará até que o valor de N seja menor ou igual a zero. Isso permite que você processe vários casos de teste.

A, B = input().split(): Dentro do loop, esta linha lê uma linha da entrada padrão e a divide em duas partes usando o método .split(). O método split() divide a linha em palavras (separadas por espaços em branco por padrão) e, neste caso, atribui essas duas partes às variáveis A e B. Isso assume que cada linha da entrada contém dois números separados por espaço.

if A.endswith(B):: Esta linha verifica se a string B é uma subsequência (sufixo) da string A usando o método .endswith(). Se for verdadeiro, significa que B corresponde aos últimos dígitos de A.

print("encaixa"): Se a condição do if for verdadeira, ou seja, se B corresponder aos últimos dígitos de A, então "encaixa" é impresso na saída.

else:: Se a condição do if não for verdadeira, significa que B não corresponde aos últimos dígitos de A.

print("nao encaixa"): Neste caso, "nao encaixa" é impresso na saída.

N -= 1: Por fim, decrementamos o valor de N em 1, o que significa que estamos indo para o próximo caso de teste na próxima iteração do loop.

Este código lê vários casos de teste e verifica se o segundo valor (B) corresponde aos últimos dígitos do primeiro valor (A) para cada caso de teste. Ele imprime "encaixa" se for verdadeiro e "nao encaixa" se for falso para cada caso de teste. O loop continua até que todos os casos de teste tenham sido processados.