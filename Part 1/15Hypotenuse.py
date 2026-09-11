import math

cateto1: float = 0
cateto2: float = 0
hipotenusa: float = 0

cateto1 = float(input("Insira o primeiro cateto: "))
cateto2 = float(input("Insira o segundo cateto: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
# (ou math.hypot)

print("Hipotenusa:", hipotenusa)