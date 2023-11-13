class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = list()
        more = list()
        same = list()
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                more.append(num)
            else:
                same.append(num)
        return less + same + more
