class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map1, map2 = {}, {}
        words = s.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            c1 = pattern[i]
            w1 = words[i]
            if c1 in map1 and map1[c1] != w1:
                return False
            if w1 in map2 and map2[w1] != c1:
                return False
            else:
                map1[c1] = w1
                map2[w1] = c1
        return True