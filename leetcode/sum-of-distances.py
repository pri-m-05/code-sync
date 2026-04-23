from collections import defaultdict

class Solution(object):
    def distance(self, nums):
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = [0] * len(nums)

        for arr in pos.values():
            total = sum(arr)
            pref = 0
            m = len(arr)

            for k, i in enumerate(arr):
                left = i * k - pref
                right = (total - pref - i) - i * (m - k - 1)
                ans[i] = left + right
                pref += i

        return ans