# 

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        # code here
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            return [root.data]
        
        result = [root.data]
        self.leftTraversal(root.left, result)
        self.leafTraversal(root, result)
        self.rightTraversal(root.right, result)
        
        return result
        # [1, 4, 2, 1]
        
    def leftTraversal(self, node, result):
        
        if node is None:
            return
        if node.left is None and node.right is None:
            return 
        
        result.append(node.data)
        if node.left:
            self.leftTraversal(node.left,result)
        else:
            self.leftTraversal(node.right,result)
            
    def leafTraversal(self, node, result):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            result.append(node.data)
            return
            
        self.leafTraversal(node.left, result)
        self.leafTraversal(node.right, result)
        
    def rightTraversal(self, node, result):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            return
        if node.right:
            self.rightTraversal(node.right, result)
        else:
            self.rightTraversal(node.left, result)
        
        result.append(node.data)
        

        
        
        
        