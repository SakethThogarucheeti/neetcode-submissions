# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1 = l1
        d2 = l2
        carry = 0
        res = l2
        reshead = res
        while d1 or d2:
            summ = 0
            if d1:
                summ += d1.val
                d1 = d1.next
            if d2:
                summ += d2.val
                d2 = d2.next

            summ += carry
            carry = summ // 10

            res.next = ListNode(summ%10)

            res = res.next
        
        if carry == 1:
            res.next = ListNode(1)
            
        
        return reshead.next
            
        