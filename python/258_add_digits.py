class Solution:
    def addDigits(self, num: int) -> int:
        result = num
        while num // 10:
            result = 0
            while num:
                result += num % 10
                num = num // 10
            num = result
        return result 
