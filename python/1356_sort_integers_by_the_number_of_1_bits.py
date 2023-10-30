class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_ones(n):
            ones = 0
            quotient = n
            while quotient:
                quotient,remainder = divmod(quotient,2)
                if remainder:
                    ones += 1
            return ones
        
        arr = [(arr[i],count_ones(arr[i])) for i in range(len(arr))]
        arr = sorted(arr, key=lambda num:(num[1],num[0]))
        return [arr[i][0] for i in range(len(arr))]
