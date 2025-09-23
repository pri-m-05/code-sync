class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj = (len(nums)/2)
        for i in range(len(nums)):
            x = nums.count(nums[i])
            if x > maj:
                maj = nums[i]
                return maj
        return maj