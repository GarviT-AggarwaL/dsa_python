#brute approach
import math
n=20
result=[]
for i in range(1,n+1):
    if(n%i==0):
        result.append(i)
print(result)
#better approach
n=30
result=[]
for i in range(1,n//2):
    if(n%i==0):
        result.append(i)
result.append(n)
print(result)

#optimum
n=36
result=[]
for i in range(1,int(math.sqrt(n)+1)):
    if(n%i==0):
        result.append(i)
    if(n//i!=i):
        result.append(n//i)#yeh isliye likha hai jissa same no jaise6,6 do baar append na ho per baaki sab hojaye isme isliye 1 ke baad 36 as a factor print then 2 k baad 18
print(result)