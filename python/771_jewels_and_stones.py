class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        hash_jewels = set()
        for jewel in jewels:
            hash_jewels.add(jewel)
        for stone in stones:
            if stone in hash_jewels:
                count += 1
        return count
