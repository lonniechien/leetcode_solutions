class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.vals = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for row in range(row1, row2+1):
            for col in range(col1, col2+1):
                self.vals[row][col] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.vals[row][col]


# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)
