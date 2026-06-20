nums=[3,9,5,6,7,2]
n=len(nums)
k=3
#brute
'''
rotations=k%n
for _ in range(0,rotations):
    e=nums.pop()
    nums.insert(0,e)
print(nums) '''
#better
'''
nums[:]=nums[n-k:] + nums[:n-k]
print(nums) '''


#optimal
def reverse(nums,left,right):
    while left<right:
        nums[left],nums[right]=nums[right],nums[left]
        left+=1
        right-=1
    print(nums) 
reverse(nums,n-k,n-1)
reverse(nums,0,n-k-1)
reverse(nums,0,n-1)