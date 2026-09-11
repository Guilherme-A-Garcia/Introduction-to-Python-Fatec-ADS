comprimento: int = 0
altura: int = 0
largura: int = 0
volume: int = 0

comprimento = int(input("Insira o valor do comprimento em cm: "))
altura = int(input("Insira o valor da altura em cm: "))
largura = int(input("Insira o valor da largura em cm: "))

volume = comprimento * largura * altura

print("Volume:", volume,"cm³")