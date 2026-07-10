# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        stack = []

        while head:
            stack.append(head)
            head = head.next
        start = ListNode(0)
        cur = start
        while stack:
            val = stack.pop()
            print(val.val)
            cur.next = val
            cur = cur.next

        cur.next = None
        return start.next

        





        