# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root
        
        while current:
            # If both p and q are greater than parent, go right
            if p.val > current.val and q.val > current.val:
                current = current.right
            # If both p and q are lesser than parent, go left
            elif p.val < current.val and q.val < current.val:
                current = current.left
            # We have found the split point, which is the LCA
            else:
                return current
        