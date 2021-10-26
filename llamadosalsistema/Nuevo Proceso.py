#Imprime una lista con las rutas de los directorios que se utilizarán para buscar un ejecutable con nombre al iniciar un proceso.
import os

path = os.get_exec_path()
print("Following paths will be searched for a named executable:", path)
