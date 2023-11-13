class Solution:
    def reverseVowels(self, s: str) -> str:
        valid_vowels = {'a','A','e','E','i','I','o','O','u','U'}
        vowels = list()
        positions = list()
        for i,char in enumerate(s):
            if char in valid_vowels:
                vowels.append(char)
                positions.append(i)
        vowels.reverse()
        result = str()
        j = 0
        max_j = len(positions)
        for i,char in enumerate(s):
            if j == max_j:
                return result + s[i:]
            if i == positions[j]:
                result += vowels[j]
                j += 1
            else:
                result += char
        return result
