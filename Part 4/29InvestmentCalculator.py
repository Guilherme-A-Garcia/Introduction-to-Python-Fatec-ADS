def calcInvest(tipoInv: int, valorInv:float) -> float | None:
    valor_final: float = 0

    if tipoInv == 1:
        valor_final = (valorInv * 0.03) + valorInv
        return valor_final
    elif tipoInv == 2:
        valor_final = (valorInv * 0.05) + valorInv
        return valor_final
    else:
        return None

def main() -> None:
    tipo: int = 0
    valor: float = 0

    print("Tipos de investimento:\n1 - Poupança\n2 - Renda fixa")

    tipo = int(input("Insira o tipo do investimento: "))
    valor = float(input("Insira o valor do investimento: "))

    if tipo == 1:
        print(f"O valor final após 30 dias em poupança é de R${calcInvest(tipo, valor)}")
    elif tipo == 2:
        print(f"O valor final após 30 dias em renda fixa é de R${calcInvest(tipo, valor)}")
    else:
        print("Tipo inválido:", tipo)

if __name__ == "__main__":
    main()