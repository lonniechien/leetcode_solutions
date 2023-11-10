class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        locs = dict()
        for i, num in enumerate(nums):
            if num in locs:
                j = locs[num]
                if i - j <= k:
                    return True
            locs[num] = i
        return False
