class Solution:
    def maxArea(self, height: List[int]) -> int:
        def get_area(heights, i, j):
            L = j - i
            H = min(heights[i], heights[j])
            return L * H

        i = 0
        j = len(height) - 1
        most = get_area(height, i, j)
        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            area = get_area(height, i, j)
            if area > most:
                most = area
        return most
