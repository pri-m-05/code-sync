class Solution(object):
    def maxStability(self, n, edges, k):
        class DSU(object):
            def __init__(self, n):
                self.p = list(range(n))
                self.sz = [1] * n
                self.cnt = n

            def find(self, x):
                while self.p[x] != x:
                    self.p[x] = self.p[self.p[x]]
                    x = self.p[x]
                return x

            def union(self, a, b):
                a = self.find(a)
                b = self.find(b)
                if a == b:
                    return False
                if self.sz[a] < self.sz[b]:
                    a, b = b, a
                self.p[b] = a
                self.sz[a] += self.sz[b]
                self.cnt -= 1
                return True

        max_s = 0
        for _, _, s, _ in edges:
            if s > max_s:
                max_s = s

        def can(t):
            dsu = DSU(n)

            for u, v, s, must in edges:
                if must:
                    if s < t:
                        return False
                    if not dsu.union(u, v):
                        return False

            for u, v, s, must in edges:
                if must == 0 and s >= t:
                    dsu.union(u, v)

            need = dsu.cnt - 1
            if need == 0:
                return True
            if need > k:
                return False

            for u, v, s, must in edges:
                if must == 0 and s < t and s * 2 >= t:
                    dsu.union(u, v)

            return dsu.cnt == 1

        if not can(1):
            return -1

        lo, hi = 1, max_s * 2
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo