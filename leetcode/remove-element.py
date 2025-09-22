class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = len(nums)
        i = 0
        k = 0
        while i < x:
            if nums[i] == val:
                j = i+1
                while j < x:
                    nums[j-1] = nums[j]
                    j +=1
                x -= 1
            else:
                k+=1
                i+=1
        return k