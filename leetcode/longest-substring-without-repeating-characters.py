class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        last = {}

        if len(s) == 1:
            max_len = 1
            return max_len

        for right, i in enumerate(s):
            length = 0
            if s[right] in last and last[i] >= left:
                left = last[i] + 1
            last[i] = right
            length = right - left +1
            if length > max_len:
                max_len = length
        return max_len