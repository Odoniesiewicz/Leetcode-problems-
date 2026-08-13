#20.VALID PARENTHESES

def isValid(s: str) -> bool:
        stack=[]
        mappings={")":"(" , "}":"{" , "]":"["}
        if len(s)//2==0:
            return False
        for i in s:
            if i in mappings and stack and mappings[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(i)       
        return len(stack)==0

print(isValid("([)]"))
