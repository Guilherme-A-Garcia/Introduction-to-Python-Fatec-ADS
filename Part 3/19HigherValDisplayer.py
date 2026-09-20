val1: int = 0
val2: int = 0

def determinante():
    global val1, val2
    if val1 > val2:
        print("Maior valor:", val1)
    else:
        print("Maior valor:", val2)

def main():
    global val1, val2
    val1 = int(input("Insira o primeiro valor: "))
    val2 = int(input("Insira o segundo valor: "))
    determinante()

if __name__ == "__main__":
    main()