def countBits(n: int):
    output=[]
    for i in range(n+1):
        binary=""
        variable=i
        count=0
        while variable !=0:
            binary+=f"{variable%2}"
            variable = variable//2
        for j in binary:
            if j=="1":
                count+=1
        output.append(count)
    print(output)
        
print(countBits(2))
