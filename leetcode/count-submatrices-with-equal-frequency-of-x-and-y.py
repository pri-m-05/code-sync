class Solution(object):
    def numberOfSubmatrices(self, grid):
        m, n = len(grid), len(grid[0])
        diff = [0] * n
        xs = [0] * n
        ans = 0

        for i in range(m):
            d = 0
            x = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    diff[j] += 1
                    xs[j] += 1
                elif grid[i][j] == 'Y':
                    diff[j] -= 1

                d += diff[j]
                x += xs[j]

                if d == 0 and x > 0:
                    ans += 1

        return ans