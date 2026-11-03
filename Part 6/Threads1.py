# 1) Fazer uma aplicação que rode 5 Threads que cada uma delas receba um inteiro chamado id
# como parâmetro e imprima no console o texto “Thread N” + id. Antes de imprimir o valor, deve-
# se fazer um sleep de 0.5 segundos.

import multiprocessing
import time

def task(id: int) -> None:
    time.sleep(0.5)
    print("Thread N.", id)
    

def main() -> None:
    ids: int = [0]*5
    p: int = 0

    for p in range(5):
        ids[p] = p + 1

    with multiprocessing.Pool(processes=5) as threads:
        threads.map(task, ids)

if __name__ == "__main__":
    main()
