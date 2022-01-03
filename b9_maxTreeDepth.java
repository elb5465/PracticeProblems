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
    public int maxDepth(TreeNode root) {
        
        // base case: if root is null, return 0 bc you reached the end of a root
        if (root==null)
            return 0;
            
        // o.w., add one for current level and recurse down left and right sides seperately, taking the max of the two
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
