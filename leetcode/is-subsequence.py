class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        temp =[]
        i = 0
        j = 0
        if s == "":
            return True
        while j< len(t):
            if t[j] == s[i]:
                temp.append(t[j])
                if len(s) > 1:
                    i+=1
                if "".join(temp) == s:
                    return True
            j+=1
        return False