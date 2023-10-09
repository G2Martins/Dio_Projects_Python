linguagens = ["python", "js", "c", "java", "csharp"]

# Ordenação pelo Tamanho da palavra Ascendentemente
print(sorted(linguagens, key=lambda x: len(x)))
# ["c", "js", "java", "python", "csharp"]

# Ordenação pelo Tamanho da palavra Decrescentemente
print(sorted(linguagens, key=lambda x: len(x), reverse=True))
# ["python", "csharp", "java", "js", "c"]
