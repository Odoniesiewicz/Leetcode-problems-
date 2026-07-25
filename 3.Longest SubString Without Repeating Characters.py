#Scenario

#You are building a username validation system.

#A username is considered “strong” if it contains a long sequence of characters without any repeats.

#Given a string s, return the length of the longest substring that contains no repeated characters.


string="hello11234"
start=0
seen={}
biggest=0
for i in range(len(string)):
    if string[i] in seen and (seen[string[i]]+1>start):
       start=seen[string[i]]+1   
    seen[string[i]]=i
    biggest = max(biggest, i-start+1)

print(biggest)

