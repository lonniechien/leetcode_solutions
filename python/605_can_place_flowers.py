class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        pad = [0] + flowerbed + [0]
        for i in range(1,len(pad)-1):
            if pad[i-1] == pad[i] == pad[i+1] == 0:
                pad[i] = 1
                n -= 1
            if n == 0:
                return True
        return False
