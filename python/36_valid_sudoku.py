class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = set()
            for col in row: 
                if col == ".":
                    continue
                elif col in nums:
                    return False
                else:
                    nums.add(col)
        
        for col in range(9):
            nums = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in nums:
                    return False
                else:
                    nums.add(board[row][col])
        
        boxes = dict()
        for i in range(9):
            boxes[i] = set()

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in boxes[row//3*3 + col//3]:
                    return False
                else:
                    boxes[row//3*3 + col//3].add(board[row][col])
        return True
