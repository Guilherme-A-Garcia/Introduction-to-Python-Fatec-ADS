import multiprocessing
import time
import random

def task(params: list) -> None:
    soma: int = 0
    i: int = 0
    time.sleep(0.2)
    for i in range(1, 7):
        soma += params[1]
    print("Thread:", params[0], "| Soma:", soma)
    
def main() -> None:
    id: int = 0
    params = []
    vals: int = [0]*6
    val1: int = 0
    val2: int = 0
    val3: int = 0
    val4: int = 0
    val5: int = 0
    i: int = 0

    for i in range(3):
        id = i + 1

        val1 = random.randint(1, 100)
        val2 = random.randint(1, 100)
        val3 = random.randint(1, 100)
        val4 = random.randint(1, 100)
        val5 = random.randint(1, 100)
        vals = [id, val1, val2, val3, val4, val5]
        params.append(vals)

    with multiprocessing.Pool(processes=3) as threads:
        threads.map(task, params)

if __name__ == "__main__":
    main()
