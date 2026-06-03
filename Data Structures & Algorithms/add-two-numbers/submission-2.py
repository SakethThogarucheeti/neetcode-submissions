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
            v1 = 0
            v2 = 0
            if d1:
                v1 = d1.val
                d1 = d1.next
            if d2:
                v2 = d2.val
                d2 = d2.next

            summ = v1 + v2 + carry
            carry = summ // 10

            res.next = ListNode(summ%10)

            res = res.next
        
        if carry == 1:
            res.next = ListNode(1)
            
        
        return reshead.next
            
        