base: int
expoente: int
potencia: int

potencia = 1

base = int(input("Insira a base: "))
expoente = int(input("Insira o expoente: "))

for i in range(1, expoente):
    potencia *= base
print(potencia)