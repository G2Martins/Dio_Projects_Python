# Ordenação por ordem Alfabetica normal
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"]
print(linguagens)

# Ordenação por ordem Alfabetica Inversa
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"]
print(linguagens)

# Ordenação pelo Tamanho da palavra Ascendentemente
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"
print(linguagens)

# Ordenação pelo Tamanho da palavra Decrescentemente
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)
# ["python","csharp","java","js","c"]
print(linguagens)


# Lambda = função anonima sem nome
