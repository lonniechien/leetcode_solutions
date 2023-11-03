class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) < 1:
            return 0
        if s[0] == '-':
            negative = True
            s = s[1:]
        elif s[0] == '+':
            negative = False
            s = s[1:]
        else:
            negative = False
        nums = set([str(i) for i in range(10)])
        digits = '0'
        for char in s:
            if char not in nums:
                break
            digits += char
        ans = int(digits)
        if negative:
            return max(0-ans, -2**31)
        else:
            return min(ans, 2**31-1)
