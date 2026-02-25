# Given a binary tree root[], you need to find the sum 
# of the nodes on the longest path from the root to any leaf node.
#  If two or more paths have the same length, the path with 
# the maximum sum of node values should be considered.

'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        #code here
       
        self.max_sum = 0
        self.max_path = 0
        
        self.maxSumPath(root, self.max_sum, 0)
        
        return self.max_sum
        
    def maxSumPath(self, node, curr_sum, curr_len):
        if node is None:
            return
        
        curr_sum += node.data
        curr_len += 1
        
        if node.left is None and node.right is None:
            if curr_len > self.max_path:
                self.max_path = curr_len
                self.max_sum =  curr_sum
            
            if curr_len == self.max_path:
                self.max_sum = max(self.max_sum, curr_sum)
                
                
        self.maxSumPath(node.left, curr_sum, curr_len)
        self.maxSumPath(node.right, curr_sum , curr_len)
                
        
            
        