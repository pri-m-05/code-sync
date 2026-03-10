class Solution:
    def numberOfStableArrays(self, zero, one, limit):
        MOD = 10**9 + 7
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]
        row0 = [[0] * (one + 1) for _ in range(zero + 1)]
        col1 = [[0] * (one + 1) for _ in range(zero + 1)]

        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(zero + 1):
            for j in range(one + 1):
                if i >= 1 and j >= 1:
                    dp0[i][j] = col1[i - 1][j]
                    if i - limit - 1 >= 0:
                        dp0[i][j] = (dp0[i][j] - col1[i - limit - 1][j]) % MOD

                    dp1[i][j] = row0[i][j - 1]
                    if j - limit - 1 >= 0:
                        dp1[i][j] = (dp1[i][j] - row0[i][j - limit - 1]) % MOD

                row0[i][j] = dp0[i][j]
                if j > 0:
                    row0[i][j] = (row0[i][j] + row0[i][j - 1]) % MOD

                col1[i][j] = dp1[i][j]
                if i > 0:
                    col1[i][j] = (col1[i][j] + col1[i - 1][j]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD