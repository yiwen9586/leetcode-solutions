# 
# Generated by fetch-leetcode-submission project on GitHub.
# https://github.com/gitzhou/fetch-leetcode-submission
# Contact Me: aaron67[AT]aaron67.cc
# 
# Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
# 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def inorder(root, lis):
            if root is None:
                return
            inorder(root.left, lis)
            lis.append(root.val)
            inorder(root.right, lis)
        
        lis = []
        inorder(root, lis)
         
        dic = {}
        for num in lis:
            dic[num] = k - num
        for num in lis:
            if dic[num] in lis and dic[num] != num:
                return True
        
        return False
            

