class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        most = 0
        for customer in accounts:
            wealth = 0
            for account in customer:
                wealth += account
            if wealth > most:
                most = wealth
        return most
