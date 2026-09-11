n: int = 0
x: int = 0
fatorial: int = 0

n = int(input("Insira um número: "))

fatorial = 1

for x in range(n, 0, -1):
    fatorial *= x

print(fatorial)