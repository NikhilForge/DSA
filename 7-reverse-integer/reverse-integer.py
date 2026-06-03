class Solution:
    def reverse(self, x: int) -> int:
       s = -1 if x < 0 else 1
       x = abs(x)
       b = int(str(x)[::-1])
       ans = s * b
       if ans < -(2**31) or ans > (2**31 - 1):
        return 0

       return ans
        