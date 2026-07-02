# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s=f=head
        while f and f.next:
            s = s.next
            f = f.next.next
        head1 = head
        head2 = s.next
        s.next = None

        cur,prev = head2,None
        while cur:
            saved = cur.next
            cur.next = prev
            prev = cur
            cur = saved
        head2 = prev
        p,p2 = head1,prev
        while p2:
            saved1 = p.next
            saved2 = p2.next
            p.next = p2
            p2.next = saved1
            p = saved1
            p2 = saved2
        return