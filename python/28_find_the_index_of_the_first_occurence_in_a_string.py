class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0
        N = len(haystack)
        n = len(needle)
        for i in range(N-n+1):
            print(i)
            if haystack[i:i+n] == needle:
                return i
        return -1
