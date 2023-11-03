class Solution:
    def frequencySort(self, s: str) -> str:
        chars = dict()
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        result = str()
        while chars:
            char = max(chars, key=chars.get)
            result += char * chars[char]
            chars.pop(char)
        return result
