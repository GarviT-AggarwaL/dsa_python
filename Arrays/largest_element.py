nums=[55,32,-97,99,3,67]
largest=nums[0]
n=len(nums)
for i in range(0,n):
    largest=max(largest,nums[i])
print(largest)
#without inbuilt
for i in range(0,n):
    if(nums[i]>largest):
        largest=nums[i]
print(largest)