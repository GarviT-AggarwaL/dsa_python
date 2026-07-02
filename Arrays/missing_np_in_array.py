nums=[9,6,4,2,3,5,7,0,1]
n=len(nums)
#brute
for i in range(0,n+1):
    if i not in nums:
        print(i)
#better
freq={}
for i in range(0,n+1):
    freq[i]=0
for num in nums:
    freq[num]=1
for k,v in freq.items():
    if v==0:
        print(k)

#optimal
arr_sum=0
for i in nums:
    arr_sum+=i
expected_sum=n*(n+1)//2
missing=expected_sum - arr_sum
print("missing no ",missing)