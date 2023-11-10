class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr = 0
        result = list()
        for num in nums:
            curr += num
            result.append(curr)
        return result
