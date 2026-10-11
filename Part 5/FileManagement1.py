import os

valor: int = 0
diretorio: str = ""
arquivo: str = ""

def grava(tab: int, rslt: int) -> int:
    global diretorio, arquivo
    file: str = ""
    tipo: str = ""
    enc: str = ""
    linha: str = ""

    if (tab > 1):
        tipo = 'a'
    else:
        tipo = 'w'
    linha = str(rslt) + "\n"
    enc = "utf-8"

    if (os.path.exists(diretorio) and os.path.isdir(diretorio)):
        file = os.path.join(diretorio, arquivo)

        if (os.path.exists(file) and os.path.isfile(file)):
            with open(file=file, mode=tipo, encoding=enc) as file:
                file.write(linha)
                file.close()
        else:
            with open(file=file, mode="w", encoding=enc) as file:
                file.write(linha)
                file.close()

def mult(vlr: int, tab: int) -> int:
    res: int = 0

    res = (vlr * tab)
    print(res)
    grava(tab, res)

    return res

def main():
    global valor, diretorio, arquivo
    contador: int = 0
    result: int = 0
    vlr: int = 0

    # Verificar permissões da /tmp/exercicios
    caminho_exercicios = "/tmp/exercicios"
    if not os.path.exists(caminho_exercicios):
        os.mkdir(caminho_exercicios)
    os.chmod(caminho_exercicios, 0o744)

    diretorio = caminho_exercicios
    arquivo = "ex34.txt"

    while (vlr < 1 or vlr >= 10):
        vlr = int(input("Insira um valor entre 1 e 10: "))

    for i in range(10):
        result = mult(vlr, i)

if __name__ == '__main__':
    main()