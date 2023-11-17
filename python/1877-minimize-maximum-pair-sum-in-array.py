class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)//2
        front = nums[:n]
        back = nums[n:]
        back.reverse()
        big = 0
        for i in range(n):
            x = front[i] + back[i]
            if x > big:
                big = x
        return big
