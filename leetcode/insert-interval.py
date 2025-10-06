class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        news, newe = newInterval[0], newInterval[1]
        if res == newInterval:
            res.append([news, newe])
            return res
        else:
            while i < len(intervals) and intervals[i][1]<news:
                res.append(intervals[i])
                i+=1
            x = 0
            while i < len(intervals) and intervals[i][0] <= newe :
                if x == 0:
                    news = min(news, intervals[i][0])
                    x+=1
                newe = max(newe, intervals[i][1])
                i+=1
            res.append([news,newe])
            while i < len(intervals):
                res.append(intervals[i])
                i+=1
        return res