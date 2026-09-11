n: int = 0
termo1: int = 0
termo2: int = 0
aux: int = 0

n = int(input("Insira um número: "))
termo2 = 1

while termo1 <= n:
    aux = termo1 + termo2
    termo1 = termo2
    termo2 = aux
    print(termo1)
