ang1: int = 0
ang2: int = 0
ang3: int = 0

ang1 = int(input("Insira o primeiro ângulo: "))
ang2 = int(input("Insira o segundo ângulo: "))

ang3 = 180 - (ang1 + ang2)

print("Terceiro ângulo:", ang3)
