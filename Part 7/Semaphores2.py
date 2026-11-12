import multiprocessing
import random
import time

def pessoa(id, ms):
    corredor: int = 200
    atual: int = 0
    tempo = random.randint(1, 2)

    while(atual < corredor):
        atual += ms

    time.sleep(tempo)
    print(f"A pessoa N{id} cruzou a porta.")

def main():
    params = []
    ms: int = 0
    id: int = 0

    for i in range(4):
        id = i + 1
        ms = random.randint(4, 6)

        params.append((id, ms))

    with multiprocessing.Pool(processes=4) as pool:
        pool.starmap(pessoa, params)

if __name__ == "__main__":
    main()