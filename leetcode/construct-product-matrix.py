class Solution(object):
    def constructProductMatrix(self, grid):
        mod = 12345
        flat = [x for row in grid for x in row]
        n = len(flat)
        prod = [1] * n

        cur = 1
        for i in range(n):
            prod[i] = cur
            cur = (cur * flat[i]) % mod

        cur = 1
        for i in range(n - 1, -1, -1):
            prod[i] = (prod[i] * cur) % mod
            cur = (cur * flat[i]) % mod

        res = []
        idx = 0
        for row in grid:
            m = len(row)
            res.append(prod[idx:idx + m])
            idx += m

        return res