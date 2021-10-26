import os
path = "path"
X = os.lstat(path)
major_dnum = os.major(X.st_dev)
minor_dnum = os.minor(X.st_dev)

print ("Major Number :", major_dnum)
print ("Minor Number :", minor_dnum)

