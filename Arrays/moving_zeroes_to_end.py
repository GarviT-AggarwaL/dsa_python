#brute
nums=[1,0,2,4,0,3,5,2,0,9]
n=len(nums)
'''
temp=[]
for i in range(0,n):
    if(nums[i]!=0):
        temp.append(nums[i])
nz=len(temp)
for i in range(0,nz):
    nums[i]=temp[i]
for i in range(nz,n):
    nums[i]=0
print(nums) '''

#optimal
if n <= 1:
    print(nums)

i = 0

# Find first zero
while i < n:
    if nums[i] == 0:
        break
    i += 1

if i == n:
    print(nums)

j = i + 1

while j < n:
    if nums[j] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
    j += 1

print(nums)