valor: int = 0

def verificar():
    global valor
    
    if valor % 2 == 0 and valor % 3 == 0:
        print(valor, "é divisível por 2 e 3.")
    else:
        print(valor, "não é divisível por 2 e 3.")

def main():
    global valor

    valor = int(input("Insira o valor a ser verificado: "))

    verificar()

if __name__ == "__main__":
    main()
