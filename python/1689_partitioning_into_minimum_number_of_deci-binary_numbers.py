class Solution:
    def minPartitions(self, n: str) -> int:
        biggest = 0
        for char in n:
            num = int(char)
            if num == 9:
                return 9
            if num > biggest:
                biggest = num
        return biggest
            
