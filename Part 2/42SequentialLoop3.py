x: float
result: float

x = 1
result = 0

for i in range(1, 50):
    result+= i/x
    x+=2

print(result)