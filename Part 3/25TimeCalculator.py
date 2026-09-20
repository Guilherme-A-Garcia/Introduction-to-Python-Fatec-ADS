hrInicio: int = 0
minInicio: int = 0
hrFinal: int = 0
minFinal: int = 0
hrTotal: int = 0
minTotal: int = 0

def calcTempo():
    global hrInicio, minInicio, hrFinal, minFinal, hrTotal, minTotal

    if(hrFinal < hrInicio):
        hrFinal += 24

    if minFinal < minInicio:
        hrFinal -= 1
        minFinal += 60

    hrTotal = hrFinal - hrInicio
    minTotal = minFinal - minInicio

def main():
    global hrInicio, minInicio, hrFinal, minFinal, hrTotal, minTotal

    hrInicio = int(input("Insira a hora de início: "))
    minInicio = int(input("Insira os minutos de início: "))
    hrFinal = int(input("Insira a hora do final: "))
    minFinal = int(input("Insira os minutos do final: "))

    calcTempo()

    print(f"A partida durou {hrTotal}:{minTotal} horas.")

if __name__ == "__main__":
    main()
