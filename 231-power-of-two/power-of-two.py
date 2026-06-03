class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        b=n-1
        a=n&b
        if a==0:
            return True
        else:
            return False
        