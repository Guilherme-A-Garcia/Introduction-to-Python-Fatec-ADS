val1: int = 0
val2: int = 0
maior: int = 0
menor: int = 0

val1 = int(input("Insira o primeiro valor: "))
val2 = int(input("Insira o segundo valor: "))

if val1 > val2:
    maior = val1
    menor = val2
else:
    maior = val2
    menor = val1

if maior % menor == 0:
    print("O maior múltiplo do menor.")
else:
    print("O maior não é múltiplo do menor.")