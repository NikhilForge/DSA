class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r=0
        l=0
        count=0
        for ch in s:
            if ch=="R":
                r=r+1
            else:
                l=l+1
            if r==l:

                count=count+1
        return count


        