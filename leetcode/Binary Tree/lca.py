# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

# According to the definition of LCA on Wikipedia:
#  “The lowest common ancestor is defined between two nodes p and q as the lowest node
#  in T that has both p and q as descendants (where we allow a node to be a descendant 
# of itself).”

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # case if any found return to above 
        if left  and right :
            return root

        elif left  and right is None:
            return left
        elif right and left is None:
            return right
        else:
            return None
        