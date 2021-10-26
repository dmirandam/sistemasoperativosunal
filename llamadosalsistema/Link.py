#crea un enlace duro que apunta a src llamado dst
import os

path = "path"
fd = os.open( path, os.O_RDWR|os.O_CREAT )
os.close( fd )
dst = "/tmp/foo.txt"
os.link( path, dst)

