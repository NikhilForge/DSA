class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ml=len(strs[0])
        for s in strs:
            if len(s)<ml:
                ml=len(s)
        i=0
        while i<ml:
            for s in strs:
                if s[i]!=strs[0][i]:
                    return s[:i]
            i+=1
        return s[:i]


       
                

        


        
        