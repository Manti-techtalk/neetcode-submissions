# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return False

        def dfs(node):
            if not node:
                return [None]

            left = dfs(node.left)
            right = dfs(node.right)

            return [node.val] + left + right

        big = dfs(root)
        small = dfs(subRoot)

        print(big,small)


        for i in range(len(big)-len(small) + 1):
            win = big[i:i + len(small)]
            if win == small:
                return True

        return False
        