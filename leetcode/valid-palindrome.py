class Solution:
    def isPalindrome(self, s: str) -> bool:
        copy = []
        rem = {chr(c) for c in range(32, 127) if not chr(c).isalnum()}
        s = s.lower()
        for i in range(len(s)):
            if s[i] in rem:
                continue
            copy.append(s[i])
        rev = copy[::-1]
        print(rev)
        print(copy)
        if rev == copy:
            return True
        return False