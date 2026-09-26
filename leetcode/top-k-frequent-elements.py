class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        out = []
        keys = sorted(count, key= count.get, reverse = True)
        for i in range(k):
            out.append(keys[i])
        return out