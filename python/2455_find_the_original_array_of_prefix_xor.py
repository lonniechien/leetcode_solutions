class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        result = [pref[0]]
        xor = result[0]
        pref.pop(0)
        for num in pref:
            result.append(xor^num)
            xor = xor^(xor^num)
        return result
