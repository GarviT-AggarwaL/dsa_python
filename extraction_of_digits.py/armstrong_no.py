n=1634
num=n
result=0
nod=len(str(n))
while n>0:
    ld=n%10
    result=result+(ld**nod)
    n=n//10
print(result)
if(num==result):
    print("armstrong")
  
