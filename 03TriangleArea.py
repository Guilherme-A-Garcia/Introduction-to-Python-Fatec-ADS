base: float = 0
altura: float = 0
area: float = 0

base = float(input("Insira a base em cm: "))
altura = float(input("Insira a altura em cm: "))

area = (base * altura / 2)

print("Área:", area, "cm²")