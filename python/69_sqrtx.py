class Solution:
    def mySqrt(self, x: int) -> int:
        root = 0
        square = 0
        while square < x:
            root += 1
            square = root * root
        if square > x:
            return root - 1
        return root
