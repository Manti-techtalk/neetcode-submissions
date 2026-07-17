# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        # Find size
        c = 0
        f = head

        while f:
            c += 1
            f = f.next

        # Not enough nodes to reverse
        if c < k:
            return head

        cur, prev = head, None

        # Reverse the first k nodes
        st = 0

        while st != k:
            st += 1

            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        # Original head is now the tail
        # Process the remaining linked list
        head.next = self.reverseKGroup(cur, k)

        # prev is the new head of this reversed group
        return prev