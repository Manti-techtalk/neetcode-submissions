# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. Cut the linked List into halves
2. Build a dummy that initializes the new linked Lists
3. Reverse the last head
3. Alternate both cut linked lists,putting them into the dummy's linked list
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # print("We cut at",slow.val)
        # print("Where head2:", slow.next.val)
        head2 = slow.next
        # print("head2 start", head2.val)
        slow.next = None

        
        # print("first head valies")
        # while head:
        #     print(head.val)
        #     head = head.next

        # print("Second head values")

        # while head2:
        #     print(head2.val)
        #     head2 = head2.next

        # now lets reverse head2 
        
        prev, cur = None, head2


        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        print("head2  After reverse", prev.val)

        #test if we didnt lose the nodes

        # while prev:
        #     print(prev.val)
        #     prev = prev.next

        # now lets alternate the linked List

        while prev:
            first_temp = head.next
            second_temp = prev.next

            head.next = prev
            prev.next = first_temp

            head = first_temp
            prev = second_temp







        


        