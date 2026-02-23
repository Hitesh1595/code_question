# 

'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def topView(self, root):
        # code here
        from collections import deque
        
        if root is None:
            return []
            
        queue = deque([(root,0)])
        
        hd_map = {}
        result = []
        
        while queue:
            for _ in range(len(queue)):
                node, hd = queue.popleft()
                
                if hd not in hd_map:
                    hd_map[hd] = node.data
                
                if node.left:
                    queue.append((node.left, hd-1))
                if node.right:
                    queue.append((node.right, hd + 1))
                    
        
        for key in sorted(hd_map):
            result.append(hd_map[key])
            
        return result
                
            
            
        
        
        