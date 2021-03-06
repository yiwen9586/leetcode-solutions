// 
// Generated by fetch-leetcode-submission project on GitHub.
// https://github.com/gitzhou/fetch-leetcode-submission
// Contact Me: aaron67[AT]aaron67.cc
// 
// Lowest Common Ancestor of a Binary Tree
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
// 

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root == null)
            return null;
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        if(left == null && right == null){
            if(root == p || root == q)
                return root;
            else return null;
        }
        else if (left == null){
            if(root == p || root == q)
                return root;
            else return right;
        }
        else if(right == null){
            if(root == p || root == q)
                return root;
            else return left;
        }
        else
            return root;
    }
}

