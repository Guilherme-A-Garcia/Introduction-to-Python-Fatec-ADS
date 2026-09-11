num: int  = 0
index: int = 0
result: float = 0

num = int(input("Insira um número: "))

for index in range(1, num + 1):
    result = result + (1/index)
    print(result)
