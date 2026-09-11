preco_atual: float = 0
vendas_mensais: float = 0
preco_novo: float = 0

preco_atual = float(input("Insira o preço atual do produto: "))
vendas_mensais = float(input("Insira a média de vendas mensais do produto: "))

if vendas_mensais < 500 and preco_atual < 30:
    preco_novo = (preco_atual * 0.10) + preco_atual
elif (vendas_mensais >= 500 and vendas_mensais < 100) and (preco_atual >= 30 and preco_atual < 80):
    preco_novo = (preco_atual * 0.15) + preco_atual
elif vendas_mensais >= 1000 and preco_atual >=80:
    preco_novo = (preco_atual * 0.05) - preco_atual
else:
    preco_novo = preco_atual

print("Preço novo:", preco_novo)