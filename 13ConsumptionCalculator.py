qtd_kg: float = 0
qtd_g: float = 0
dias: float = 0

qtd_kg = float(input("Insira a quantidade de alimentos em kg: "))
qtd_g = qtd_kg * 1000
dias = qtd_g/50

print(qtd_kg,"kgs durarão", dias, "dias se forem consumidas 50g por dia.")