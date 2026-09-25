def calcVelMed(tempo, circ, vlt):
    tempo: float
    circ: float
    vm: float

    tempo_h = tempo / 60
    circ_km = (circ/1000) * vlt
    vm = circ_km / tempo_h
    return vm

def main():
    voltas: float = 0
    circ_m: float = 0
    tempo_m: float = 0

    voltas = float(input("Insira a quantidade de voltas: "))
    circ_m = float(input("Insira a extensão do circuito em metros: "))
    tempo_m = float(input("Insira o tempo de duração em minutos: "))

    print(f"Velocidade média: {calcVelMed(tempo_m, circ_m, voltas)} km/h")

if __name__ == "__main__":
    main()