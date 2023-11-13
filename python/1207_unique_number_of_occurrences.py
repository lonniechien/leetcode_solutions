class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = dict()
        for num in arr:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        seen = set()
        for num in counts:
            if counts[num] in seen:
                return False
            else:
                seen.add(counts[num])
        return True
