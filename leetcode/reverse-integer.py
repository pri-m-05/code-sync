class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = -1 if x < 0 else 1
        x = abs(x)

        res = 0

        limit = INT_MAX if sign == 1 else 2**31
        last_digit_limit = 7 if sign == 1 else 8

        while x != 0:
            digit = x % 10
            x //= 10

            if res > limit // 10 or (res == limit // 10 and digit > last_digit_limit):
                return 0

            res = res * 10 + digit

        res *= sign

        if res < INT_MIN or res > INT_MAX:
            return 0
        return res