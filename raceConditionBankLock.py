import threading  # para manejar threads 
import time       # para implementar retardos  
import random     # para generar números/retardos aleatorios  

movimientos = [-10000, 50000] # simula movimientos en la cuenta extraccion/deposito

operaciones = [] # se guardaran objetos thread despues de generarlos para poder generar luego operaciones sobre esos objetos usando bucles

#tambien puedo definir el lock fuera para usarlo

class cuentaBancaria():                 #se define la clase cuenta bancaria
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.lock = threading.Lock() ########defino/declaro el lock para que se lo haga el constructor

    def movimiento(self,monto):
        self.lock.acquire()  ####adquiero/solicito el lock , inicio de la seccion crítica
        try:                 #se ejecuta dentro de una estructura try
            time.sleep(random.randint(1,5)/10)
            copia_local = self.saldo
            copia_local += monto
            time.sleep(random.randint(1,5)/10)
            self.saldo = copia_local
        finally:                #se ejecuta si o si al terminar
            self.lock.release() #### libera el lock , fin de la seccion  critica

cuenta = cuentaBancaria(20000)

print("Saldo Inicial:", cuenta.saldo)

for i in range(2):
    operacion = threading.Thread(target=cuenta.movimiento, args = (movimientos[i],))
    operacion.start()
    operaciones.append(operacion)

for i in range(2):
    operaciones[i].join()

print("Saldo Final:",cuenta.saldo)
