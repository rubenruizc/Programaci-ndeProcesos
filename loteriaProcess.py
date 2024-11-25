from multiprocessing import Process,Value,Lock

def incremento(id,variable,lock):
    for i in range(1000):
        with lock:
            print(f"P{id} incrementa el valor {variable.value}")
            variable.value += 1

if __name__ == "__main__":

    numProcesos = 4
    contador = Value("i",0)
    procesos = []
    lock = Lock()

    for i in range(numProcesos):
        p = Process(target=incremento,args=(i,contador,lock,))
        p.start()
        procesos.append(p)

    for p in procesos:
        p.join()

    print("Resultado:", contador.value)
    
    