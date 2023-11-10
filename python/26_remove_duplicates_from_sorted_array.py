class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        removed = 0
        prev = nums[0]
        i = 1
        while i < n:
            num = nums[i]
            if num is None:
                break
            elif num == prev:
                nums[i:n-1] = nums[i+1:]
                nums[-1] = None
                removed += 1
            else:
                i += 1
            prev = num
        return n - removed
