import threading    # para manejar threads 
import time         # para implementar retardos
import random       # para generar números/retardos aleatorios  

movimientos = [-10000, 50000]   # simula movimientos en la cuenta extraccion/deposito

operaciones = []    # se guardaran objetos thread despues de generarlos para poder generar luego operaciones sobre esos objetos usando bucles

class cuentaBancaria():
    def __init__(self, saldo_inicial): #  método con atributo en constructor que representa el saldo de la cuenta
        self.saldo = saldo_inicial      # inicializa saldo

    def movimiento(self,monto):             #método movimiento actualiza y evalua el saldo de acuerdo al monto recibido si son depositos , recibira montos positivos y son extracciones negativos
        time.sleep(random.randint(1,5)/10)  #se incorporan retardos aleatorios para simular una situacion no determinista
        copia_local = self.saldo
        copia_local += monto
        time.sleep(random.randint(1,5)/10)
        self.saldo = copia_local

cuenta = cuentaBancaria(20000)

print("Saldo Inicial:", cuenta.saldo)

for i in range(2):
    operacion = threading.Thread(target=cuenta.movimiento, args = (movimientos[i],))
    operacion.start()
    operaciones.append(operacion)

for i in range(2):
    operaciones[i].join()

print("Saldo Final:",cuenta.saldo)
