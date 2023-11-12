class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return N-1
        for i in range(1,N-1):
            if nums[i] > max(nums[i-1],nums[i+1]):
                return i
