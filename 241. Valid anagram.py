class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dictionary={}
        t_dictionary={}
        for i in s:
            if i in s_dictionary:
                s_dictionary[i]+=1
            else:
                s_dictionary[i]=1
        for i in t:
            if i in t_dictionary:
                t_dictionary[i]+=1
            else:
                t_dictionary[i]=1
        return s_dictionary == t_dictionary
                        
