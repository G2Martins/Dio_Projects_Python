class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("AuAu")
    
    
    def dormir(self):
        self.acordado = False
        print("Zzzzzz...")

cao_1 = Cachorro("Barto", "preto", False)
cao_2 = Cachorro("Fred", "branco e bege")

cao_1.latir()

print(cao_2.acordado)
cao_2.dormir()
print(cao_2.acordado)