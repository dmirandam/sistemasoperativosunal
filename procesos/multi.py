import threading

Num_Hilos = 10 

class Hilos(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        threadName = threading.currentThread().getName()
        print("Ejecutando %s" % threadName)

print(f'[Ejecutando {Num_Hilos} Hilos]')

for i in range(Num_Hilos):
    hilos = Hilos()
    hilos.start()



