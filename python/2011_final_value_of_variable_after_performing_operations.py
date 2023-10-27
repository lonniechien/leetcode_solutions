class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for oper in operations:
            if oper in [--X, X--]:
                X -= 1
            else:
                X += 1
        return X
