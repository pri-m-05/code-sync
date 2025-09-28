class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t = list(t)
        for i in s:
            if i not in t:
                return False
            if i in t:
                t.remove(i)
            
        return True