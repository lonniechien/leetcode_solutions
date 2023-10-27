class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        i = 0
        for time in hours:
            if time >= target:
                i += 1
        return i
