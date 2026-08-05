class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i=len(s)-1
        while i >=0 and s[i]==" ":
            i=i-1
        j=i

        while j>=0 and s[j]!=" ":
            j=j-1
        return len(s[j+1:i+1])
        