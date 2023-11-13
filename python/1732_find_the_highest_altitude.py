class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        peak = 0
        for dy in gain:
            altitude += dy
            if altitude > peak:
                peak = altitude
        return peak
