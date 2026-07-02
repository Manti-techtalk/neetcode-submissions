# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        stack = [root]
        res = []

        while stack:
            for _ in range(len(stack)):
                node = stack.pop()
                res.append(node.val)

                if node.right:
                    stack.append(node.right)

                if node.left:
                    stack.append(node.left)

        print(res)
        res.sort()
        print(res)
        if k in range(len(res)):
            return res[k - 1]
        return res[len(res)-1]





        

        