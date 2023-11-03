class Solution:
    def isPalindrome(self, x: int) -> bool:
        target = x
        if x < 0:
            return False
        backwards = 0
        while x:
            backwards *= 10
            backwards += (x % 10)
            x = x // 10
        if backwards == target:
            return True
        else:
            return False
