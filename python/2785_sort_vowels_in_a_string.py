class Solution:
    def sortVowels(self, s: str) -> str:
        valid_vowels = {'a','e','i','o','u','A','E','I','O','U'}
        positions = list()
        vowels = list()
        for i,char in enumerate(s):
            if char in valid_vowels:
                positions.append(i)
                vowels.append(char)
        vowels.sort()
        result = str()
        j = 0
        done = False
        for i,char in enumerate(s):
            try:
                if i == positions[j]:
                    result += vowels[j]
                    j += 1
                else:
                    result += s[i]
            except IndexError:
                result += s[i]
        return result
