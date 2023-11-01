class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums) - 1
        result = list()
        nums = sorted(nums)
        for i in range(n):
            target = 0 - nums[i]
            j = i + 1
            k = n
            while j < k:
                doublet = nums[j] + nums[k]
                if doublet < target:
                    j += 1
                elif doublet > target:
                    k -= 1
                elif doublet == target:
                    triplet = [nums[i],nums[j],nums[k]]
                    if triplet not in result:
                        result.append(triplet)
                    j += 1
        return result
