class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        size = len(nums)
        for n in range(size):
            x = target - nums[n]
            if nums[n] not in seen:
                if x in seen:
                    return [seen[x], n]
                if x not in seen:
                    seen[nums[n]] = n
                    n += 1
            if nums[n] in seen:
                if x in seen:
                    return [seen[x], n]