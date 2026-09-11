voltas: float = 0
circ_m: float = 0
tempo_m: float = 0
circ_km: float = 0
tempo_h: float = 0
vm: float = 0

voltas = float(input("Insira a quantidade de voltas: "))
circ_m = float(input("Insira a extensão do circuito em metros: "))
tempo_m = float(input("Insira o tempo de duração em minutos: "))

tempo_h = tempo_m / 60
circ_km = (circ_m/1000) * voltas
vm = circ_km / tempo_h

print(f"Velocidade média: {vm} km/h")