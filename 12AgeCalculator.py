anoNasc: int = 0
anoAtual: int = 0
idadeAtual: int = 0
idadeFutura: int = 0

anoNasc = int(input("Insira o ano do seu nascimento: "))
anoAtual = int(input("Insira o ano atual: "))

idadeAtual = anoAtual - anoNasc
idadeFutura = idadeAtual + 17


print("Você tem", idadeAtual, "anos.\nDaqui a 17 anos, você terá", idadeFutura, "anos.")