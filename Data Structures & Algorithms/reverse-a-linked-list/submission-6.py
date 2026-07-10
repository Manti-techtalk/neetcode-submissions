# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        res = []
        while head:
            print(head.val)
            res.append(head.val)
            head = head.next

        

        res = res[::-1]
        print(res)

        dummy = ListNode(0)

        cur = dummy

        for val in res:
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next



        