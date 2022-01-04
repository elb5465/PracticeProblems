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
        
        // Binary Search Tree (BST): AKA -> Sorted / ordered to have each left and right node be less than or greater than its parent node respectively
        
        // if p and q less than root, they're to left
        if (p.val < root.val   &&   q.val < root.val)
            return lowestCommonAncestor(root.left, p, q);
        
        // if p and q greater than root, they're to right
        if (p.val > root.val   &&   q.val > root.val)
            return lowestCommonAncestor(root.right, p, q);
        
        // o.w., they're on either side of the current root, so you should return the root
        return root;
        
    }
}
