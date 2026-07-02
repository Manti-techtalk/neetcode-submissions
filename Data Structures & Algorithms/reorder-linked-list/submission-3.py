# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        head1 = head
        head2 = slow.next
        slow.next = None

        #now reverse the head2
        cur, prev = head2,None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head2 = prev

        p1, p2 = head1, head2

        while p2:
            next1 = p1.next
            next2 = p2.next

            #now link 
            p1.next = p2
            p2.next = next1

            # now move pointers forward

            p1 = next1
            p2 = next2

        return



        