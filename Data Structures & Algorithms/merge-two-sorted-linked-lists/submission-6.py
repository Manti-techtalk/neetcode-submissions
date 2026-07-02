# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        p,p1 = list1,list2

        while p and p1:
            if p.val < p1.val:
                cur.next = p
                p = p.next
            
            else:
                cur.next = p1
                p1 = p1.next
            cur = cur.next
        cur.next = p if p else p1

        return dummy.next

