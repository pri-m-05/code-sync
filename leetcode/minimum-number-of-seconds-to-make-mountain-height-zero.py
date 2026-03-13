class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def can_finish(t):
            total = 0
            for w in workerTimes:
                s = t // w
                x = int(((1 + 8 * s) ** 0.5 - 1) // 2)
                while w * x * (x + 1) // 2 > t:
                    x -= 1
                while w * (x + 1) * (x + 2) // 2 <= t:
                    x += 1
                total += x
                if total >= mountainHeight:
                    return True
            return False

        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left