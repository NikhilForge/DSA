class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        a=[]
        for i in range(len(words)):
            for ch in words[i]:
                if ch==x:
                    a.append(i)
                    break
        return a
        