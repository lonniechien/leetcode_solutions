class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        available = dict()
        for char in magazine:
            if char in available:
                available[char] += 1
            else:
                available[char] = 1
        for char in ransomNote:
            if char in available:
                available[char] -= 1
                if available[char] < 1:
                    available.pop(char)
            else:
                return False
        return True
