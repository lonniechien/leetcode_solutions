class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        locations = dict()
        for i,char in enumerate(s):
            if char in locations:
                locations[char].append(i)
            else:
                locations[char] = [i]
        result = 0
        for bun in locations:
            first = locations[bun][0]
            last = locations[bun][-1]
            if first+1 < last:
                for meat in locations:
                    if meat in s[first+1:last]:
                        result += 1
        return result
