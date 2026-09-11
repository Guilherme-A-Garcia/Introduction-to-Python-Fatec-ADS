int1: int = 0
int2: int = 0
index: int = 0
maior: int = 0
result: int = 0

int1 = int(input("Insira o primeiro número: "))
int2 = int(input("Insira o segundo número: "))

if int1 > int2:
    index = int2
    maior = int1
else:
    index = int1
    maior = int2

while index <= maior:
    if index % 2 != 0:
        result += index
    # print(result)
    index += 1

print(result)