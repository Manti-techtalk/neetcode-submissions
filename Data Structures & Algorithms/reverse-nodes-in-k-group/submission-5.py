# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #find size
        c = 0
        f = head
        while f:
            c += 1
            f = f.next
        # print(c)
        dif = c - k
        cur , prev = head, None
        # print(dif)

        if dif >= k:
            #reverse the first k elements , 
            #reveser the next remain nodes
            st = 0
            while st != k:
                st += 1
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            head.next = cur
            prevv = None
            # print(cur.val)

            #now rev the rest of the half
            f = cur
            while f:
                temp = f.next
                f.next = prevv
                prevv = f
                f = temp

            print(prevv.val,head.val)
            head.next = prevv
            return prev
        # nodes are smalller than the value k
        # cur , prev = head, None
        # print(cur.val, "Starting")
        st = 0
        while st != k:
            st += 1
            temp = cur.next 
            cur.next = prev
            prev = cur
            cur = temp
        # print(prev.val,cur.val, head.val)

        head.next = cur

        return prev
        