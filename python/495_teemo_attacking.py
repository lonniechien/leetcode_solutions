class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        timeSeries = sorted(list(set(timeSeries)))
        if not timeSeries:
            return 0
        T = timeSeries[-1] + duration
        total = 0
        stop = 0
        poison = False
        i = 0
        for t in range(T):
            if i < len(timeSeries):
                if t == timeSeries[i]:
                    poison = True
                    stop = t + duration
                    i += 1
            if t == stop:
                poison = False
            if poison:
                total += 1
        return total
