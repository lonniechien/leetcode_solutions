class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        result = list()
        for count in candies:
            if count + extraCandies >= greatest:
                result.append(True)
            else:
                result.append(False)
        return result
