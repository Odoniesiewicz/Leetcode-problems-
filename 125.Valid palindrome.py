def isPalindrome(s: str) -> bool:
        s=s.lower()
        cleaned=""
        for i in s:
            if i.isnumeric() or i.isalpha():
                cleaned+=i
        print(cleaned[::-1])
        return cleaned[::-1]==cleaned

        
print(isPalindrome("AB!!!A{)_A'A"))
