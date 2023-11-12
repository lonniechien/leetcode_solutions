class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        teams = set(range(n))
        for j in range(n):
            for i in range(n):
                if grid[i][j]:
                    teams.remove(j)
                    break
        return next(iter(teams))
