hrInicio: int = 0
minInicio: int = 0
hrFinal: int = 0
minFinal: int = 0
hrTotal: int = 0
minTotal: int = 0

hrInicio = int(input("Insira a hora de início: "))
minInicio = int(input("Insira os minutos de início: "))
hrFinal = int(input("Insira a hora do final: "))
minFinal = int(input("Insira os minutos do final: "))

if(hrFinal < hrInicio):
    hrFinal += 24

if minFinal < minInicio:
    hrFinal -= 1
    minFinal += 60

hrTotal = hrFinal - hrInicio
minTotal = minFinal - minInicio

print(f"{hrTotal}:{minTotal}")


