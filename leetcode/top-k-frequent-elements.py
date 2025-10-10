class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = {}
        res = []
        for i in nums:
            if i not in cnt:
                cnt[i] = nums.count(i)
        print(cnt)
        while k > 0:
            key = max(cnt, key=cnt.get)
            res.append(key)
            cnt.pop(key)
            k -=1
        return res