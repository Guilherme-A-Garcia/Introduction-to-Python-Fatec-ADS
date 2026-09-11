import math

a: float = 0
b: float = 0
c: float = 0
x1: float = 0
x2: float = 0
delta: float = 0

a = float(input("Insira o valor do termo A: "))
b = float(input("Insira o valor do termo B: "))
c = float(input("Insira o valor do termo C: "))

delta = b ** 2 - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = x1
else:
    x1 = None
    x2 = x1

print("Valor 1:", x1,"\nValor 2:", x2)