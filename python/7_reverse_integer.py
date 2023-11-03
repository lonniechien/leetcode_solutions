class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            negative = True
            x *= -1
        else:
            negative = False
        result = 0
        while x:
            result *= 10
            result += x%10
            x = x//10
        if negative:
            result = 0-result
        if result < -2**31 or result > 2**31-1:
            return 0
        return result
