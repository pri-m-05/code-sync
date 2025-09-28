class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumsquares(n)

            if n == 1:
                return True

        return False

    def sumsquares(self, n: int) -> int:
        output = 0
        while n:
            dig = n % 10
            dig = dig ** 2
            output += dig
            n = n//10
        return output