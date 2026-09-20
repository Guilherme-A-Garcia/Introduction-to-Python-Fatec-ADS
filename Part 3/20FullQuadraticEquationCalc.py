import math

a: float = 0
b: float = 0
c: float = 0
x1: float = 0
x2: float = 0
delta: float = 0

def calcRaizes():
    global a, b, c, x1, x2, delta
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

def main():
    global a, b, c, x1, x2
    a = float(input("Insira o valor do termo A: "))
    b = float(input("Insira o valor do termo B: "))
    c = float(input("Insira o valor do termo C: "))

    calcRaizes()

    if x1 != None and x2 != None:
        print("Valor 1:", x1,"\nValor 2:", x2)

if __name__ == "__main__":
    main()
