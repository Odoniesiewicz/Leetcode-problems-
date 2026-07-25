#You are given a string s and an integer k.
#You can choose any character of the string and change it to any other uppercase English character.
#You can perform this operation at most k times.

#Return the length of the longest substring containing the same letter you can get after performing the above operations.

#use sliding window method, condition is when you find a new character replace it by reducing k 

k=2
s="ABBB"
copy=s
start=0
count=0
lengths=[]
seen={}
max_count=0
max_length=0

            
for index in range (len(s)):
    if s[index] in seen:
        seen[s[index]]+=1
    else:
        seen[s[index]]=1

    if seen[s[index]] > max_count:
        max_count = seen[s[index]]
    
    window =index-start+1
    to_change=window-max_count

    if to_change > k:
        leaving=s[start]
        seen[leaving] -=1
        start+=1
        
    current_window = index-start+1
    if current_window > max_length:
        max_length=current_window
print( max_length)

##for index in range (len(s)):
##    if s[index]== s[start] :
##        count+=1
##        lengths.append(index-start+1)
##        #print(count)
##    else:
##        if k>0:
##            k-=1
##            count+=1
##            lengths.append(index-start+1)
##        else:
##            #lengths.append(index-start+1)
##            start+=1
