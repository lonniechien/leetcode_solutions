class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        code = dict()
        i = 0
        s_encoded = list()
        for char in s:
            if char not in code:
                code[char] = i
                i+=1
            s_encoded.append(code[char])
        code = dict()
        i = 0
        t_encoded = list()
        for char in t:
            if char not in code:
                code[char] = i
                i += 1
            t_encoded.append(code[char])
        return s_encoded == t_encoded
