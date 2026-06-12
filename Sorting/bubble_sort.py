nums=[7,8,4,1,2,9,5]
def bubble_sort(nums):
    n=len(nums)
    for i in range(n-2,-1,-1):
        for j in range(0,i+1):
            if(nums[j]>nums[j+1]):
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
print(bubble_sort(nums))