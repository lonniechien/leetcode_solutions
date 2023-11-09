class Solution:
    def countHomogenous(self, s: str) -> int:
            N = len(s)
            if N == 1:
                return 1
            substrs = list()
            front = 0
            for i in range(1,N):
                if s[i] != s[front]:
                    substrs.append(s[front:i])
                    print(front, i)
                    front = i
            substrs.append(s[front:N])
            ans = 0
            for substr in substrs:
                n = len(substr)
                ans += int(n * (n + 1) / 2)
            print(substrs)
            return ans % (10**9 + 7)
