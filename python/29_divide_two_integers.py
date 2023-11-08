class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend < 0 and divisor < 0:
            dividend = 0 - dividend
            divisor = 0 - divisor
            negative = False
        elif dividend < 0:
            dividend = 0 - dividend
            negative = True
        elif divisor < 0:
            divisor = 0 - divisor
            negative = True
        else:
            negative = False
        result = len(range(divisor,dividend+1,divisor))
        if negative: 
            return max(-2**31,-result)
        else:
            return min(2**31-1,result)
