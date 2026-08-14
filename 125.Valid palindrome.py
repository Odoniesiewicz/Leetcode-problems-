def isPalindrome(s: str) -> bool:
        s=s.lower()
        cleaned=""
        for i in s:
            if i.isnumeric() or i.isalpha():
                cleaned+=i
        return cleaned[::-1]==cleaned

        
print(isPalindrome("A!!!A{)_A'A"))
