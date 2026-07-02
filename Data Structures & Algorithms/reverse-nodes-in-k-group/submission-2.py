# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        print(arr)
        res = []
        for i in range(0,len(arr),k):
            group = arr[i:i + k]
            print(group)
            if len(group) == k:
                g = group[::-1]
            else:
                g = group
            res.extend(g)

        d = ListNode(0)
        cur = d
        for val in res:
            cur.next = ListNode(val)
            cur = cur.next
        return d.next
        