tipo: float = 0
valor: float = 0
valor_final: float = 0

tipo = float(input("Insira o tipo do investimento: "))
valor = float(input("Insira o valor do investimento: "))

if tipo == 1:
    valor_final = (valor * 0.03) + valor
    print(f"O valor final após 30 dias em poupança é de R${valor_final}")
elif tipo == 2:
    valor_final = (valor * 0.05) + valor
    print(f"O valor final após 30 dias em renda fixa é de R${valor_final}")
else:
    print("Tipo inválido:", int(tipo))