# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        prv = None
        cur = head

        while cur:
            temp = cur.next
            cur.next = prv
            prv = cur
            cur = temp
        
        return prv
            

        