class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g={}
        for ch in strs:
            key="".join(sorted(ch))
            if key not in g:
                g[key]=[]
            g[key].append(ch)
        return list(g.values())
       
                    
            
        