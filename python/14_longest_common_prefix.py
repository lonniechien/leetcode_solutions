class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = len(strs[0])
        for s in strs:
            if len(s) < shortest:
                shortest = len(s)
        result = str()
        for i in range(shortest):
            curr = strs[0][i]
            for s in strs:
                if s[i] != curr:
                    return result
            result += strs[0][i]
        return result
