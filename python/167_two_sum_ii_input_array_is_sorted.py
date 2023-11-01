class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while 1:
            n = numbers[i] + numbers[j]
            if n < target:
                i += 1
            elif n > target:
                j -= 1
            else:
                i += 1
                j += 1
                return [i, j] 
