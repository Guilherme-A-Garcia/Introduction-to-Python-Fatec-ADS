import os

nome: str = ""
nota1: float
nota2: float
nota3: float
nota4: float
valor_media: float
diretorio: str = ""
arquivo: str = ""

def escreveArq(caminho: str, arquivo: str, linha_arq: str):
    file: str = ""
    tipo: str = ""
    enc: str = ""

    enc = "utf-8"

    if (os.path.exists(caminho) and os.path.isdir(caminho)):
        file = os.path.join(caminho, arquivo)

        if (os.path.exists(file) and os.path.isfile(file)):
            tipo = "a"
        else:
            tipo = "w"

        with open(file=file, mode=tipo, encoding=enc) as file1:
            file1.write(linha_arq)
            file1.close()

def cadastro(nm: str, nt1: int, nt2: int, nt3: int, nt4: int, vlr_med: float):
    global arquivo, diretorio
    linha: str = ""

    linha = "Nome: " + nm + "; " + "Nota 1: " + str(nt1) + "; " + "Nota 2: " + str(nt2) + "; " + "Nota 3: " + str(nt3) + "; " + "Nota 4: " + str(nt4) + "; " + "Média: " + str(vlr_med) + "\n"
    escreveArq(diretorio, arquivo, linha)

def med(n1: int, n2: int, n3: int, n4: int) -> float:
    media = (n1 + n2 + n3 + n4) / 4
    return media

def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media
    nome = input("Insira o nome: ")
    nota1 = int(input("Insira a primeira nota: "))
    nota2 = int(input("Insira a segunda nota: "))
    nota3 = int(input("Insira a terceira nota: "))
    nota4 = int(input("Insira a quarta nota: "))

    valor_media = med(nota1,nota2,nota3,nota4)

def main():
    global nome, nota1, nota2, nota3, nota4, valor_media, diretorio, arquivo
    contador: int

    # Verificar permissões da /tmp/exercicios
    caminho_exercicios = "/tmp/exercicios"
    if not os.path.exists(caminho_exercicios):
        os.mkdir(caminho_exercicios)
    os.chmod(caminho_exercicios, 0o744)

    diretorio = caminho_exercicios
    arquivo = "ex21.txt"
    
    for i in range(5):
        entrada()
        print("Nota média:", valor_media)
        cadastro(nome, nota1, nota2, nota3, nota4, valor_media);

if __name__ == '__main__':
    main()