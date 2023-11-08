class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_times = list()
        n = len(dist)
        for i in range(n):
            d = dist[i]
            v = speed[i]
            t = d/v
            if d%v:
                t += 1
            arrival_times.append(t)
        arrival_times.sort()
        result = 1
        for i in range(1,n):
            t = arrival_times[i]
            if t < i+1:
                return result
            else:
                result += 1
        return result
