class Solution(object):
    def minOperations(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        z = s.count('0')

        if z == 0:
            return 0

        if k == n:
            return 1 if z == n else -1

        def ceil_div(a, b):
            return (a + b - 1) // b

        ans = float('inf')

       
        for parity in (0, 1):
            
            if (parity * (k % 2)) % 2 != (z % 2):
                continue

            
            t = ceil_div(z, k)

            
            if parity == 0:   
                t = max(t, ceil_div(z, n - k))
            else:             
                t = max(t, ceil_div(n - z, n - k))

            
            if t % 2 != parity:
                t += 1

            ans = min(ans, t)

        return -1 if ans == float('inf') else ans