# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, current_max=None) -> int:
        
        if not root:
            return 0
        
        # initialize max only once (at the root)
        if current_max is None:
            current_max = root.val
        
        count = 0
        if root.val >= current_max:
            count = 1
        
        # update max before going down the tree
        current_max = max(current_max, root.val)
        
        # accumulate results from subtrees
        count += self.goodNodes(root.left, current_max)
        count += self.goodNodes(root.right, current_max)
        
        return count
