n: int = 0
index: int = 0
termo: float = 0
fatorial: float = 0
soma: float = 0

n = int(input("Insira um número: "))
soma = 1
fatorial = 1
index = 1

for index in range(1, n + 1):
    fatorial *= index
    termo = 1.0 / fatorial
    soma += termo

print(soma)