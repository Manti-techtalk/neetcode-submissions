# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0)
        d.next = head
        s=f=d
        for i in range(n):
            f = f.next
        while f and f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return d.next
