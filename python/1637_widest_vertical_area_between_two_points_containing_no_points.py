class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        prev = points[0]
        wide = 0
        for point in points[1:]:
            if point[0] == prev[0]:
                continue
            wide = max(wide, point[0] - prev[0])
            prev = point
        return wide
