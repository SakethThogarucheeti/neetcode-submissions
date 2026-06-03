# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prv = None
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        print(slow.val)

        cur = slow.next
        slow.next = None

        prv = None
        while cur:
            nxt = cur.next
            cur.next = prv
            prv = cur
            cur = nxt
        
        cur1 = head
        cur2 = prv

        while cur2:
            print(cur1 and cur1.val, cur2 and cur2.val)
            t2 = cur2.next
            t1 = cur1.next
            cur1.next = cur2
            cur2.next = t1            
            cur1 = t1
            cur2 = t2
        