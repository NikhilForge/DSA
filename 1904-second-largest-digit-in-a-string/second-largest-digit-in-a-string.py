class Solution:
    def secondHighest(self, s: str) -> int:
        count=[]
        for ch in s:
            if ch.isdigit():
                count.append(int(ch))
        u=set(count)

        if len(u)<2:
            return -1
        u=sorted(u)
        return (u[-2])


        