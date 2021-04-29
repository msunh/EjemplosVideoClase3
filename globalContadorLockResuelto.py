import threading

contador = 0
lock = threading.Lock()

def funcion():
    lock.acquire() #declaro el lock / inicio de zona crítica
    try:
        global contador
        for i in range(1000000):
            contador += 1
    finally:
        lock.release() #libero el lock / finde de la seccion crítica
            
print("Inicio programa principal")
print("Valor Inicial: " + str(contador))

thread_1=threading.Thread(target=funcion)
thread_2=threading.Thread(target=funcion)
thread_3=threading.Thread(target=funcion)

thread_1.start()
thread_2.start()
thread_3.start()

thread_1.join()
thread_2.join()
thread_3.join()

print("Valor Final: " + str(contador))



