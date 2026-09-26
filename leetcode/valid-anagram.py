class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_t = len(t)
        s_s = len (s)
        counts = Counter(t)
        if s_t != s_s:
            return False
        if s_t == s_s:
            for letter in s:
                if counts[letter] == 0:
                    return False
                counts[letter] -= 1 
        return True