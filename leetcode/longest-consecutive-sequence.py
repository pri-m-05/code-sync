class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        best = 0
        for x in s:
            if x - 1 not in s:          # start of a streak
                y = x
                while y in s:
                    y += 1
                best = max(best, y - x)
        return best