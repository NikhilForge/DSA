class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=""
        for ch in s:
            if ch.isalnum():
                n+=ch
        n=n.lower()
        if n[::-1]==n:
            return True
        else:
            return False
        


        