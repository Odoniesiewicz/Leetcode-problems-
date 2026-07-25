#Given an array of strings strs, group the anagrams together.
#You can return the answer in any order.

#each word should store its own dictionary 
strs=["eat","tea","tan","ate","nat","bat"]
words=[]
seen={}



for word in strs:
    word=sorted(word)
    words.append("".join(word))
for i in range(len(words)):
    if words[i] in seen:
        seen[words[i]].append(strs[i])
    else:
        seen[words[i]]=[strs[i]]

print(list(seen.values()))


##for i in range(len(strs)):
##    words.append({})
##    for j in range(len(strs[i])):
##        if strs[i][j] in words[i]:
##            words[i][strs[i][j]]+=1
##        else:
##            words[i][strs[i][j]]=1
