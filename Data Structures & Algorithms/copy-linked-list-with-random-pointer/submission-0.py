"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        nodeMap = {None:None}

        cur = head
        while cur:
            nodeMap[cur] = Node(cur.val)
            cur = cur.next

        #now map the random pointers
        cur = head
        while cur:
            newNode = nodeMap[cur]
            newNode.next = nodeMap[cur.next]
            newNode.random = nodeMap[cur.random]
            cur = cur.next

        return nodeMap[head]
        