# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr_new = dummy  # builds the final linked list

        curr = head

        while curr:
            # 1. Collect up to k nodes
            group_nodes = []
            temp = curr
            for _ in range(k):
                if not temp:
                    break
                group_nodes.append(temp)
                temp = temp.next

            # If we did NOT collect k nodes → append remaining as-is
            if len(group_nodes) < k:
                for node in group_nodes:
                    curr_new.next = node
                    curr_new = curr_new.next
                break  # finished

            # 2. Reverse this full group
            group_nodes.reverse()

            # 3. Attach reversed group
            for node in group_nodes:
                curr_new.next = node
                curr_new = curr_new.next

            # Move curr forward after this group
            curr = temp

        # End the list
        curr_new.next = None

        return dummy.next
