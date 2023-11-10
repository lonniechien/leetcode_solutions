class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        idxs = dict()
        for i, num in enumerate(sorted_nums):
            if num not in idxs:
                idxs[num] = i
        result = list()
        for num in nums:
            result.append(idxs[num])
        return result
