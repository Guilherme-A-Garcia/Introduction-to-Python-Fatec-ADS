val1: int = 0
val2: int = 0

def organizar():
    global val1, val2

    if val1 > val2:
        print(val1, val2)
    else:
        print(val2, val1)

def main():
    global val1, val2

    val1 = int(input("Insira o primeiro valor: "))
    val2 = int(input("Insira o segundo valor: "))

    organizar()

if __name__ == "__main__":
    main()