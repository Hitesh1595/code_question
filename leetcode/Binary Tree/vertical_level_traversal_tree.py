# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        from collections import deque,defaultdict

        if root is None:
            return []
        if root.left is None and root.right is None:
            return [[root.val]]

        result = []
        col_map = defaultdict(list)
        queue = deque([(root,0,0)])

        while queue:
            
            node,col,row = queue.popleft()
            
            col_map[col].append((row,node.val))

            if node.left:
                queue.append((node.left, col-1,row + 1))
            if node.right:
                queue.append((node.right, col + 1, row + 1))

        for col in sorted(col_map):
            # again sort on row basis
            nodes = sorted(col_map[col])
            result.append([val for row, val in nodes])

        return result
        