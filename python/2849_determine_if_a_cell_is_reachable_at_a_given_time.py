class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx = abs(fx - sx)
        dy = abs(fy - sy)
        dist = max(dx, dy)
        if not dist:
            if t == 1:
                return False
            else:
                return True
        if dist > t:
            return False
        else:
            return True
