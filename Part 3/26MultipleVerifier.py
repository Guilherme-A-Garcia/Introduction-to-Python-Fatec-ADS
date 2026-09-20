val1: int = 0
val2: int = 0
maior: int = 0
menor: int = 0

def verifMultiplos():
    global val1, val2, maior, menor
    if val1 > val2:
        maior = val1
        menor = val2
    else:
        maior = val2
        menor = val1

    if maior % menor == 0:
        print("O maior é múltiplo do menor.")
    else:
        print("O maior não é múltiplo do menor.")

def main():
    global val1, val2
    val1 = int(input("Insira o primeiro valor: "))
    val2 = int(input("Insira o segundo valor: "))

    verifMultiplos()

if __name__ == "__main__":
    main()