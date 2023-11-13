class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        i = 2**31
        j = 2**31
        for num in nums:
            if num <= i:
                i = num
            elif num <= j:
                j = num
            else:
                return True
        return False
