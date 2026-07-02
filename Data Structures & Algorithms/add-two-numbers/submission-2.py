# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nex
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        arr2 = []
        while l1:
            arr1.append(str(l1.val))
            l1 = l1.next
        while l2:
            arr2.append(str(l2.val))
            l2 = l2.next
        print(arr1,arr2)
        # now order in original form
        arr1 = arr1[::-1]
        arr2 = arr2[:: -1]
        print(arr1,arr2)
        # now we change into numbers 
        num1 = int(''.join(arr1))
        num2 = int(''.join(arr2))
        print(num1,num2)
        res = num1 + num2
        print(res)
        # now convert it to srt
        res = [int(c) for c in str(res)]
        print(res)
        # now to reversed order
        res = res[::-1]
        print(res)
        d = ListNode(0)
        cur = d
        for val in res:
            cur.next = ListNode(val)
            cur = cur.next
        return d.next
