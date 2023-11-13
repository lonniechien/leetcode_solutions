class Solution:
    def tribonacci(self, n: int) -> int:
        sequence = {i:[0,1,1][i] for i in range(3)}
        if n < 3:
            return sequence[n]
        for i in range(3,n+1):
            sequence[i] = sum([sequence[i-j] for j in range(1,4)])
        return sequence[n]
