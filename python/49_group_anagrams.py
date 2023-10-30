class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for word in strs:
            chars = str().join(sorted(word))
            if chars in dic:
                dic[chars].append(word)
            else:
                dic[chars] = [word]
        return [words for words in dic.values()]
