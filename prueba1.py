from multiprocessing import Pool
from time import sleep

def square (number):
    print("Entrando...",number)
    sleep(2)
    cuadrado = number * number
    print(number,"x",number,"=",cuadrado)
    sleep(2)
    return cuadrado

if __name__ == '__main__':
    with Pool(processes = 3) as pool:
        numbers = [1,2,3,4,5]
        results = pool.map(square,numbers)

    print("Resultados:",results)

