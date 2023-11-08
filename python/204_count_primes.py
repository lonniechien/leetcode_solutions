class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        nums = list(range(2,n))
        composites = set()
        for num in nums:
            if num in composites:
                continue
            curr = num * num
            if curr >= n:
                break
            while curr < n:
                composites.add(curr)
                curr += num
        return n - len(composites) - 2
