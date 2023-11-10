class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        if n < 1:
            return 0
        elif n < 2:
            if nums[0] == val:
                nums.pop()
                return 0
            else:
                return 1
        k = n
        i = 0
        while nums[i] is not None:
            if nums[i] == val:
                nums[i:n-1] = nums[i+1:]
                nums[-1] = None
                k -= 1
                i -= 1
            i += 1
            if i == n:
                break
        return k
