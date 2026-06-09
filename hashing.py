n=[5,3,2,2,1,5,5,7,5,10]
m=[10,111,1,9,5,67,2]
hash_list=[0]*11
for num in n:
    hash_list[num]+=1
for num in m:
    if(num<1 or num>10):
        print("zero")
    else:
        print(hash_list[num])

#using dictionary
freq_map=dict()
l=len(n)
for i in range(0,l):
    freq_map[n[i]]=freq_map.get(n[i],0)+1
print(freq_map)
for i in m:
    print(freq_map.get(i,0))