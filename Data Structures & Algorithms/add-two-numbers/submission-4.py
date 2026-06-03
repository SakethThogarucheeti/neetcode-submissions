# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d1 = l1
        d2 = l2
        summ = 0
        res = l2
        reshead = res
        while d1 or d2:
            if d1:
                summ += d1.val
                d1 = d1.next
            if d2:
                summ += d2.val
                d2 = d2.next

            res.next = ListNode(summ%10)
            summ = summ//10
            res = res.next
        
        if summ == 1:
            res.next = ListNode(1)
            
        
        return reshead.next
            
        