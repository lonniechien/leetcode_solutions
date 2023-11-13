class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        targets = dict()
        count = 0
        for num in nums:
            if num in targets:
                targets[num] -= 1
                if targets[num] == 0:
                    targets.pop(num)
                count += 1
                continue
            target = k - num
            if target not in targets:
                targets[target] = 1
            else:
                targets[target] += 1
        return count
