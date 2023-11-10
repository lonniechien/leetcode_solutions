class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = i = 0
        while i < n:
            if a > m + i:
                nums1[a-1:] = nums2[i:]
                break
            elif nums2[i] < nums1[a]:
                nums1[a+1:m+i+1] = nums1[a:m+i]
                nums1[a] = nums2[i]
                i += 1
            else:
                a += 1
