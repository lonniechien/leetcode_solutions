class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        count = 1
        big = 1
        for num in nums:
            curr = num
            if curr - 1 in nums:
                continue
            while curr in nums:
                curr += 1
                if curr in nums:
                    count += 1
            if count > big:
                big = count
            count = 1
        return big
