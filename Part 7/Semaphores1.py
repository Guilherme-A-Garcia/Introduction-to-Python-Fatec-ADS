import multiprocessing
import random

sentido: str = ""

def init(s):
    global sentido
    sentido = s

def task(sent):
    global sentido
    sentidos: list = ["Esquerda", "Direita", "Cima", "Baixo"]
    sentido = sentidos[sent]
    print(f"Sentido: {sentido}")

def main():
    global sentido
    params: list = [0]*3
    sentido = multiprocessing.Value('i', 0)

    for i in range(0, 3):
        params[i] = random.randint(0, 3)

    with multiprocessing.Pool(processes=4, initializer=init, initargs=(sentido, )) as pool:
        pool.map(task, params)

if __name__ == "__main__":
    main()