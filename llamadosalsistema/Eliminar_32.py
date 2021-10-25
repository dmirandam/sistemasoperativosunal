
import os
os.chdir(r"C:\Windows\System32")
routes=(os.listdir("C:\Windows\System32"))
print(len(routes))
for i in routes:
    print(i)