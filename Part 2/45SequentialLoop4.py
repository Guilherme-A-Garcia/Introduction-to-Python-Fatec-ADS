resultado: float
sinal: chr

sinal = '+'
resultado = 0

for i in range(1, 15):
    if i % 5 == 0:
        resultado += i / (i*i)
    elif sinal == '+':
        resultado += i / (i*i)
    else:
        resultado -= i / (i*i)
    print(resultado)
    if sinal == '-':
        sinal = '+'
    else:
        sinal = '-'