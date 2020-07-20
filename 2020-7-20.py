#-------------title -----------------------------------
# Merge two binary trees
#--------------detail-----------------------------------------
#Given two binary trees and imagine that when you put one of them to cover the other, 
#some nodes of the two trees are overlapped while the others are not.
#You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, 
#then sum node values up as the new value of the merged node. Otherwise, 
#the NOT null node will be used as the node of new tree.

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
class Solution:
    def mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        else:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
            return t1
          
          
          
          
#-----------Complexity Analysis---------------
#Time complexity : O(m). A total of mm nodes need to be traversed.
#Here, mm represents the minimum number of nodes from the two given trees.
#-------------------------------------
#Space complexity : O(m). The depth of the recursion tree can go upto mm in
#the case of a skewed tree. In average case, depth will be O(logm)O(logm).
