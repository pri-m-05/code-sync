class Solution(object):
    def minimumDistance(self, nums):
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = []
            pos[x].append(i)

        ans = float('inf')

        for arr in pos.values():
            if len(arr) >= 3:
                for i in range(len(arr) - 2):
                    ans = min(ans, 2 * (arr[i + 2] - arr[i]))

        return -1 if ans == float('inf') else ans