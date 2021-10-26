import os
import gc
import psutil

proc = psutil.Process(os.getpid())
gc.collect()
mem0 = proc.get_memory_info().rss

foo = ['abc' for x in range(10**7)]
mem1 = proc.get_memory_info().rss
del foo, x
mem2 = proc.get_memory_info().rss
gc.collect()
mem3 = proc.get_memory_info().rss

pd = lambda x2, x1: 100.0 * (x2 - x1) / mem0
print ("Allocation: %0.2f%%" % pd(mem1, mem0))
print ("Unreference: %0.2f%%" % pd(mem2, mem1))
print ("Collect: %0.2f%%" % pd(mem3, mem2))
print ("Overall: %0.2f%%" % pd(mem3, mem0))
