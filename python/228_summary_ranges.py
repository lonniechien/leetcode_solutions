class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if not n:
            return list()
        head = nums[0]
        tail = nums[0]
        to = "->"
        out = list()
        for i,num in enumerate(nums[1:]):
            if num == tail + 1:
                tail = num
            else:
                if head == tail:
                    out.append(str(head))
                else:
                    out.append(str(head)+to+str(tail))
                head = nums[i+1]
                tail = head
        if head == tail:
            out.append(str(head))
        else:
            out.append(str(head)+to+str(tail))
        return out
