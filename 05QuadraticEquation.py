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
x1 = -b + math.sqrt(delta) / 2 * a
x2 = -b - math.sqrt(delta) / 2 * a

#5. Receba os coeficientes A, B e C de uma equação do 2o grau (AX2+BX+C=0). Calcule e mostre
# as raízes reais (considerar que a equação possui 2 raízes reais).
print("Valor 1:", x1,"\nValor2:", x2)
