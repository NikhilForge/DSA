class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={}

        for ch in s:
            if ch in "aeiou":
                if ch in d:
                    d[ch]+=1
                else:
                    d[ch]=1

        a=max(d.values(),default=0)
        con={}
   
        for ch in s:
            if ch not in "aeiou":
                if ch in con:
                    con[ch]+=1
                else:
                    con[ch]=1

        b=max(con.values(),default=0)
        return a+b


        