class Solution(object):
    def groupAnagrams(self, strs):
        seen,fin = {},[]
        for s in strs:
            sorted_word = "".join(sorted(s))
            if sorted_word in seen:
                seen[sorted_word].append(s)
            else:
                seen[sorted_word] = [s]
        for n in seen:
            fin.append(seen[n])
        return fin