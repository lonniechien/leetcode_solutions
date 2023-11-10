class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(words) != len(pattern):
            return False
        code = dict()
        used_words = set()
        for letter, word in zip(pattern,words):
            if letter not in code:
                if word not in used_words:
                    code[letter] = word
                    used_words.add(word)
                else:
                    return False
            elif code[letter] != word:
                return False
        return True
