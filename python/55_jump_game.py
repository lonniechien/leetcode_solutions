class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        n = len(nums)
        if n < 2:
            return True
        for i in range(n):
            target = i + nums[i]
            if target > furthest:
                furthest = target
            if i == furthest:
                return False
            if furthest >= n-1:
                return True
