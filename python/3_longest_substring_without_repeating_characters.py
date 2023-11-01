class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        i = 0
        streak = 0
        longest = 0
        n = len(s)
        seen = set()
        while i < n:
            if s[i] in seen:
                start = i - streak + 1
                streak = 0
                i = start
                seen = set()
                continue
            seen.add(s[i])
            i += 1
            streak += 1
            if streak > longest:
                longest = streak
        return longest
