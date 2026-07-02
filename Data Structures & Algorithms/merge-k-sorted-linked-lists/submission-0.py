# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for head in lists:
            cur = head
            while cur:
                arr.append(cur.val)
                cur = cur.next
        print(arr)
        arr.sort()
        print(arr)
        d = ListNode(0)
        cur = d
        for val in arr:
            cur.next = ListNode(val)
            cur = cur.next
        return d.next