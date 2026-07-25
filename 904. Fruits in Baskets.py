#fruits in baskets


fruits=[0,1,2,1]
start=0
seen={}
biggest=0
lengths=[]
for i in range(len(fruits)):
    if fruits[i] not in seen:
        seen[fruits[i]]=1
    else:
        seen[fruits[i]]+=1
    while len(seen)>2:
        seen[fruits[start]]-=1
        if seen[fruits[start]] ==0:
            del(seen[fruits[start]])
        start+=1
    lengths.append(i-start+1)


print(max(lengths))
