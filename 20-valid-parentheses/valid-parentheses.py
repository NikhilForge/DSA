class Solution:
    def isValid(self, s: str) -> bool:
         k = []
         for i in s:
            if i==" ":
                continue

            if i in "([{":
                k.append(i)
            else:
                if not k:
                    return False

                a = k.pop()

                if i == ')' and a != '(':
                    return False

                if i == ']' and a != '[':
                    return False

                if i == '}' and a != '{':
                    return False

         return len(k) == 0

    
    
        