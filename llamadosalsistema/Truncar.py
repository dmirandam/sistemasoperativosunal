#truncar archivo
import os 
path = 'path'
fd = os.open(path, os.O_RDWR|os.O_CREAT)
string = 'String'
line = str.encode(string)
os.write(fd, line)
os.truncate(path, 15)

  


