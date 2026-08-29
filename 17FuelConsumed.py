temp_perc: float = 0
vel_media: float = 0
km: float = 0
litros: float = 0

temp_perc = float(input("Insira o tempo de percurso (horas): "))
vel_media = float(input("Insira a velocidade média (km/h): "))

km = vel_media * temp_perc
litros = km/12

print("Litros gastos:", litros)