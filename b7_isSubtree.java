/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // if recursed down to a null root, then no subroot was found (therefore false)
        if (root==null)
            return false;

        // if trees at current level are same, finish
        if (this.areSameTree(root, subRoot))
            return true;
        
        // o.w., check each subTree of root to see if any match
        else
            return (isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot));
    }
    
    public boolean areSameTree(TreeNode r1, TreeNode r2){
        // if recursed down to end of trees and are both null, they're identical
        if (r1==null && r2==null)
            return true;

        // if only one is null, then they're not identical
        if (r1==null || r2==null)
            return false;
        
        // check if head of current levels are equal - if not, return false
        if (r1.val != r2.val)
            return false;
        
        // otherwise, continue to recurse down each side and make sure they are all true
        return (areSameTree(r1.left, r2.left) && areSameTree(r1.right, r2.right));
    }
}
