import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Add the head of each list to the heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        cur = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next

            # Move to next node in the list
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
