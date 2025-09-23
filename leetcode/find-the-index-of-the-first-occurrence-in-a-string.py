class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = len(needle)
        start = 0
        for i in range(len(haystack)-x+1):
            start = i
            temp = []
            j = i
            while j < x+i:
                temp.append(haystack[j])
                if ''.join(temp) == needle:
                    return start
                j += 1
        return -1