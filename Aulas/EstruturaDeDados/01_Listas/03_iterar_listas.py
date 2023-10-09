carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro, end=" ")

print("\n")
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
