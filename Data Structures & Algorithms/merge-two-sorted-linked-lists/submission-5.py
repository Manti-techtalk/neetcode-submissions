# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        d = ListNode(0)
        cur = d
        p,p2 = list1,list2
        while p and p2:
            if p.val < p2.val:
                cur.next = p
                p = p.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        cur.next = p if p else p2
        return d.next