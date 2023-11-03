class Solution:
    def intToRoman(self, num: int) -> str:
        result = str()
        if num >= 1000:
            thousands = num // 1000
            for i in range(thousands):
                result += 'M'
            num -= thousands * 1000
        if num >= 100:
            if num >= 900:
                result += 'CM'
                num -= 900
            elif num >= 500:
                result += 'D'
                num -= 500
            elif num >= 400:
                result += 'CD'
                num -= 400
            hundreds = num // 100
            for i in range(hundreds):
                result += 'C'
            num -= hundreds * 100
        if num >= 10:
            if num >= 90:
                result += 'XC'
                num -= 90
            elif num >= 50:
                result += 'L'
                num -= 50
            elif num >= 40:
                result += 'XL'
                num -= 40
            tens = num // 10
            for i in range(tens):
                result += 'X'
            num -= tens * 10
        if num >= 9:
            result += 'IX'
            num -= 9
        elif num >= 5:
            result += 'V'
            num -= 5
        elif num >= 4:
            result += 'IV'
            num -= 4
        for i in range(num):
            result += 'I'
        return result
