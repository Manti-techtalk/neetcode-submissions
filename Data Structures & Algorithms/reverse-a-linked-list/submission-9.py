# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        stack = deque()
        cur = head
        while cur:
            stack.append(cur)
            cur = cur.next

        print("Test stack property",stack[-1].val)

        d = ListNode(0)
        cur = d

        while stack:
            node = stack.pop()
            print("We getting the right nodes",node.val)
            cur.next = node
            cur = cur.next
        cur.next = None
        return d.next


