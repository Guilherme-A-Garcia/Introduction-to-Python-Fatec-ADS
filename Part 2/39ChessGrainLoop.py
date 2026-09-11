casa: int
qtd_casa: int
qtd_total: int

qtd_total = 1
qtd_casa = 1

casa = int(input("Insira o número máximo de casas (menor que 65): "))
while casa > 64:
    casa = int(input("Insira o número máximo de casas (menor que 65): "))

for i in range(1, casa):
    qtd_total += qtd_casa
    qtd_casa *= 2
print("Total de grãos:", qtd_total)