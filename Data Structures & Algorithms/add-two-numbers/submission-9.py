# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q = deque()

        while l1 or l2:
            q.append((l1.val,l2.val))
            l1 = l1.next
            l2 = l2.next

        print(q)

        d = ListNode(0)
        cur = d
        carry = 0

        while q:
            node = q.popleft()
            total = sum(node) + carry
            ta = total % 10
            carry = total // 10
            print(ta, "we here", carry)
            
            cur.next = ListNode(ta)

            cur = cur.next
            print(node,total)

        if carry:
            cur.next = ListNode(carry)

        return d.next

        