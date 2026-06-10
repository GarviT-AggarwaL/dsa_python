def func(sum,i,N):
    if(i>N):
        print(sum)
        return
    func(sum+i,i+1,N)

func(0,1,4)
  
def func1(N):
    if N==1:
        return 1
    return N + func1(N-1)
func1(4)
