#printing 1 to n
def func(i,N):
    if(i>N):
        return
    print(i)
    func(i+1,N)
func(1,4)