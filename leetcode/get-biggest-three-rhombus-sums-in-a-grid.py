class Solution(object):
    def getBiggestThree(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(grid), len(grid[0])
        sums = set()

    
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])

        for i in range(m):
            for j in range(n):
                k = 1
                while i + 2 * k < m and j - k >= 0 and j + k < n:
                    total = 0

                    for t in range(k):
                        total += grid[i + t][j + t]

                  
                    for t in range(k):
                        total += grid[i + k + t][j + k - t]

                
                    for t in range(k):
                        total += grid[i + 2 * k - t][j - t]

                    
                    for t in range(k):
                        total += grid[i + k - t][j - k + t]

                    sums.add(total)
                    k += 1

        return sorted(sums, reverse=True)[:3]