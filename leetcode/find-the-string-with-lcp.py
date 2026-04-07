class Solution:
    def findTheString(self, lcp):
        n = len(lcp)

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(n):
                if lcp[i][j] != lcp[j][i]:
                    return ""

        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    union(i, j)

        groups = {}
        chars = [""] * n
        cur = 0

        for i in range(n):
            r = find(i)
            if r not in groups:
                if cur == 26:
                    return ""
                groups[r] = chr(ord("a") + cur)
                cur += 1
            chars[i] = groups[r]

        for i in range(n):
            for j in range(i + 1, n):
                if (chars[i] == chars[j]) != (find(i) == find(j)):
                    return ""

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if chars[i] == chars[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1

        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""

        return "".join(chars)