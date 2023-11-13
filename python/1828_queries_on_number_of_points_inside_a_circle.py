class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        answer = list()
        for circle in queries:
            count = 0
            for point in points:
                dx = point[0] - circle[0]
                dy = point[1] - circle[1]
                r = ( dx*dx + dy*dy ) ** 0.5
                if r <= circle[2]:
                    count += 1
            answer.append(count)
        return answer
