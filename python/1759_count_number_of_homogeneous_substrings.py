class Solution:
    def countHomogenous(self, s: str) -> int:
            N = len(s)
            if N == 1:
                return 1
            front = 0
            ans = 0
            for i in range(1,N):
                if s[i] != s[front]:
                    n = len(s[front:i])
                    ans += int(n * (n + 1) / 2)
                    front = i
            n = len(s[front:N])
            ans += int(n * (n + 1) / 2)
            return ans % (10**9 + 7)
