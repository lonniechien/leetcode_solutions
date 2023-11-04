class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = grid
        cols = [[0 for row in rows] for row in rows]
        for i in range(len(grid)):
            for j in range(len(grid)):
                cols[j].append(grid[i][j])
        maxrows = [max(row) for row in rows]
        maxcols = [max(col) for col in cols]
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                result += min(maxrows[i],maxcols[j]) - grid[i][j]
        return result
