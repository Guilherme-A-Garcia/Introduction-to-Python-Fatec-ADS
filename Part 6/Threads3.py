import multiprocessing
import time
import random

def task(params: list) -> None:
    # Distância máxima = 30cm
    dist_max: int = 30
    dist_atual: int = 0
    salto: int = 0

    while dist_atual < dist_max:
        time.sleep(0.2)
        salto = random.randint(0, params[1])
        dist_atual += salto
        print(f"O sapo {params[0]} saltou {salto}cm. Distância percorrida: {dist_atual}")

    print(f"\nO sapo {params[0]} chegou! <--\n")
    
def main() -> None:
    sapo: int = 0
    params: list = []
    vals: int = [0]*2
    dist_pulo: int = 0
    i: int = 0

    for i in range(3):
        sapo = i + 1

        dist_pulo = random.randint(1, 5)
        vals = [sapo, dist_pulo]
        params.append(vals)

    with multiprocessing.Pool(processes=3) as pool:
        pool.map(task, params)

if __name__ == "__main__":
    main()
