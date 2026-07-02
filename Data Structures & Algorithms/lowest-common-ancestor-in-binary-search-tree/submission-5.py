# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None

        def dfs(node):
            if not node:
                return None

            dfs(node.left)
            dfs(node.right)

            if p.val <= node.val <=q.val or q.val <= node.val <= p.val:
                self.res = node
                return

        dfs(root)
        return self.res
        