# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
from collections import deque
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        d= ListNode(0)
        cur = d

        for lt in lists:
            print(lt)
            head = lt
            while head:
                # print(head.val)
                cur.next = head
                cur = cur.next
                head = head.next
        # see how new formed lisked list
        res = []

        head = d.next
        while head:
            res.append(head.val)
            head = head.next
        res.sort()
        print(res)

        d = ListNode(0)
        cur = d
        for val in res:
            cur.next = ListNode(val)
            cur = cur.next

        return d.next


        