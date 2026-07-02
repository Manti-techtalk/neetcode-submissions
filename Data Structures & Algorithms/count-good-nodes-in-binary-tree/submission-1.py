# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.c = 0
        self.m = None
        stack = [(root,root.val)]
        while stack:
            node,max_so_far = stack.pop()

            if max_so_far <= node.val:
                self.c += 1

            self.new_max = max(max_so_far,node.val)

            if node.left:
                stack.append((node.left,self.new_max))
            if node.right:
                stack.append((node.right,self.new_max))
        return self.c
            

