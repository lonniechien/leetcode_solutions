class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        pairs = 0
        for num in nums:
            if num in seen:
                pairs += seen[num]
                seen[num] += 1
            else:
                seen[num] = 1
        return pairs
