# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        seen = set()

        fast = head

        while fast:
            seen.add(fast)

            fast = fast.next

            if fast in seen:
                return True

        return False
        