nums=[1,1,1,2,3,4,4,7,9,9,9,10]
#brute
'''q_map={}
n=len(nums)
for i in range(0,n):
    freq_map[nums[i]]=0
j=0
for k in freq_map:
    nums[j]=k
    j+=1
print(j)'''
#optimal
n=len(nums)
if(n==1):
    print("1")
i=0
j=i+1
while j<n:
    if(nums[j]!=nums[i]):
        i+=1
        nums[i]=nums[j]
    j+=1
print(i+1)
