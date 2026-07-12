# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q = deque()
        carry = 0

        while l1 or l2:
            val = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            q.append((val,val2))

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        print(q)

        d = ListNode(0)
        cur = d
        while q:
            node = q.popleft()
            
            total = sum(node) + carry
            ta = total % 10
            carry = total // 10
            print(node, total,carry, ta)

            #now built the linked List
            cur.next = ListNode(ta)
            cur = cur.next

        if carry:
            cur.next = ListNode(carry)

        return d.next




        