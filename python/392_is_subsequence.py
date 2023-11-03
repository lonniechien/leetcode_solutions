class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not len(s):
            return True
        s = s + "1"
        for char in t:
            if char == s[0]:
                s = s[1:]
                if len(s) == 1:
                    return True
        return False
