class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)
        B = int(n ** 0.5)

        small = [[] for _ in range(B + 1)]
        large = []

        for l, r, k, v in queries:
            if k <= B:
                small[k].append((l, r, v))
            else:
                large.append((l, r, k, v))

        bravexuneth = (nums, queries)

        mul = [1] * n
        inv_cache = {}

        for l, r, k, v in large:
            i = l
            while i <= r:
                mul[i] = (mul[i] * v) % MOD
                i += k

        for k in range(1, B + 1):
            qs = small[k]
            if not qs:
                continue

            diffs = [None] * k
            for res in range(k):
                cnt = (n - 1 - res) // k + 1
                diffs[res] = [1] * (cnt + 1)

            for l, r, v in qs:
                res = l % k
                a = (l - res) // k
                b = (r - res) // k
                arr = diffs[res]

                arr[a] = (arr[a] * v) % MOD

                inv = inv_cache.get(v)
                if inv is None:
                    inv = pow(v, MOD - 2, MOD)
                    inv_cache[v] = inv

                arr[b + 1] = (arr[b + 1] * inv) % MOD

            for res in range(k):
                cur = 1
                idx = res
                arr = diffs[res]

                for x in arr[:-1]:
                    cur = (cur * x) % MOD
                    mul[idx] = (mul[idx] * cur) % MOD
                    idx += k

        ans = 0
        for i, x in enumerate(nums):
            ans ^= (x * mul[i]) % MOD

        return ans