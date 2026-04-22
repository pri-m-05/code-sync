class Solution(object):
    def twoEditWords(self, queries, dictionary):
        def ok(a, b):
            diff = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff += 1
                    if diff > 2:
                        return False
            return True

        ans = []
        for q in queries:
            for d in dictionary:
                if ok(q, d):
                    ans.append(q)
                    break
        return ans