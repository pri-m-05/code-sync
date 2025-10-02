class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_count, have_count = {}, {}
        l = 0
        formed = 0
        best = float("inf")
        for i in range(len(t)):
            if t[i] not in need_count:
                need_count[t[i]] = 0
            need_count[t[i]] += 1
        print(need_count)

        required = len(need_count)
        for r in range(len(s)):
            if s[r] not in have_count:
                have_count[s[r]] = 0
            have_count[s[r]] += 1
            if s[r] in need_count and need_count[s[r]] == have_count[s[r]]:
                formed +=1
                if formed == required:
                    while formed == required:
                        if (r-l+1) < best:
                            best = r-l+1
                            best_l = l
                            best_r = r
                        c = s[l]
                        have_count[c] -= 1
                        if c in need_count and need_count[c] > have_count[c]:
                            formed -= 1
                        l+=1
        if best == float("inf"):
            return ""
        return s[best_l:best_r+1]