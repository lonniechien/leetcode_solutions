class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        k = n
        i = 1
        samesies = 0
        while nums[i] is not None:
            if nums[i] == nums[i-1]:
                samesies += 1
            else:
                samesies = 0
            if samesies > 1:
                nums[i:n-1] = nums[i+1:n]
                nums[-1] = None
                k -= 1
                i -= 1
            i += 1
            if i == n:
                break
        return k
