n=5438
count=0
while n>0:
    count+=1
    n=n//10
print(count)

#logaristhmic based approach
from math import *
def count(a):
    return int(log10(a)+1)
print(count(3456))