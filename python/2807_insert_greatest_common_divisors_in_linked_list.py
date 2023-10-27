class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next is not None:
            nxt = curr.next
            num1 = curr.val
            num2 = nxt.val
            while num2 != 0:
                temp = num2
                num2 = num1 % num2
                num1 = temp
            curr.next = ListNode(val=num1,next=nxt)
            curr = nxt
        return head
