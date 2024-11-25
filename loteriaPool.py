from multiprocessing import Pool
from time import sleep

def incremento(numero):
    print("Proceso",numero)
    incremento = 0

    for i in range(1000):
        incremento+= 1
    sleep(1)
    return incremento


if __name__ == "__main__":
    with Pool(processes=4) as pool:
        numeros = [1,2,3,4]
        resultados = pool.map(incremento,numeros)
        total = sum(resultados)
        print(resultados)
        print("Total:",total)