class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        a=list(jewels)
        b=list(stones)
        count=0
        for ch in a:
            for bh in b:
                if ch==bh:
                    count=count+1
        return count