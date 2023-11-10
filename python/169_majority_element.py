class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = [0,0]
        for num in nums:
            if num == curr[0]:
                curr[1] += 1
            elif curr[1] == 0:
                curr = [num,1]
            else:
                curr[1] -= 1
        return curr[0]
