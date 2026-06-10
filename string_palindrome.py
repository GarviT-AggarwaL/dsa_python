#using iterative approach
s='NITIN'
n=len(s)
left=0
right=n-1
while left<=right:
    if(s[left]!=s[right]):
        print("npt plaindrome") 
    left+=1
    right-=1
print("palindrome") 
#recursion method
str='ABCDDCBA'
def func(str,left,right):
    if(left>=right):
        return True
    if(str[left]!=str[right]):
        return False
    return func(str,left+1,right-1)
print(func(str,0,7))
