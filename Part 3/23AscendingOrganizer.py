val1: int = 0
val2: int = 0
val3: int = 0
val4: int = 0

def organizar():
    if val4 > val3:
        print(val1, val2, val3, val4)
    elif val4 > val2 and val4 < val3:
        print(val1, val2, val4, val3)
    elif val4 > val1 and val4 < val2:
        print(val1, val4, val2, val3)
    else:
        print(val4, val1, val2, val3)

def main():
    global val1, val2, val3, val4
    
    val1 = int(input("Insira o primeiro valor: "))
    val2 = int(input("Insira o segundo valor: "))
    val3 = int(input("Insira o terceiro valor: "))
    val4 = int(input("Insira o quarto valor: "))

    organizar()

if __name__ == "__main__":
    main()
