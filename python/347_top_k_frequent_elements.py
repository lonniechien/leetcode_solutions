class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        tups = [(count, counts[count]) for count in counts]
        tups = sorted(tups, key=lambda count:count[1], reverse=True)

        return [tup[0] for tup in tups[:k]]
