class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        b=sorted(s)
        c=sorted(t)
        if len(b)!=len(c):
            return False
        else:
            for i in range(len(b)):
                if b[i]==c[i]:
                    pass
                 
                else:
                    return False
            return True

        