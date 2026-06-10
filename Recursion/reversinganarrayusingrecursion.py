num=[2,4,1,7,6,3,8,9,5]
def fun(arr,left,right):
    if(left>=right):
        return
    arr[left],arr[right]=arr[right],arr[left]
    fun(arr,left+1,right-1)
fun(num,0,8)
print(num)