class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        rev = int(str(x)[::-1])
        reg = int(str(x))
        if rev == reg:
            return True
        return False