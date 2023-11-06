class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = list()

    def push(self, val: int) -> None:
        if not self.min:
            self.min.append(val)
        elif self.min[-1] < val:
            self.min.append(self.min[-1])
        else:
            self.min.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.min.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
