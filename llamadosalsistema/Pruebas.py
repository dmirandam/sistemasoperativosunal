import os
import gc
import psutil

proc = psutil.Process(os.getpid())
gc.collect()
mem0 = proc.get_memory_info().rss

# create approx. 10**7 int objects and pointers
foo = ['abc' for x in range(10**7)]
mem1 = proc.get_memory_info().rss

# unreference, including x == 9999999
del foo, x
mem2 = proc.get_memory_info().rss

# collect() calls PyInt_ClearFreeList()
# or use ctypes: pythonapi.PyInt_ClearFreeList()
gc.collect()
mem3 = proc.get_memory_info().rss

pd = lambda x2, x1: 100.0 * (x2 - x1) / mem0
print ("Allocation: %0.2f%%" % pd(mem1, mem0))
print ("Unreference: %0.2f%%" % pd(mem2, mem1))
print ("Collect: %0.2f%%" % pd(mem3, mem2))
print ("Overall: %0.2f%%" % pd(mem3, mem0))