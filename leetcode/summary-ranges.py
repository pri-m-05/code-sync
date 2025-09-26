class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 1
        start =0
        def fmt_range(a, b):
            return str(a) if a == b else f"{a}->{b}"
        res = []
        if not nums:
            return res
        while i < len(nums):
            if nums[i] != nums[i-1]+1:
                res.append(fmt_range(nums[start], nums[i-1]))
                start = i   
            i+=1
        res.append(fmt_range(nums[start], nums[-1]))
        return res