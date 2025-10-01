class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long_num = 0
        longest = []
        for i in range(len(s)):
            seen = []
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.append(s[j])
            if len(seen)> long_num:
                longest = seen[:]
                long_num = len(seen)
        print( ''.join(str(x)for x in longest))
        return long_num