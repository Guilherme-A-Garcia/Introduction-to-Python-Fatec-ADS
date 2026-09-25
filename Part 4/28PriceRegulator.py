def calcPreco(preco_atual:float, vendas_mensais:float) -> float:
    preco_novo: float = preco_atual
    if vendas_mensais < 500 and preco_atual < 30:
        preco_novo = (preco_atual * 0.10) + preco_atual
    elif (vendas_mensais >= 500 and vendas_mensais < 100) and (preco_atual >= 30 and preco_atual < 80):
        preco_novo = (preco_atual * 0.15) + preco_atual
    elif vendas_mensais >= 1000 and preco_atual >=80:
        preco_novo = (preco_atual * 0.05) - preco_atual
    else:
        preco_novo = preco_atual

    return preco_novo

def main() -> None:
    preco_atual: float = 0
    vendas_mensais: float = 0

    preco = float(input("Insira o preço atual do produto: "))
    vendas = float(input("Insira a média de vendas mensais do produto: "))

    print("Preço novo:", calcPreco(preco, vendas))

if __name__ == "__main__":
    main()