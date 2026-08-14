integer=11
variable=integer
binary=""
count=0
while variable!=0:
    binary+=f"{variable%2}"
    variable=variable//2
 
for i in binary:
    if i=="1":
        count+=1

print(count)
