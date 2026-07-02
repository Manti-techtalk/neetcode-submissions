# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1arr =[]
        l2arr = []
        cur,cur2 = l1,l2
        while cur:
            l1arr.append(str(cur.val))
            cur= cur.next
        while cur2:
            l2arr.append(str(cur2.val))
            cur2 = cur2.next
        num1 = int(''.join(l1arr[::-1]))
        num2 = int(''.join(l2arr[::-1]))
        result = num1 + num2
        d = ListNode(0)
        p = d
        for num in str(result)[::-1]:
            p.next = ListNode(int(num))
            p = p.next
        return d.next

            