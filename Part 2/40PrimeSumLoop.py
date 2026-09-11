num1: int
num2: int
divisores: int

num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

while num1 <= num2:
    if num1 >= 2:
        divisores = 0

        for i in range(1, num1):
            if num1 % i == 0:
                divisores += 1
            
        if divisores == 2:
            print(num1)
    num1 += 1
