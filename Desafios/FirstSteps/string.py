# Python Strings

# Printar na tela pode usar aspas duplas ou simples
print("Ola")
print('Ola')

# Guardar na memoria uma string
w = "Curso de Python 3"
print(w)

# comentarios com """cometarios""" --> Comentarios em blocos ou strings em blocos com formatação definida

a = """ Ola,
Este é o curso de python
espero que goste"""

# Métodos das Strings
b = " OLA MUNDO "
print(b)
print(b.strip())  # Método para ignorar os espaços na declaração da variavel

c = "Ola Mundo"
print(c)
print(c.lower())  # Método para imprimir na tela a frase toda em minúsculo

d = "Ola Mundo"
print(d)
print(d.upper())  # Método para imprimir na tela a frase toda em Maiúsculo

e = "Ola"
f = "Mundo"
g = e + " " + f
print(g)  # Concantenado Strings