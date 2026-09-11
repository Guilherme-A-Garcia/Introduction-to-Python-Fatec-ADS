val1: int = 0
val2: int = 0

val1 = int(input("Insira o primeiro valor: "))
val2 = int(input("Insira o segundo valor: "))

if val1 > val2:
    print(val1, val2)
else:
    print(val2, val1)