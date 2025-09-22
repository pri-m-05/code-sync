class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = len(s)
        count = 0
        while x > 0:
            if s[x-1] == " " and count != 0:
                return count
            else:
                if s[x-1] != " ":
                    count +=1
                x-=1
        return count