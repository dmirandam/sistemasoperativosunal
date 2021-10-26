#Lee como máximo n bytes del descriptor de archivo fd
import os
path = "path"
fd = os.open(path, os.O_RDONLY)
n = 10
bytes = os.read(fd, n)
print(bytes)

