x: int = 0
y: int = 0
z: int = 0

x = int(input("Insira o valor de X: "))
y = int(input("Insira o valor de Y: "))

z = x
x = y
y = z

print("Valor de X:", x)
print("Valor de Y:", y)