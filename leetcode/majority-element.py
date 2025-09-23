class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        ans = 0
        for i in range(len(nums)):
            if count == 0:
                count = 1
                ans = nums[i]
            elif ans == nums[i]:
                count +=1
            else:
                count -=1
        count2 = 0
        for i in range(len(nums)):
            if ans == nums[i]:
                count2+=1
        return ans if count2 > (len(nums) // 2) else -1