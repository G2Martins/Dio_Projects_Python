direcao = 0
movimento = 0
limite = 0
detector = "não"

limite = int(input())
count = 1

while movimento >= 0:
    print("\n")
    print(f"{count}° Laço")
    movimento = int(input())

    if movimento > limite:
        detector = "sim"

    if movimento < 0:
        break
    
    count += 1

print(detector)