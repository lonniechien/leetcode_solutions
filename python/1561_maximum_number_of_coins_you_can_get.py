class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        total = 0
        while piles:
            total += piles[-2]
            for i in [-1,-2,0]:
                piles.pop(i)
        return total
