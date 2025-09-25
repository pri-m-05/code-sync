class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        for i in range(len(ransomNote)):
            ch = ransomNote[i]
            if ransomNote[i] in mag:
                j = mag.index(ch)
                del mag[j]
            else:
                return False
        return True