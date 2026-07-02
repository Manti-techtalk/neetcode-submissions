# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next
        arr = arr[::-1]
        print(arr)
        arr.pop(n - 1)
        print(arr)
        arr = arr[::-1]
        d = ListNode(0)
        cur = d

        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next

        return d.next


        