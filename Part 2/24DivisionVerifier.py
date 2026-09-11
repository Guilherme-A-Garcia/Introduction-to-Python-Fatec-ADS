valor: int = 0

valor = int(input("Insira o valor a ser verificado: "))

if valor % 2 == 0 and valor % 3 == 0:
    print(valor, "é divisível por 2 e 3.")
else:
    print(valor, "não é divisível por 2 e 3.")
