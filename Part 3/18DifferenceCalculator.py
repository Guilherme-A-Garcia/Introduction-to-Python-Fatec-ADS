int1: int = 0
int2: int = 0
int3: int = 0

def subtrair():
    global int1, int2, int3
    if int1 > int2:
        int3 = int1 - int2
    else:
        int3 = in2 - int1

def main():
    global int1, int2, int3
    int1 = int(input("Insira o primeiro número: "))
    int2 = int(input("Insira o segundo número: "))
    subtrair()

    print("Diferença:", int3)


if __name__ == "__main__":
    main()