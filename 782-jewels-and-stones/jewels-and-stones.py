class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
    
        count=0
        for ch in jewels:
            for bh in stones:
                if ch==bh:
                    count=count+1
        return count