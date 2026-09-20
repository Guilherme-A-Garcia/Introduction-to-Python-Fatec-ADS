n1: float = 0
n2: float = 0
n3: float = 0
n4: float = 0
media: float = 0

def calcMedia():
    global n1, n2, n3, n4, media

    media = (n1 + n2 + n3 + n4) / 4
    print("Média:", media)

    if media >= 6.0:
        print("Aprovado.")
    elif media >= 3.0 and media < 6.0:
        print("Exame.")
    else:
        print("Retido.")

def main():
    global n1, n2, n3, n4
    n1 = float(input("Insira a primeira nota: "))
    n2 = float(input("Insira a segunda nota: "))
    n3 = float(input("Insira a terceira nota: "))
    n4 = float(input("Insira a quarta nota: "))

    calcMedia()

if __name__ == "__main__":
    main()