def calcFat(num: int) -> int:
    x: int = 0
    fatorial: int = 1

    for x in range(num, 0, -1):
        fatorial *= x
    
    return fatorial

def main() -> None:
    n: int = 0
    fat: int = 0

    n = int(input("Insira um número: "))
    fat = calcFat(n)

    print(fat)

if __name__ == "__main__":
    main()