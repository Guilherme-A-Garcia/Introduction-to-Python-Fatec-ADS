atual: int
maior: int
menor: int

atual = int(input("Insira um número: "))
maior = atual
menor = atual

for i in range(1, 99):
    atual = int(input("Insira um número: "))
    if atual > maior:
        maior = atual
    if atual < menor:
        menor = atual
print("O maior é:", maior)
print("O menor é:", menor)