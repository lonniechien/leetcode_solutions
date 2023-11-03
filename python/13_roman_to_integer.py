class Solution:
    def romanToInt(self, s: str) -> int:
        chars = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        pairs = {
            'IV',
            'IX',
            'XL',
            'XC',
            'CD',
            'CM',
        }
        result = 0
        for i in range(len(s)-1):
            pair = s[i] + s[i+1]
            if pair in pairs:
                result -= chars[s[i]]
            else:
                result += chars[s[i]]
        return result + chars[s[-1]]
