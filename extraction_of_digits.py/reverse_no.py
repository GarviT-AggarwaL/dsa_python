n=1234
result=0
while n>0:
    ld=n%10
    result=(result*10)+ld
    n=n//10
print(result)
if(n==result):
    print("palindrom")
else:
    print("not palindrome")
