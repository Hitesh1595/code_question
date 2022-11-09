# time O(n)
# space O(h)

import queue
class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
def topview(root):
    d = {}

    def traverse(root, key, level):
        if root is None:
            return None

        if key not in d:
            d[key] = [root.data, level]
        elif d[key][1] > level:
            # for bottom view upper line condition needs to be changed
            d[key] = [root.data, level]
            
        traverse(root.left, key - 1, level + 1)
        traverse(root.right, key + 1, level + 1)
        
    traverse(root, 0, 0)
    
    for i in sorted(d):
        print(d[i][0],end = ' ')

        


    
 
 
# Driver program to test above function
root = Node(10)
root.left = Node(3)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(8)
root.right.right = Node(15)
root.right.left = Node(12)
root.right.right.left = Node(14)
topview(root)