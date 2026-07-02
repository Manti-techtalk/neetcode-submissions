class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        

        # Step 1: Find the middle (slow will point to the mid node)
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next

        # Step 2: Break the list into two halves
        head1 = head          # first half
        head2 = s.next        # second half starts after middle
        s.next = None         # cut off the first half

        # Step 3: Reverse the second half (required for correct reorder)
        prev = None
        cur = head2
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        head2 = prev  # new head of reversed second half

        # Step 4: Merge the two halves alternately
        p1, p2 = head1, head2
        while p2:
            tmp1, tmp2 = p1.next, p2.next
            p1.next = p2
            p2.next = tmp1
            p1 = tmp1
            p2 = tmp2
