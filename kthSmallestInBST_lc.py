"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.


Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3


Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?



"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None





# inorder traversal is what they say 
#  
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root, l, k):
            if root == None or len(l)>k:
                return
            inorder(root.left, l, k)
            l.append(root.val)
            inorder(root.right, l, k)
        
        l=[]
        inorder(root, l, k)
        return l[k]
        


        