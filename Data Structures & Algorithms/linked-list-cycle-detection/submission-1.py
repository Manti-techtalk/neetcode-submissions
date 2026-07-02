class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head  # slow pointer
        f = head  # fast pointer
        
        while f and f.next:  # While there's still a node and the next node exists
            s = s.next        # Move slow pointer one step
            f = f.next.next   # Move fast pointer two steps

            if s == f:        # If they meet, there is a cycle
                return True
        
        return False           # If fast pointer reaches the end, no cycle
