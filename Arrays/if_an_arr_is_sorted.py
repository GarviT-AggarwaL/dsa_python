nums=[3,4,51,1,2,67,8]
n=len(nums)

sorted_flag=True

for i in range(0,n-1):
    if nums[i] > nums[i+1]:
        sorted_flag=False
        break

if sorted_flag:
    print("sorted")
else:
    print("false")