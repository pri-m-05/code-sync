class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        i = 1
        intervals.sort()
        while i < len(intervals):
            s1, e1 = intervals[i-1][0], intervals[i-1][1]
            s2, e2 = intervals[i][0], intervals[i][1]
            if s2 < e1:
                count+=1
                if e1 < e2:
                    intervals.pop(i)
                    i -= 1
                else:
                    intervals.pop(i-1)
                    i -= 1
            i += 1
        return count