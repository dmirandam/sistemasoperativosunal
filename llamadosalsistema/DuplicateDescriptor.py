import os
path = "path"
fd = os.open(path, os.O_WRONLY)

dup_fd = os.dup(fd)
pid = os.getpid()


 
