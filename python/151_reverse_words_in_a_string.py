class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ")
        result = str()
        for i in range(len(words)-1,-1,-1):
            word = words[i]
            if word:
                result += word + " "
        return result[:-1]
