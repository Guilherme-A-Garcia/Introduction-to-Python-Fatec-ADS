def calcFat(num: int) -> int:
    x: int = 0
    fatorial: int = 1

    for x in range(num, 0, -1):
        fatorial *= x
    
    return fatorial

def div(val1: int, val2: int) -> float:
    result: float = 0
    
    result = val1 / val2

    return result

def main() -> None:
    i: int = 0
    n: int = 0
    result: float = 1

    n = int(input("Insira um número: "))

    for i in range(1, n, 1):
        result += div(1, calcFat(i))
    
    print(result)
    
if __name__ == "__main__":
    main()